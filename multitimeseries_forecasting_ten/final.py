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

import numpy as np # linear algebra
import pandas as pd
data = pd.read_csv("reframed_10.csv")
reframed = data
reframed.drop(reframed.columns[0], axis=1, inplace=True)

values = reframed.values
n_train_time = 150000
test = values[n_train_time:, :]
test_x, test_y = test[:60000, :-10], test[:60000, 120:130]

model = keras.models.load_model('using_20_timesteps_for_next_10_100epochs.h5')

username = 'influx2'
password = 'influxdb'
database = 'DB1'
retention_policy = 'autogen'
bucket = f'{database}/{retention_policy}'
client = InfluxDBClient(url='http://influxdb:8086', token=f'{username}:{password}', org='-')
write_api = client.write_api(write_options=SYNCHRONOUS)
#delete_api = client.delete_api()

for i in range(60000):
  yhat = model.predict(test_x[i].reshape(1, 120, 1))
  ts = time.time()
  x = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')
  p = Point("my_measurement").tag("location", "Prague").field("actual_current", test_y[i][0]).time(time=x)
  write_api.write(bucket=bucket, record=p)
  
  for j in range(10):
    pred = yhat[0][j]
    pred = pred.item()    #change from numpy data type
    print("pred now is", pred)
    print("The type is : ",type(pred))
    ts = ts+5
    y = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%SZ')
    r = Point("prediction").tag("location", "Prague").field("predicted_state", round(pred,3)).time(time=y)
    write_api.write(bucket=bucket, record=r)
  time.sleep(5)















