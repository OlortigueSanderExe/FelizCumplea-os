import streamlit as st  

# Configurar la página
st.set_page_config(page_title="FelizCumple", layout="wide")

# Cargar el contenido de los archivos
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

with open("styles.css", "r", encoding="utf-8") as f:
    css_code = f.read()

with open("script.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Incluir CSS dentro del HTML
html_code = f"""
    <style>{css_code}</style>
    {html_code}
    <script>{js_code}</script>
"""

# Mostrar el HTML en Streamlit
st.components.v1.html(html_code, height=800, scrolling=True)
