"""Reglas y generación de preguntas a partir de actuaciones reales."""
import random
NIVELES={'Fácil':(5,6,20),'Intermedio':(10,4,10),'Difícil':(15,3,10)}
PISTAS=['puntos','rebotes','asistencias','minutos','robos','bloqueos']
def generar(datos,nivel):
    if nivel not in NIVELES: raise ValueError("Nivel desconocido.")
    n,k,_=NIVELES[nivel]
    candidatos=datos.loc[datos.puntos.ge(20)].drop_duplicates('jugador')
    if len(candidatos)<n: raise ValueError('No hay suficientes jugadores.')
    preguntas=[]
    for r in candidatos.sample(n).to_dict('records'):
        otros=datos.loc[(datos.temporada==r['temporada']) & (datos.jugador!=r['jugador']),'jugador'].unique().tolist()
        if len(otros)<3: raise ValueError("No hay suficientes opciones en la temporada.")
        opciones=random.sample(otros,3)+[r['jugador']]; random.shuffle(opciones)
        preguntas.append({'respuesta':r['jugador'],'opciones':opciones,'fecha':r['fecha'],'equipo':r['equipo'],'pistas':{p:r[p] for p in PISTAS[:k]}})
    return preguntas
