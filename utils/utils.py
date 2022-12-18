# util/helper functions
from sklearn.model_selection import train_test_split

def data_split(df):
    """ Split data into X_train, X_test, y_train, y_test """
    X = df.iloc[:, :-1] # Filter out target column
    y = df['target'] # Select target column

    # Split variables into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, #independent variables 
                                                        y, #dependent variable
                                                        random_state = 3)
    return X_train, X_test, y_train, y_test