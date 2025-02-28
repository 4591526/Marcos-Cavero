# Cargar las librerias necesarias
import streamlit as st
import pandas as pd
import graphviz
import xml.etree.ElementTree as ET
from PIL import Image
import requests
from io import BytesIO


st.markdown(f'<h1 style="font-size: 42px; text-align: center; ">Los cuadernos de Marcos Cavero</h1>', unsafe_allow_html=True)

# Crear un family tree con graphviz 
st.write('''
    ## Árbol genealógico: Familia ...
    ''')

# Crear columnas para presentar escudos
col1, col2= st.columns([1, 1])

escudo1 = Image.open('escudo_familia_torre_tagle.jpg')
col1.image(escudo1, use_column_width=True)

escudo1 = Image.open('escudo1.jpg')
col2.image(escudo1, use_column_width=True)

# Crear un grafo con graphviz
dot = graphviz.Digraph()

# Agrupar los nodos de los ancestros
with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('G1', 'Gregorio Laureano Cavero de Céspedes')
    s.node('G2', 'Rosa María Vasquez de Acuña Iturguyen Amasa')
with dot.subgraph() as s:
    s.attr(rank='same')    
    s.node('G3', 'Ignacio Cavero Vásquez de Acuña')
    s.node('G4', 'Micaela de Tagle e Isásaga')
with dot.subgraph() as s:
    s.attr(rank='same')    
    s.node('G5', 'Ignacio Cavero Vásquez de Acuña (Tagle)')
    s.node('G6', 'Nicolasa de Valdiviezo')
with dot.subgraph() as s:
    s.attr(rank='same')    
    s.node('G7', 'Pedro Cavero de Frnancia Vázquez de Acuña')
    s.node('G8', 'Luisa Nuñez')

with dot.subgraph() as s:
    s.attr(rank='same')    
    s.node('G9', 'Mercedes Cavero Vazquez de Acuña Isasaga Valdiviezo y Nuñez')

# Conectar los nodos padres a hijos
dot.edge('G1', 'G3')
dot.edge('G2', 'G3')
dot.edge('G3', 'G5')
dot.edge('G4', 'G5')
dot.edge('G5', 'G7')
dot.edge('G6', 'G7')
dot.edge('G7', 'G9')
dot.edge('G8', 'G9')

st.graphviz_chart(dot)

# Los más recomendable es tener un df con la información de la familia y luego crear el grafo con graphviz
# La información de la familia puede extraerse de los metadatos de las transcripciones en xml

## st.image(image, caption='Digitalización', use_container_width=True)##

# Visualizar un html en streamlit
st.write('''
    ## Transcripciones
    ''')


# Download the image from the URL
url_image = 'https://drive.google.com/uc?export=download&id=1vBfdh2B8bwDfV9IlpErEgQ-9IZy7xS0z'
response = requests.get(url_image)
image = Image.open(BytesIO(response.content))

st.image(image, caption='Digitalización', use_container_width=True)

# Leer el contenido del archivo de texto desde la carpeta local
file_path = 'transcripciones/EAP1495_FDL-0438-IT001_002.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

st.text(content)
