#!/bin/bash

# chmod 700 add-column.sh 

PATH=~/Desktop/data/*.csv
PREFIX='/Users/lethuhang/Desktop/data/processed/with-country-'

for filepath in $PATH; do
	filename=$(/usr/bin/basename $filepath)
	country_code=$(/usr/bin/cut -d '_' -f6 <<< ${filepath} | /usr/bin/sed 's/.csv//')
	/usr/bin/awk -F ',' \
		-v country_code="$country_code" \
		-v country="Country" \
		'{
			if ($0 ~ /"Date","Publisher","Calls","Uniques"/) {
				print "\""country"\","$0;
			} else {
				print "\""country_code"\","$0;
			}
		}' $filepath > $PREFIX$filename
done