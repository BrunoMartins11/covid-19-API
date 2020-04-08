from statsmodels.tsa.holtwinters import SimpleExpSmoothing
import numpy as np
import pandas as pd

def predict_with_exp(data, days=5):
    tmp_data = data.values
    history = [x for x in tmp_data]
    for i in range(days):
        model = SimpleExpSmoothing(history)
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        history.append(np.array([round(yhat)]))
    return history