from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from dataset.load_data import load_dataset


def train_model():

    df, iris = load_dataset()

    X = df.iloc[:, :-1]
    y = df["species"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        stratify=y,
        random_state=42
    )

    model = LogisticRegression(max_iter=200)

    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, accuracy, iris