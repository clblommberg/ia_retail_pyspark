# Desarrollo del Modelo en PySpark con FastAPI y Docker

## Resumen

Este proyecto busca implementar un modelo de regresión lineal utilizando PySpark, expuesto a través de un endpoint con FastAPI, y encapsulado en un contenedor Docker. El objetivo es brindar una solución escalable y fácilmente implementable.

## Datos de la Data
El conjunto de datos "Online Retail II" contiene transacciones de comercio minorista en línea durante dos años. Con variables como InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID y Country, es un recurso valioso para tareas de clasificación, regresión y agrupamiento.

## Desafíos y Soluciones

### Configuración del Entorno PySpark

- **Desafío:** Configurar un entorno PySpark para el desarrollo del modelo.
- **Solución:** Implementación de un entorno Docker basado en Jupyter con soporte para PySpark.

### Desarrollo del Modelo

- **Desafío:** Diseñar un modelo de regresión lineal eficiente.
- **Solución:** Utilización del módulo `pyspark.ml` para implementar un modelo robusto.

### Manejo de Archivos Parquet

- **Desafío:** Cargar y procesar datos desde archivos Parquet.
- **Solución:** Aplicación de funciones PySpark para la lectura eficiente de archivos Parquet.

### Configuración de Docker

- **Desafío:** Crear un contenedor Docker que incluya todas las dependencias necesarias.
- **Solución:** Desarrollo de un Dockerfile basado en la imagen oficial de Jupyter con soporte para PySpark.

### Exposición del Endpoint con FastAPI

- **Desafío:** Implementar un servidor FastAPI para gestionar solicitudes HTTP y realizar predicciones.
- **Solución:** Desarrollo de un endpoint `/predict` que utiliza el modelo PySpark para generar predicciones.

[![api-retail.png](https://i.postimg.cc/Vv9xYx2d/api-retail.png)](https://postimg.cc/zHBt7czr)

## Instrucciones de Ejecución

1. **Construir la imagen Docker:**

   ```bash
   docker build -t nombre_del_proyecto .
   ```

2. **Ejecutar el contenedor:**

   ```bash
   docker run -p 8000:8000 nombre_del_proyecto
   ```

3. **Acceder a la documentación del API FastAPI:**

   [http://localhost:8000/docs](http://localhost:8000/docs)

4. **Realizar solicitudes POST al endpoint `/predict` para obtener predicciones.**

## Referencia del Conjunto de Datos

Chen, Daqing. (2019). Online Retail II. UCI Machine Learning Repository. [DOI](https://doi.org/10.24432/C5CG6D).

Este conjunto de datos está bajo la licencia Creative Commons Attribution 4.0 International (CC BY 4.0), permitiendo compartir y adaptar los datos con el crédito adecuado. 
