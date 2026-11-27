import streamlit as st
from utils.comun import iniciar,partidos,ROOT
iniciar('Inicio')
st.image(str(ROOT/'assets/banner.png'),use_container_width=True)
st.header('Bienvenido a BasketData')
st.write('Explora, analiza y juega con datos históricos de partidos de la NBA.')
d=partidos(); a,b,c=st.columns(3)
a.metric('Partidos',len(d)); b.metric('Equipos',len(set(d.local)|set(d.visitante))); c.metric('Temporadas',d.temporada.nunique())
for col,path,label,desc in zip(st.columns(3),['pages/1_Explorar.py','pages/2_Jugar.py','pages/3_Mis_datos.py'],['Explorar','Jugar','Mis datos'],['Consulta partidos y estadísticas.','Adivina el jugador.','Revisa tu progreso.']):
    with col:
        with st.container(border=True):
            st.subheader(label); st.write(desc); st.page_link(path,label='Abrir '+label)
st.subheader('Acerca de'); st.write('Proyecto académico de análisis de datos deportivos realizado por Yuliana Giraldo.')
st.subheader('Créditos y licencias'); st.markdown('Fuente: [NBA Games — Nathan Lauga, Kaggle](https://www.kaggle.com/datasets/nathanlauga/nba-games). Recursos gráficos originales generados con IA. Licencia de redistribución de datos pendiente de confirmación; no publicar los CSV sin verificarla.')
