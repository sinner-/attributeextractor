#brain

## Usage
```
python setup.py install
rm -rf brain.egg-info build data.db dist train.dat test.dat model output features
brain-manage -c -d data.db -f SPY.csv
brain-manage -i -d data.db -t SPY -f SPY.csv
brain -e -d data.db -t SPY -f features -l 21 -p 5
grep "^0 " features > test.dat
grep -v "^0 " features > train.dat
~/Downloads/svm_learn ./train.dat ./model
~/Downloads/svm_classify ./test.dat ./model ./output
rm -rf brain.egg-info build data.db dist train.dat test.dat model features
```
