# util/helper functions
import pickle
from conf.conf import logger
from sklearn.model_selection import train_test_split
from conf.conf import settings

def data_split(df):
    """ Split data into X_train, X_test, y_train, y_test """
    X = df.iloc[:, :-1] # Filter out target column
    y = df['target'] # Select target column

    # Split variables into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, #independent variables 
                                                        y, #dependent variable
                                                        random_state = 3)
    return X_train, X_test, y_train, y_test

def save_model(path, model):
    """ Save model into pickle file"""
    pickle.dump(model, open(path, 'wb'))
    logger.info(f'Saved the model in: {path}')


def return_settings_section(section, var):
    """ return values in the config file based on section and name"""
    with settings.using_env(section):
        if section == "DATA" and var == "dataset":
            return settings.dataset
        elif section == "MODEL" and var == "dt":
            return settings.decision_tree_path
        elif section == "MODEL" and var == "rf":
            return settings.random_forest_path
        elif section == "MODEL" and var == "svm":
            return settings.svm_path
        



