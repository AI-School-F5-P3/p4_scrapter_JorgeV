# Proyecto 4 - Web Scraping Individual

## Jorge Vázquez

### Enlaces:

SCRUM (Jira): https://bcf5projects.atlassian.net/jira/software/projects/SCRAP/boards/3?atlOrigin=eyJpIjoiNmIxMDhkN2NhOWNkNDg5YjllYWVjYmZiMjBkMDY4ZDMiLCJwIjoiaiJ9


### Planteamiento
 
La empresa XYZ Corp está pensando en utilizar una frase que se identifique con sus
valores y su misión. El objetivo de este proyecto es desarrollar un programa en Python que
realice web scraping para extraer todas las frases de la web https://quotes.toscrape.com/  ,
además de las frases se quieren recuperar el autor de cada frase, los tags asociados a
cada frase, y la pagina "about" con información de los autores. Los datos extraídos deben
ser formateados y almacenados adecuadamente.


### Condiciones de Entrega

 
Para el día de la entrega, será necesario presentar:

1. Repositorio en GitHub: El repositorio con todo el código fuente desarrollado.

2. Demo del programa: Presentar una demo donde se muestre el funcionamiento del
programa de scraping.

3. Presentación de negocio para un publico técnico: Explicar el objetivo del proyecto y
cómo se llevó a cabo, así como una breve descripción del código desarrollado, y las
tecnologías empleadas, formato libre, una sola presentación del proyecto. (5 min)

4. Tablero Kanban: El enlace al tablero Kanban (Trello, Jira, etc.) utilizado para organizar
el trabajo.
  


#### Tecnologias utilizadas

a. Selenium + BeautifulSoup para Scraping
b. SQLAlchemy (Object Relational Mapping)
c. Azure Database for PostgreSQL flexible
d. pgadmin 4
e. Gradio
f. Jira
g. Visual Studio Code
h. Github


### Entregables
 

#### Nivel Esencial

1. Un script que accede a la web, extrae las frases y la información asociada y la imprime en la consola.
2. Limpieza básica de los datos extraídos.
3. Documentación básica del código y README en GitHub.
 

#### Nivel Medio:

1. Almacenamiento de los datos extraídos en una base de datos.

 

#### Nivel Avanzado:

1. Programación orientada a objetos (OOP) para estructurar mejor el código.



#### Nivel Experto:

2. Implementación de un frontend básico para visualizar los datos extraídos.
3. Despliegue de la aplicación en un servidor web accesible públicamente.



### Solución

P4_SCRAPTER/
├── app/
│   ├── __init__.py
│   ├── selenium_scraper.py
│   ├── database.py
│   └── models.py
├── gradio_interface/
│   ├── __init__.py
│   └── interface.py
├── data/
│   ├── soup.html
│   └── author_soup.html
│   └── quotes.txt
├── main.py
├── requirements.txt
└── README.md



1. Se utiliza webdriver de Selenium para controlar el acceso a las páginas del sitio web https://quotes.toscrape.com/ así como a las subpáginas que contienen las biografías de los autores de las frases.
2. Para cada páginas visitada, se descarga el código html en un objeto de BeautifulSoup.
3. Se recorre el código html identificando las etiquetas de los campos que deben ser extraerse y se extraen a listas.
4. Hay un doble loop. El exterior recorriendo las páginas de https://quotes.toscrape.com/ y el interior extrayendo la biografía de cada uno de los autores que se mencionan en la página. También hay un mini loop a la altura del loop exterior que captura las etiquetas con las que están clasificadas las frases.
5. El resultado del scraping es una lista que incluyen la siguiente información en formato diccionario:
quote_text -> frase
name -> nombre del autor
tags -> lista de etiquetas
author_url -> ruta relativa donde se encuentra la biografía
quote_source_url -> ruta absoluta para acceder a la frase
birth_date -> fecha de nacimiento del autor
birth_place -> lugar de nacimiento del autor
biography -> texto relativo al autor de la frase.
6. Con la información del paso 5, se procede a guardar la información en la base de datos asegurando que un mismo registro no se guarda más de una vez. Para este proceso de utiliza models.py que es la estructura de datos modelada con SQLAlchemy junto con la conexión a la base de datos PostgreSQL.
7. Inicialmente se utilizo una base de datos PostgreSQL local. Una vez que el modelo funcionaba, se genero una base de datos PostgreSQL en la plataforma Azure y se actualizó la conexión de la app para apuntar a Azure.
8. Finalmente, se utiliza Gradio como interfaz gráfica para mostrar la información de frases y biografías permitiendo al usuario seleccionar el autor del que quiere desplegar la información. Se aprovecha la funcionalidad de Gradio para desplegar una web de acceso público. 