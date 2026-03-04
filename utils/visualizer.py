import matplotlib.pyplot as plt
import seaborn as sns

def plot_pairplot(df):

    fig = sns.pairplot(df, hue="species")
    return fig