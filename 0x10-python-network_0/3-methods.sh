#!/bin/bash
# To display every HTTP method that the server will accept.
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
