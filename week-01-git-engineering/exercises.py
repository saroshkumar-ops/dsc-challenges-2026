"""
Week 1: Modern Git Engineering & Python Fundamentals
Data Science Club (DSC KLE) — Sprint Challenge Practice Tasks

Instructions for Recruits:
1. Complete the TODO sections in each function.
2. We have provided beginner-friendly scaffolding and hints so you can focus on core logic.
3. Test your code at any time by running: `python verify_submission.py`
"""

import csv
import json
from typing import Dict, List, Tuple, Any


# ==============================================================================
# TASK 1: Conditionals & Defensive Error Handling
# ==============================================================================

def evaluate_attendance_status(attended: int, total: int) -> str:
    """
    Evaluates attendance status based on institutional criteria.

    Rules:
      - If total <= 0: return 'NO_SESSIONS'
      - If attendance >= 75%: return 'ELIGIBLE' (meets academic credit criteria)
      - If attendance >= 65% and < 75%: return 'WARNING' (close to shortage)
      - If attendance < 65%: return 'SHORTAGE'

    Args:
        attended: Number of sessions attended.
        total: Total number of sessions held.
    """
    # Step 1: Check edge case where no sessions have occurred
    if total <= 0:
        return "NO_SESSIONS"

    # Step 2: Compute attendance percentage
    pct = (attended / total) * 100.0

    # TODO: Complete the conditional branching below:
    # If pct >= 75.0: return "ELIGIBLE"
    # Elif pct >= 65.0: return "WARNING"
    # Else: return "SHORTAGE"
    # (Hint: replace the line below with your if/elif/else block)
    raise NotImplementedError("Task 1a: Implement the if/elif/else logic")


def safe_parse_float(raw_value: Any, default: float = 0.0) -> float:
    """
    Safely converts dirty/raw input into a float without crashing your program.

    If conversion fails (e.g. ValueError when passing 'corrupted_string'),
    catch the error and return the default value.

    Args:
        raw_value: The value to parse (could be string, int, None, etc.)
        default: Fallback float if conversion fails.
    """
    # TODO: Implement a try/except block
    # Step 1: try returning float(raw_value)
    # Step 2: except (ValueError, TypeError), return default
    raise NotImplementedError("Task 1b: Implement try/except block")


# ==============================================================================
# TASK 2: Collections & Comprehensions
# ==============================================================================

def analyze_pod_scores(records: List[Tuple[str, str, float]]) -> Dict[str, Any]:
    """
    Analyzes student scores across pods using sets, dicts, and comprehensions.

    Args:
        records: A list of tuples formatted as (student_usn, pod_name, score).
                 Example: [("01FE25BCS122", "Parth's POD", 88.0), ...]

    Returns:
        dict:
          - 'unique_student_count': int (number of unique USNs, using set)
          - 'high_scorers': List[str] (list of USNs with score >= 80, using list comprehension)
          - 'pod_averages': Dict[str, float] (average score per pod, rounded to 2 decimals)
    """
    if not records:
        return {"unique_student_count": 0, "high_scorers": [], "pod_averages": {}}

    # Step A: Find unique student USNs using a set
    # Hint: Extract the first element (r[0]) from each tuple in records into a set
    # TODO: Replace the line below with your set of USNs:
    # unique_usns = {r[0] for r in records}
    unique_usns = set()  # TODO: extract unique USNs

    # Step B: Filter high scorers (score >= 80) using a list comprehension
    # Hint: [r[0] for r in records if r[2] >= 80.0]
    # TODO: Complete the list comprehension below:
    high_scorers = []  # TODO: implement list comprehension

    # Step C: Compute pod averages
    # We have already written the pod grouping accumulator loop for you!
    pod_totals: Dict[str, float] = {}
    pod_counts: Dict[str, int] = {}

    for usn, pod_name, score in records:
        pod_totals[pod_name] = pod_totals.get(pod_name, 0.0) + score
        pod_counts[pod_name] = pod_counts.get(pod_name, 0) + 1

    # Calculate average for each pod rounded to 2 decimal places
    pod_averages: Dict[str, float] = {}
    for pod_name in pod_totals:
        pod_averages[pod_name] = round(pod_totals[pod_name] / pod_counts[pod_name], 2)

    return {
        "unique_student_count": len(unique_usns),
        "high_scorers": high_scorers,
        "pod_averages": pod_averages,
    }


# ==============================================================================
# TASK 3: File I/O Pipeline (CSV & JSON)
# ==============================================================================

def summarize_csv_to_json(csv_path: str, json_path: str) -> Dict[str, Any]:
    """
    Reads a cohort CSV file and exports summary statistics into a JSON file.

    Summary structure:
      - 'total_students': int
      - 'branches': List[str] (sorted unique branch codes, e.g. ['BAR', 'BCI', 'BCS'])
      - 'average_score': float (overall cohort average rounded to 2 decimals)

    Args:
        csv_path: Path to input CSV (e.g., 'sample_cohort.csv')
        json_path: Path where summary JSON should be written
    """
    scores: List[float] = []
    branches: set = set()

    # Step 1: Read the CSV using Python's built-in csv.DictReader
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # TODO: Extract score as float and append to scores list:
            # if "score" in row and row["score"]:
            #     scores.append(float(row["score"]))
            #
            # TODO: Extract branch code and add to branches set:
            # if "branch" in row and row["branch"]:
            #     branches.add(row["branch"].strip().upper())
            pass

    # Step 2: Compute summary statistics (Scaffolded for you!)
    total_students = len(scores)
    sorted_branches = sorted(list(branches))
    avg_score = round(sum(scores) / total_students, 2) if total_students > 0 else 0.0

    summary = {
        "total_students": total_students,
        "branches": sorted_branches,
        "average_score": avg_score
    }

    # Step 3: Write out to JSON file (Scaffolded for you!)
    with open(json_path, mode="w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    return summary


# ==============================================================================
# TASK 4: Object-Oriented Domain Modeling (StudentRecord)
# ==============================================================================

class StudentRecord:
    """
    Tracks weekly performance scores for an individual DSC recruit.
    """

    def __init__(self, usn: str, name: str):
        """
        Initializes the student record.
        """
        self.usn = usn.strip().upper()
        self.name = name.strip()
        self.scores: List[float] = []

    def add_score(self, score: float) -> None:
        """
        Appends a new score. Validates that 0 <= score <= 100.

        Raises:
            ValueError: If score is less than 0 or greater than 100.
        """
        # TODO: Validate that score is between 0.0 and 100.0 (inclusive)
        # If valid: self.scores.append(float(score))
        # If invalid: raise ValueError("Score must be between 0 and 100")
        raise NotImplementedError("Task 4: Implement score range validation")

    def average(self) -> float:
        """
        Returns the mean score rounded to 2 decimal places.
        Returns 0.0 if no scores have been recorded yet.
        """
        # TODO: If self.scores is empty, return 0.0
        # Otherwise: return round(sum(self.scores) / len(self.scores), 2)
        raise NotImplementedError("Task 4: Implement average score calculation")

    def is_passing(self, threshold: float = 50.0) -> bool:
        """
        Returns True if the student's average score is >= threshold, else False.
        """
        # TODO: Check if self.average() >= threshold
        raise NotImplementedError("Task 4: Implement passing threshold check")
