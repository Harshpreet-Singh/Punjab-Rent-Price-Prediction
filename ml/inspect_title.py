from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent


def inspect_titles():

    df = pd.read_csv(
        BASE_DIR / "data" / "punjab_rental_dataset.csv"
    )

    print("=" * 50)
    print("Sample Titles")
    print("=" * 50)

    for title in df["title"].head(50):
        print(title)


if __name__ == "__main__":
    inspect_titles()