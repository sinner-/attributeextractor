#brain

## Usage
```
usage: brain [-h] [-e] [-d DATABASE_FILE] [-t TICKER] [-f FEATURE_FILE]
             [-l LOOK_AHEAD] [-p PROFIT] [-L] [-m MODEL_FILE] [-c]
             [-o OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -e, --extract-features
  -d DATABASE_FILE, --database-file DATABASE_FILE
  -t TICKER, --ticker TICKER
  -f FEATURE_FILE, --feature-file FEATURE_FILE
  -l LOOK_AHEAD, --look-ahead LOOK_AHEAD
  -p PROFIT, --profit PROFIT
  -L, --learn
  -m MODEL_FILE, --model-file MODEL_FILE
  -c, --classify
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
```

```
python setup.py install
rm -rf brain.egg-info build data.db dist train.dat test.dat model output features
brain-manage -c -d data.db -f SPY.csv 
brain-manage -i -d data.db -t SPY -f SPY.csv 
brain -e -d data.db -t SPY -f features -l 10 -p 2
grep "^0 " features > test.dat
grep -v "^0 " features > train.dat
brain -L -f train.dat -m model
brain -c -f test.dat -m model -o output
rm -rf brain.egg-info build data.db dist train.dat test.dat model features
```
