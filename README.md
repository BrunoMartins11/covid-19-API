# covid-19-API
COVID-19 API to fetch data and predictions done with ML

## Endpoints
### GO data API (localhost:8000)
* /overallData - to get overall data on every case reported
* /countryData?Country=??? - to get overall data for contry ??? where ??? is the country eg: PT
* /countryHistory?Country=??? -to get the timeline of cases for country ???

### Python predictions API
* /country.csv - request parameters: json with countries e.g: ``` {'PT': 'Portugal', 'ES': 'Spain'} ```

## RUN (in separate terminals if local dev)
``` make run ``` 

``` python predictions/src/api.py ```
 