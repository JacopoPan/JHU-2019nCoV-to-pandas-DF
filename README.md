# JHU-2019nCoV-to-pandas-DF
Simple Bash/Python scripting to import JHU CSSE's time series (confirmed cases, deaths, and recovered patients) into 3 pandas DataFrames

# Requirements
- OS X or Ubuntu
- `git` (`$ sudo apt-get install git`)
- Python (if you are not using `pyhton3.7`, change line 17 of `run.sh` accordingly) 

# Usage
```
./run.sh
```

# Example

### Confirmed cases
![alt text](https://i.ibb.co/F3mtrZf/Screen-Shot.png "Plot1")

Disclaimer: the y-axes are not to scale, the absolute number of confirmed cases seems an indicator of testing more than anything else.

### Deaths and recoveries
![alt text](https://i.ibb.co/LNCNwv3/Screen-Shot-2020-03-21-at-1-06-34-PM.png "Plot2")

Disclaimer: the number of recoveries reported by JHU for France is likely incorrect.
