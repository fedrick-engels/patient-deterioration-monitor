from pyspark.sql import SparkSession
from pyspark.ml.classification import GBTClassifier
from pyspark.ml.feature import VectorAssembler

spark = SparkSession.builder.appName("ICU Model").getOrCreate()

df = spark.read.csv("data/sample_vitals.csv", header=True, inferSchema=True)

assembler = VectorAssembler(
    inputCols=["heart_rate", "spo2", "map", "resp_rate", "temp"],
    outputCol="features"
)

df = assembler.transform(df)

train, test = df.randomSplit([0.8, 0.2])

model = GBTClassifier(labelCol="label").fit(train)

model.write().overwrite().save("model/saved_model")

print("Model trained and saved!")