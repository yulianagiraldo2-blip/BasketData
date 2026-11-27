from pathlib import Path
import pandas as pd
import streamlit as st
ROOT=Path(__file__).resolve().parents[1]
@st.cache_data
def partidos():
    return cargar('datos.csv', parse_dates=['fecha'])
@st.cache_data
def jugadores():
    return cargar('jugadores.csv')
def cargar(nombre, **kwargs):
    try:
        return pd.read_csv(ROOT/'data'/nombre, **kwargs)
    except (OSError, ValueError) as error:
        st.error(f'No se pudo cargar {nombre}. Ejecuta limpieza.ipynb desde la raíz del proyecto. Detalle: {error}')
        st.stop()
def iniciar(titulo):
    st.set_page_config(page_title=f'{titulo} | BasketData',layout='wide',page_icon='🏀')
    st.session_state.setdefault('historial',[])
    st.session_state.setdefault('consultados',[])
    with st.sidebar:
        st.image(str(ROOT/'assets/logo.png'),width=180)
        st.page_link('pages/0_Inicio.py',label='Inicio',icon='🏠')
        st.page_link('pages/1_Explorar.py',label='Explorar',icon='🔎')
        st.page_link('pages/2_Jugar.py',label='Jugar',icon='🎮')
        st.page_link('pages/3_Mis_datos.py',label='Mis datos',icon='👤')
    st.title(titulo)
