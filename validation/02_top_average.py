import pandas as pd

def validate_top_average(csv_path="../data/AllOdiPlayers.csv"):
    # Load and clean
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()

    # Convert 'Avg' to numeric
    df["Avg"] = pd.to_numeric(df["Avg"], errors="coerce")

    # Drop missing and sort
    df_valid_avg = df.dropna(subset=["Avg"])
    top_avg = df_valid_avg.sort_values(by="Avg", ascending=False).iloc[0]

    print("📊 Top ODI Batting Average:")
    print(f"Name: {top_avg['Name']}")
    print(f"Average: {top_avg['Avg']}")
    print(f"Runs: {top_avg['Runs']}")
    print(f"Matches: {top_avg['Mat']}")
    print(f"Innings: {top_avg['Inn']}")
    print(f"Highest Score: {top_avg['HS']}")

if __name__ == "__main__":
    validate_top_average()