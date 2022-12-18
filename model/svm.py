import sys
# append modules path
sys.path.append("D:\HSE Classes\HSE MSc Big Data\Sem 1\Research seminar\Last HW\MiniProject\MiniProjectML")
import pickle
from conf.conf import logger
from connector.connect import get_data
from sklearn.svm import SVC
from utils.utils import data_split

def init_model():
    """ Initialize the model with given parameters"""
    loaded_model = SVC(random_state=3, probability=True)
    logger.info("Initialzied the model")

    return loaded_model

def train(x, y):
    ready_model = init_model()

    logger.info("Training the model")
    ready_model.fit(x, y)

    pickle.dump(ready_model, open("model/saved/svm.pkl", 'wb'))

    return ready_model

logger.info("Loading data set..")
df = get_data('https://raw.githubusercontent.com/5x12/ml-cookbook/master/supplements/data/heart.csv')
X_train, X_test, y_train, y_test = data_split(df)
model = train(X_train, y_train)

logger.info(f'accuracy is {model.score(X_test, y_test)}')