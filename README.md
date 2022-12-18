# MiniProjectML
## HSE Assignment Mini Project

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

