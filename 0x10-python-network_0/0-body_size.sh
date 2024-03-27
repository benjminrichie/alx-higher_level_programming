#!/bin/bash
# Send a request to the URL, and display size of the body of the response
curl -s "${1}" | wc -c
