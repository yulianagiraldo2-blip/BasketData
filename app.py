import streamlit as st

pagina = st.navigation([
    st.Page("pages/inicio.py", title="Inicio", default=True),
    st.Page("pages/explorar.py", title="Explorar"),
    st.Page("pages/jugar.py", title="Jugar"),
    st.Page("pages/mis_datos.py", title="Mis datos")
], position="hidden")

pagina.run()