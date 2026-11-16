# 🌿 Week 1 Sprint Challenge: Modern Git Engineering & Python Fundamentals
> **Track**: Credit Track (2nd Year) & Growth Track (1st Year)  
> **Deadline**: Sunday, November 22, 2026 @ 11:59 PM IST  
> **Submission Platform**: DSC Nexus (`/modules` → Week 1)

---

## 🎯 Learning Objectives
1. **Git CLI Mastery**: Configure terminal identity, understand project hierarchy, and practice feature branching with conventional commit messages.
2. **Core Python Fundamentals**: Learn defensive input handling (`try/except`), collections (`set`, list comprehensions), clean file I/O (`csv` & `json`), and object-oriented programming (`class`).
3. **Automated Verification**: Run the built-in local self-grader (`python verify_submission.py`) to verify all 10 checks.

---

## 📁 Files in This Challenge
```
week-01-git-engineering/
├── README.md               ← Complete challenge guide (Start here!)
├── exercises.py            ← Complete Python tasks here (Scaffolded with hints)
├── sample_cohort.csv       ← Sample dataset for Task 3 (File I/O)
├── verify_submission.py    ← Local automated self-grader (checks all 10 tasks)
├── .gitignore              ← Production gitignore rules
├── data/raw/.gitkeep       ← Raw dataset placeholder
├── notebooks/.gitkeep      ← Exploration notebooks placeholder
└── src/
    └── fetch_metadata.py   ← Environment diagnostic script (Update your USN here)
```

---

## 📋 Part 1: Git & GitHub Engineering Tasks

### Task 1: Terminal Identity Setup
Make sure your Git CLI is configured with your full name and university email:
```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.usn@kletech.ac.in"
```

### Task 2: Build the Directory Layout
Ensure the following folders exist inside `week-01-git-engineering/`:
- `data/raw/`
- `notebooks/`
- `src/`

*(Tip: Empty folders are ignored by Git unless they contain a `.gitkeep` file!)*

### Task 3: Complete `src/fetch_metadata.py`
Open `src/fetch_metadata.py` and:
1. Replace `01FEXXXXXXXX` and `"Your Full Name"` with your actual college USN and Name.
2. Run `python src/fetch_metadata.py` to verify it prints your diagnostic JSON.

### Task 4: Terminal Branching & Atomic Commits
In professional data science teams, engineers never commit directly to `main`:
1. Create and switch to a feature branch:
   ```bash
   git checkout -b feature/setup-eda
   ```
2. Stage and commit your changes using a conventional commit prefix (`feat:`, `fix:`, `docs:`, `chore:`):
   ```bash
   git add src/fetch_metadata.py
   git commit -m "feat(metadata): configure student identity"
   ```
3. Switch back to `main` and merge your feature branch:
   ```bash
   git checkout main
   git merge feature/setup-eda
   ```

---

## 📋 Part 2: Python Fundamentals Practice (`exercises.py`)

Open `exercises.py`. We have provided beginner-friendly scaffolding and comments for all 4 tasks:

### Task 1: Conditionals & Defensive Error Handling
- **`evaluate_attendance_status(attended, total)`**:
  - If `total <= 0`, return `"NO_SESSIONS"`.
  - Otherwise calculate `pct = (attended / total) * 100`.
  - Return `"ELIGIBLE"` if $\ge 75\%$, `"WARNING"` if between $65\%$ and $74.9\%$, and `"SHORTAGE"` if $< 65\%$.
- **`safe_parse_float(raw_value, default=0.0)`**:
  - Wrap `float(raw_value)` in a `try...except (ValueError, TypeError)` block to return `default` instead of crashing when dirty data arrives.

### Task 2: Collections & List Comprehensions
- **`analyze_pod_scores(records)`**:
  - Extract unique USNs using a `set`: `{r[0] for r in records}`.
  - Filter USNs with score $\ge 80$ using a list comprehension: `[r[0] for r in records if r[2] >= 80.0]`.
  - The pod grouping accumulator loop is already written for you!

### Task 3: File I/O Pipeline (`csv` & `json`)
- **`summarize_csv_to_json(csv_path, json_path)`**:
  - Read `sample_cohort.csv` with `csv.DictReader`.
  - Extract `float(row["score"])` and `row["branch"]`.
  - The summary computation and `json.dump` are scaffolded for you!

### Task 4: Object-Oriented Domain Modeling (`StudentRecord`)
- Complete the `StudentRecord` class:
  - `add_score(self, score)`: Check that `0.0 <= score <= 100.0`. If valid, append to `self.scores`; otherwise raise `ValueError`.
  - `average(self)`: Return `round(sum(self.scores) / len(self.scores), 2)`, or `0.0` if `self.scores` is empty.
  - `is_passing(self, threshold=50.0)`: Return `True` if `self.average() >= threshold`.

---

## ✅ Run the Local Auto-Grader
Execute the verification script inside your terminal anytime:
```bash
python verify_submission.py
```
Target: **10/10 checks passed (100%)**!

---

## 🚀 How to Submit on DSC Nexus
1. Stage, commit, and push your changes to your personal GitHub fork:
   ```bash
   git add .
   git commit -m "feat(week01): complete simplified git and python challenge"
   git push origin main
   ```
2. Copy your fork's GitHub repository link:  
   `https://github.com/<your-username>/dsc-challenges-2026`
3. Log into **DSC Nexus** ([dsc-nexus-app-production.up.railway.app](https://dsc-nexus-app-production.up.railway.app)), open **Modules → Week 1**, paste your URL, and click **Submit sprint work**.
4. Your assigned 3rd-year mentor will review your submission and provide feedback.
