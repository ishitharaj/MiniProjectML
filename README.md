# MiniProjectML
## HSE Assignment Mini Project

### DESCRIPTION:  
This is a mini project which can make predictions using ML algorithms based on given set of data.

Example input set of data:
![image](https://user-images.githubusercontent.com/38528963/208321709-10cdbacc-6213-46ba-881e-3bbc5ffff923.png)


Dataset which used to train the models:  
https://github.com/5x12/ml-cookbook/blob/master/supplements/data/heart.csv 


### USAGE:   
#### flags:  
    -t   : passing this flag will triggier the train process again for all models  
    -dt  : passing this flag will use decision tree model to predict  
    -rf  : passing this flag will use random forest model to predict  
    -svm : passing this flag will use svm model to predict  
    -p   : with this flag you can pass the input data to predict  

Example:  
To train only:  
`python .\myproject_cli.py -t`  

To predict using random forest:  
`python .\myproject_cli.py -rf -p 52 1 0 125 212 0 1 168 0 1 2 2 3`  

To predict using all models:  
`python .\myproject_cli.py -dt -rf -svm -p 52 1 0 125 212 0 1 168 0 1 2 2 3`  

To train and predict using all models:  
`python .\myproject_cli.py -t -dt -rf -svm -p 52 1 0 125 212 0 1 168 0 1 2 2 3`  


Expected results:  
![image](https://user-images.githubusercontent.com/38528963/208633781-5a466b11-419d-4b77-afa6-e6e4d5bfef46.png)


