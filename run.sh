#! /bin/bash


# if dir 'COVID-19' exists
if [ -d './COVID-19' ]
then
	# pull the most recent data
	cd ./COVID-19
	git pull
	cd ..
else
	# otherwise, clone it from JHU's repo
	git clone https://github.com/CSSEGISandData/COVID-19.git
fi

# run the python script
python3.7 ./script.py