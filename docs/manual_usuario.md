\# Manual de usuario — BasketData



\## 1. Introducción



BasketData es una aplicación interactiva que permite consultar estadísticas históricas de la NBA y participar en un juego de identificación de jugadores.



\## 2. Ejecución local



Desde la carpeta principal del proyecto, ejecutar:



```bash

python -m pip install -r requirements.txt

python -m streamlit run app.py

```



Acceder desde el navegador a http://localhost:8501.



\## 3. Página Inicio



Presenta la descripción, los objetivos, la identidad visual y los créditos del proyecto.



\## 4. Página Explorar



Permite consultar partidos históricos, aplicar filtros, visualizar estadísticas y analizar información mediante gráficos interactivos.



\## 5. Página Jugar



El objetivo consiste en identificar a un jugador de la NBA mediante pistas obtenidas de actuaciones deportivas reales.



El usuario debe seleccionar la respuesta correcta entre cuatro opciones.



| Dificultad | Preguntas | Pistas por pregunta | Puntos por acierto | Puntuación máxima |

|---|---:|---:|---:|---:|

| Fácil | 5 | 6 | 20 | 100 |

| Intermedio | 10 | 4 | 10 | 100 |

| Difícil | 15 | 3 | 10 | 150 |



Las pistas pueden incluir puntos, rebotes, asistencias, minutos jugados, robos y bloqueos, dependiendo del nivel seleccionado.



\## 6. Página Mis datos



Permite consultar las puntuaciones, el historial de juego y el progreso registrado durante la sesión.



\## 7. Solución de problemas



\- Verificar que las dependencias estén instaladas.

\- Comprobar que los archivos CSV estén en la carpeta data/.

\- Ejecutar la aplicación mediante app.py.

\- Verificar que se esté utilizando el entorno de Python correspondiente.



\## 8. Fuente de datos



NBA Games — Nathan Lauga, Kaggle.



https://www.kaggle.com/datasets/nathanlauga/nba-games

