from pyspark.ml import PipelineModel
from pyspark.sql import DataFrame, SparkSession

def load_and_predict(spark: SparkSession, data: DataFrame) -> DataFrame:
    # Cargar el modelo
    loaded_model = PipelineModel.load("datasets/path_model")

    # Hacer predicciones utilizando la sesión de Spark proporcionada
    predictions = loaded_model.transform(data)

    return predictions
