import pandas as pd

def validate_best_captain(csv_path="../data/AllOdicaptains.csv"):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()

    # Convert Win% to numeric
    df["Win%"] = pd.to_numeric(df["Win%"], errors="coerce")

    # Sort by highest win percentage
    top = df.sort_values(by="Win%", ascending=False).iloc[0]

    print("🏆 Best ODI Captain (by Win%):")
    print(f"Name: {top['Name']}")
    print(f"Matches Played: {top['Played']}")
    print(f"Wins: {top['Won']}")
    print(f"Losses: {top['Lost']}")
    print(f"Win Percentage: {top['Win%']}")

if __name__ == "__main__":
    validate_best_captain()