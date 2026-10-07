#!/usr/bin/env python3
"""
Needs Analysis Generator
========================
Takes a brief project description and structures it into a needs analysis document.

Usage:
    python needs_analysis.py

Or import and call generate_needs_analysis() with a dictionary of inputs.
"""

from datetime import date


def prompt_input(label, help_text=""):
    """Prompt for a single input with optional help text."""
    if help_text:
        print(f"\n  {help_text}")
    value = input(f"  {label}: ").strip()
    return value


def generate_needs_analysis(data):
    """
    Generate a structured needs analysis document from input data.

    Args:
        data (dict): Project information with the following keys:
            - project_name
            - client_or_org
            - designer
            - audience_description
            - current_situation (what is happening now)
            - desired_situation (what should happen after training)
            - gap_description (what is missing)
            - constraints (time, budget, tech, language)
            - recommended_approach

    Returns:
        str: Formatted needs analysis as a markdown string.
    """
    today = date.today().strftime("%d %B %Y")

    doc = f"""# Needs Analysis — {data.get('project_name', 'Untitled Project')}

**Client / Organisation:** {data.get('client_or_org', '—')}
**Designer:** {data.get('designer', '—')}
**Date:** {today}

---

## 1. Project overview

{data.get('project_name', 'This project')} is a learning design engagement for {data.get('client_or_org', 'the client organisation')}.

---

## 2. Audience

{data.get('audience_description', 'Not specified.')}

---

## 3. Current situation

{data.get('current_situation', 'Not specified.')}

---

## 4. Desired situation

{data.get('desired_situation', 'Not specified.')}

---

## 5. Performance gap

{data.get('gap_description', 'Not specified.')}

---

## 6. Constraints

{data.get('constraints', 'None noted.')}

---

## 7. Recommended approach

{data.get('recommended_approach', 'To be determined following further analysis.')}

---

## 8. Proposed next steps

1. Validate this needs analysis with the client / key stakeholders
2. Conduct learner interviews or surveys if audience information is limited
3. Define measurable learning objectives aligned to the performance gap
4. Propose a learning solution and timeline for sign-off

---

*This document is a working draft for stakeholder review. It should be updated as further information is gathered.*
"""
    return doc


def interactive_mode():
    """Run the needs analysis generator interactively."""
    print("\n" + "="*60)
    print("  NEEDS ANALYSIS GENERATOR")
    print("  Learning Experience Design Tool")
    print("="*60)
    print("\nAnswer the prompts below. Press Enter to skip any field.")

    data = {}
    data['project_name'] = prompt_input(
        "Project name",
        "What is this project called? (e.g. 'Sales Onboarding Programme')"
    )
    data['client_or_org'] = prompt_input(
        "Client or organisation",
        "Who is the client or organisation commissioning this work?"
    )
    data['designer'] = prompt_input(
        "Designer name",
        "Your name"
    )
    data['audience_description'] = prompt_input(
        "Describe the target audience",
        "Who are the learners? Role, experience level, context, number of people."
    )
    data['current_situation'] = prompt_input(
        "Current situation",
        "What is happening now? What are people doing or not doing?"
    )
    data['desired_situation'] = prompt_input(
        "Desired situation",
        "What should be happening after the learning? What will people do differently?"
    )
    data['gap_description'] = prompt_input(
        "Performance gap",
        "What is the gap between current and desired? Is this a knowledge, skill or behaviour gap?"
    )
    data['constraints'] = prompt_input(
        "Constraints",
        "Time, budget, technology, language, accessibility requirements?"
    )
    data['recommended_approach'] = prompt_input(
        "Recommended approach",
        "Based on the above, what type of learning solution do you recommend? (e.g. self-paced eLearning, blended, workshop)"
    )

    doc = generate_needs_analysis(data)

    safe_name = data.get('project_name', 'needs_analysis').replace(' ', '_').lower()
    filename = f"{safe_name}_needs_analysis.md"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(doc)

    print(f"\n{'='*60}")
    print(f"  Needs analysis saved to: {filename}")
    print(f"{'='*60}\n")
    print(doc)


if __name__ == "__main__":
    interactive_mode()
