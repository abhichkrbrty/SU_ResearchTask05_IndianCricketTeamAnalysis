import pandas as pd

def validate_top_match_player(csv_path="../data/AllOdiPlayers.csv"):
    # Load and clean data
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()

    # Convert matches to numeric
    df["Mat"] = pd.to_numeric(df["Mat"], errors="coerce")

    # Sort by most matches
    top_player = df.sort_values(by="Mat", ascending=False).iloc[0]

    print("🏏 Most ODI Matches Played:")
    print(f"Name: {top_player['Name']}")
    print(f"Matches: {top_player['Mat']}")
    print(f"Innings: {top_player['Inn']}")
    print(f"Runs: {top_player['Runs']}")
    print(f"Average: {top_player['Avg']}")
    print(f"Highest Score: {top_player['HS']}")

if __name__ == "__main__":
    validate_top_match_player()