# Cargar las librerias necesarias
import streamlit as st
import pandas as pd
import graphviz
import xml.etree.ElementTree as ET
from PIL import Image
import requests
from io import BytesIO


st.markdown(f'<h1 style="font-size: 42px; text-align: center; ">Los cuadernos de Marcos Cavero</h1>', unsafe_allow_html=True)

# Crear tres columnas, la del medio contendrá la imagen para centrarla
col1, col2 = st.columns([1, 1])

col1 = st.write('''
    ¿Quién es Cavero?
             
          ''')

col2 = st.empty()
    #st.image(nombre,  width=300, use_container_width=True)

# Crear un family tree con graphviz 
st.write('''
    ## Family Tree
    ''')

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

# Conectar los nodos padres a los abuelos
dot.edge('G1', 'G3')
dot.edge('G3', 'G5')
dot.edge('G5', 'G')

dot.node('C', 'Cavero')
dot.node('D', 'Hermano 1')
dot.node('E', 'Hermano 2')

# Conectar los nodos hijos al grupo de padres
dot.edge('A', 'C')
dot.edge('B', 'C')
dot.edge('A', 'D')
dot.edge('B', 'D')
dot.edge('A', 'E')
dot.edge('B', 'E')

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