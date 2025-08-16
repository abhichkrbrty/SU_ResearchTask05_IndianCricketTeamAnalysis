import pandas as pd

def validate_most_hundreds(csv_path="../data/AllOdiPlayers.csv"):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()

    # Convert 100s to numeric
    df['100'] = pd.to_numeric(df['100'], errors='coerce')
    top_100s = df.sort_values(by='100', ascending=False).iloc[0]

    print("🏆 Most ODI Hundreds:")
    print(f"Name: {top_100s['Name']}")
    print(f"100s: {top_100s['100']}")
    print(f"Matches: {top_100s['Mat']}")
    print(f"Innings: {top_100s['Inn']}")
    print(f"Runs: {top_100s['Runs']}")
    print(f"Average: {top_100s['Avg']}")

if __name__ == "__main__":
    validate_most_hundreds()