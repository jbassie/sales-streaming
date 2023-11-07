import time
import json
import random
from datetime import datetime
from data_generator import generate_order
from kafka import KafkaProducer


#message will be serialized as JSON
def serializer(message):
    return josn.dump(message).encode('utf-8')


#Kakfa Producer
producer = KafkaProducer(
    bootstrap_servers = ['172.18.0.4:9092'],
    value_serialize=serializer
)

if __name__=='__main__':
    #Infinite loop - runs untill you kill the program

    while True:
        #Generate a message
        dummy_message = generate_order()

        #sens it to our 'message' topic
        print(f'Producing message @{datetime.now()} | ,message ={str(dummy_messagae)}')
        producer.send('Order', dummy_message)
        producer.flush()

        #sleep for a random number of seconds
        time_to_sleep = random.randint(1,11)
        time.sleep(time_to_sleep)