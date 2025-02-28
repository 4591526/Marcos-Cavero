# Cargar las librerias necesarias
import streamlit as st #permite generar una aplicación web interactiva
import pandas as pd # trabajar con df ya sea excel o csv
import graphviz # librería que permite realizar diagramas y árboles
import xml.etree.ElementTree as ET # permite trabajar con xml
from PIL import Image # trabajar con imágenes
import requests # permite realizar tareas como abrir archivos en la red
from io import BytesIO # permite trabajar con archivos web 


st.markdown(f'<h1 style="font-size: 42px; text-align: center; ">Los cuadernos de Marcos Cavero</h1>', unsafe_allow_html=True)

# Crear un family tree con graphviz 
st.write('''
    ## Los escudos familiares ...
    ''')

# Crear columnas para presentar escudos
col1, col2= st.columns([1, 1])

escudo1 = Image.open('escudo_familia_torre_tagle.jpg')
col1.image(escudo1, use_container_width=True)

escudo1 = Image.open('escudo1.jpg')
col2.image(escudo1, use_container_width=True)

# Crear un family tree con graphviz 
st.write('''
    ## Árbol genealógico: Familia ...
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
    s.node('G7', 'Pedro Cavero de Francia Vázquez de Acuña')
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
    ## Nube de palabras con las transcripciones realizadas
    ''')

# Agregar los gráficos de Voyant
voyant = Image.open('nube_50.jpg')
st.image(voyant, use_container_width=True)

st.link_button("Vamos a Voyant", "https://voyant-tools.org/?corpus=9efe3bd682773679efe0b026e8218603")

# Visualizar un html en streamlit
st.write('''
    ## Transcripciones
    ''')

## Visualizador html (iamgen + xml)
## Tomar todas imágenes del drive y tomar los archivos txt
## generar un selectbox en cual si uno selecciona el nombre de un archivo o tópicos pueda acceder a la imagen junto con la transcripción

# Download the image from the URL
url_image = 'https://drive.google.com/uc?export=download&id=1vBfdh2B8bwDfV9IlpErEgQ-9IZy7xS0z'
response = requests.get(url_image)
image = Image.open(BytesIO(response.content))

st.image(image, caption='Digitalización', use_container_width=True)

# Agregar el txt de la digitalización 
st.write('''
    CCLX. \\
    Emito: El 30 de No- \\
    viembre de 1539 erige Francisco \\
    Pizarro la Gobernación de Quito \\
    que Comprendia esta provincia, \\
    los territorios de Pasto y Po- \\
    payán y de todo cuanto más \\
    se discubriese al oriente de \\
    la Cordillera de estas regiones, \\
    y nombra hora servirla á su \\
    hermano Gonzalo Pizarro \\
    La Republica dominicana \\
    ó de Santo Domingo se inde- \\
    pendizó de España el 30 de \\
    Noviembre de 1821 \\
    El Ferrocarril de Lima á \\
    Chorrillos se entregó al tráfico \\
    publico el 30 de Nobre de 1858 \\
    Oyanguren en of. 33 acusaba recibo de \\
    los manifiestos de julio, pero se olvida \\
    de qe las tiene y en inalavibr ama, de 13 de \\
    Novbre. los reclama, Quitio. 
''')

# Leer el contenido del archivo de texto desde la carpeta local
#file_path = 'transcripciones/EAP1495_FDL-0438-IT001_002.txt'
#with open(file_path, 'r', encoding='utf-8') as file:
    #content = file.read()

#st.text(content)
