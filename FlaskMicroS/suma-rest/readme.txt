Para ejecutar el entorno phyton 
    --> D:\FlaskMS\suma-rest\venv\Scripts>activate.bat

En Mac, Para crear el entorno phyton3 primera vez 
    --> python3 -m venv venv 

En Mac, Para activar el entorno phyton
    --> . venv/bin/activate

En Mac, instalar flask
    --> pip install flask

En Mac, instalar behave
    --> pip install behave

En Mac, instalar requests
    --> pip install requests

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

Compilar OcelotApiGetway
    --> cd OcelotApiGetway
    --> dotnet build OcelotApiGetway.sln

Ejecutar OcelotApiGetway
    --> cd OcelotApiGetway
    --> dotnet run OcelotApiGetway.csproj