import streamlit as st
import plotly.express as px
from src.comun import iniciar,partidos
iniciar('Explorar')
d=partidos(); st.write('Consulta y analiza partidos históricos de la NBA.')
a,b,c=st.columns(3)
s=a.multiselect('Temporada',sorted(d.temporada.unique())); e=b.multiselect('Equipo',sorted(set(d.local)|set(d.visitante))); f=c.date_input('Rango de fechas',(d.fecha.min().date(),d.fecha.max().date()),min_value=d.fecha.min().date(),max_value=d.fecha.max().date())
if s: d=d[d.temporada.isin(s)]
if e: d=d[d.local.isin(e)|d.visitante.isin(e)]
if isinstance(f, (tuple, list)) and len(f)==2: d=d[d.fecha.dt.date.between(*f)]
if d.empty: st.warning('No hay partidos para estos filtros.'); st.stop()
a,b,c=st.columns(3); a.metric('Partidos',len(d)); b.metric('Prom. local',f'{d.puntos_local.mean():.2f}'); c.metric('Prom. visitante',f'{d.puntos_visitante.mean():.2f}')
cols=['fecha','temporada','local','visitante','puntos_local','puntos_visitante','ganador']
sel=st.dataframe(d[cols],hide_index=True,use_container_width=True,on_select='rerun',selection_mode='single-row',key='tabla_'+str((s,e,f)))
if sel.selection.rows and sel.selection.rows[0] < len(d):
    r=d.iloc[sel.selection.rows[0]]; ident=int(r.id_partido)
    if ident not in st.session_state.consultados: st.session_state.consultados.append(ident)
    st.subheader(f'{r.local} {r.puntos_local:.0f} – {r.puntos_visitante:.0f} {r.visitante}'); st.write(f'Fecha: {r.fecha.date()} | Ganador: {r.ganador}'); st.write(f'Rebotes: {r.rebotes_local:.0f} / {r.rebotes_visitante:.0f}; asistencias: {r.asistencias_local:.0f} / {r.asistencias_visitante:.0f}')
a,b=st.columns(2)
v=d.ganador.value_counts().head(10).rename_axis('Equipo').reset_index(name='Victorias'); t=d.groupby('temporada',as_index=False).puntos_totales.mean()
a.plotly_chart(px.bar(v,x='Equipo',y='Victorias',title='Victorias registradas',color_discrete_sequence=['#FF7A00']),use_container_width=True)
b.plotly_chart(px.line(t,x='temporada',y='puntos_totales',markers=True,title='Puntos totales promedio por temporada',color_discrete_sequence=['#FF7A00']),use_container_width=True)
