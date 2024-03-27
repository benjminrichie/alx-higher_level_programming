#!/bin/bash
# Sends DELETE request to any URL passed as first argument & display body of the respons
curl -s -X DELETE "${1}"
