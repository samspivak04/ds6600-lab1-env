# happiness-analysis

Reports the mean happiness score of the ten highest-scoring countries in the
World Happiness Report 2018, and plots happiness against GDP per capita.

## Data

`data/happiness.csv` — World Happiness Report 2018, 156 countries, 11 columns.
Bundled with the repo, so no network access is needed.

## Setup

```
pip install -r requirements.txt
python analyze.py
```

That's it. Should take a couple of minutes.

## Output

Prints one number and writes `output/figure.png`.

---

*This ran fine on my laptop in the spring. If it doesn't run for you, check that
you're on a recent Python — I never had any trouble with it.*
