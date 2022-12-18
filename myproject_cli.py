# main part

import pickle
from conf.conf import logger
import numpy as np

# import argparse

# parser = argparse.ArgumentParser(description='Machine Learning Mini Project')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()

def execute_train():
    logger.info("Run trainning process..")
    return


def prediction(model_name, vals):
    logger.info("Loading models..")
    logger.info("Ready to predict..")
    model_to_load = 'model/saved/' + str(model_name)
    pickled_model = pickle.load(open(model_to_load, 'rb'))
    res = pickled_model.predict(vals)
    logger.info(f'Prediction result using {model_name} model is : {res}')
    return res

model_x = 'decision_tree.pkl'
model_y = 'random_forest.pkl'
model_z = 'svm.pkl'
data = np.array([52, 1, 0, 125, 212, 0, 1, 168, 0, 1, 2, 2, 3]).reshape(1, -1)

prediction(model_x, data)
prediction(model_y, data)
prediction(model_z, data)

