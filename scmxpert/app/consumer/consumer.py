import socket   
import os 
import time    
import pymongo   
import json 
import sys
from kafka import KafkaConsumer
from dotenv import load_dotenv
load_dotenv()


CLIENT = pymongo.MongoClient(os.getenv("mongodbUri"))
DB = CLIENT['scmxpertlite']
DATA_STREAM = DB["datastream"]

topicName = os.getenv("topic_name")    
print(topicName)
bootstrap_servers= "localhost:9092"

try:
    consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers,auto_offset_reset = 'latest')
    for d in consumer:
        try:
            d = json.loads(d.value)
            print(d)
            mdata = DATA_STREAM.insert_one(d)
        except json.decoder.JSONDecodeError:
            continue
except KeyboardInterrupt:
    sys.exit()