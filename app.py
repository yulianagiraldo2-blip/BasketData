import streamlit as st

pagina = st.navigation([
    st.Page("pages/0_Inicio.py", title="Inicio", default=True),
    st.Page("pages/1_Explorar.py", title="Explorar"),
    st.Page("pages/2_Jugar.py", title="Jugar"),
    st.Page("pages/3_Mis_datos.py", title="Mis datos")
], position="hidden")

pagina.run()