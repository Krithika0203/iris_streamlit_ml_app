def predict_flower(model, iris, features):

    prediction = model.predict([features])

    return iris.target_names[prediction][0]