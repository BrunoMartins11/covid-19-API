import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tf.keras.models import Sequential
from tf.keras.layers import Dense, LSTM

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0],True)

def create_dataset_v2(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)

def transform_data(dataset, div=0.8, code=''):
    values = dataset[['Total_CasesIT']].values.reshape(-1,1)
    values = values.astype('float32')
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled = scaler.fit_transform(values)

    train_size = int(len(scaled) * div)
    test_size = len(scaled) - train_size
    train, test = scaled[0:train_size,:], scaled[train_size:len(scaled),:]
    print(len(train), len(test))

    trainX, trainY = create_dataset_v2(train, 5)
    testX, testY = create_dataset_v2(test, 5)

    print(trainX.shape)

    trainX = np.reshape(trainX, (trainX.shape[0], 5, 1))
    testX = np.reshape(testX, (testX.shape[0], 5, 1))
    
    return trainX, testX, trainY, testY

def predict_with_lstm(dataset, code='PT', y='TotalCases'):
    trainX, testX, trainY, testY = transform_data(dataset, code=code)
    
    model= Sequential()
    model.add(LSTM(18,input_shape=(trainX.shape[1],trainX.shape[2])))
    model.add(Dense(6, activation='relu'))
    model.add(Dense(1, activation='relu'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    history = model.fit(trainX, trainY, epochs=100, batch_size=32, validation_data=(testX,testY), shuffle=False)