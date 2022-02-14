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
 
#%% ALTA NOMINA - PRINCIPAL
def alta_nomina_principal():
    
    st.title('Alta en Nomina')
    
        #%% DATOS INICIALES
    
    global csv
    flag_obligatorio = False
    csv = ""
    #creo un dataframe vacio para usar mas tarde
    columnas=[  "valor_proceso",
                "valor_servicio",
                "valor_sucursal",
                "valor_agente",
                "valor_moneda",
                "valor_titularidad",
                "valor_limite_tarjeta",
                "valor_tipo_persona",
                "valor_apellido",
                "valor_nombre",
                "valor_tipo_documento",
                "valor_numero_documento",
                "valor_posicion_iva",
                "valor_tipo_clave_tributaria",
                "valor_clave_tributaria",
                "valor_fecha_nacimiento",
                "valor_nacionalidad",
                "valor_sexo",
                "valor_estado_civil",
                "valor_calle_particular",
                "valor_numero_particular",
                "valor_piso_particular",
                "valor_dpto_particular",
                "valor_postal_particular",
                "valor_localidad_particular",
                "valor_provincia_particular",
                "valor_telefono_particular",
                "valor_fax_particular",
                "valor_calle_laboral",
                "valor_numero_laboral",
                "valor_piso_laboral",
                "valor_dpto_laboral",
                "valor_postal_laboral",
                "valor_localidad_laboral",
                "valor_provincia_laboral",
                "valor_telefono_laboral",
                "valor_fax_laboral",
                "valor_tipo_persona_2",
                "valor_apellido_2",
                "valor_nombre_2",
                "valor_tipo_documento_2",
                "valor_numero_documento_2",
                "valor_posicion_iva_2",
                "valor_tipo_clave_tributaria_2",
                "valor_clave_tributaria_2",
                "valor_fecha_nacimiento_2",
                "valor_nacionalidad_2",
                "valor_sexo_2",
                "valor_estado_civil_2",
                "valor_calle_particular_2",
                "valor_numero_particular_2",
                "valor_piso_particular_2",
                "valor_dpto_particular_2",
                "valor_postal_particular_2",
                "valor_localidad_particular_2",
                "valor_provincia_particular_2",
                "valor_telefono_particular_2",
                "valor_fax_particular_2",
                "valor_calle_laboral_2",
                "valor_numero_laboral_2",
                "valor_piso_laboral_2",
                "valor_dpto_laboral_2",
                "valor_postal_laboral_2",
                "valor_localidad_laboral_2",
                "valor_provincia_laboral_2",
                "valor_telefono_laboral_2",
                "valor_fax_laboral_2",
                "valor_filler_laboral_2",
                "valor_lecop_laboral_2",
                "valor_filler2_laboral_2",
                "valor_marca_laboral_2"

                ]
                      
        
    df_ = pd.DataFrame(columns=columnas)
    df_ = df_.fillna(0)
  
    # persist state of dataframe
    if 'df' not in st.session_state:
        st.session_state.df = df_

  
    
    with st.form("formulario_alta"):
            
        texto_label = ["(*) PROCESO - Valor Alfabético de 2 caracteres máximo",
                       "(*) SERVICIO - Valor Alfabético de 4 caracteres máximo",
                       "(*) SUCURSAL - Valor Numérico de 4 caracteres máximo",
                       "(*) CODIGO AGENTE - Valor Numérico de 20 caracteres máximo",
                       "(*) MONEDA DE LA CUENTA",
                       "(*) TITULARIDAD",
                       "(*) LIMITE DE TARJETA - Valor Numérico de 2 caracteres máximo",
                       
                       "(*) TIPO DE PERSONA - Valor Alfabético de 1 caracteres máximo",
                       "(*) APELLIDO - Valor Alfabético de 40 caracteres máximo",
                       "(*) NOMBRE - Valor Alfabético de 40 caracteres máximo",
                       "(*) TIPO DE DOCUMENTO",
                       "(*) NUMERO DE DOCUMENTO",
                       "(*) POSICION ANTE EL IVA",
                       "(*) TIPO CLAVE TRIBUTARIA", 
                       "(*) NUMERO CLAVE TRIBUTARIA", 
                       "(*) FECHA DE NACIMIENTO",
                       "(*) NACIONALIDAD",
                       "(*) SEXO",
                       "(*) ESTADO CIVIL",
                       
                       "(*) CALLE - Valor Alfabético de 30 caracteres máximo",                       
                       "(*) NUMERO - Valor Alfabético de 6 caracteres máximo",
                       "PISO - Valor Alfabético de 3 caracteres máximo",
                       "DEPARTAMENTO - Valor Alfabético de 4 caracteres máximo",
                       "(*) CODIGO POSTAL - Valor Numérico de 5 caracteres máximo", 
                       "(*) LOCALIDAD - Valor Alfabético de 20 caracteres máximo",
                       "(*) CODIGO DE PROVINCIA - Valor Alfabético de 2 caracteres máximo",
                       "(*) TELEFONO - Valor Alfabético de 15 caracteres máximo",
                       "(*) FAX - Valor Alfabético de 15 caracteres máximo",
                       
                       "CALLE - Valor Alfabético de 30 caracteres máximo",                       
                       "NUMERO - Valor Alfabético de 6 caracteres máximo",
                       "PISO - Valor Alfabético de 3 caracteres máximo",
                       "DEPARTAMENTO - Valor Alfabético de 4 caracteres máximo",
                       "CODIGO POSTAL - Valor Numérico de 5 caracteres máximo", 
                       "LOCALIDAD - Valor Alfabético de 20 caracteres máximo",
                       "CODIGO DE PROVINCIA - Valor Alfabético de 2 caracteres máximo",
                       "TELEFONO - Valor Alfabético de 15 caracteres máximo",
                       "FAX - Valor Alfabético de 15 caracteres máximo",
                       
                       "TIPO DE PERSONA - Valor Alfabético de 1 caracteres máximo",
                       "APELLIDO - Valor Alfabético de 40 caracteres máximo",
                       "NOMBRE - Valor Alfabético de 40 caracteres máximo",
                       "TIPO DE DOCUMENTO",
                       "NUMERO DE DOCUMENTO",
                       "POSICION ANTE EL IVA",
                       "TIPO CLAVE TRIBUTARIA", 
                       "NUMERO CLAVE TRIBUTARIA", 
                       "FECHA DE NACIMIENTO",
                       "NACIONALIDAD",
                       "SEXO",
                       "ESTADO CIVIL",
                       
                       "CALLE - Valor Alfabético de 30 caracteres máximo",                       
                       "NUMERO - Valor Alfabético de 6 caracteres máximo",
                       "PISO - Valor Alfabético de 3 caracteres máximo",
                       "DEPARTAMENTO - Valor Alfabético de 4 caracteres máximo",
                       "CODIGO POSTAL - Valor Numérico de 5 caracteres máximo", 
                       "LOCALIDAD - Valor Alfabético de 20 caracteres máximo",
                       "CODIGO DE PROVINCIA - Valor Alfabético de 2 caracteres máximo",
                       "TELEFONO - Valor Alfabético de 15 caracteres máximo",
                       "FAX - Valor Alfabético de 15 caracteres máximo",
                       
                       "CALLE - Valor Alfabético de 30 caracteres máximo",                       
                       "NUMERO - Valor Alfabético de 6 caracteres máximo",
                       "PISO - Valor Alfabético de 3 caracteres máximo",
                       "DEPARTAMENTO - Valor Alfabético de 4 caracteres máximo",
                       "CODIGO POSTAL - Valor Numérico de 5 caracteres máximo", 
                       "LOCALIDAD - Valor Alfabético de 20 caracteres máximo",
                       "CODIGO DE PROVINCIA - Valor Alfabético de 2 caracteres máximo",
                       "TELEFONO - Valor Alfabético de 15 caracteres máximo",
                       "FAX - Valor Alfabético de 15 caracteres máximo",
                       "FILLER - Valor Alfabético de 23 caracteres máximo",
                       "CONVENIO EN LECOP - Valor Alfabético de 4 caracteres máximo",
                       "FILLER  - Valor Alfabético de 1 caracteres máximo",
                       "Marca Cliente YA existente OK (*) - Valor Alfabético de 1 caracteres máximo",

                       
                       ]
        
        
        texto_tooltip = ["Nombre del proceso al que se vincula la Empresa solicitante. Por ejemplo: JP; TR; AH; TF; etc.",
                         "Código de Ente según tabla 808. Se lo provee el BNA",
                         "Se informará el código correspondiente a la casa de radicación de la nueva cuenta. Ejemplo: Suc S.S. Jujuy corresponde el valor 3315",
                         "Numero del Beneficiario",
                         "Pesos o Dólares",
                         "SF = Sola Firma / OR = Orden recíproca",
                         "Limite según tabla 802",
                         
                         "Fijo “F” = persona física",
                         "",
                         "",
                         "",
                         "",
                         "Según tabla 4",
                         "Según tabla 5",
                         "",
                         "Formato Año Mes Dia de la forma AAAAMMDD",
                         "Según tabla 1",
                         "F = femenino / M = masculino",
                         "según tabla 2",
                         
                         "",
                         "De no existir escribir S/N",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "",
                         "",
                         "Según tabla 3",
                         "",
                         "",
                         
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         "Puede quedar en blanco este campo",
                         
                         ]
        
        
        num_chars = [2,4,4,20,1,2,2,
                     1,40,40,2,8,3,1,11,8,2,1,1,
                     30,6,3,4,5,20,2,15,15,
                     30,6,3,4,5,20,2,15,15,
                     1,40,40,2,8,3,1,11,8,2,1,1,
                     30,6,3,4,5,20,2,15,15,
                     30,6,3,4,5,20,2,15,15,23,4,1,1
                     
                     ]
        
        
        moneda = ["P", "D"] 
        
        titularidad = ["SF", "OR"]
        
        limite_tarjeta = list(range(1,21))
        
        tipo_persona = ["","F"]
        
        tipo_documento = ["","CF", "BA", "CT", "CD", "CR", "ER", "JJ", "MZ", "LR",
                          "ST", "SJ", "SL", "SF", "SE", "TC", "CC", "CH", "FM", 
                          "MS", "NQ", "LP", "RN", "SC", "TF", "LC", "LE", "DU",
                          "EX", "PA"]
        
        posicion_iva = ["","CFI", "EXE", "MOT", "NOR", "RIN", "RNI", "RNR"]
        
        clave_tributaria = ["",1,2,3,4,5]
        
        nacionalidad = ["","AA","AB","AD","AE","AF","AG","AI","AL","AM","AN",
                        "AO","AR","AS","AT","AU","AY","AZ","BA","BB","BD",
                        "BE","BG","BH","BI","BK","BL","BM","BN","BR","BS",
                        "BT","BV","BW","CA","CC","CD","CE","CF","CG","CH",
                        "CI","CM","CO","CP","CR","CS","CT","CU","CV","DJ",
                        "DM","DN","DY","EA","EC","EG","EL","EM","EN","EP",
                        "EQ","ER","ES","ET","EU","FA","FE","FF","FJ","FL",
                        "FN","FR","GA","GB","GD","GE","GG","GH","GN","GR",
                        "GT","GU","GY","HD","HG","HK","HT","ID","IH","II",
                        "IL","IM","IN","IO","IQ","IR","IS","IT","JD","JM",
                        "JP","KB","KG","KW","KY","KZ","LB","LC","LH","LI",
                        "LO","LR","LT","LU","LX","MA","MB","MC","MD","MF",
                        "MG","MI","ML","MN","MO","MR","MS","MT","MV","MW",
                        "MX","MY","MZ","NC","NG","NN","NP","NR","NZ","OA",
                        "OC","OE","OF","OM","OO","OR","OS","OT","OU","OZ",
                        "PA","PB","PE","PG","PL","PM","PO","PQ","PR","PU",
                        "QA","RA","RC","RD","RH","RM","RS","RU","RW","RY",
                        "SA","SC","SD","SE","SF","SG","SI","SJ","SK","SL",
                        "SM","SN","SO","SP","SR","SS","ST","SU","SV","SW",
                        "SY","SZ","TA","TG","TK","TL","TO","TQ","TT","TU",
                        "TW","TY","TZ","UC","UG","UK","UN","UR","VA","VN",
                        "VT","YG","ZA","ZR","ZW"]
        
        sexo = ["","F", "M"]
        
        estado_civil = ["", "C","D","H","L","S","V","X"]
        
        provincia = ["", "CF", "BA", "CT", "CD", "CR", "ER", "JJ", "MZ", "LR",
                     "ST", "SJ", "SL", "SF", "SE", "TC", "CC", "CH", "FM", 
                     "MS", "NQ", "LP", "RN", "SC", "TF"]
        
        #%% DATOS BANCARIOS
        
        st.markdown("### DATOS BANCARIOS")
        st.markdown("(*) Campos Obligatorios")
        
        n = 0
        valor_proceso = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_proceso = completar_espacios(valor_proceso,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_proceso, num_chars[n],flag_obligatorio)
        
        
        n = 1
        valor_servicio = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_servicio = completar_espacios(valor_servicio,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_servicio, num_chars[n],flag_obligatorio)
        
        n = 2
        valor_sucursal = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_sucursal = completar_espacios(valor_sucursal,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_sucursal, num_chars[n],flag_obligatorio)
        
        
        n = 3
        valor_agente = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_agente = completar_ceros(valor_agente,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_agente, num_chars[n],flag_obligatorio)
        
                
        n = 4
        valor_moneda = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=moneda,
                                      key=n)
        valor_moneda = completar_espacios(valor_moneda,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_moneda, num_chars[n],flag_obligatorio)
        
        
        n = 5
        valor_titularidad = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=titularidad,
                                      key=n)
        valor_titularidad = completar_espacios(valor_titularidad,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_titularidad, num_chars[n],flag_obligatorio)
        
        
        n = 6
        valor_limite_tarjeta = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=limite_tarjeta,
                                      key=n)
        valor_limite_tarjeta = completar_ceros(str(valor_limite_tarjeta),num_chars[n])
        flag_obligatorio = check_obligatorio(valor_limite_tarjeta, num_chars[n],flag_obligatorio)
        
        
        #%% DATOS PERSONALES
        
        st.markdown("### DATOS PERSONALES")
        st.markdown("(*) Campos Obligatorios")
        
        n = 7
        valor_tipo_persona = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=tipo_persona,
                                      key=n)
        valor_tipo_persona = completar_espacios(valor_tipo_persona,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_tipo_persona, num_chars[n],flag_obligatorio)
        
        
        n = 8
        valor_apellido = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_apellido = completar_espacios(valor_apellido,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_apellido, num_chars[n],flag_obligatorio)
        
        
        n = 9
        valor_nombre = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_nombre = completar_espacios(valor_nombre,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_nombre, num_chars[n],flag_obligatorio)
        
        
        n = 10
        valor_tipo_documento = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=tipo_documento,
                                      key=n)
        valor_tipo_documento = completar_espacios(valor_tipo_documento,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_tipo_documento, num_chars[n],flag_obligatorio)
        
        
        n = 11
        valor_numero_documento = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_numero_documento = completar_ceros(valor_numero_documento,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_numero_documento, num_chars[n],flag_obligatorio)
        
        
        n = 12
        valor_posicion_iva = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=posicion_iva,
                                      key=n)
        valor_posicion_iva = completar_espacios(valor_posicion_iva,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_posicion_iva, num_chars[n],flag_obligatorio)
        
        
        n = 13
        valor_tipo_clave_tributaria = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=clave_tributaria,
                                      key=n)
        valor_tipo_clave_tributaria = completar_espacios(valor_tipo_clave_tributaria,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_tipo_clave_tributaria, num_chars[n],flag_obligatorio)
        
        
        n = 14
        valor_clave_tributaria = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_clave_tributaria = completar_ceros(valor_clave_tributaria,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_clave_tributaria, num_chars[n],flag_obligatorio)
        
        
        n = 15
        valor_fecha_nacimiento = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_fecha_nacimiento = completar_ceros(valor_fecha_nacimiento,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_fecha_nacimiento, num_chars[n],flag_obligatorio)
        
        
        n = 16
        valor_nacionalidad = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=nacionalidad,
                                      key=n)
        valor_nacionalidad = completar_espacios(valor_nacionalidad,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_nacionalidad, num_chars[n],flag_obligatorio)
        
        
        n = 17
        valor_sexo = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=sexo,
                                      key=n)
        valor_sexo = completar_espacios(valor_sexo,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_sexo, num_chars[n],flag_obligatorio)
        
        
        n = 18
        valor_estado_civil = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=estado_civil,
                                      key=n)
        valor_estado_civil = completar_espacios(valor_estado_civil,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_estado_civil, num_chars[n],flag_obligatorio)
        
        
        #%% DOMICILIO PARTICULAR
        
        st.markdown("### DOMICILIO PARTICULAR")
        st.markdown("(*) Campos Obligatorios")
        
        n = 19
        valor_calle_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_calle_particular = completar_espacios(valor_calle_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_calle_particular, num_chars[n],flag_obligatorio)
        
        
        n = 20
        valor_numero_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_numero_particular = completar_espacios(valor_numero_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_numero_particular, num_chars[n],flag_obligatorio)
        
        
        n = 21
        valor_piso_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_piso_particular = completar_espacios(valor_piso_particular,num_chars[n])
        
        
        n = 22
        valor_dpto_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_dpto_particular = completar_espacios(valor_dpto_particular,num_chars[n])
        
        
        n = 23
        valor_postal_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_postal_particular = completar_ceros(valor_postal_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_postal_particular, num_chars[n],flag_obligatorio)

        
        n = 24
        valor_localidad_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_localidad_particular = completar_espacios(valor_localidad_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_localidad_particular, num_chars[n],flag_obligatorio)
        
        
        n = 25
        valor_provincia_particular = st.selectbox(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      options=provincia,
                                      key=n)
        valor_provincia_particular = completar_espacios(valor_provincia_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_provincia_particular, num_chars[n],flag_obligatorio)


        n = 26
        valor_telefono_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_telefono_particular = completar_espacios(valor_telefono_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_telefono_particular, num_chars[n],flag_obligatorio)


        n =27
        valor_fax_particular = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_fax_particular = completar_espacios(valor_fax_particular,num_chars[n])
        flag_obligatorio = check_obligatorio(valor_fax_particular, num_chars[n],flag_obligatorio)
        
        #%% DOMICILIO LABORAL
        st.markdown("### DOMICILIO LABORAL")
        
        n = 28
        valor_calle_laboral = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_calle_laboral = completar_espacios(valor_calle_laboral,num_chars[n])   
        
        
        n = 29
        valor_numero_laboral = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_numero_laboral = completar_espacios(valor_numero_laboral,num_chars[n])   
        
        
        n = 30
        valor_piso_laboral = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_piso_laboral = completar_espacios(valor_piso_laboral,num_chars[n])
        
        
        n = 31
        valor_dpto_laboral = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_dpto_laboral = completar_espacios(valor_dpto_laboral,num_chars[n])
        
        
        n = 32
        valor_postal_laboral = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_postal_laboral = completar_ceros(valor_postal_laboral,num_chars[n])


        n = 33
        valor_localidad_laboral = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_localidad_laboral = completar_espacios(valor_localidad_laboral,num_chars[n])
        
        
        n = 34
        valor_provincia_laboral = st.selectbox(label=texto_label[n], 
                                                  options=provincia,
                                                  help=texto_tooltip[n],
                                                  key=n)
        valor_provincia_laboral = completar_espacios(valor_provincia_laboral,num_chars[n])


        n = 35
        valor_telefono_laboral = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_telefono_laboral = completar_espacios(valor_telefono_laboral,num_chars[n])


        n = 36
        valor_fax_laboral = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_fax_laboral = completar_espacios(valor_fax_laboral,num_chars[n]) 
        
        
        #%% DATOS 2do TITULAR
        st.markdown("### DATOS 2do TITULAR")
        
        n = 37
        valor_tipo_persona_2 = st.selectbox(label=texto_label[n], 
                                         options=tipo_persona,
                                         help=texto_tooltip[n],
                                         key=n)
        valor_tipo_persona_2 = completar_espacios(valor_tipo_persona_2,num_chars[n]) 
        
        
        n = 38
        valor_apellido_2 = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_apellido_2 = completar_espacios(valor_apellido_2,num_chars[n]) 
        
        
        n = 39
        valor_nombre_2 = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_nombre_2 = completar_espacios(valor_nombre_2,num_chars[n]) 
        
        
        n = 40
        valor_tipo_documento_2 = st.selectbox(label=texto_label[n], 
                                         options=tipo_documento,
                                         help=texto_tooltip[n],
                                         key=n)
        valor_tipo_documento_2 = completar_espacios(valor_tipo_documento_2,num_chars[n]) 
        
        
        n = 41
        valor_numero_documento_2 = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_numero_documento_2 = completar_ceros(valor_numero_documento_2,num_chars[n])
        
        
        n = 42
        valor_posicion_iva_2 = st.selectbox(label=texto_label[n], 
                                         options=posicion_iva,
                                         help=texto_tooltip[n],
                                         key=n)
        valor_posicion_iva_2 = completar_espacios(valor_posicion_iva_2,num_chars[n]) 
        
        n = 43
        valor_tipo_clave_tributaria_2 = st.selectbox(label=texto_label[n], 
                                         options=clave_tributaria,
                                         help=texto_tooltip[n],
                                         key=n)
        valor_tipo_clave_tributaria_2 = completar_ceros(valor_tipo_clave_tributaria_2,num_chars[n])
        
        
        n = 44
        valor_clave_tributaria_2 = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_clave_tributaria_2 = completar_ceros(valor_clave_tributaria_2,num_chars[n])
        
        
        n = 45
        valor_fecha_nacimiento_2 = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_fecha_nacimiento_2 = completar_ceros(valor_fecha_nacimiento_2,num_chars[n])
        
        
        n = 46
        valor_nacionalidad_2 = st.selectbox(label=texto_label[n], 
                                         options=nacionalidad,
                                         help=texto_tooltip[n],
                                         key=n)
        valor_nacionalidad_2 = completar_espacios(valor_nacionalidad_2,num_chars[n])
        
        
        n = 47
        valor_sexo_2 = st.selectbox(label=texto_label[n], 
                                         options=sexo,
                                         help=texto_tooltip[n],
                                         key=n)
        valor_sexo_2 = completar_espacios(valor_sexo_2,num_chars[n])
        
        
        n = 48
        valor_estado_civil_2 = st.selectbox(label=texto_label[n], 
                                         options=estado_civil,
                                         help=texto_tooltip[n],
                                         key=n)
        valor_estado_civil_2 = completar_espacios(valor_estado_civil_2,num_chars[n])
        
        
        #%% DOMICILIO PARTICULAR 2do TITULAR
        
        st.markdown("### DOMICILIO PARTICULAR 2do TITULAR")
                
        n = 49
        valor_calle_particular_2 = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_calle_particular_2 = completar_espacios(valor_calle_particular_2,num_chars[n])
        
        
        n = 50
        valor_numero_particular_2 = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_numero_particular_2 = completar_espacios(valor_numero_particular_2,num_chars[n])
        
        
        n = 51
        valor_piso_particular_2 = st.text_input(label=texto_label[n], 
                                      help=texto_tooltip[n],
                                      max_chars=num_chars[n],
                                      key=n)
        valor_piso_particular_2 = completar_espacios(valor_piso_particular_2,num_chars[n])
        
        
        n = 52
        valor_dpto_particular_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_dpto_particular_2 = completar_espacios(valor_dpto_particular_2,num_chars[n])
        
        
        
        n = 53
        valor_postal_particular_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_postal_particular_2 = completar_ceros(valor_postal_particular_2,num_chars[n])
        
        
        n = 54
        valor_localidad_particular_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_localidad_particular_2 = completar_espacios(valor_localidad_particular_2,num_chars[n])
        
        
        n = 55
        valor_provincia_particular_2 = st.selectbox(label=texto_label[n], 
                                                  options=provincia,
                                                  help=texto_tooltip[n],
                                                  key=n)
        valor_provincia_particular_2 = completar_espacios(valor_provincia_particular_2,num_chars[n])


        n = 56
        valor_telefono_particular_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_telefono_particular_2 = completar_espacios(valor_telefono_particular_2,num_chars[n])


        n = 57
        valor_fax_particular_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_fax_particular_2 = completar_espacios(valor_fax_particular_2,num_chars[n])     
        
        
        
        #%% DOMICILIO LABORAL 2do TITULAR
        st.markdown("### DOMICILIO LABORAL 2do TITULAR")
        
        n = 58
        valor_calle_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_calle_laboral_2 = completar_espacios(valor_calle_laboral_2,num_chars[n])
        
        
        n = 59
        valor_numero_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_numero_laboral_2 = completar_espacios(valor_numero_laboral_2,num_chars[n])
        
        
        n = 60
        valor_piso_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_piso_laboral_2 = completar_espacios(valor_piso_laboral_2,num_chars[n])
        
        
        n = 61
        valor_dpto_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_dpto_laboral_2 = completar_espacios(valor_dpto_laboral_2,num_chars[n])
        
        
        n = 62
        valor_postal_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_postal_laboral_2 = completar_ceros(valor_postal_laboral_2,num_chars[n])


        n = 63
        valor_localidad_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_localidad_laboral_2 = completar_espacios(valor_localidad_laboral_2,num_chars[n])
        
        
        n = 64
        valor_provincia_laboral_2 = st.selectbox(label=texto_label[n], 
                                                  options=provincia,
                                                  help=texto_tooltip[n],
                                                  key=n)
        valor_provincia_laboral_2 = completar_espacios(valor_provincia_laboral_2,num_chars[n])


        n = 65
        valor_telefono_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_telefono_laboral_2 = completar_espacios(valor_telefono_laboral_2,num_chars[n])
        

        n = 66
        valor_fax_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_fax_laboral_2 = completar_espacios(valor_fax_laboral_2,num_chars[n])
        
        
        n = 67
        valor_filler_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_filler_laboral_2 = completar_espacios(valor_filler_laboral_2,num_chars[n])
        
        
        n = 68
        valor_lecop_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_lecop_laboral_2 = completar_espacios(valor_lecop_laboral_2,num_chars[n])
        
        
        n = 69
        valor_filler2_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_filler2_laboral_2 = completar_espacios(valor_filler2_laboral_2,num_chars[n])
        
        
        n = 70
        valor_marca_laboral_2 = st.text_input(label=texto_label[n], 
                                               help=texto_tooltip[n],
                                               max_chars=num_chars[n],
                                               key=n)
        valor_marca_laboral_2 = completar_espacios(valor_marca_laboral_2,num_chars[n])
        
        #%% CHEQUEAR QUE INFO OBLIGATORIA
        nuevo_registro =  [valor_proceso,
                           valor_servicio,
                           valor_sucursal,
                           valor_agente,
                           valor_moneda,
                           valor_titularidad,
                           valor_limite_tarjeta,
                           
                           valor_tipo_persona,
                           valor_apellido,
                           valor_nombre,
                           valor_tipo_documento,
                           valor_numero_documento,
                           valor_posicion_iva,
                           valor_tipo_clave_tributaria,
                           valor_clave_tributaria,
                           valor_fecha_nacimiento,
                           valor_nacionalidad,
                           valor_sexo,
                           valor_estado_civil,
                           
                           valor_calle_particular,
                           valor_numero_particular,
                           valor_piso_particular,
                           valor_dpto_particular,
                           valor_postal_particular,
                           valor_localidad_particular,
                           valor_provincia_particular,
                           valor_telefono_particular,
                           valor_fax_particular,
                           
                           valor_calle_laboral,
                           valor_numero_laboral,
                           valor_piso_laboral,
                           valor_dpto_laboral,
                           valor_postal_laboral,
                           valor_localidad_laboral,
                           valor_provincia_laboral,
                           valor_telefono_laboral,
                           valor_fax_laboral,
                       
                           valor_tipo_persona_2,
                           valor_apellido_2,
                           valor_nombre_2,
                           valor_tipo_documento_2,
                           valor_numero_documento_2,
                           valor_posicion_iva_2,
                           valor_tipo_clave_tributaria_2,
                           valor_clave_tributaria_2,
                           valor_fecha_nacimiento_2,
                           valor_nacionalidad_2,
                           valor_sexo_2,
                           valor_estado_civil_2,
                       
                           valor_calle_particular_2,
                           valor_numero_particular_2,
                           valor_piso_particular_2,
                           valor_dpto_particular_2,
                           valor_postal_particular_2,
                           valor_localidad_particular_2,
                           valor_provincia_particular_2,
                           valor_telefono_particular_2,
                           valor_fax_particular_2,
                           
                           valor_calle_laboral_2,
                           valor_numero_laboral_2,
                           valor_piso_laboral_2,
                           valor_dpto_laboral_2,
                           valor_postal_laboral_2,
                           valor_localidad_laboral_2,
                           valor_provincia_laboral_2,
                           valor_telefono_laboral_2,
                           valor_fax_laboral_2,
                           
                           valor_filler_laboral_2,
                           valor_lecop_laboral_2,
                           valor_filler2_laboral_2,
                           valor_marca_laboral_2,
            
                        ]
        
        largo_texto = len(''.join(nuevo_registro))
        st.write("Cantidad de Caracteres en Bloque: " + str(largo_texto))
        
        
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
                         file_name='alta_nomina.txt',
                         mime='text/plain',
                     )
                        
                