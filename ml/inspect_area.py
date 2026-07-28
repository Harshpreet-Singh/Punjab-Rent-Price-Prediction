from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "punjab_rental_dataset.csv"


def inspect_area():
    df = pd.read_csv(DATA_PATH)

    print("=" * 50)
    print("Area Statistics")
    print("=" * 50)

    print(df["area"].describe())

    print("\nQuartiles:")
    print(df["area"].quantile([0.25, 0.50, 0.75]))


if __name__ == "__main__":
    inspect_area()