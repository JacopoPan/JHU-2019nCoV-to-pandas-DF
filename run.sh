#! /bin/bash

if [ -d "./COVID-19" ]
then
	cd ./COVID-19
	git pull
	cd ..
else
	git clone https://github.com/CSSEGISandData/COVID-19.git
fi

python3.7 ./script.py