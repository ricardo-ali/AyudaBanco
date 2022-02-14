# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:13:11 2021

@author: tearil
"""

#%% LIBRERIAS
import streamlit as st

import alta_nomina, cese_laboral


#%% APLICACION PRINCIPAL


#Configuracion general de la pagina
st.set_page_config(
     page_title="AyudaBanco",
     page_icon=":bank:",
     layout="wide",
     initial_sidebar_state="expanded"
 )

#Agrego la Barra lateral para seleccionar la aplicacion a usar
aplicaciones = ['Alta Nomina',]
                #'Cese Laboral']


barra_lateral = st.sidebar.title("Ayuda Banco")
barra_lateral = st.sidebar.selectbox(
                 'Seleccione la aplicación:',
                 (aplicaciones))


#%% ALTA NOMINA
if barra_lateral == aplicaciones[0]:
    
    #Va al archivo alta_nomina.py
    alta_nomina.alta_nomina_principal()
    
    
#%% CESE LABORAL
elif barra_lateral == aplicaciones[1]:
    
    #Va al archivo cese_laboral.py
    cese_laboral.cese_laboral_principal()
        
   
   
    
    
    
    