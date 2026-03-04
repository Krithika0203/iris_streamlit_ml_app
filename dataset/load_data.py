from sklearn.datasets import load_iris
import pandas as pd

def load_dataset():

    iris = load_iris()

    df = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )

    df["species"] = iris.target

    return df, iris