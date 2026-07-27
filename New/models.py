# ==========================================================
# Election Software - Data Models
# ----------------------------------------------------------
# Responsibilities:
# - Defines the structure of the application's data
# - Keeps candidate information together
# - Prevents image/name/vote mismatches
#
# This file DOES NOT:
# - Read CSV files
# - Load images
# - Handle networking
# - Display the UI
# ==========================================================

from dataclasses import dataclass, field

@dataclass
class Candidate:
    id: int
    name: str
    image_path: str


@dataclass
class Election:
    id: int
    title: str
    candidates: list[Candidate] = field(default_factory=list)


@dataclass
class Vote:
    selections: dict[int, int] = field(default_factory=dict)