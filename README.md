# 🏏 SU_ResearchTask05_IndianCricketTeamAnalysis

This research project explores career statistics of Indian national cricket team players and captains (ODI & Test) using structured datasets.  
It is part of the OPT Research Task 05 at Syracuse University.

---

## 📦 Dataset

We use 4 CSV files:
- `AllOdiPlayers.csv` – 241 rows × 10 columns  
- `AllOdicaptains.csv` – 25 rows × 8 columns  
- `AllTestplayers.csv` – 303 rows × 10 columns  
- `AllTestcaptains.csv` – 31 rows × 7 columns  

**Source**: [Wikipedia](https://en.wikipedia.org/)

> ⚠️ **These files are not committed to the repo**. Please download them and place under `/data`.

---

## 🧠 Research Goal

The objective is to evaluate how well LLMs (like GPT-4) can answer questions using this dataset.  
We write natural language prompts and compare LLM outputs to actual values computed via Python.

Key research questions:
- Can the LLM answer direct stats queries reliably?
- Where does it hallucinate or approximate?
- How much reasoning does it apply?
- Can prompt engineering improve its accuracy?

---

## 📂 Project Structure

```
SU_ResearchTask05_IndianCricketTeamAnalysis/
├── data/                      # CSV files (ignored in Git)
├── prompts/                  # Natural language questions + LLM answers
├── validation/               # Python scripts to compute actual results
├── .gitignore
└── README.md
```

---

## 💬 Prompt & Validation Flow

Each prompt follows this flow:

1. **Markdown File** (in `/prompts`)  
   - Contains the prompt question  
   - Captures the LLM response  
   - Logs the Python validation result

2. **Validation Script** (in `/validation`)  
   - Loads the CSVs  
   - Computes the actual answer  
   - Compares to LLM’s output

### Example:
- `01_top_runs.md`: "Who scored the most ODI runs?"
- `01_top_runs.py`: Python to get the real answer from `AllOdiPlayers.csv`

---

## 📊 Visualizations

Some answers (e.g. top captains by win %) are also visualized using `matplotlib`.  
Example script: `08_best_captain_min20_visual.py`

To run charts:

```bash
pip install pandas matplotlib
```

---

## ✍️ Reflections

This task made it clear that:
- **LLMs handle simple stats well** but need help on multi-condition filters
- Prompt phrasing plays a huge role
- Combining LLMs with Python validation ensures factual correctness
- This hybrid approach is ideal for research and dashboard automation

---

## 🔄 Week 1–2: Progress Summary

During the first two weeks of Task 05, we focused on verifying how accurately an LLM (ChatGPT 4) could answer cricket-related statistical queries using structured CSV datasets of Indian ODI players and captains.

We designed and tested **9 core prompts** including:

- Top run scorer  
- Best batting average  
- Most matches played  
- Highest individual score  
- Most hundreds  
- Most runs as captain  
- Best win percentage (overall)  
- Best captain with 20+ matches  
- Visualization of top 5 captains by win %

For each question:
- We recorded the LLM’s natural language response
- We validated it using custom Python scripts (in `/validation`)
- In some cases, we plotted results with Matplotlib

The LLM performed **well on direct queries** but required guidance or clarification for:
- Edge cases (e.g., single-match captains with 100% win)
- Ambiguities in columns or formatting

This dual approach proved effective in spotting LLM errors and helped us design better prompts for future experiments.

> All results are recorded in the `/prompts/` folder  
> All validation scripts are available in `/validation/`

---

## 📌 Author

**Abhi Chakraborty**  
M.S. Applied Data Science, Syracuse University  
GitHub: [abhichkrbrty](https://github.com/abhichkrbrty/SU_ResearchTask05_IndianCricketTeamAnalysis)