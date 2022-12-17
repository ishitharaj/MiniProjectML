from conf.conf import logging
from connector.connector import get_data
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def data_split(df):
    """ Split data into X_train, X_test, y_train, y_test """
    X = X = df.iloc[:, :-1] # Filter out target column
    y = df['target'] # Select target column

    # Split variables into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, #independent variables 
                                                        y, #dependent variable
                                                        random_state = 3)
    return X_train, X_test, y_train, y_test


def init_model(*args):
    """ Initialize the model with given parameters"""
    loaded_model = DecisionTreeClassifier(args)
    logging.info("Initialzied the model")

    return loaded_model

def train(x, y):
    ready_model = init_model(max_depth=3, random_state=3)


    logging.info("Training the model")
    ready_model.fit(x, y)


logging.INFO("Loading data set..")
df = get_data("https://github.com/5x12/ml-cookbook/blob/882ad1141b32155a4e3ec56e7bc16a3257bdb3c9/supplements/data/heart.csv")
X_train, X_test, y_train, y_test = data_split(df)
model = train(X_train, y_train)

logging.info(f'accuracy is {model.score(X_test, y_test)}')