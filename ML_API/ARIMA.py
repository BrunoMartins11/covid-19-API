# ARIMA Model
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import pandas as pd

def predict_with_arima(data, days=5):
    tmp_data = data.values
    history = [x for x in tmp_data]
    for i in range(days):
        model = ARIMA(history[i:], order=(4,1,0))
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        history.append(np.array([round(yhat)]))
    return history