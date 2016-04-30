#!/bin/bash

URL="https://api.hearthstonejson.com/v1/latest/enUS/"
FILES=( "cards" "carbacks" "cards.collectible")

for i in "${FILES[@]}"
do
	curl "${URL}${i}.json" -o data/${i}.txt
done
