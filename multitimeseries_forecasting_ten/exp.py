import numpy as np # linear algebra
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import matplotlib.pyplot as plt
import time
from datetime import datetime     #necessary for writing data points at regular interval
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.write_api import ASYNCHRONOUS


username = 'influx2'
password = 'influxdb'
database = 'DB1'
retention_policy = 'autogen'
bucket = f'{database}/{retention_policy}'
client = InfluxDBClient(url='http://influxdb:8086', token=f'{username}:{password}', org='-')
write_api = client.write_api(write_options=SYNCHRONOUS)


for i in range(5000):
#  ts = time.time()
#  x = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ') #got the timestamp now
#  q = Point("my_measurement").tag("location", "Prague").field("predicted", 50).time(time=x)
#  write_api.write(bucket=bucket, record=q)
  ts = time.time()+5
  x = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')
  r = Point("my_measurement").tag("location", "Prague").field("predicted", 60).time(time=x)
  write_api.write(bucket=bucket, record=r)
  ts = time.time()+10
  x = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')
  s = Point("my_measurement").tag("location", "Prague").field("second", 100).time(time=x)
  write_api.write(bucket=bucket, record=s)
  time.sleep(15)


