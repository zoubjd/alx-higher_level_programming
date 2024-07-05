#!/bin/bash
# displays the methodes
curl -si -L -X OPTIONS "$1" | grep "Allow:" | cut -d ':' -f 2- | cut -c 2-
