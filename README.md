## Folder Structure
In Code/ folder, it contains all code needed to run the experiments on data in Java and data in Python. <br/>
In Data/ folder, it contains all original clone pairs in Java and Python, the statement labels and token labels. <br/>
In Result/ folder, it contains all experiment results. 

## How to run experiments
First, you need to install all required package,
```angular2html
pip install transformers==4.0.1
pip install torch===1.7.0
pip install numpy===1.19.2
pip install -U scikit-learn
pip install seaborn===0.11.0
pip install pandas===1.1.3
pip install tqdm===4.50.2
pip install shap
```
Then download mymodel.bin and put it in Code/Java and Code/Python folder, then copy the data in Data/ folder into corresponding folder in Code/. (e.g. put three folders in Data/Python folder into Code/Python folder)
```angular2html
cd Code/Python
python Statement&Token.py
cd Code/Java
python Statement&Token.py
```
After that, two files python_result.csv and java_result.csv will be generated