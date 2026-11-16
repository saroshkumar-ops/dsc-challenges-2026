# 🚀 Data Science Club (DSC KLE) — Sprint Challenges 2026
> **Official Monorepo Starter Template for Junior Recruits (1st-Year Growth Track & 2nd-Year Credit Track)**  
> KLE Technological University, Hubballi • Lead: Sarosh Kumar • Faculty Coordinator: Prof. Sneha Madam

---

## 📌 How This Repository Works
This single repository is your **Data Science Portfolio** for the entire semester. Instead of managing multiple separate repositories, each weekly sprint will live here in organized sprint folders:

```
dsc-challenges-2026/
├── week-01-git-engineering/        ← Sprint 1: Git/GitHub Engineering & Core Python Fundamentals
└── (Upcoming weekly sprints are unlocked every Monday at 5:00 PM during lab sync)
```

---

## 🛠️ Step 1: One-Time Local Setup (Week 1)

### 1. Fork this Repository
Click the **Fork** button (top-right of this GitHub page) to create a copy under your personal GitHub profile:  
`https://github.com/<your-github-username>/dsc-challenges-2026`

### 2. Clone your Fork locally
Open your terminal (PowerShell, Bash, or Zsh) and run:
```bash
git clone https://github.com/<your-github-username>/dsc-challenges-2026.git
cd dsc-challenges-2026
```

### 3. Add Upstream Remote (To pull future weekly sprints)
```bash
git remote add upstream https://github.com/saroshkumar-ops/dsc-challenges-2026.git
git remote -v
# You should see 'origin' (your fork) and 'upstream' (the club's master template)
```

### 4. Create a Virtual Environment & Install Dependencies
```bash
# Python 3.10+ recommended
python -m venv .venv

# Activate on Windows PowerShell:
.venv\Scripts\Activate.ps1

# Activate on Mac/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

---

## ⚡ Weekly Workflow (Every Monday 5:00 PM)

Whenever a new sprint is released on **DSC Nexus**:

1. **Pull the newest sprint from upstream**:
   ```bash
   git pull upstream main
   ```
2. **Open the week's folder** (e.g., `cd week-01-git-engineering`).
3. **Follow the instructions** in that week's `README.md`.
4. **Run the local self-verification script** before submitting:
   ```bash
   python verify_submission.py
   ```
5. **Commit your work** with descriptive messages:
   ```bash
   git add .
   git commit -m "feat(week01): complete project structure and metadata script"
   git push origin main
   ```
6. **Submit your GitHub repo URL** on **DSC Nexus** (https://dsc-nexus-app-production.up.railway.app) before Sunday 11:59 PM.

---

## 🛡️ Anti-Plagiarism & Authentic Learning Policy
- **LLM Assistance (ChatGPT, Claude, Copilot)**: You are welcome to use AI as a tutor to explain syntax and compiler errors. However, all submissions require:
  1. Passing local test assertions with your **unique student USN seed**.
  2. A verified **Git commit history** showing genuine progression (not a single bulk copy-paste commit).
  3. Personal written insight callouts.
- Pod mentors review code quality, test results, and commit logs during Monday 5:00 PM sprint roll-calls.

---

*Need help? Reach out to your assigned 3rd-year Pod Mentor or post in the DSC KLE Discord/WhatsApp group.*
