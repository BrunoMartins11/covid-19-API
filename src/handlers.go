package main

import (
	"encoding/json"
	"net/http"
)

func getOverallDataHandler(w http.ResponseWriter, req *http.Request) {
	//Allow CORS here By * or specific origin
	w.Header().Set("Access-Control-Allow-Origin", "*")

	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")
	var data OverallData
	data, error := getOverallData()
	if error != nil {
		http.Error(w, error.Error(), http.StatusNotFound)
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(data)
}

func getCountryOverallDataHandler(w http.ResponseWriter, req *http.Request) {
	//Allow CORS here By * or specific origin
	w.Header().Set("Access-Control-Allow-Origin", "*")

	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")
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

func getCountryHistoryHandler(w http.ResponseWriter, req *http.Request) {
	//Allow CORS here By * or specific origin
	w.Header().Set("Access-Control-Allow-Origin", "*")

	w.Header().Set("Access-Control-Allow-Headers", "Content-Type")
	var country string
	param := req.URL.Query().Get("Country")

	if param == "" {
		http.Error(w, "", http.StatusBadRequest)
		return
	}
	country = param
	data := getCountryHistory(country)

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(data)
}