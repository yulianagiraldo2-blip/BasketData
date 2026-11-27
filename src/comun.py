from pathlib import Path
import streamlit as st
from src.data import partidos, jugadores, cargar

ROOT = Path(__file__).resolve().parents[1]

def iniciar(titulo):
    st.set_page_config(
        page_title=f'{titulo} | BasketData',
        layout='wide',
        page_icon='🏀'
    )

    st.session_state.setdefault('historial', [])
    st.session_state.setdefault('consultados', [])

    with st.sidebar:
        st.image(str(ROOT / 'assets/logo.png'), width=180)

        st.page_link('pages/inicio.py',
                     label='Inicio', icon='🏠')

        st.page_link('pages/explorar.py',
                     label='Explorar', icon='🔎')

        st.page_link('pages/jugar.py',
                     label='Jugar', icon='🎮')

        st.page_link('pages/mis_datos.py',
                     label='Mis datos', icon='👤')

    st.title(titulo)