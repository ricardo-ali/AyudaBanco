# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 09:11:03 2022

@author: tearil
"""
import streamlit as st
import pandas as pd

   
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(sep="|", header=False, index=False).encode('utf-8')


def completar_ceros(cadena, nros_chars):
    return '0'*(nros_chars - len(str(cadena))) + cadena

def completar_espacios(cadena, nros_chars):
       
    texto_inicial = (" "*(nros_chars - len(str(cadena))))
    
    texto_final = str(cadena) + str(texto_inicial)
    
    return texto_final

def check_obligatorio(cadena, num_char, flag_obligatorio):
    if cadena == " "*num_char or cadena == "0"*num_char or flag_obligatorio==True:
        return True


#%% CESE LABORAL - PRINCIPAL
def cese_laboral_principal():
    st.title('Cese Laboral')
    
        #%% DATOS INICIALES
    
    global csv
    flag_obligatorio = False
    csv = ""
    #creo un dataframe vacio para usar mas tarde
    columnas=[  "valor_sucursal",
                "valor_empresa",
                "valor_agente",
                "valor_apellido_nombre",
                "valor_tipo_persona",
                "valor_tipo_documento",
                "valor_numero_documento",
                "valor_cuil",
                "valor_calle_particular",
                "valor_numero_particular",
                "valor_piso_particular",
                "valor_dpto_particular",
                "valor_telefono_particular",
                "valor_localidad_particular",
                "valor_postal_particular",
                "valor_provincia_particular",
                "valor_filler",
                ]
    
        
    df_ = pd.DataFrame(columns=columnas)
    df_ = df_.fillna(0)
  
    # persist state of dataframe
    if 'df' not in st.session_state:
        st.session_state.df = df_

  
    
    with st.form("formulario_cese_laboral"):
            
        texto_label = ["(*) CASA (Sucursal) - Valor Numérico de 4 caracteres máximo",
                       "(*) EMPRESA (Servicio) - Valor Alfabético de 4 caracteres máximo",
                       "(*) CODIGO AGENTE - Valor Numérico de 9 caracteres máximo",
                       "(*) APELLIDO y NOMBRE DEL TITULAR - Valor Alfabético de 30 caracteres máximo",
                       "(*) TIPO DE PERSONA - Valor Numérico de 1 caracteres máximo",
                       "(*) TIPO DE DOCUMENTO",
                       "(*) NUMERO DE DOCUMENTO",
                       "(*) CUIL",
                       "(*) CALLE - Valor Alfabético de 15 caracteres máximo",
                       "NUMERO - Valor Alfabético de 5 caracteres máximo",
                       "PISO - Valor Alfabético de 2 caracteres máximo",
                       "DEPARTAMENTO - Valor Alfabético de 2 caracteres máximo",
                       "TELEFONO - Valor Alfabético de 8 caracteres máximo",
                       "(*) LOCALIDAD - Valor Alfabético de 15 caracteres máximo",
                       "(*) CODIGO POSTAL - Valor Numérico de 4 caracteres máximo", 
                       "(*) PROVINCIA - Valor Numérico de 3 caracteres máximo",
                       "FILLER  - Valor Alfabético de 13 caracteres máximo",
                       ]
                       
                               
        
        texto_tooltip = ["",
                         "",
                         "",
                         "",
                         "1 = Masculino, 2 = Femenino, 3 = Extranjero",
                         "",
                         "",
                         "",
                         "",
                         "De no existir integrar con S/N",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         "",
                         ]
                         
                         
                         
        
        
        num_chars = [4,4,9,30,1,2,8,15,15,5,2,2,8,15,4,3,13]
        
                
        tipo_persona = ["1","2","3"]
        
        tipo_documento = ["89","90","94","96","97"]
        
        provincia = ["001", "002", "003", "004", "005", "006", "007", "008",
                     "009", "010", "011", "012", "013", "014", "015", "016",
                     "017", "018", "019", "020", "021", "022","023","024"]
        
        #%% DATOS
                
        st.markdown("(*) Campos Obligatorios")
        
        n = 0
        valor_sucursal = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_sucursal = completar_ceros(valor_sucursal,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_sucursal, num_chars[n],flag_obligatorio)
        
        
        n = 1
        valor_empresa = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_empresa = completar_espacios(valor_empresa,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_empresa, num_chars[n],flag_obligatorio)
        
        n = 2
        valor_agente = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_agente = completar_ceros(valor_agente,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_agente, num_chars[n],flag_obligatorio)
        
        
        n = 3
        valor_apellido_nombre = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_apellido_nombre = completar_espacios(valor_agente,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_apellido_nombre, num_chars[n],flag_obligatorio)
        
                
        n = 4
        valor_tipo_persona = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=tipo_persona,
                                      key=n)
        valor_tipo_persona = completar_ceros(valor_tipo_persona,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_tipo_persona, num_chars[n],flag_obligatorio)
        
        
        n = 5
        valor_tipo_documento = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=tipo_documento,
                                      key=n)
        valor_tipo_documento = completar_ceros(valor_tipo_documento,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_tipo_documento, num_chars[n],flag_obligatorio)
        
        
        n = 6
        valor_numero_documento = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_numero_documento = completar_ceros(str(valor_numero_documento),num_chars[n])
        flag_obligatorio = check_obligatorio(valor_numero_documento, num_chars[n],flag_obligatorio)
                   
        
        n = 7
        valor_cuil = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_cuil = completar_espacios(valor_cuil,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_cuil, num_chars[n],flag_obligatorio)
        
        
        n = 8
        valor_calle_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_calle_particular = completar_espacios(valor_calle_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_calle_particular, num_chars[n],flag_obligatorio)
        
        
        n = 9
        valor_numero_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_numero_particular = completar_espacios(valor_numero_particular,num_chars[n])
                
        
        n = 10
        valor_piso_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_piso_particular = completar_espacios(valor_piso_particular,num_chars[n])
        
        
        
        n = 11
        valor_dpto_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_dpto_particular = completar_ceros(valor_dpto_particular,num_chars[n])
        
        
        
        n = 12
        valor_telefono_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_telefono_particular = completar_espacios(valor_telefono_particular,num_chars[n])
        
        
        
        n = 13
        valor_localidad_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_localidad_particular = completar_espacios(valor_localidad_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_localidad_particular, num_chars[n],flag_obligatorio)
        
        
        n = 14
        valor_postal_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_postal_particular = completar_ceros(valor_postal_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_postal_particular, num_chars[n],flag_obligatorio)
        
        
        n = 15
        valor_provincia_particular = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=provincia,
                                      key=n)
        valor_provincia_particular = completar_ceros(valor_provincia_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_provincia_particular, num_chars[n],flag_obligatorio)
        
        
        n = 16
        valor_filler = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_filler = completar_espacios(valor_filler,num_chars[n])
        
        
        #%% CHEQUEAR QUE INFO OBLIGATORIA
        nuevo_registro =  [ valor_sucursal,
                            valor_empresa,
                            valor_agente,
                            valor_apellido_nombre,
                            valor_tipo_persona,
                            valor_tipo_documento,
                            valor_numero_documento,
                            valor_cuil,
                            valor_calle_particular,
                            valor_numero_particular,
                            valor_piso_particular,
                            valor_dpto_particular,
                            valor_telefono_particular,
                            valor_localidad_particular,
                            valor_postal_particular,
                            valor_provincia_particular,
                            valor_filler,
                            ]
            
                        
        largo_texto = len(''.join(nuevo_registro))
        st.write("Cantidad de Caracteres en Bloque (debe ser 140): " + str(largo_texto))
        
        
        #%% AGREGAR A LA TABLA
        
        # Instancio el boton
        submitted = st.form_submit_button("Agregar")
        
        # cuando se presiona el boton agregar
        if submitted:
            if flag_obligatorio == True:
                st.markdown("### COMPLETAR TODOS LOS CAMPOS OBLIGATORIOS")
            else:                                    
                #Agrego la lista con los nuevos valores al dataframe
                #Si no uso el session_state, pierdo el historico agregado            
                st.session_state.df.loc[len(st.session_state.df)] = nuevo_registro
                
                #Muestro la tabla con los datos
                st.dataframe(st.session_state.df)    
                
                
                #Convierto a txt            
                csv = convert_df(st.session_state.df)
                
                #Le saco los separadores del tipo | para que sean
                csv = csv.replace(b'|',b'')
            
    
        #%% BOTON PARA DESCARGAR
    
    #agrego un boton para exportar a txt
    st.download_button(
                         label="Descargar como TXT",
                         data=csv,
                         file_name='cese_laboral.txt',
                         mime='text/plain',
                     )
                