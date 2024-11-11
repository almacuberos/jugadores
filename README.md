# Soluc10nes

Trabajo para Metodologias Cuantitativas, UNSAM 2024.

**Docente** Gustavo Navarro

**Integrantes** Santiago Stekolschik, Ivan Lockett y Alma Cuberos

## Introducción
La expansión en el uso del big data como herramienta para la resolución de problemas es un fenómeno que cobró relevancia en la segunda década del siglo XXI y que viene acentuándose con el correr de los años.
En esa línea, los ámbitos en los que tuvo un impacto fueron ampliándose. Un área en la que su utilización logró permear fuertemente fue el deporte. Los clubes comenzaron a tomar decisiones apoyándose en estadísticas, las cuales revelan características específicas sobre jugadores y equipos permitiendo la creación de perfiles particulares para cada uno de ellos.
Estos clubes, en su mayoría, trabajan con un equipo de *scouting* el cual, a partir de una cantidad determinada de partidos vistos, se encarga de observar y analizar con el objetivo de sacar conclusiones que optimicen los gastos en incorporaciones y poder descubrir al jugador antes que cualquier otro club. Este proceso se facilita con el complemento del uso del big data y las estadísticas.
Por otro lado, los clubes más chicos en términos presupuestarios quedan resignados a fichar los sobrantes de los otros equipos o jugadores de menor jerarquía, ya sea por no tener acceso a estadísticas jerarquizadas que permitan la elaboración de estos perfiles o por no saber interpretarlas comparativamente y correctamente.

## Problema

Los clubes argentinos con menor porcentaje de ganancias suelen prescindir de equipos de *scouting* o los mismos no tienen acceso a plataformas de estadísticas jerarquizadas que faciliten y enriquezcan este trabajo por el alto costo de los mismos.
Por ello, no pueden tener al alcance ni generar estos perfiles elaborados mediante las estadísticas, los cuales permitirían economizar sus búsquedas en dos dimensiones: el dinero y el tiempo.

## Objetivos

- Jerarquizar y filtrar estadísticas provistas por bases de datos ya existentes para poder crear perfiles a partir de determinadas características.
- Brindarle a los clubes con menor capacidad adquisitiva un motor de búsqueda para acceder a información jerarquizada con el fin de orientar una búsqueda de un tipo de perfil determinado.
- Funcionar como un parámetro más cuantificable que complemente la visión subjetiva de los equipos de *scouting* o reemplazar su rol en clubes con menos recursos económicos.

## Librerias 

- streamlit
- pandas

## Ejecución en Windows
			
### La primera vez

* Bajar fuentes
```
git clone https://github.com/almacuberos/jugadores.git
```
* Crear environment
```
cd jugadores
```
```
cd pythonProject
```
```
python -m venv venv
```
* Activar environment
```
venv\Scripts\activate
```

* Instalar librerias
```
pip install -r requirements.txt
```

### El resto de las veces 
```
cd jugadores
```
```
cd pythonProject
```
```
venv\Scripts\activate
```

### Para ejecutar 
```
streamlit run jugadores.py
```
## Ejecución en Linux

### La primera vez

* Bajar fuentes
```
git clone https://github.com/almacuberos/jugadores.git
```
* Crear environment
```
cd jugadores
```
```
cd pythonProject
```
```
python -m venv venv
```
* Activar environment
```
source venv/bin/activate
```
* Instalar librerias
```
pip install -r requirements.txt
```
### El resto de las veces 
```
cd jugadores
```
```
cd pythonProject
```
```
source venv/bin/activate
```

### Para ejecutar 
```
streamlit run jugadores.py
```
## Ejecución en MacOS

### La primera vez

* Bajar fuentes 
```
git clone https://github.com/almacuberos/jugadores.git
```
* Crear Enviroment
```
cd jugadores
```
```
cd pythonProject
```
```
python3 -m venv venv
```
* Activar Enviroment
```
source venv/bin/activate
```
* Instalar librerías 
```
pip install -r requirements.txt
```
### El resto de las veces
```
cd jugadores
```
```
cd pythonProject
```
```
source venv/bin/activate
```
### Ejecutar el archivo con Streamlit
```
streamlit run jugadores.py
```
-------------------------------------
El markdown fue editado con: [Markdown Live Preview](https://markdownlivepreview.com/)
