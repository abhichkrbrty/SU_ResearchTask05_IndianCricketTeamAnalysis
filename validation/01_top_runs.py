import pandas as pd

def validate_top_run_scorer(csv_path="../data/AllOdiPlayers.csv"):
    # Load data
    df = pd.read_csv(csv_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert Runs to numeric (handle non-numeric like '-')
    df["Runs"] = pd.to_numeric(df["Runs"], errors="coerce")

    # Drop NaNs and sort
    df = df.dropna(subset=["Runs"])
    top = df.sort_values(by="Runs", ascending=False).iloc[0]

    print("🏏 Top ODI Run Scorer:")
    print(f"Name: {top['Name']}")
    print(f"Runs: {int(top['Runs'])}")
    print(f"Matches: {top['Mat']}")
    print(f"Innings: {top['Inn']}")
    print(f"Average: {top['Avg']}")
    print(f"Highest Score: {top['HS']}")

if __name__ == "__main__":
    validate_top_run_scorer()