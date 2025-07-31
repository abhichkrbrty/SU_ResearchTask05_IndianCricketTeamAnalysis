import pandas as pd

def validate_best_captain_min20(csv_path="../data/AllOdicaptains.csv"):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()

    # Clean and convert numeric columns
    df["Win%"] = pd.to_numeric(df["Win%"], errors="coerce")
    df["Played"] = pd.to_numeric(df["Played"], errors="coerce")

    # Filter for captains with >= 20 matches
    df_filtered = df[df["Played"] >= 20]

    # Sort by highest win%
    top = df_filtered.sort_values(by="Win%", ascending=False).iloc[0]

    print("🏆 Best ODI Captain (Min 20 Matches, by Win%):")
    print(f"Name: {top['Name']}")
    print(f"Matches Played: {top['Played']}")
    print(f"Wins: {top['Won']}")
    print(f"Losses: {top['Lost']}")
    print(f"Win Percentage: {top['Win%']}")

if __name__ == "__main__":
    validate_best_captain_min20()