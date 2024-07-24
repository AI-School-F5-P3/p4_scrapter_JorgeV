# Proyecto 4 - Web Scraping (Individual)

## Jorge Vázquez


### Planteamiento
 
La empresa XYZ Corp está pensando en utilizar una frase que se identifique con sus
valores y su misión. El objetivo de este proyecto es desarrollar un programa en Python que
realice web scraping para extraer todas las frases de la web https://quotes.toscrape.com/  ,
además de las frases se quieren recuperar el autor de cada frase, los tags asociados a
cada frase, y la pagina "about" con información de los autores. Los datos extraídos deben
ser formateados y almacenados adecuadamente.


### Objetivos del Proyecto

Acceder a una web preparada para ser scrapeada: La web contiene muchas frases,
con información relacionada .
Extraer información relevante: Utilizar técnicas de web scraping en Python para
obtener todas las frases con la información extra (autor, tags, about).
Formatear los datos: Asegurarse de que los datos extraídos estén limpios y
organizados de manera coherente.

Almacenar los datos en una base de datos: Utilizar una base de datos SQL o
NoSQL para guardar la información extraída.


### Plazos
 
Entrega y presentación de la solución: Martes 30 de Julio.

 
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
  

### Tecnologías útiles

Git/GitHub
Docker
Python (bibliotecas: BeautifulSoup, Scrapy, Requests, etc.)
SQL/NoSQL (MySQL, PostgreSQL, MongoDB, etc.)
Herramientas de gestión de proyectos (Trello, Jira)


#### De las seleccionables, Se seleccionaron:

Selenium + BeautifulSoup para Scraping
SQLAlchemy como ORM y comunicación con la base de datos SQL
PostgreSQL 16 con Pgadmin 4
Streamlit



### Niveles de Entrega
 

#### Nivel Esencial:

1. Un script que accede a la web, extrae las frases y la información asociada y la imprime en la consola.
2. Limpieza básica de los datos extraídos.
3. Documentación básica del código y README en GitHub.

 

#### Nivel Medio:

1. Almacenamiento de los datos extraídos en una base de datos.
2. Implementación de un sistema de logs para la trazabilidad del código.
3. Test unitarios para asegurar el correcto funcionamiento del scraper.

 

#### Nivel Avanzado:

1. Programación orientada a objetos (OOP) para estructurar mejor el código.
2. Gestión de errores robusta para manejar excepciones comunes en web scraping.
3. Un script que actualiza automáticamente la base de datos con nuevos datos a intervalos regulares.



#### Nivel Experto:

1. Dockerización del proyecto para asegurar un entorno de ejecución consistente.
2. Implementación de un frontend básico para visualizar los datos extraídos.
3. Despliegue de la aplicación en un servidor web accesible públicamente.
4. Utilizar otras webs de frases para aumentar la cantidad de frases scrapeadas.

