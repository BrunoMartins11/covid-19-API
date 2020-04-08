# ARIMA Model
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import pandas as pd
import datetime

class ArimaModel:
    def __init__(self, order=(4,1,0)):
        self.order = order
    
    
    def predict_with_arima(self, dataset, code='PT', y='Total_Cases', days=5):
        tmp = dataset[[y+code]]
        history = [x for x in tmp.values]
        news = []
        data_mod = dataset[[y+code]].reset_index()
        for i in range(days):
            model = ARIMA(history[i:], order=self.order)
            model_fit = model.fit()
            output = model_fit.forecast()
            yhat = output[0]
            history.append(np.array([round(yhat)]))
            
            xn = datetime.datetime.strptime(data_mod.iloc[-1]['Date'], '%m/%d/%Y') \
                + datetime.timedelta(days=i+1)
            news.append(
                pd.Series([xn.strftime("%m/%d/%Y"), yhat], index=data_mod.columns)
            )

        data_mod = data_mod.append(news)
        data_mod.set_index('Date', inplace=True, drop=True)
        
        return data_mod