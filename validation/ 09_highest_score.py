import pandas as pd

def validate_highest_score(csv_path="../data/AllOdiPlayers.csv"):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()

    # Clean and extract numeric values (handle * in scores)
    df['HS_numeric'] = df['HS'].astype(str).str.replace('*', '', regex=False)
    df['HS_numeric'] = pd.to_numeric(df['HS_numeric'], errors='coerce')

    top_score = df.sort_values(by='HS_numeric', ascending=False).iloc[0]

    print("🏏 Highest ODI Score:")
    print(f"Name: {top_score['Name']}")
    print(f"Score: {top_score['HS']}")
    print(f"Matches: {top_score['Mat']}")
    print(f"Innings: {top_score['Inn']}")
    print(f"Runs: {top_score['Runs']}")
    print(f"Average: {top_score['Avg']}")

if __name__ == "__main__":
    validate_highest_score()