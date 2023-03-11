import matplotlib.pyplot as plt
import pandas as pd

def create_plot():
    df = pd.read_excel('data.xlsx')
    freqs = df.groupby(['Themes']).size()
    pie = freqs.plot.pie()
    plt.savefig('figures/pie.jpg')
