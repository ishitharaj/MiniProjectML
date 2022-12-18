# main part
import pickle
import warnings
from conf.conf import logger
import numpy as np
from argparse import ArgumentParser
from model import decision_tree, random_forest, svm
warnings.filterwarnings("ignore")

def execute_train(flag=True):
    """ Execute training"""
    if flag == True:
        logger.info("\n\nRun trainning process for decsion tree..")
        decision_tree.run()
        logger.info("\n\nRun trainning process for Random forest..")
        random_forest.run()
        logger.info("\n\nRun trainning process for SVM ..")
        svm.run()
        logger.info("\n\nTraning completed!")

    
def prediction(model_name, vals):
    logger.info("Loading models..")
    logger.info("Ready to predict..")
    model_to_load = 'model/saved/' + str(model_name)
    pickled_model = pickle.load(open(model_to_load, 'rb'))
    res = pickled_model.predict(vals)
    logger.info(f'Prediction result using {model_name} model is : {res}')
    return res

parser = ArgumentParser()
parser.add_argument("-t", "--train", action="store_true")
parser.add_argument("-dt", "--decision_tree", action="store_true")
parser.add_argument("-rf", "--random_forest", action="store_true")
parser.add_argument("-svm", "--svm", action="store_true")
parser.add_argument('-p','--predict', nargs='+', help='<Required> Set flag', required=True)
args = parser.parse_args()
if args.train:
    execute_train()

if args.predict:
    data_to_predict = np.array([eval(i) for i in args.predict]).reshape(1, -1)
    if args.decision_tree:
        model_x = 'decision_tree.pkl'
        prediction(model_x, data_to_predict)
    if args.random_forest:
        model_y = 'random_forest.pkl'
        prediction(model_y, data_to_predict)
    if args.svm:
        model_z= 'svm.pkl'
        prediction(model_z, data_to_predict)