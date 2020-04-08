#PROPHET
from fbprophet import Prophet

class ProphetModel:
    def __init__(self, changepoint=0.1):
        self.changepoing = changepoint
        
    def predict_with_prophet(self, dataset,days=15, code='PT', y='Total_Cases'):
        tmp = dataset[[y+code]]
        data_prophet = tmp.reset_index()
        data_prophet = data_prophet.rename(columns={'Date': 'ds', y+code: 'y'})
        
        model_prophet = Prophet(changepoint_prior_scale=self.changepoing)
        model_prophet.fit(data_prophet)

        
        data_prophet_forecast = model_prophet.make_future_dataframe(periods=days)
        data_prophet_forecast = model_prophet.predict(data_prophet_forecast)

        dt = data_prophet_forecast[['ds','yhat']][-days:]
        dt = dt.rename(columns={'ds': 'Date', 'yhat': 'Total_CasesIT'})
        dt['Date'] = dt['Date'].dt.strftime('%m/%d/%Y')
        dt.set_index('Date', inplace=True, drop=True)
        
        tmpdata = dataset[[y+code]]
        tmpdata = tmpdata.append(dt)

        return tmpdata