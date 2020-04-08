#PROPHET
from fbprophet import Prophet

def predict_with_prophet(data,days=15, code='PT', y='Total_Cases'):
    data_prophet = data[[y+code]]
    data_prophet.reset_index(inplace=True)
    data_prophet = data_prophet.rename(columns={'Date': 'ds', y+code: 'y'})
    
    model_prophet = Prophet(changepoint_prior_scale=0.1)
    model_prophet.fit(data_prophet)

    
    data_prophet_forecast = model_prophet.make_future_dataframe(periods=days)
    data_prophet_forecast = model_prophet.predict(data_prophet_forecast)

    dt = data_prophet_forecast[['ds','yhat']][-days:]
    dt = dt.rename(columns={'ds': 'Date', 'yhat': 'Total_CasesIT'})
    dt['Date'] = dt['Date'].dt.strftime('%m/%d/%Y')
    dt.set_index('Date', inplace=True, drop=True)
    
    tmpdata = data[[y+code]]
    tmpdata = tmpdata.append(dt)

    return tmpdata