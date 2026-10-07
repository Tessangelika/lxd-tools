#!/usr/bin/env python3
"""
Storyboard Scaffold Generator
==============================
Generates a blank storyboard framework for a given number of slides/screens.

Usage:
    python storyboard_generator.py

Or import and call generate_storyboard() directly.
"""

import csv
import os
from datetime import date


STORYBOARD_FIELDS = [
    "Slide",
    "Screen title",
    "Narration script",
    "On-screen text",
    "Visual / graphic notes",
    "Interaction type",
    "Interaction notes",
    "Audio cues",
    "Branching / next slide",
    "Status",
    "Notes"
]

INTERACTION_TYPES = [
    "Linear (click to advance)",
    "Multiple choice question",
    "Drag and drop",
    "Hotspot",
    "Scenario / branching",
    "Reflection prompt",
    "Video",
    "Animation",
    "Knowledge check — true/false",
    "Summary / recap"
]


def generate_storyboard_csv(project_name, num_slides, designer, filename=None):
    """
    Generate a storyboard scaffold as a CSV file.

    Args:
        project_name (str): Name of the course or module
        num_slides (int): Number of slides/screens to scaffold
        designer (str): Designer name for the header
        filename (str): Output filename (optional, auto-generated if not provided)

    Returns:
        str: Path to the generated CSV file
    """
    if not filename:
        safe_name = project_name.replace(' ', '_').lower()
        filename = f"{safe_name}_storyboard.csv"

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Header rows
        writer.writerow(["STORYBOARD", project_name])
        writer.writerow(["Designer", designer])
        writer.writerow(["Date", date.today().strftime("%d %B %Y")])
        writer.writerow(["Slides", num_slides])
        writer.writerow([])

        # Column headers
        writer.writerow(STORYBOARD_FIELDS)

        # Slide rows
        for i in range(1, num_slides + 1):
            row = [str(i)] + [""] * (len(STORYBOARD_FIELDS) - 1)
            writer.writerow(row)

    return filename


def generate_storyboard_markdown(project_name, num_slides, designer, filename=None):
    """
    Generate a storyboard scaffold as a Markdown file.

    Args:
        project_name (str): Name of the course or module
        num_slides (int): Number of slides/screens to scaffold
        designer (str): Designer name
        filename (str): Output filename (optional)

    Returns:
        str: Path to the generated markdown file
    """
    if not filename:
        safe_name = project_name.replace(' ', '_').lower()
        filename = f"{safe_name}_storyboard.md"

    today = date.today().strftime("%d %B %Y")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Storyboard — {project_name}\n\n")
        f.write(f"**Designer:** {designer}  \n")
        f.write(f"**Date:** {today}  \n")
        f.write(f"**Total slides:** {num_slides}\n\n")
        f.write("---\n\n")

        f.write("## Interaction types reference\n\n")
        for i, t in enumerate(INTERACTION_TYPES, 1):
            f.write(f"{i}. {t}\n")
        f.write("\n---\n\n")

        for i in range(1, num_slides + 1):
            f.write(f"## Slide {i:02d}\n\n")
            f.write(f"**Screen title:**  \n\n")
            f.write(f"**Narration script:**  \n\n")
            f.write(f"**On-screen text:**  \n\n")
            f.write(f"**Visual / graphic notes:**  \n\n")
            f.write(f"**Interaction type:**  \n\n")
            f.write(f"**Interaction notes:**  \n\n")
            f.write(f"**Audio cues:**  \n\n")
            f.write(f"**Next slide / branching:**  \n\n")
            f.write(f"**Status:** [ ] Draft  [ ] In review  [ ] Approved  \n\n")
            f.write(f"**Notes:**  \n\n")
            f.write("---\n\n")

    return filename


def interactive_mode():
    """Run the storyboard generator interactively."""
    print("\n" + "="*60)
    print("  STORYBOARD SCAFFOLD GENERATOR")
    print("  Learning Experience Design Tool")
    print("="*60)

    project_name = input("\n  Project / module name: ").strip() or "Untitled Course"
    designer = input("  Designer name: ").strip() or "Designer"

    while True:
        try:
            num_slides = int(input("  Number of slides/screens: ").strip())
            if num_slides < 1:
                print("  Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("  Please enter a whole number.")

    print("\n  Output format:")
    print("  1. CSV (open in Excel or Google Sheets)")
    print("  2. Markdown (open in any text editor)")
    print("  3. Both")

    choice = input("\n  Choose (1/2/3): ").strip()

    generated = []

    if choice in ('1', '3'):
        path = generate_storyboard_csv(project_name, num_slides, designer)
        generated.append(path)

    if choice in ('2', '3'):
        path = generate_storyboard_markdown(project_name, num_slides, designer)
        generated.append(path)

    if not generated:
        path = generate_storyboard_csv(project_name, num_slides, designer)
        generated.append(path)

    print(f"\n{'='*60}")
    for path in generated:
        print(f"  Generated: {path}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    interactive_mode()
