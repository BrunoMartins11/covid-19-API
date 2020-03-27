package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", HelloServer)
	http.HandleFunc("/countryData", getCountryOverallDataHandler)
	http.HandleFunc("/overallData", getOverallDataHandler)

	// start the server on port 8000
	log.Fatal(http.ListenAndServe(":8000", nil))
}

func HelloServer(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World!")
}
