import pandas as pd
import matplotlib.pyplot as plt

def plot_captain_win_rates(csv_path="../data/AllOdicaptains.csv"):
    # Load and clean
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    df["Played"] = pd.to_numeric(df["Played"], errors="coerce")
    df["Win%"] = pd.to_numeric(df["Win%"], errors="coerce")

    # Filter captains with ≥ 20 matches
    df_filtered = df[df["Played"] >= 20]

    # Sort by Win%
    df_sorted = df_filtered.sort_values(by="Win%", ascending=False)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.barh(df_sorted["Name"], df_sorted["Win%"], color="skyblue")
    plt.xlabel("Win Percentage")
    plt.ylabel("Captain")
    plt.title("🏏 Indian ODI Captains with ≥ 20 Matches — Win %")
    plt.gca().invert_yaxis()  # Highest on top
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_captain_win_rates()