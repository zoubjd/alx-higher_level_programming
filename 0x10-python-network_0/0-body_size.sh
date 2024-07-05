#!/bin/bash
# sends a request to that URL, and displays the size
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
