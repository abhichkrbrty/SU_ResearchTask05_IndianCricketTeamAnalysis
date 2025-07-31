import pandas as pd

def validate_most_wins(csv_path="../data/AllOdicaptains.csv"):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()

    # Ensure numeric
    df["Won"] = pd.to_numeric(df["Won"], errors="coerce")

    # Get captain with max wins
    top = df.sort_values(by="Won", ascending=False).iloc[0]

    print("🧢 Most ODI Wins as Captain:")
    print(f"Name: {top['Name']}")
    print(f"Matches Played: {top['Played']}")
    print(f"Wins: {top['Won']}")
    print(f"Losses: {top['Lost']}")
    print(f"Win Percentage: {top['Win%']}")

if __name__ == "__main__":
    validate_most_wins()