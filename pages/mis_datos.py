import pandas as pd
import streamlit as st
import plotly.express as px
from src.comun import iniciar
iniciar('Mis datos'); h=st.session_state.historial; c=st.columns(4)
c[0].metric('Partidas',len(h)); c[1].metric('Puntaje acumulado',sum(x['puntaje'] for x in h)); c[2].metric('Mejor puntaje',max((x['puntaje'] for x in h),default=0)); c[3].metric('Partidos consultados',len(st.session_state.consultados))
if not h: st.info('Todavía no has finalizado partidas.')
else:
    d=pd.DataFrame(h); d['partida']=range(1,len(d)+1); d['porcentaje']=100*d.puntaje/d.maximo
    st.dataframe(d,hide_index=True); st.plotly_chart(px.line(d,x='partida',y='porcentaje',markers=True,title='Progreso (% del máximo)',color_discrete_sequence=['#FF7A00']))
if st.session_state.consultados: st.write('Identificadores consultados:',st.session_state.consultados)
st.caption('Los datos se conservan durante la sesión actual.')
