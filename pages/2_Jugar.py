from datetime import datetime
import streamlit as st
from utils.comun import iniciar,jugadores
from utils.juego import generar,NIVELES
iniciar('Jugar'); st.header('Adivina el jugador')
st.write('Identifica al jugador a partir de una actuación real. Elige una opción y confirma. No hay límite de tiempo.')
nivel=st.selectbox('Dificultad',list(NIVELES)); n,k,p=NIVELES[nivel]; st.caption(f'{n} preguntas · {k} pistas · {p} puntos por acierto')
if st.button('Nueva partida',type='primary'):
    try:
        preguntas=generar(jugadores(),nivel)
    except ValueError as error:
        st.error(str(error)); st.stop()
    st.session_state.partida={'uid':datetime.now().isoformat(),'nivel':nivel,'preguntas':preguntas,'i':0,'aciertos':0,'confirmada':False,'terminada':False}
g=st.session_state.get('partida')
if not g: st.info('Inicia una partida.'); st.stop()
n,k,p=NIVELES[g['nivel']]
if g['terminada']: st.success(f'Partida finalizada: {g["aciertos"]*p} de {n*p} puntos.'); st.stop()
i=g['i']; q=g['preguntas'][i]; st.progress(i/n); st.write(f'Nivel {g["nivel"]} | Pregunta {i+1}/{n} | Puntaje {g["aciertos"]*p}')
st.write(f'Partido del {q["fecha"]} · Equipo {q["equipo"]}')
for col,(nombre,valor) in zip(st.columns(k),q['pistas'].items()): col.metric(nombre.capitalize(),valor)
with st.form('respuesta'):
    respuesta=st.radio('¿Quién es el jugador?',q['opciones'],index=None,key=f"pregunta_{g['uid']}_{i}",disabled=g['confirmada']); confirmar=st.form_submit_button('Confirmar respuesta',disabled=g['confirmada'])
if confirmar:
    if respuesta is None: st.warning('Selecciona una opción.')
    else:
        g['confirmada']=True; g['correcta']=respuesta==q['respuesta']; g['aciertos']+=int(g['correcta']); st.rerun()
if g['confirmada']:
    if g['correcta']: st.success('¡Correcto!')
    else: st.error('Respuesta correcta: '+q['respuesta'])
    if st.button('Finalizar' if i+1==n else 'Siguiente pregunta'):
        if i+1==n:
            g['terminada']=True; st.session_state.historial.append({'fecha':datetime.now().isoformat(timespec='seconds'),'nivel':g['nivel'],'aciertos':g['aciertos'],'preguntas':n,'puntaje':g['aciertos']*p,'maximo':n*p})
        else: g['i']+=1; g['confirmada']=False
        st.rerun()
