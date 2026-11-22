"""Week 0: Python Fundamentals Bootcamp — Beginner Practice Tasks."""

import csv
import json
from typing import Dict, List, Tuple, Any


def evaluate_attendance_status(attended: int, total: int) -> str:
    """Return 'ELIGIBLE' (>=75%), 'WARNING' (65% to <75%), or 'SHORTAGE' (<65%).

    If total <= 0, return 'NO_SESSIONS'.
    """
    if total<=0:
        return "NO_SESSIONS"
    percentage=(attended/total)*100
    if percentage>=75:
        return "ELIGIBLE"
    elif percentage >=65:
        return "WARNING"
    else:
        return "SHORTAGE"


def safe_parse_float(raw_value: Any, default: float = 0.0) -> float:
    """Convert raw_value to float safely using try/except. Return default on failure."""
    try:
        return float(raw_value)
    except (ValueError,TypeError):
        return default

def analyze_pod_scores(records: List[Tuple[str, str, float]]) -> Dict[str, Any]:
    """Analyze (usn, pod_name, score) tuples using sets, dicts, and comprehensions.

    Returns a dictionary with keys:
      - 'unique_student_count': int (number of unique USNs via set)
      - 'high_scorers': List[str] (USNs with score >= 80 using a list comprehension)
      - 'pod_averages': Dict[str, float] (average score per pod rounded to 2 decimals)
    """
    unique_usns = set(record[0] for record in records)
    unique_student_count = len(unique_usns)
    high_scorers = list(set(
        record[0] for record in records if record[2] >= 80
    ))
    pod_scores = {}
    for usn, pod_name, score in records:
        if pod_name not in pod_scores:
            pod_scores[pod_name] = []
        pod_scores[pod_name].append(score)
    pod_averages = {
        pod: round(sum(scores) / len(scores), 2)
        for pod, scores in pod_scores.items()
    }
    return {
        "unique_student_count": unique_student_count,
        "high_scorers": high_scorers,
        "pod_averages": pod_averages
    }

def summarize_csv_to_json(csv_path: str, json_path: str) -> Dict[str, Any]:
    """Read cohort CSV using built-in csv module and export summary JSON.

    Summary dictionary must contain:
      - 'total_students': int
      - 'branches': List[str] (sorted unique branch codes)
      - 'average_score': float (rounded to 2 decimals)
    """

    students = []
    branches = []
    scores = []


    with open(csv_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)
            branches.append(row["branch"])
            scores.append(float(row["score"]))

    total_students = len(students)

    unique_branches = sorted(set(branches))

    if total_students > 0:
        average_score = sum(scores) / total_students
    else:
        average_score = 0.0

    average_score = round(average_score, 2)

    summary = {
        "total_students": total_students,
        "branches": unique_branches,
        "average_score": average_score
    }

    with open(json_path, "w") as file:
        json.dump(summary, file, indent=4)

    return summary


class StudentRecord:
    """Tracks weekly evaluation scores for a single DSC recruit."""

    def __init__(self, usn: str, name: str):
        """Initialize record with uppercase USN, name, and empty scores list."""
        self.usn = usn.upper()
        self.name = name
        self.scores = []

    def add_score(self, score: float) -> None:
        """Append a score (must be between 0 and 100; raise ValueError otherwise)."""
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")

        self.scores.append(score)

    def average(self) -> float:
        """Return average score rounded to 2 decimals, or 0.0 if no scores exist."""
        if len(self.scores) == 0:
            return 0.0

        total = sum(self.scores)
        avg = total / len(self.scores)

        return round(avg, 2)

    def is_passing(self, threshold: float = 50.0) -> bool:
        """Return True if average() >= threshold, else False."""
        if self.average() >= threshold:
            return True
        else:
            return False
