from fastapi import FastAPI, HTTPException
from online_retail_model import load_and_predict
import json
from pyspark.sql import SparkSession

app = FastAPI()

# Configurar la sesión de Spark
spark = SparkSession.builder.appName("example").getOrCreate()

@app.post("/predict")
def predict(data: dict):
    try:
        # Convertir los datos de entrada a un DataFrame Spark
        spark_data = spark.createDataFrame([data])
        
        # Realizar predicciones utilizando la función importada
        predictions = load_and_predict(spark, spark_data)

        # Obtener los resultados
        results = json.loads(predictions.select('InventarioAcumulado', 'prediction', *features).toJSON().first())
        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")

if __name__ == "__main__":
    # Iniciar la aplicación FastAPI
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
