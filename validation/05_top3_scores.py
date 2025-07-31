
import pandas as pd

def validate_top_3_scores(csv_path="../data/AllOdiPlayers.csv"):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    df["HS_numeric"] = df["HS"].astype(str).str.replace("*", "", regex=False).astype(float)
    top3 = df.sort_values(by="HS_numeric", ascending=False).head(3)

    print("🏏 Top 3 Highest ODI Scores:")
    for i, row in top3.iterrows():
        print(f"{row['Name']} – {row['HS']}")

if __name__ == "__main__":
    validate_top_3_scores()