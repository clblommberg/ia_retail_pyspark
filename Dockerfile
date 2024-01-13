FROM jupyter/pyspark-notebook

# Instala las dependencias de Pyspark
RUN pip install pyspark

# Instala FastAPI y Uvicorn
RUN pip install fastapi uvicorn

# Copia el código de tu aplicación
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar tu aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
