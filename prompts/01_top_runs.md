## Prompt 01 — Who scored the most runs?

**Question:**
From this dataset of Indian ODI players, who has scored the most runs?

**Dataset Preview (first 10–15 rows of AllOdiPlayers.csv):**

|   No | Name                   | First | Last | Mat | Inn | NO | Runs | HS   | Avg  | Balls | Mdn | Runs.1 | Wkt | BBM   | Avg.1 | Ca | St |
|------|------------------------|-------|------|-----|-----|----|------|------|------|--------|-----|--------|-----|--------|-------|----|----|
| 1    | Syed Abid Ali          | 1974  | 1975 | 5   | 3   | 0  | 93   | 70   | 31.0 | 336    | 10  | 187    | 7   | 22-Feb | 26.71 | 0  | 0  |
| 2    | Bishan Singh Bedi      | 1974  | 1979 | 10  | 7   | 2  | 31   | 13   | 6.2  | 590    | 17  | 340    | 7   | Feb-44 | 48.57 | 4  | 0  |
| 3    | Farokh Engineer        | 1974  | 1975 | 5   | 4   | 1  | 114  | 54*  | 38.0 | 0      | 0   | 0      | 0   | 0      | 0.0   | 3  | 1  |
| 4    | Sunil Gavaskar         | 1974  | 1987 | 108 | 102 | 14 | 3092 | 103* | 35.1 | 1204   | 3   | 873    | 1   | 34     | 873.0 | 27 | 0  |
| 5    | Madan Lal              | 1974  | 1987 | 67  | 38  | 8  | 401  | 53*  | 13.4 | 3068   | 21  | 1991   | 73  | 4-Mar  | 27.26 | 12 | 0  |
| 6    | Mohinder Amarnath      | 1975  | 1989 | 85  | 75  | 13 | 1924 | 102* | 31.0 | 2542   | 18  | 1780   | 46  | 5-Jan  | 38.69 | 19 | 0  |
| 7    | Anshuman Gaekwad       | 1975  | 1987 | 40  | 32  | 3  | 269  | 78   | 9.28 | 186    | 1   | 140    | 2   | 2-Jan  | 70.0  | 9  | 0  |
| 8    | Eknath Solkar          | 1975  | 1975 | 1   | 1   | 0  | 10   | 10   | 10.0 | 72     | 0   | 50     | 0   | 0      | 0.0   | 1  | 0  |
| 9    | Srinivas Venkataraghavan | 1975 | 1983 | 15  | 9   | 3  | 38   | 26*  | 6.33 | 933    | 20  | 480    | 5   | 3-Feb  | 96.0  | 2  | 0  |
| 10   | Brijesh Patel          | 1975  | 1980 | 21  | 20  | 1  | 493  | 82   | 25.9 | 0      | 0   | 0      | 0   | 0      | 0.0   | 4  | 0  |
| 11   | Gundappa Viswanath     | 1974  | 1982 | 25  | 22  | 0  | 439  | 75   | 20.0 | 0      | 0   | 0      | 0   | 0      | 0.0   | 8  | 0  |
| 12   | Karsan Ghavri          | 1975  | 1981 | 19  | 13  | 5  | 119  | 38*  | 14.9 | 922    | 17  | 493    | 15  | 4-Mar  | 32.86 | 2  | 0  |
| 13   | Dilip Vengsarkar       | 1976  | 1991 | 129 | 120 | 15 | 3508 | 105  | 34.6 | 125    | 0   | 97     | 1   | 1-Jan  | 97.0  | 31 | 0  |
| 14   | Chetan Chauhan         | 1976  | 1981 | 7   | 7   | 0  | 153  | 46   | 21.9 | 0      | 0   | 0      | 0   | 0      | 0.0   | 1  | 0  |
| 15   | Roger Binny            | 1980  | 1987 | 72  | 59  | 14 | 629  | 57*  | 13.9 | 3112   | 10  | 2346   | 77  | 4-Mar  | 30.45 | 10 | 0  |



**LLM Answer:**

Sachin Tendulkar scored the most runs in ODI matches for India.

---

### ✅ Validation (Python Result)

```text
Name: Sachin Tendulkar  
Runs: 18426  
Matches: 463  
Innings: 452  
Average: 44.83  
Highest Score: 200*