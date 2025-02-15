# -*- coding: utf-8 -*-
"""TFG NITRATOS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RnYU1zvo3JsrPIah0xqiN2XATfSpWzHk

> Elaborado por: Geóg. Godofredo Rojas Mata

# **Proyecto Nitratos**

##### **Información importante**

<p align="justify">La información que es encuentra en este codigo esta basado en la problematica que esta viviendo las poblaciones del norte de Cartago, sobre la contaminacion de nitrato en las nacientes de los cantones de Alvarado, Cartago, Paraiso y Oreamuno.

<p align="justify">Se tomaron los datos que se estan actualizacion para el proyecto de tesis denominado “Seguimiento de la contaminación con nitratos en los acuíferos de la región norte de la provincia de Cartago mediante herramientas de software geoespacial”.

<p align="justify">A menudo, un aumento en la concentración de nitratos en el agua es causado por actividades antropológicas. Los grandes contribuyentes pueden ser la fertilización excesiva de las tierras agrícolas y la fuga contaminada de aguas residuales domésticas. La falta de conocimiento sobre el uso de pesticidas y fertilizantes puede ser una razón de los problemas, así como fallas en el sistema de descarga doméstico. A menudo se utilizan tanques escépticos, pero los desechos no se tratan en consecuencia. El fertilizante contiene amonio, que se convertirá en su forma más estable, nitrato. Algunos fertilizantes ya tienen el compuesto de nitrato en forma de nitrato de amoníaco. Este nitrato puede escurrirse a cuerpos de agua o filtrarse al suelo y contaminar el agua subterránea en el acuífero. Otra causa de las altas concentraciones de nitratos puede ser el tratamiento insuficiente de las aguas residuales.

> *Portales y noticias relacionados con la tematica*

*   [DELFT](https://repository.tudelft.nl/islandora/object/uuid%3Ad79fab47-f203-4de2-aee6-047c92f67afd)
*   [Contaminación de fuentes de agua en dos comunidades de Oreamuno de Cartago](https://www.facebook.com/watch/?v=1098798327384633)

*   [Caso sobre agua contaminada con pesticida en Cartago llega hasta Europa](https://www.larepublica.net/noticia/caso-sobre-agua-contaminada-con-pesticida-en-cartago-llega-hasta-europa)
*   [Salud clausura cinco nacientes más en Cartago por contaminación con clorotalonil](https://semanariouniversidad.com/pais/salud-clausura-cinco-nacientes-mas-en-cartago-por-contaminacion-con-clorotalonil/)

*   [Salud clausura cinco nacientes más en Cartago por contaminación con clorotalonil](https://delfino.cr/2023/09/50-mil-personas-firman-peticion-para-prohibir-plaguicida-relacionado-a-contaminacion-de-agua-en-cartago)
*   [AYA dice que puede ser “imposible” resolver problema de agua contaminada en Cartago](https://www.crhoy.com/nacionales/aya-dice-que-puede-ser-imposible-resolver-problema-de-agua-contaminada-en-cartago/)
"""

# Commented out IPython magic to ensure Python compatibility.
# #@title Plaguicidas en Costa Rica: salud versus intereses económicos
# %%html
# <iframe width="1280" height="720" src="https://www.youtube.com/embed/iNmJu4dMIgw" title="Plaguicidas en Costa Rica: salud versus intereses económicos" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

"""###### Carga de paquetes

Instalacion de paquetes y librerias
"""

# Carga de plotly express
import plotly.express as px

# Carga de plotly figure factory,
# para tipos adicionales de gráficos
import plotly.figure_factory as ff

# Carga de pandas
import pandas as pd

"""###### Carga de los archivos csv del proyecto y graficación por medio de la biblioteca plotly"""

#Carga de archivos csv
#realizamos el proceso en orden, cargando una tabla generando su visualización y posteriormente lo hacemos con la siguiente
#cargamos la tabla de distritos

from google.colab import files
file = files.upload()

distritos= pd.read_csv("/content/Limite_distrital_5k_ABRIL_2022.csv",sep=",")
distritos

# Información general sobre nuestro csv
distritos.info()

# Reducción de columnas
distritos = distritos[["codigo_dta", "provincia", "canton", "distrito", "cod_provin", "area"]]

# Cambio de nombre de las columnas a minúsculas y a nombres más claros
distritos = distritos.rename(columns={"codigo_dta": "Código Distrito",
                                              "provincia": "Provincia",
                                              "canton": "Cantón",
                                              "distrito": "Distrito",
                                              "cod_provin": "Código Provincia",
                                              "area": "Área"})

# Selección de los distritos de Cartago para su visualización como tabla
distritos[distritos["Código Provincia"] == 3]

"""<p align="justify">Determinar los distritos de Cartago permite realizar el primer cruce de información, determinando valor de importancia para el cruce de variables que se requiere y determinar los distritos del área de investigación del proyecto de tesis a desarrollar y poder tener los datos necesarios de la tarea."""

# Gráfico Strip de las áreas de los distritos
px.strip(distritos,
         x="Área",
         hover_name="Distrito",
         color="Provincia",
         title="Distribución del espacial de las área territorio nacional por distrito",
         labels={"Área"})

"""<p align="justify">El gráfico de strip creador anteriormente muestra la distribución de las áreas de los distritos en el territorio nacional. Cada punto en el gráfico representa un distrito, y los colores indican la provincia a la que pertenecen. Este tipo de gráfico es útil para visualizar la variabilidad en las áreas de los distritos y cómo se distribuyen en el territorio. Adiccionalmente por el tipo de invesigacion este grafico permite saber cuanto territorio de Costa Rica es reoresentado por los distritos de Cartago."""

# Distritos de Cartago creación del dataframe
cartago = distritos[distritos["Provincia"] == "Cartago"]

# Histograma con "nbins" dividido por la provincia de Cartago según cantones
px.histogram(data_frame=cartago,
             x="Área",
             nbins=10,
             color="Cantón",
             title="Distribución del Área en Cantones de la Provincia de Cartago")

"""<p align="justify">El histograma te permite ver la variabilidad en el tamaño de los distritos, más que nuestra área de estudio solo comprende los distritos del norte de la provincia y es donde este tipo de grafico nos permite ver tamaños de cantones con respecto a la futura área de estudio. También se pueden identificar distritos que son significativamente más grandes o más pequeños que la mayoría más que el grafico es interactivo permitiendo profundizar cuales cantones tiene distrito con áreas muy importantes y ver cuales están en nuestra área de estudio, siendo muy relevante para la planificación territorial y el análisis regional, de nuestra investigación."""

# Gráfico de barras
# Graficación del área de cada distrito de Cartago por kilómetros cuadrados
# Subconjunto Distritos de Cartago creación del dataframe
cartago = distritos[distritos["Provincia"] == "Cartago"]

# Se establece la columna "Distrito" como índice del dataframe
# y este se ordena por la cantidad de casos positivos
cartago = cartago.set_index("Distrito") \
                                             .sort_values(by="Área")

px.bar(cartago,
       x="Área",
       orientation="h",
       height=800, # altura del gráfico
       title="Cantidad de kilometros cuadrados que tiene los distritos de Cartago",
       labels={"Área km2", "Distrito"})

"""<p align="justify">En este grafico de barras se mejor la distribución espacial de los distritos por kilómetros cuadrados y tener una mejor perspectiva de la información a desarrollar con respecto a la área seleccionada de estudio de la investigación."""

#Cargamos el csv concentración de nitratos

from google.colab import files
file = files.upload()

nitratos= pd.read_csv("/content/Mean_contamination_CANTONES.csv",sep=",")
nitratos

# Información general sobre nuestro csv
nitratos.info()

# Reducción de columnas
nitratos = nitratos[["Sistema", "Punto_de_m", "Nitrato", "CANTON"]]

# Cambio de nombre de las columnas a minúsculas y a nombres más claros
nitratos = nitratos.rename(columns={"Sistema": "Sistema que alimenta",
                                              "Punto_de_m": "Nacientes",
                                              "Nitrato": "Concentración de Nitratos",
                                              "CANTON": "Cantón"})

nitratos

# Gráficos de caja
px.box(
    data_frame=nitratos,
    y="Concentración de Nitratos",
    x="Cantón",
    points="all",
    hover_name="Cantón",
    title=" Concentración de Nitratos en los distritos de la zona de estudio")

"""<p align="justify">El gráfico de caja proporciona una representación visual de la distribución de la concentración de nitratos en los distintos cantones de la zona de estudio, lo que puede ayudar en el análisis y la toma de decisiones relacionadas con la calidad del agua. En el caso de este grafico podemos ver mayor concentración de nitratos en el cantón de Oreamuno siendo que patrón de distribución centraliza los datos entre el rango de 25 a 30y teniendo concentraciones en los cantones de Paraíso, pero en rangos muy bajos y en el cantón de Alvarado y Cartago se ver una dispersión de los datos, esto se ve principalmente en el cantón de Cartago."""

# Subconjunto Distritos de Cartago creación del dataframe
cartago_n = nitratos[nitratos["Cantón"] == "Cartago"]

# Gráficos de pastel

# utilizamos el dataframe del Subconjunto Distritos de Cartago
# y este se ordena por la cantidad de casos positivos
cartago_n = cartago_n.sort_values(by="Concentración de Nitratos", ascending=False)


px.pie(cartago_n,
       names="Nacientes",
       values='Concentración de Nitratos',
       color_discrete_sequence=px.colors.sequential.YlOrRd[::-1],
       title="Porcentaje concentración de nitratos de las nacientes del cantón de Cartago",
       labels={"Nacientes", "Concentración de Nitratos"})

"""<p align="justify">El grafico de pastel que se presenta anteriormente es el reflejo del porcentaje total de las concentraciones de nitratos en las nacientes que son administradas por el cantón de Cartago, siendo que de la naciente de San Luis presenta mayor concentración de nitratos a comparación a la naciente Vuelta León 3. Siendo que la representación de la distribución porcentual del conjunto de datos de la concentración de nitratos se puede representar de esta manera y saber que naciente esta afectando mas el sistema."""

#cargamos el csv de las nacientes de la zona norte de Cartago

from google.colab import files
file = files.upload()

nacientes= pd.read_csv("/content/springs_of_water.csv",sep=",")
nacientes

# Información general sobre nuestro csv
nacientes.info()

# Reducción de columnas
nacientes = nacientes[["SISTEMA_DE", "PUNTO_DE_M", "Nitrato", "Distrito", "Canton"]]

# Cambio de nombre de las columnas a minúsculas y a nombres más claros
nacientes = nacientes.rename(columns={"SISTEMA_DE": "Sistema que alimenta",
                                              "PUNTO_DE_M": "Nacientes",
                                              "Nitrato": "Concentración de Nitratos",
                                              "Canton": "Cantón"})

nacientes

# Gráficos de Treemaps

# Treemap de casos positivos en cantones (una variable)
px.treemap(nacientes,
           values="Concentración de Nitratos",
           color_discrete_sequence=px.colors.sequential.YlOrRd[::-1],
           path=["Cantón", "Distrito"], # jerarquía de variables
           title="Concentración de Nitratos por Distrito de la zona Norte de Cartago")

"""<p align="justify">La representación de la concentración de nitratos por distritos de la zona Norte de Cartago es para determinar las jerarquías de datos mediante la visualización de áreas proporcionales dentro de un rectángulo. Cada rectángulo representa una categoría y su tamaño está relacionado con la magnitud de la variable que se está visualizando, por eso aunque Cot es un distrito con una área media de territorio, representa la mayor contaminación de nitratos en el cantón de Oreamuno. En el caso de la jerarquía del cantón de Paraíso la subdivisión de los distritos al igual que Oreamuno es por la concentración de nitratos siendo que el distrito de Llanos de Santa Lucia (territorio de menor tamaño en el cantón), tiente la mayor concentración de nitratos y las nacientes de mayor importancia."""

nacientes2= pd.read_csv("/content/springs_of_water.csv",sep=",")
nacientes2

# Reducción de columnas
nacientes2 = nacientes2[["SISTEMA_DE", "Nitrato", "Distrito", "Canton", "r_cont_n", "c_canton"]]

# Cambio de nombre de las columnas a minúsculas y a nombres más claros
nacientes2 = nacientes2.rename(columns={"SISTEMA_DE": "Sistema que alimenta",
                                              "Nitrato": "Concentración Nitratos",
                                              "r_cont_n": "Clasificación por parámetros de ley",
                                              "Distrito": "Distrito",
                                              "Canton": "Cantón",
                                              "c_canton": "Código de cantón"})

nacientes2

#Gráfico de dispersión

# Crear el gráfico de dispersión con elementos adicionales
fig = px.scatter(
    nacientes2,
    x="Clasificación por parámetros de ley",
    y="Concentración Nitratos",
    color="Cantón",
    marginal_y="violin",
    marginal_x="box",
    trendline="ols",
    template="simple_white",
    title="Riesgo por contaminación de Nitratos en los cantones del norte de Cartago"
)

# Mostrar el gráfico
fig.show()

"""<p align="justify">El gráfico de dispersión con elementos marginales y línea de tendencia proporciona una visión detallada de la relación entre el "Clasificación por parámetros de ley"  y la "Concentración de Nitratos" en los cantones del norte de Cartago. Para los datos de Clasificación por parámetros de ley se denotan en valores de 1 a 3, donde 1, respresenta los valores de 0 a 10 mg/L, 2 respresenta los valores de 10 a 50 mg/L y 3 respresenta los valores de 50 o mas mg/L.
<p align="justify">Sumado a esto los gráficos de dispersión con elementos adicionales permiten la visualizacion de elememtos marginales y la línea de tendencia que tienen los datos, entendiento la distribución y las tendencias de los mismos.
"""

# Matriz de dispersión

#matriz de gráficos de dispersión en función de las variables
fig = px.scatter_matrix(nacientes2, dimensions=[ "Clasificación por parámetros de ley", "Concentración Nitratos"], color="Sistema que alimenta",
                        title="Matriz de Clasificación por parámetros de ley y concentración de Nitratos en los sistemas de acueductos o asadas del norte de Cartago")
fig.show()

"""<p align="justify">Este tipo de gráfico es útil para visualizar la relación entre múltiples variables al mismo tiempo, y la coloración por los sistemas que tiene cada acueducto o asada en los distritos estudiados, permitiendo identificar patrones específicos para cada sistema en la relación entre las variables.

<p align="justify">En este caso, la matriz superior de la izquierda presenta los valores de los sistemas más bajos, medios y altos. En la inferior izquierda la agrupación de los sistemas según el riesgo por contaminación.
"""

nacientes3= pd.read_csv("/content/springs_of_water.csv",sep=",")
nacientes3

nacientes3.info()

# Reducción de columnas
nacientes3 = nacientes3[["Nitrato", "Distrito", "Canton", "r_cont_n", "POINT_X", "POINT_Y" ]]

# Cambio de nombre de las columnas a minúsculas y a nombres más claros
nacientes3 = nacientes3.rename(columns={"POINT_X": "Longitud",
                                              "POINT_Y": "Latitud",
                                              "Nitrato": "Concentración Nitratos",
                                              "r_cont_n": "Clasificación por parámetros de ley",
                                              "Distrito": "Distrito",
                                              "Canton": "Cantón"})

nacientes3

#Gráfico de dispersión interactivo en Mapbox

fig = px.scatter_mapbox(nacientes3, lat="Latitud", lon="Longitud", color="Clasificación por parámetros de ley", size="Clasificación por parámetros de ley",
                  color_continuous_scale=px.colors.sequential.Viridis, size_max=15, zoom=10,
                  mapbox_style="carto-positron",
                  title="Mapa Interactivo de Clasificación por parámetros de ley de concentración nitratos por cada naciente utilizadas por las asadas y acueductos del Norte de Cartago")
fig.show()

"""<p align="justify">Se genero a partir de la tabla de Nacientes, esta representación espacial de la ubicación geográfica de cada naciente con respecto a la clasificación por parámetros de ley de concentración nitratos de las fuentes de agua demostrando que espacialmente existe mayor concentración de las fuentes del sector oeste de Cartago tomando como punto de referencia el volcán Irazú.

##### Mapas interactivos implementados con la biblioteca folium
"""

# Carga de folium
import folium

# Versión de folium
folium.__version__

"""######Mapa1"""

import geopandas as gpd

# Nacientes
Nacientes = gpd.read_file("/content/nacientes.geojson")

Nacientes

from folium import Marker, Icon

# Control de capas (clase LayerControl)

# Creación de un mapa
m = folium.Map(
    location=[9.9, -83.9],
    width=950, height=850,
    zoom_start=11,
    control_scale=True,
    tiles='CartoDB dark_matter')


# Se añaden capas base adicionales
folium.TileLayer(
    tiles='CartoDB positron',
    name='CartoDB positron').add_to(m)


# ESRI NatGeo World Map
folium.TileLayer(
    tiles='http://services.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer/MapServer/tile/{z}/{y}/{x}',
    name='NatGeo World Map',
    attr='ESRI NatGeo World Map').add_to(m)



# Adición de marcadores con íconos personalizados
for idx, row in Nacientes.iterrows():
    color = 'red'  # Puedes cambiar el color según tus preferencias
    icon = Icon(color=color, icon='info-sign')  # Puedes cambiar el estilo del ícono
    Marker([row['POINT_Y'], row['POINT_X']], popup=row['Distrito'], icon=icon).add_to(m)


# Se añade un control de capas
folium.LayerControl().add_to(m)

m

"""<p align="justify">El desarrollo del Mapa Interactivo con Capas Base y Marcadores Personalizados, combina capas base, marcadores personalizados y control de capas para ofrecer una experiencia de visualización rica y personalizable. Facilita la identificación de ubicaciones específicas y la comparación entre diferentes fondos de mapa.

######Mapa2
"""

from folium import Marker

# Creación de un mapa
m = folium.Map(
    location=[10, -83.9],
    width=950, height=850,
    zoom_start=11,
    control_scale=True)


# Se añaden capas base adicionales
folium.TileLayer(
    tiles='CartoDB positron',
    name='CartoDB positron').add_to(m)

# ESRI World Imagery
folium.TileLayer(
    tiles='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/MapServer/tile/{z}/{y}/{x}',
    name='ESRI World Imagery',
    attr='ESRI World Imagery').add_to(m)

# Lectura del archivo
folium.GeoJson(data="/content/C_N_distritos.geojson", name='Concentración Nitratos por Distrito').add_to(m)
folium.GeoJson(data="/content/nacientes.geojson", name='Nacientes').add_to(m)

# Control de capas
folium.LayerControl().add_to(m)

m

"""<p align="justify">El desarrollo del mapa interactivo con capas múltiples, ofrece una experiencia completa al usuario al presentar múltiples capas de información geográfica. Facilita la visualización de la concentración de nitratos por distrito junto con la ubicación de los "Nacientes", permitiendo un análisis más profundo de la información espacial.

######Mapa3
"""

from folium.plugins import HeatMap

# Creación del mapa base
m = folium.Map(location=[9.6, -84.2], tiles='CartoDB positron', zoom_start=8, width=950, height=850)

# Mapa de color
HeatMap(data=Nacientes[['POINT_Y', 'POINT_X']], radius=10).add_to(m)

# ESRI World Imagery
folium.TileLayer(
    tiles='http://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/MapServer/tile/{z}/{y}/{x}',
    name='ESRI World Imagery',
    attr='ESRI World Imagery').add_to(m)

# Control de capas
folium.LayerControl().add_to(m)

# Despliegue del mapa
m

"""<p align="justify">El desarrollo del mapa de calor permite determinar la densidad de los puntos y su relación de ubicación espacial con respecto a la distribución del recurso. Permitiendo analizar que la cercanía de una fuente a otra podría afectarlas y contaminarlas. Se determino un radio de 10 km para dar una representación visual efectiva de la distribución espacial de los puntos, facilitando la identificación de áreas de mayor densidad.

###### ***Información adicional***

> *Portales y noticias*

*   [Segundo acuífero contaminado en Cartago con Plaguicidas](https://www.youtube.com/watch?v=6LT9z82u3CA)
*   [Estudio encuentra moléculas de plaguicida 240 veces más de lo permitido en agua de Cipreses de Cartago](https://delfino.cr/2023/01/estudio-encuentra-moleculas-de-plaguicida-240-veces-mas-de-lo-permitido-en-agua-de-cipreses-de-cartago)
*   [Agro advierte de problemas para control de plagas en cultivos, al prohibirse clorotalonil](https://www.teletica.com/nacional/agro-advierte-de-problemas-para-control-de-plagas-en-cultivos-al-prohibirse-clorotalonil_348589)
*   [Costa Rica prohíbe el plaguicida clorotalonil por riesgos a la salud pública y el ambiente](https://www.swissinfo.ch/spa/costa-rica-plaguicidas_costa-rica-proh%C3%ADbe-el-plaguicida-clorotalonil-por-riesgos-a-la-salud-p%C3%BAblica-y-el-ambiente/49021822#:~:text=San%20Jos%C3%A9%2C%2030%20nov%20(EFE,es%20considerado%20un%20probable%20carcin%C3%B3geno.)
*   [Plaguicida Clorotalonil queda oficialmente prohibido en Costa Rica tras firma de Rodrigo Chaves](https://delfino.cr/2023/11/plaguicida-clorotalonil-queda-oficialmente-prohibido-en-costa-rica-tras-firma-de-rodrigo-chaves)
"""

# Commented out IPython magic to ensure Python compatibility.
# #@title Parámetros Químicos en la Calidad del Agua Nitrógeno: Amonio, Nitritos y Nitratos
# %%html
# <iframe width="1280" height="720" src="https://www.youtube.com/embed/Y8GNQvYDHfM" title="Parámetros Químicos en la Calidad del Agua Nitrógeno: Amonio, Nitritos y Nitratos" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

"""##### **Instalación y carga de paquetes**
<p align="justify">Instalamos en nuestra máquina virtual de Google, que tiene sistema operativo Linux. Utilizamos el comando sudo que es tiene la función de realizar las operaciones como un super usuario y el comando apt para instalar o desinstalar aplicaciones.
"""

# Instalación de la biblioteca GDAL, para lectura y escritura de formatos geoespaciales

!sudo apt install -qq gdal-bin

# Instalación de DuckDB

!pip install --quiet duckdb
!pip install --quiet duckdb-engine

# Instalación de geopandas y paquetes relacionados

# Instalación de libspatialindex-dev y rtree
# Debe realizarse antes de la instalación de geopandas
!apt install -qq libspatialindex-dev
!pip install --quiet --upgrade rtree

# Instalación de geopandas y otros paquetes
!pip install --quiet --upgrade geopandas
!pip install --quiet --upgrade pyshp
!pip install --quiet --upgrade shapely
!pip install --quiet --upgrade mapclassify
!pip install --quiet --upgrade descartes

# Instalación de Leafmap

!pip install --quiet leafmap

# Carga de paquetes de Python

import duckdb
import pandas as pd
import geopandas as gpd
import plotly.express as px
import leafmap

"""#####**Carga de datos en DuckDB**

######**Nacientes**
<p align="justify">Para poder realizar el proyecto se importaron directamente desde la computadora el archivo zip de los datos de nacientes a trabajar y poder extraer el archivo .csv, para poder realizar el proceso con el DUCK DB.
"""

#cargamos el csv de las nacientes de la zona norte de Cartago

from google.colab import files
file = files.upload()

# Descompresión del archivo ZIP, para obtener el archivo CSV

!unzip springs_of_water.zip

# Renombre del archivo CSV

!mv springs_of_water.csv nacientes.csv

"""######**Distritos**
<p align="justify">Los datos a trabajar proviene Sistema Nacional de Coordinación de la Información Territorial (SNIT), que tiene el repositorio de información geoespacial del país. Se utilizo específicamente la capa “DTA (Límite Distrital)” publicada en el nodo que está conformado por las capas geográficas del Instituto Geográfico Nacional alojadas en IGN Cartografía 1:5mil CO (https://geos.snitcr.go.cr/be/IGN_5_CO/wfs?)

<p align="justify"> Con el comando ogr2ogr, es una herramienta de la biblioteca GDAL (Geospatial Data Abstraction Library) que se utiliza para realizar operaciones de conversión y manipulación de datos geoespaciales. GDAL es una biblioteca de código abierto que proporciona funciones y herramientas para trabajar con una amplia variedad de formatos de datos geoespaciales.
"""



# Descarga de la capa de Límite Distrital

!ogr2ogr \
  -makevalid \
  -nln distritos \
  -nlt PROMOTE_TO_MULTI \
  -lco GEOMETRY_NAME=geom \
  -s_srs EPSG:5367 \
  -t_srs EPSG:4326 \
  distritos.gpkg \
  WFS:"https://geos.snitcr.go.cr/be/IGN_5_CO/wfs" "IGN_5_CO:limitedistrital_5k"

"""######**API de DuckDB para Python**
<p align="justify">Permite realizar operaciones más avanzadas, como ejecutar consultas parametrizadas, trabajar con pandas DataFrames y más. De esta forma permite cargar los datos de DuckDB en dataframes de Python.
"""

# Creamos la Conexión

con = duckdb.connect()

# Extensines de DuckDB

con.sql("SELECT * FROM duckdb_extensions()")

# Carga de datos de nacientes

con.sql("CREATE OR REPLACE TABLE nacientes AS SELECT * FROM read_csv_auto('nacientes.csv')")

# Despliegue de la tabla nacientes

con.sql("SELECT * FROM nacientes;")

# Cantidad de registros

con.sql("SELECT COUNT(*) FROM nacientes")

Nitrato_distrito = '''
SELECT Distrito, SUM(Nitrato::numeric) AS Nitrato
FROM nacientes
GROUP BY Distrito
ORDER BY Nitrato DESC;
'''
con.sql(Nitrato_distrito)

# Exportación de datos a un dataframe

nacientes_df = con.sql("SELECT * FROM nacientes").df()

nacientes_df

"""######**Extensión espacial**"""

# Instalación y carga

con.install_extension("spatial")
con.load_extension("spatial")

# Formatos soportados por la extensión espacial

con.sql("SELECT * FROM ST_Drivers() ORDER BY short_name;")

# Carga de datos de nacientes (con geometrías)

con.sql(
    "CREATE OR REPLACE TABLE nacientes AS " \
    "SELECT * FROM ST_Read('nacientes.csv', " \
    "open_options=['X_POSSIBLE_NAMES=POINT_X', " \
                  "'Y_POSSIBLE_NAMES=POINT_Y'])"
)

# Consulta de la tabla "nacientes"

con.sql("SELECT * FROM nacientes")

# Carga de datos de distritos

con.sql("CREATE TABLE distritos AS SELECT * FROM ST_Read('distritos.gpkg')")

# Consulta de la tabla "distritos"

con.sql("SELECT * FROM distritos")

con.sql("SHOW TABLES")

# Commented out IPython magic to ensure Python compatibility.
# # concentracion de nitratos en canton
# 
# %%time
# 
# consulta_sql = '''
# CREATE OR REPLACE TABLE concentracion_nitratos_canton AS
# SELECT
#   d.CANTÓN AS CANTÓN,
#   d.geom AS geom,
#   SUM(Nitrato::numeric) AS Nitrato
# FROM distritos AS d JOIN nacientes AS n
#   ON ST_Contains(d.geom, n.geom)
# WHERE n.Canton IN (
#   'Cartago', 'Alvarado', 'Paraiso',
#   'Oreamuno')
#   GROUP BY d.CANTÓN, d.geom
# ORDER BY Nitrato DESC;
# '''
# 
# con.sql(consulta_sql)

# Consulta de la tabla "concentracion_nitratos_canton"

con.sql("SELECT * FROM concentracion_nitratos_canton")

# Commented out IPython magic to ensure Python compatibility.
# # concentracion de nitratos en distritos
# 
# %%time
# 
# consulta_sql = '''
# CREATE OR REPLACE TABLE concentracion_nitratos_distritos AS
# SELECT
#   d.DISTRITO AS DISTRITO,
#   d.geom AS geom,
#   SUM(Nitrato::numeric) AS Nitrato
# FROM distritos AS d JOIN nacientes AS n
#   ON ST_Contains(d.geom, n.geom)
# WHERE d.Distrito IN (
#   'Birrisito', 'Cachí', 'Capellades',
#   'Cipreses', 'Cot', 'Llano Grande', 'Llanos de Santa Lucía',
#   'Pacayas', 'Potrero Cerrado', 'San Rafael',
#   'Santa Rosa', 'Santiago', 'Tierra Blanca')
#   GROUP BY d.DISTRITO, d.geom
# ORDER BY Nitrato DESC;
# '''
# 
# con.sql(consulta_sql)

# Consulta de la tabla "concentracion_nitratos_distritos"

con.sql("SELECT * FROM concentracion_nitratos_distritos")

# Exportación a un dataframe

consulta_sql = '''
SELECT * EXCLUDE geom, ST_AsText(geom) as geometry FROM concentracion_nitratos_distritos
'''

concentracion_nitratos_distritos_df = con.sql(consulta_sql).df()

concentracion_nitratos_distritos_df

# Exportación a geodataframe

concentracion_nitratos_distritos_gdf = leafmap.df_to_gdf(
    concentracion_nitratos_distritos_df,
    src_crs="EPSG:4326",
    dst_crs="EPSG:4326"
)

concentracion_nitratos_distritos_gdf

"""#####**Gráfico estadístico en Plotly**"""

# Gráfico de barras plotly a partir de DataFrame 'concentracion_nitratos_distritos_df'
fig = px.bar(concentracion_nitratos_distritos_df,
             x="DISTRITO",
             y="Nitrato",
             orientation="v",
             title="Concentración de Nitratos en los Distritos del Norte de la Provincia de Cartago",
             labels={"DISTRITO": "Distritos", "Nitrato": "Concentración de Nitratos"},
             color="Nitrato",  # Columna de datos
             color_discrete_sequence=px.colors.qualitative.Set1)  # Paleta de colores por Concentración
fig.show()

"""<p align="justify">El grafico generado de concentración de nitratos en los diferentes distritos del Norte de la Provincia de Cartago, permite realizar una comparación de concentraciones e identificar la concentración más elevada de nitratos, determinando los distritos más críticos y generar las tendencias o patrones geográficos de porque la contaminación de las fuentes de agua. De esta forma el gráfico de barras ofrece una representación visual efectiva de la concentración de nitratos en los distritos, permitiéndote identificar patrones, tendencias y áreas de interés de manera rápida y accesible.

#####**Mapa interactivo en Leafmap**

<p align="justify">Leafmap es una biblioteca de Python que proporciona herramientas para visualizar y analizar datos geoespaciales en Jupyter Notebooks. Está construido sobre otras bibliotecas populares de Python como Folium, ipyleaflet e ipywidgets. Leafmap simplifica la creación de mapas interactivos y visualiza fácilmente datos espaciales de una manera accesible para los científicos y desarrolladores de datos.
"""

# Mapa de coropletas Concentración de Nitratos en los Distritos del Norte de la Provincia de Cartago

# Creación de un mapa con un centro y un nivel inicial de acercamiento
m = leafmap.Map(center=[10, -83.9], zoom=11, legend=True)

# Capa de coropletas con cambio de color a "YlOrRd"
m.add_data(
    concentracion_nitratos_distritos_gdf,
    column='Nitrato',
    scheme='Quantiles',
    cmap='YlOrRd',  # Cambia el esquema de colores aquí
    legend_title='Concentración de Nitratos (mg/L)',
    widget=True  # Agrega un widget de leyenda al mapa
)

# Despliegue del mapa
m

"""<p align="justify">El mapa de coropleta realizado epresentan la concentración de nitratos en los distritos del Norte de la Provincia de Cartago, ofreciendo varias oportunidades de análisis y comprensión de patrones espaciales. Donde podemos determinar la Variabilidad Espacial observando las variaciones y los patrones de concentración. Tambien la determinación de los puntos calientes y fríos donde se registran los valores mas altos y bajos. Otro análisis es la identificación de tendencias según la ubicación geográfica y determinar si es por posibles fuentes de contaminación o patrones de dispersión. Tambien comparar la concentración de nitratos en los distritos con los niveles estándar o recomendados permitiendo con esto poder identificar las áreas que podrían estar en riesgo de contaminación o que requieren medidas correctivas.

##**Conclusiones**

<p align="justify">Las herramientas que nos ofrecen el lenguaje de programación Python y la herramienta Colab Research Google, es fundamental para el desarrollo científico, técnico y profesional en materia de datos, análisis de variables y representación de los mismos para la toma de decisiones y para poder también integrar datos geoespaciales, en los procesos, investigaciones o en labor diaria de cada uno.

<p align="justify">El análisis de los resultados es muy prometedor y se integran en los plasmado en los objetivos de la tesis y las instrucciones de esta tarea. Siendo que Colab es una herramienta que se integra excelente con el análisis de datos y la ejecución de comandos para poder visualizar y analizar la información que nos presenta.

<p align="justify">La utilización de Python y de la herramienta del Colab, nos permite utilizar librerías especializadas, facilidad de uso, integración con herramientas de visualización, machine learning, open source, flexibilidad y compatibilidad con bases de datos. La elección de Python para el análisis de datos de contaminación de nacientes se debe a su versatilidad, su comunidad activa y las numerosas herramientas y librerías especializadas disponibles, lo que facilita la realización de análisis robustos y la generación de conocimiento significativo a partir de los datos medioambientales.

<p align="justify">En este proyecto, exploramos los datos de contaminación de nitratos en el norte de Cartago. Los gráficos estadísticos desarrollados con Plotly proporcionan una visión clara de la contaminación de cada fuente por acumulación de nitratos. Además, los mapas interactivos en Folium permiten visualizar geoespacilamente los datos y tener una conceptualización mejor de la investigación.

<p align="justify">La interactividad de Plotly y Folium ha mejorado significativamente la capacidad de exploración y comprensión de los datos. Al implementar múltiples capas y controles en los mapas, se ha facilitado la comparación y análisis de la información. Permitiendo de manera efectiva para comunicar información compleja de manera visual y accesible.

<p align="justify">La eficiencia en el manejo de datos con DuckDB es por su manejo de grandes conjuntos de datos. Y que permite la carga de datos de una forma rápida y eficiente, permitiendo un acceso eficaz a los datos geoespaciales para su análisis. Sumado a esto la combinación de DuckDB y Leafmap permite la exploración eficiente de patrones espaciales y la optimización de recursos para el manejo y la visualización interactiva sin requerir recursos excesivos.

<p align="justify">La integración de herramientas eficientes de visualización y gestión de datos para obtener información valiosa a partir de datos geoespaciales es un elemento esencial del proceso de investigación e interpretación de datos. La combinación de DuckDB y Leafmap es particularmente beneficiosa para proyectos que involucran grandes conjuntos de datos geoespaciales que requieren una representación visual eficiente.

<p align="justify">La combinación de Python como lenguaje de programación, Google Colab como plataforma de colaboración y desarrollo, Plotly y Folium para la visualización de datos, y DuckDB junto a Leafmap para la gestión eficiente de datos geoespaciales han demostrado ser estrategias poderosas y efectivas para resolver problemas de investigación, proyectos y análisis de datos. Estas herramientas proporcionan un enfoque integral y eficiente para el análisis de datos geoespaciales, proporcionando un marco poderoso para tomar decisiones informadas en los campos científicos y profesionales. Este proyecto demuestra cómo estas tecnologías se pueden aprovechar de forma colaborativa para resolver problemas y generar conocimiento valioso a partir de datos complejos.

##**Recursos**



*   [DuckDB Documentation](https://duckdb.org/duckdb-docs.pdf)
*   [Cómo crear un mapa con Leaflet](https://mappinggis.com/2013/06/como-crear-un-mapa-con-leaflet/)

##**Referencia**

> Gandhi, U. (2020a). Python Foundation for Spatial Analysis. Spatial Thoughts.
https://spatialthoughts.com/courses/python-foundation-for-spatial-analysis/

> Python Software Foundation. (2021). Python Language Reference.
https://www.python.org/

> Rey, S. J., Arribas-Bel, D., & Wolf, L. J. (2020). Geographic Data Science with Python.
https://geographicdata.science/book/

> Severance, D. C. R. (2016). Python for Everybody: Exploring Data in Python 3 (S.
Blumenberg & E. Hauser, Eds.). CreateSpace Independent Publishing Platform.
https://www.py4e.com/html3/
"""