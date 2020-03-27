package main

import (
	"encoding/json"
	"net/http"
)

func getOverallDataHandler(w http.ResponseWriter, req *http.Request) {
	var data OverallData
	data, error := getOverallData()
	if error != nil {
		http.Error(w, error.Error(), http.StatusNotFound)
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(data)
}

func getCountryOverallDataHandler(w http.ResponseWriter, req *http.Request) {
	var country string
	param := req.URL.Query().Get("Country")

	if param == "" {
		http.Error(w, "", http.StatusBadRequest)
		return
	}
	country = param
	data, error := getCountryData(country)
	if error != nil {
		http.Error(w, error.Error(), http.StatusNotFound)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(data)
}
