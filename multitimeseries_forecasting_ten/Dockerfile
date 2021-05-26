FROM python:3.8
RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip3 install influxdb-client[ciso]
RUN pip3 install pandas
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install seaborn
RUN pip3 install scikit-learn
RUN pip3 install keras
RUN pip3 install tensorflow
WORKDIR /code
COPY using_20_timesteps_for_next_10_100epochs.h5 .
COPY reframed_10.csv .
COPY final.py .
CMD [ "python", "-u", "final.py" ] 
