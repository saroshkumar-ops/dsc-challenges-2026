
"""Week 1: Python Fundamentals Bootcamp."""

import csv
import json
from typing import Dict, List, Tuple, Any


def evaluate_attendance_status(attended: int, total: int) -> str:
    if total <= 0:
        return "NO_SESSIONS"

    percentage = attended / total * 100

    if percentage >= 75:
        return "ELIGIBLE"
    elif percentage >= 65:
        return "WARNING"
    else:
        return "SHORTAGE"


def safe_parse_float(raw_value: Any, default: float = 0.0) -> float:
    try:
        return float(raw_value)
    except (ValueError, TypeError):
        return default


def analyze_pod_scores(records: List[Tuple[str, str, float]]) -> Dict[str, Any]:
    unique_students = set(usn for usn, pod, score in records)

    high_scorers = [
        usn for usn, pod, score in records if score >= 80
    ]

    pod_names = set(pod for usn, pod, score in records)

    pod_averages = {}

    for pod in pod_names:
        scores = [score for usn, name, score in records if name == pod]
        pod_averages[pod] = round(sum(scores) / len(scores), 2)

    return {
        "unique_student_count": len(unique_students),
        "high_scorers": high_scorers,
        "pod_averages": pod_averages
    }


def summarize_csv_to_json(csv_path: str, json_path: str) -> Dict[str, Any]:
    scores = []
    branches = set()

    with open(csv_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            branches.add(row["branch"])
            scores.append(float(row["score"]))

    summary = {
        "total_students": len(scores),
        "branches": sorted(branches),
        "average_score": round(sum(scores) / len(scores), 2) if scores else 0.0
    }

    with open(json_path, "w") as file:
        json.dump(summary, file, indent=4)

    return summary


class StudentRecord:
    def __init__(self, usn: str, name: str):
        self.usn = usn.upper()
        self.name = name
        self.scores = []

    def add_score(self, score: float) -> None:
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.scores.append(score)

    def average(self) -> float:
        if not self.scores:
            return 0.0
        return round(sum(self.scores) / len(self.scores), 2)

    def is_passing(self, threshold: float = 50.0) -> bool:
        return self.average() >= threshold
