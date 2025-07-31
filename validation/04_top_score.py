import pandas as pd

def validate_top_score(csv_path="../data/AllOdiPlayers.csv"):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    df["HS_numeric"] = df["HS"].astype(str).str.replace("*", "", regex=False).astype(float)
    top = df.sort_values(by="HS_numeric", ascending=False).iloc[0]

    print("🏏 Highest Individual ODI Score:")
    print(f"Name: {top['Name']}")
    print(f"Highest Score: {top['HS']}")
    print(f"Matches: {top['Mat']}")
    print(f"Runs: {top['Runs']}")
    print(f"Average: {top['Avg']}")

if __name__ == "__main__":
    validate_top_score()