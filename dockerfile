# usa una imagem do ubuntu 20.04
FROM ubuntu:20.04


# carga  el arcuivo de dependencias  necesarias de python
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential

# Establece el directori de trabajo en el contenidor
WORKDIR /app

# copia la ruta actual al directorio de trabajo
ADD . /app

# copia el archivo de dependencias al directorio de trabajo
COPY requirements.txt /app

# instala las dependencias de python segun el archivo de dependencias
RUN pip3 install -r requirements.txt

# expone el puerto 5000 del contenedor al puerto 5000 del host
EXPOSE 5000

# Copia el contenido del directorio actual al directorio de trabajo
COPY . /app

# añaade el contenido del directorio actual al directorio de trabajo
ADD . /app

# ejecuta el archivo app.py
CMD ["python3", "app.py"]
