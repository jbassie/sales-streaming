#/bin/bash

cd /home/scripts

spark-submit --jars jars/kafka-clients-3.4.0.jar, jars/spark-sql-kafka-0-10_2.12-3.3.0.jar,jars/spark-streaming-kafka-0-10-assembly_2.12-3.3.0.jar, jars/commons