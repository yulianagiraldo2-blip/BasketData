from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]

@st.cache_data
def partidos():
    return cargar('datos.csv', parse_dates=['fecha'])

@st.cache_data
def jugadores():
    return cargar('jugadores.csv')

def cargar(nombre, **kwargs):
    try:
        return pd.read_csv(ROOT / 'data' / nombre, **kwargs)
    except (OSError, ValueError) as error:
        st.error(
            f'No se pudo cargar {nombre}. '
            f'Revisa data/limpieza.ipynb. Detalle: {error}'
        )
        st.stop()