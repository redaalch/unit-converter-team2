# Unit Converter

A Python unit converter for temperature and length, built for Assignment 2: GitHub Collaboration & Automation.

Project status: Length conversion completed.

## Team and feature plan

Chosen theme: Unit Converter. Group size: 2 members.

| Member | GitHub username | Assigned feature | Feature branch |
| --- | --- | --- | --- |
| Reda Alalach | [redaalch](https://github.com/redaalch) | Temperature conversions: Celsius, Fahrenheit, Kelvin | `feature/temperature` |
| Hajar Ouaghad | [HJ-OGH](https://github.com/HJ-OGH) | Length conversions: meters, kilometers, miles | `feature/length` |

Each member will make at least two meaningful commits on their feature branch and add at least three meaningful unit tests. The complete suite will cover normal conversions, boundary values, and invalid inputs.

Each member will open a Pull Request into `main` and review the other member's Pull Request, leaving a meaningful line comment before approval. The group will complete a Request changes cycle and resolve a controlled conflict in the project status line above.

## Initial structure

```text
unit-converter-team2/
├── README.md
├── .gitignore
├── requirements.txt
├── unit_converter/       # Python conversion modules
├── tests/                # pytest test files
└── docs/                 # GitHub Pages project page
```

## Local setup

Use Python 3.12. Each member should clone the shared repository into their own local copy:

```bash
git clone https://github.com/redaalch/unit-converter-team2.git
cd unit-converter-team2
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the virtual environment with `.venv\Scripts\activate`.

The repository currently contains the initial structure. Conversion features and tests will be added through feature branches and Pull Requests. Once tests are added, run the complete suite from the repository root:

```bash
python -m pytest -q
```

## Collaboration workflow

Start each feature from the latest `main`:

```bash
git switch main
git pull origin main
git switch -c feature/temperature
```

Member B uses `feature/length` instead. Push the feature branch and open a Pull Request after making and checking the changes. Future feature changes go through Pull Requests.

## Project page

The GitHub Pages URL will be added here after the project page is published and verified.
