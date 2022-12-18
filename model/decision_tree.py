import sys
# append modules path
sys.path.append("D:\HSE Classes\HSE MSc Big Data\Sem 1\Research seminar\Last HW\MiniProject\MiniProjectML")
import pickle
from conf.conf import logger
from connector.connect import get_data
from sklearn.tree import DecisionTreeClassifier
from utils.utils import data_split, save_model, return_settings_section

def init_model():
    """ Initialize the model with given parameters"""
    loaded_model = DecisionTreeClassifier(max_depth=3, random_state=3)
    logger.info("Initialzied the model")
    return loaded_model

def train(x, y):
    """ Fit data into the model"""
    ready_model = init_model()
    logger.info("Training the model")
    ready_model.fit(x, y)
    return ready_model

def run():
    """ Run the whole process"""
    logger.info("Loading data set..")
    dataset_path = return_settings_section("DATA", "dataset")
    df = get_data(dataset_path)
    X_train, X_test, y_train, y_test = data_split(df)
    model = train(X_train, y_train)
    save_model(return_settings_section("MODEL", "dt"), model)
    logger.info(f'accuracy is {model.score(X_test, y_test)}')

