Para ejecutar el entorno phyton 
    --> D:\FlaskMS\suma-rest\venv\Scripts>activate.bat

Para ejecutar la app
    --> (venv) D:\FlaskMS\suma-rest>python src/app.py

Contenedor docker
    --> https://hub.docker.com/_/alpine

Ver imagenes
    --> docker images

Crear imagen
    --> docker build -t rest_api_suma .

Ejecutar contenedor en consola
    --> docker run -it --publish 42000:41000 rest_api_suma
    o
    --> docker run -it -p 42000:41000 rest_api_suma

Ejecutar contenedor en background
    --> docker run -it --publish 42000:41000 --detach rest_api_suma
    o
    --> docker run -it -p 42000:41000 -d rest_api_suma

Ver contenedores en ejecución
    --> docker container ls

Detener docker 
    --> docker stop [CONTAINER ID]
    --> ejemplo -- docker stop 27db59de1c69 (puede ser los primeros 3 caracteres)