# Cargar las librerias necesarias
import streamlit as st
import pandas as pd
import graphviz
import xml.etree.ElementTree as ET
from PIL import Image


st.markdown(f'<h1 style="font-size: 42px; text-align: center; ">Los cuadernos de Cavero</h1>', unsafe_allow_html=True)

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

# Agrupar los nodos abuelos
with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('G1', 'Abuelo Paterno')
    s.node('G2', 'Abuela Paterna')
    s.node('G3', 'Abuelo Materno')
    s.node('G4', 'Abuela Materna')

# Agrupar los nodos padres
with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('A', 'Padre de Cavero')
    s.node('B', 'Madre de Cavero')

# Conectar los nodos padres a los abuelos
dot.edge('G1', 'A')
dot.edge('G2', 'A')
dot.edge('G3', 'B')
dot.edge('G4', 'B')

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


image = Image.open('evt/data/images/single/cavero_15.jpg')
st.image(image, caption='Digitalización', use_container_width=True)


with open('Luisa1.txt', 'r', encoding='utf-8') as file:
    luisa1_content = file.read()

st.text(luisa1_content)