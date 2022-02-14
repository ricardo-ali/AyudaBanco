# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 09:11:03 2022

@author: tearil
"""
import streamlit as st
import pandas as pd
#import numpy as np
#import sqlite3

#import configparser
#import plotly.express as px

#import pathlib
#from contextlib import contextmanager
#from pathlib import Path
#from uuid import uuid4
#from openpyxl import load_workbook

#import base64


#%% ALTA NOMINA - PRINCIPAL
def cese_laboral_principal():
    
    
    #Pone una imagen al principio de la pagina principal
    # LOGO_IMAGE = "./media/saluki2.jpg"
    # st.markdown("""<style>.container {display: flex;}.logo-text 
    #                 {font-weight:700 !important;font-size:50px !important;
    #                  color: #f9a01b !important;padding-top: 5px !important;}.logo-img 
    #                  {float:right;}</style>""", unsafe_allow_html=True)
    # st.markdown(f"""<div class="container">
    #                 <img class="logo-img" src="data:image/png;base64,
    #                 {base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
    #                 <p class="logo-text"></p>
    #                 </div>
    #                 """,
    #                 unsafe_allow_html=True
    #                 )


    st.title('SALUKI (Upload File)')
    
    #PRIMERO DEFINO LAS FUNCIONES LUEGO LAS LLAMO
    
    #funcion para cargar tablas de sqlite3 en Saluki
    @contextmanager
    def sqlite_connect(db_bytes):
        fp = Path(str(uuid4()))
        fp.write_bytes(db_bytes.getvalue())
        conn = sqlite3.connect(str(fp))
    
        try:
            yield [conn, fp.absolute()]
        finally:
            conn.close()
            fp.unlink()
    
    #funcion que genera el link y archivo sqlite para descargar
    @st.cache
    def get_binary_file_downloader_html(bin_file, file_label='File'):
        with open(bin_file, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}">Download {file_label}</a>' 
        return href
    
    #el codigo mas rapido que encontre para leer las hojas de un excel xlxs
    @st.cache
    def get_sheet_details(file_path):  
        from zipfile import ZipFile
        from bs4 import BeautifulSoup  # you also need to install "lxml" for the XML parser
        
        with ZipFile(file_path) as zipped_file:
            summary = zipped_file.open(r'xl/workbook.xml').read()
        soup = BeautifulSoup(summary, "xml")
        sheets = [sheet.get("name") for sheet in soup.find_all("sheet")]
        return sheets
    
#%% Saluki - ORIGEN DE DATOS
        
    @st.cache
    def cargar_hojas_origen(uploaded_file_origen):
        #Obtengo el archivo y la extension y la paso a minuscula
        file_extension = pathlib.Path(uploaded_file_origen.name).suffix
        file_extension = file_extension.lower()
        
        #si es un archivo version 2010 o posterior
        #abre el archivo
        if file_extension in [".xlsx", ".xlsm"]:
            from zipfile import ZipFile
            from bs4 import BeautifulSoup  # you also need to install "lxml" for the XML parser
            
            with ZipFile(uploaded_file_origen) as zipped_file:
                summary = zipped_file.open(r'xl/workbook.xml').read()
            soup = BeautifulSoup(summary, "xml")
            sheets = [sheet.get("name") for sheet in soup.find_all("sheet")]
                       
        else:
            #es un archivo xls, abro el archivo
            import xlrd
            
            book = xlrd.open_workbook(file_contents=uploaded_file_origen.getvalue(), 
                                      on_demand = True)
            sheets = book.sheet_names()
            book.release_resources()  #cierro objeto y libero memoria
            del book
            
        return sheets
    
    @st.cache
    def cargar_tablas_destino(uploaded_file_destino):
        with sqlite_connect(uploaded_file_destino) as conn:
            
            
            #Abre el archivo SQL con la cadena correspondiente
            with open('sql/lista_tablas_db.sql', 'r') as file:
                strSQL = file.read().replace('\n', ' ')
            
            #carga las tablas
            data_tables = pd.read_sql(strSQL, conn[0])
            
            #devuelve una lista con los nombres de tablas
            tablas = data_tables['name'].values.tolist()
            
            return tablas
    
    @st.cache
    def cargar_campos_excel(uploaded_file_origen, combobox_hojas):
        #lista las cabeceras del archivo de excel
        #Metodo con openpyxl (rapido)
        wb = load_workbook(filename=uploaded_file_origen, read_only=True)
        sheet = wb[combobox_hojas]

        nombre_columnas_excel=[]
        for cell in sheet[1]:
            nombre_columnas_excel.append(cell.value)            
        
        #cierro el archivo xlsx
        wb.close()    
        
        return nombre_columnas_excel
    
    @st.cache
    def cargar_campos_sqlite(uploaded_file_destino, combobox_tabla_destino):
    
        #lista los campos del archivo SQLite
        #Obtengo los nombres de columnas de la tabla SQLite
        with sqlite_connect(uploaded_file_destino) as conn:
            
            #Abre el archivo SQL con la cadena correspondiente
            with open('sql/cargar_campos_tabla.sql', 'r') as file:
                strSQL = file.read().replace('\n', ' ')
                strSQL = strSQL.replace('+tabla+', str(combobox_tabla_destino))
                
            #carga las tablas
            data = pd.read_sql(strSQL , conn[0])
            nombre_columnas_sqlite = list(data.columns)    
            
            return nombre_columnas_sqlite
    
    @st.cache
    def abrir_excel_en_dataframe(uploaded_file_origen, combobox_hojas):
        # Abre el excel en un Data Frame
        df = pd.read_excel(uploaded_file_origen, sheet_name=combobox_hojas)
        max_row=len(df)
        return [df, max_row]
    
     
    
    
    #subo archivo Origen
    uploaded_file_origen = st.file_uploader("Seleccione el archivo Origen de Datos:",
                                     ['xls', 'xlsx', 'xlsm'],
                                     accept_multiple_files = False)
    
    
    if uploaded_file_origen is not None:
                
        #cargo el cache o busco las hojas del Excel
        hojas_excel = cargar_hojas_origen(uploaded_file_origen)
        combobox_hojas = st.selectbox(
             'Seleccione la hoja de Excel (Origen):',
             hojas_excel)
                            
        st.markdown("___")


#%% Saluki - DESTINO DE DATOS
        
        uploaded_file_destino = st.file_uploader("Seleccione el archivo Destino de Datos:",
                                         [".db", ".sqlite", ".db3", ".sqlite3"],
                                         accept_multiple_files = False)
        
        #Si seleccionó un archivo, lo abre
        if uploaded_file_destino:
            #cargo el cache o busco las hojas del Excel
            tablas_sqlite = cargar_tablas_destino(uploaded_file_destino)
            
            #agrega un combo para seleccionar las tabla a visualizar
            combobox_tabla_destino = st.selectbox(
                 'Seleccione la tabla que desea usar como destino:',
                 (tablas_sqlite))

#%% Saluki - COMPARAR COLUMNAS

            st.markdown("___")
            
            st.markdown("### PREVISUALIZADOR")
            st.write("Las columnas que desea copiar deben coincidir \
                      en orden y en concepto (ej: ID_PRODUCT | id_prod)")
            
            #busca en cache o llama a la funcion con el nombre de columnas excel
            nombre_columnas_excel = cargar_campos_excel(uploaded_file_origen, 
                                                        combobox_hojas)
            
            #busca en cache o llama a la funcion con el nombre de campos en sqlite
            nombre_columnas_sqlite = cargar_campos_sqlite(uploaded_file_destino, 
                                                          combobox_tabla_destino)
            
            col1, col2 = st.columns(2)
            
            col1.subheader("Origen")
            col1.write("Archivo: " + uploaded_file_origen.name)
            col1.write("Hoja: " + combobox_hojas)
            col1.write("Columnas: " + str(len(nombre_columnas_excel)))
            col1.table(nombre_columnas_excel)
            
            
            col2.subheader("Destino")
            col2.write("Archivo: "  + uploaded_file_destino.name)
            col2.write("Tabla: " + combobox_tabla_destino)
            col2.write("Columnas: " + str(len(nombre_columnas_sqlite)))
            col2.table(nombre_columnas_sqlite)

            
            #Selecciona la opcion de copia de datos
            opcion1 = 'Borrar datos en tabla destino antes de copiar'
            opcion2 = 'Agregar datos a la tabla destino (no borrar)'

            opcion_copia = st.radio("¿Qué desea hacer durante la copia?",
                                    (opcion1, opcion2))
            
            
               
            #Instancio y controlo cuando se presione el boton
            if st.button("Exportar..."):
                #with st.spinner('Por favor aguarde, se están aplicando los cambios...'):
                    
                    st.write("Cargado excel en Dataframe...")
                    #cargo el resultado de la carga del dataframe y camntidad de registros
                    resultado_df = abrir_excel_en_dataframe(uploaded_file_origen, 
                                                            combobox_hojas)
                    
                    #Si se seleccionó borrar
                    if opcion_copia == opcion1:
                        with sqlite_connect(uploaded_file_destino) as conn:
                            
                            st.write("Borrada la tabla")
                            
                            crsr = conn[0].cursor()
                            crsr.execute("DELETE FROM " + combobox_tabla_destino + ";")
                            conn[0].commit()
                            
                            #Copio el dataframe directamente en la base de datos, 
                            #reescribiendo datos existentes
                        
                            resultado_df[0].to_sql(combobox_tabla_destino, 
                                      con=conn[0], 
                                      if_exists='replace', 
                                      index=False)
                            
                            st.write("Copiados " + str(resultado_df[1]) + " registros a la tabla")
                            
                            #Compacto la BD
                            st.write("Limpiando y Compactando Base de Datos...")                                                                
                            conn[0].execute("VACUUM")
                            
                            #Agrego el link para descargar el archivo
                            st.write("Generando link de descarga...")
                            st.markdown(get_binary_file_downloader_html(bin_file=conn[1], 
                                                                        file_label=str(uploaded_file_destino.name)), 
                                        unsafe_allow_html=True)
                            
                            
                    #Si se seleccionó agregar
                    else:
                         with sqlite_connect(uploaded_file_destino) as conn:
                             
                                           
                             #Copio el dataframe directamente en la base de datos, 
                             #agregando a los datos existentes
                             resultado_df[0].to_sql(combobox_tabla_destino, 
                                       con=conn[0], 
                                       if_exists='append', 
                                       index=False)
                             
                             st.write("Agregados " + str(resultado_df[1]) + " registros a la tabla")
                             
                             #Compacto la BD
                             st.write("Limpiando y Compactando Base de Datos...")
                             conn[0].execute("VACUUM")
                            
                             st.write("Generando link de descarga...")
                             #Agrego el link para descargar el archivo
                             st.markdown(get_binary_file_downloader_html(bin_file=conn[1], 
                                                                         file_label=str(uploaded_file_destino.name)), 
                                         unsafe_allow_html=True)
                        
                