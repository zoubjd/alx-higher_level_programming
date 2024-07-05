#!/bin/bash
# sends a request to that URL, and displays the size
URL="$1"
curl -sI $URL | grep -i Content-Length | awk '{print $2}'
