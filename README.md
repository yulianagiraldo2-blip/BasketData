

\# BasketData 🏀



\## Descripción del proyecto



BasketData es una aplicación académica interactiva desarrollada en Python y Streamlit, orientada al análisis de datos históricos de la NBA y al aprendizaje mediante la gamificación.



\## Objetivo



Facilitar la exploración de estadísticas deportivas y fortalecer el conocimiento sobre jugadores y equipos de baloncesto mediante herramientas interactivas y actividades recreativas.



\## Funcionalidades



\- Inicio: presentación e información del proyecto.

\- Explorar: consulta de partidos, filtros, estadísticas y gráficos interactivos.

\- Jugar: identificación de jugadores mediante pistas estadísticas reales.

\- Mis datos: historial de partidas, puntuaciones y progreso del usuario.



\## Niveles del juego



| Nivel | Preguntas | Pistas | Puntos por acierto |

|---|---|---|---|

| Fácil | 5 | 6 | 20 |

| Intermedio | 10 | 4 | 10 |

| Difícil | 15 | 3 | 10 |



\## Tecnologías utilizadas



\- Python 3.12

\- Streamlit

\- Pandas

\- NumPy

\- Matplotlib

\- Plotly

\- Jupyter Notebook

\- Git y GitHub



\## Estructura del proyecto



\- app.py: archivo principal.

\- pages/: páginas de la aplicación.

\- data/raw/: bases de datos originales.

\- data/limpieza.ipynb: procesamiento de datos.

\- data/datos.csv: partidos procesados.

\- data/jugadores.csv: estadísticas de jugadores.

\- src/: carga de datos y lógica del programa.

\- assets/: recursos gráficos.

\- docs/: documentación del proyecto.

\- actas/: actas de trabajo.

\- tests/: pruebas automatizadas.

\- .streamlit/: configuración visual.



\## Instalación en Windows mediante Git Bash



&#x20;   py -3.12 -m venv .venv312

&#x20;   source .venv312/Scripts/activate

&#x20;   python -m pip install -r requirements.txt



\## Ejecutar la aplicación



&#x20;   python -m streamlit run app.py



\## Ejecutar las pruebas



&#x20;   python tests/test\_proyecto.py



\## Procesamiento de datos



&#x20;   python -m pip install nbconvert ipykernel

&#x20;   python -m ipykernel install --user --name basketdata

&#x20;   python -m nbconvert --to notebook --execute --inplace --ExecutePreprocessor.kernel\_name=basketdata data/limpieza.ipynb



\## Fuente de los datos



NBA Games - Nathan Lauga.



https://www.kaggle.com/datasets/nathanlauga/nba-games



Proyecto con fines académicos y educativos. La redistribución de los datos está sujeta a las condiciones de su licencia original.



