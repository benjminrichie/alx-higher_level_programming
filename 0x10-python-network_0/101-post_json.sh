#!/bin/bash
# This script sends a JSON POST request to URL passed as first argument, and displays body of the response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
