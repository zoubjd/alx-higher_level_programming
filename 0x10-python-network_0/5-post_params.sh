#!/bin/bash
# sends a POST reques
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
