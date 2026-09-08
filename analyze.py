"""
analyze.py — World Happiness Report 2018

Reports the mean happiness score of the ten highest-scoring countries and
writes a figure showing the relationship between GDP per capita and
happiness score.

Usage:
    python analyze.py
"""

import os

import matplotlib
matplotlib.use("Agg")  # write files without needing a display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# DATA = os.path.join("data", "happiness.csv")
DATA = "happiness.csv"
OUTDIR = "output"

SCORE = "Happiness score"
GDP = "Explained by: GDP per capita"


def main():
    df = pd.read_csv(DATA)

    top10 = df.nlargest(10, SCORE)
    answer = np.mean(top10[SCORE].to_numpy())
    print(f"Mean happiness score, top 10 countries: {answer:.4f}")

    os.makedirs(OUTDIR, exist_ok=True)

    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.scatterplot(data=df, x=GDP, y=SCORE, ax=ax)
    ax.set_xlabel("Happiness explained by GDP per capita")
    ax.set_ylabel("Happiness score")
    ax.set_title("World Happiness Report 2018")
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, "figure.png"), dpi=150)

    print(f"Wrote {os.path.join(OUTDIR, 'figure.png')}")


if __name__ == "__main__":
    main()
