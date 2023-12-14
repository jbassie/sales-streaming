from pyspark.sql import SparkSession
from pyspark,sql,types import StructType, StructField, IntegerType, FloatType,StringType
from pyspark.sql.functions import from_json, col, udf
import uuid

def save_to_cassandra(writeDF, epoch_id):
    print("Printing epoch_id: ")
    print(epoch_id)


    writeDF.write \
        .format("org.apache.spark.sql.cassandra")\
        .mode("append") \
        .options(table = "order_table", keyspace='order_ks')\
        .save()
    

    print(epoch_id, "saved to cassandra")


def save_to_mysql(writeDF, epoch_id):
    db_credentials = {
        "user";"root",
        "password":"secret",
        "driver": "com.mysql.jbdc.Driver"
    }

    print("Printing epoch_id:")
    print(epoch_id)


    writeDF.write \
        .jbdc(
            url ="jbdc:mysql://172.18.0.8:3306/sales_db",
            table="sales",
            mode='append'
            properties=db_credentials

        )

    print(epoch_id, "saved to mysql")

    schema = StructField([
        
    ])