package main

import (
	"fmt"
	"github.com/tidwall/gjson"
	"io/ioutil"
	"net/http"
	"time"
)

type OverallData struct {
	total    int64
	newToday int64
	cured    int64
	deaths   int64
}

type CountryData struct {
	total    int64
	newToday int64
	cured    int64
	deaths   int64
	date     string
}

func getOverallData() OverallData {
	response, err := http.Get("https://thevirustracker.com/free-api?global=stats")

	if err != nil {
		fmt.Println("Request for overall data failed")
	}

	data, _ := ioutil.ReadAll(response.Body)

	return OverallData{
		gjson.Get(string(data), "results.0.total_cases").Int(),
		gjson.Get(string(data), "results.0.total_new_cases_today").Int(),
		gjson.Get(string(data), "results.0.total_recovered").Int(),
		gjson.Get(string(data), "results.0.total_deaths").Int(),
	}
}

func getCountryData(country string) CountryData {
	response, err := http.Get("https://thevirustracker.com/free-api?countryTotal=" + country)

	if err != nil {
		fmt.Println("Request for overall  country data failed")
	}

	data, _ := ioutil.ReadAll(response.Body)

	return CountryData{
		gjson.Get(string(data), "countrydata.0.total_cases").Int(),
		gjson.Get(string(data), "countrydata.0.total_cases").Int(),
		gjson.Get(string(data), "countrydata.0.total_cases").Int(),
		gjson.Get(string(data), "countrydata.0.total_cases").Int(),
		time.Now().String(),
	}
}
