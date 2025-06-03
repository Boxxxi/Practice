import pandas as pd
import warnings


pd.set_option("display.max_columns", None)
warnings.simplefilter(action="ignore")


def load_and_display_dataset_details():
    dbpedia_14_train = pd.read_csv("../input/dbpedia_14_train.csv")
    dbpedia_14_test = pd.read_csv("../input/dbpedia_14_test.csv")
    print("Train Dataset Info: \n", dbpedia_14_train.info())
    print("Test Dataset Info: \n", dbpedia_14_test.info())
    print("\nTraining Dataset columns : \n", dbpedia_14_train.columns)
    print("\nTest Dataset columns : \n", dbpedia_14_test.columns)
    print("\nTrain dataset shape: [", dbpedia_14_train.shape, "]\n")
    print("\nTest dataset shape: [", dbpedia_14_test.shape, "]\n")
    return dbpedia_14_train, dbpedia_14_test


def create_train_test_split(dbpedia_14_train, dbpedia_14_test, model_name):
    X_train = dbpedia_14_train[:]["Content"]
    y_train = dbpedia_14_train[:]["Labels"]
    X_test = dbpedia_14_test[:]["Content"]
    y_test = dbpedia_14_test[:]["Labels"]
    print("Train Test split details for {}: \n".format(model_name), X_train.shape, y_train.shape, X_test.shape, y_test.shape)
    return X_train, X_test, y_train, y_test
