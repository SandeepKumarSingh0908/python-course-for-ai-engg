"""Python for AI Engineering — 8-week curriculum.

A progressive course from Python fundamentals through ML/AI engineering,
tailored for someone aiming to use Python professionally in AI/ML roles.
"""

import os
from datetime import date, timedelta

# ---------------------------------------------------------------- plan identity

PLAN_ID    = "python-ai-engineering"
PLAN_NAME  = "Python for AI Engineering"
PLAN_DATES = "16 Nov 2026 \u2192 10 Jan 2027"
START      = "2026-11-16"  # Monday of week 1

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS_DIR = os.path.join(HERE, "lessons")


# ---------------------------------------------------------------- helpers

def R(title, mins=0, url=None):
    """Reading item."""
    return {"kind": "reading", "title": title, "minutes": mins, "url": url}

def L(title, mins=30, url=None):
    """Lab / exercise item."""
    return {"kind": "lab", "title": title, "minutes": mins, "url": url}

def T(title, mins=0, url=None):
    """Task item (setup, admin)."""
    return {"kind": "task", "title": title, "minutes": mins, "url": url}

def E(title, mins=0, url=None):
    """Extra / optional item (does not count toward progress)."""
    return {"kind": "extra", "title": title, "minutes": mins, "url": url}

def G(title, mins):
    """Gate / exit-test item."""
    return {"kind": "gate", "title": title, "minutes": mins, "url": None}

def SEC(name, items, track=None):
    """A named section within a week."""
    return {"name": name, "track": track, "items": items}


# ---------------------------------------------------------------- schedule helpers

def week_of(day_num):
    return (day_num - 1) // 7 + 1

def week_dates(n):
    s = date.fromisoformat(START) + timedelta(days=7 * (n - 1))
    return s.isoformat(), (s + timedelta(days=6)).isoformat()

def lesson_url(folder, filename):
    rel = f"{folder}/{filename}"
    if os.path.isfile(os.path.join(LESSONS_DIR, rel)):
        return f"/reader.html?f={rel}"
    return None


# ---------------------------------------------------------------- gates

GATES = [
    {
        "code": "G1",
        "title": "Python Foundations check",
        "duration_min": 45,
        "rubric": [
            "Write a function that takes mixed-type inputs, casts them to the correct types, and returns a formatted string.",
            "Implement a program using if/elif/else and loops that solves a real problem (e.g. FizzBuzz variant) without hints.",
            "Explain the difference between mutable and immutable types with examples, and identify a bug caused by mutability.",
        ],
        "pass_line": "All three criteria met.",
    },
    {
        "code": "G2",
        "title": "Data Structures check",
        "duration_min": 45,
        "rubric": [
            "Solve a problem using list comprehensions, dict comprehensions, and set operations in a single script.",
            "Write a generator function that lazily processes a large sequence and explain why it's memory-efficient.",
            "Choose the correct data structure (list vs dict vs set vs tuple) for three different scenarios and justify each choice.",
        ],
        "pass_line": "All three criteria met.",
    },
    {
        "code": "G3",
        "title": "OOP & Modules check",
        "duration_min": 45,
        "rubric": [
            "Design a class hierarchy with inheritance, use super() correctly, and override at least one dunder method.",
            "Write a decorator that adds timing/logging to any function, and a context manager for resource cleanup.",
            "Create a Python package with __init__.py, import it, and explain the module search path.",
        ],
        "pass_line": "All three criteria met.",
    },
    {
        "code": "G4",
        "title": "Advanced Python check",
        "duration_min": 45,
        "rubric": [
            "Read a CSV and a JSON file, handle encoding errors and missing keys gracefully with proper exception handling.",
            "Write type-annotated code using dataclasses and demonstrate use of map/filter/reduce on a real dataset.",
            "Debug a provided broken script using logging, pdb, or traceback analysis and explain the root cause.",
        ],
        "pass_line": "All three criteria met.",
    },
    {
        "code": "G5",
        "title": "NumPy & Pandas check",
        "duration_min": 45,
        "rubric": [
            "Perform vectorized operations on a NumPy array: reshape, broadcast, and compute statistics without Python loops.",
            "Load a messy CSV into Pandas, clean it (handle NaN, dtypes, duplicates), and produce a grouped summary.",
            "Use Pandas merge/join to combine two datasets and create a pivot table from the result.",
        ],
        "pass_line": "All three criteria met.",
    },
    {
        "code": "G6",
        "title": "Visualization & APIs check",
        "duration_min": 45,
        "rubric": [
            "Create a multi-panel matplotlib figure with labeled axes, legend, and at least two different plot types.",
            "Write a Python script that calls a REST API, handles errors and pagination, and saves results to a file.",
            "Write at least 3 pytest tests (including one parametrized) for a function and achieve full branch coverage.",
        ],
        "pass_line": "All three criteria met.",
    },
    {
        "code": "G7",
        "title": "ML Foundations check",
        "duration_min": 60,
        "rubric": [
            "Build a complete sklearn pipeline: load data, split, preprocess, train a classifier, and evaluate with cross-validation.",
            "Explain overfitting vs underfitting, demonstrate it with learning curves, and apply regularization to fix it.",
            "Perform basic feature engineering on a raw dataset and compare model performance before and after.",
        ],
        "pass_line": "All three criteria met.",
    },
    {
        "code": "G8",
        "title": "AI Engineering capstone",
        "duration_min": 90,
        "rubric": [
            "Call an LLM API (OpenAI or Anthropic) from Python with proper error handling, retries, and structured output parsing.",
            "Build a working RAG pipeline: embed documents, store in a vector DB, retrieve relevant chunks, and generate an answer.",
            "Serve a model or AI feature behind a FastAPI endpoint with input validation and proper HTTP status codes.",
            "Write a short design doc (in code comments or markdown) explaining your architecture choices and trade-offs.",
        ],
        "pass_line": "All four criteria met.",
    },
]

GATE_DAY = {
    "G1": 7, "G2": 14, "G3": 21, "G4": 28,
    "G5": 35, "G6": 42, "G7": 49, "G8": 56,
}


# ---------------------------------------------------------------- weeks

def _build_weeks():
    weeks = []

    # -- Week 0: Setup ------------------------------------------------
    weeks.append({
        "num": 0,
        "start": "2026-11-14", "end": "2026-11-15",
        "title": "Setup",
        "gate": None, "gate_note": "No gate \u2014 just get your environment ready.",
        "planned_a": 1.5, "planned_b": 1.5, "budget_hours": 2.5,
        "resources": [
            ("Python.org Downloads", "https://www.python.org/downloads/"),
            ("VS Code Python Extension", "https://marketplace.visualstudio.com/items?itemName=ms-python.python"),
        ],
        "sections": [SEC("Environment Setup", [
            R("Setup guide: Why every tool matters (read this first)", 45,
              lesson_url("w00", "setup.md")),
            T("Install Python 3.12+ (python.org or pyenv)", 20),
            T("Install VS Code + Python extension (or your preferred IDE)", 15),
            T("Set up a virtual environment: python -m venv .venv", 10),
            T("Install ipython and jupyter for interactive work", 10),
            T("Create a git repo and initial folder structure", 10),
            T("Skim the Plan tab and choose your daily study slot", 10),
        ])],
    })

    # -- Week 1: Python Foundations ------------------------------------
    s1, e1 = week_dates(1)
    weeks.append({
        "num": 1,
        "start": s1, "end": e1,
        "title": "Python Foundations",
        "gate": "G1", "gate_note": None,
        "planned_a": 7.0, "planned_b": 7.0, "budget_hours": 8.0,
        "resources": [
            ("Python Tutorial (official)", "https://docs.python.org/3/tutorial/"),
            ("Python Cheat Sheet", "https://www.pythoncheatsheet.org/"),
        ],
        "sections": [
            SEC("Day 1 \u00b7 Variables, Types & Type Casting", [
                R("Day 1 - read: Variables, data types, and type casting", 35,
                  lesson_url("w01", "day-001.md")),
                L("Day 1 - lab: Build a unit converter (temp, weight, distance)", 25),
            ]),
            SEC("Day 2 \u00b7 Operators & Expressions", [
                R("Day 2 - read: Arithmetic, comparison, logical, and bitwise operators", 35,
                  lesson_url("w01", "day-002.md")),
                L("Day 2 - lab: Build a calculator with operator precedence", 25),
            ]),
            SEC("Day 3 \u00b7 Control Flow", [
                R("Day 3 - read: if/elif/else, match-case, truthiness", 35,
                  lesson_url("w01", "day-003.md")),
                L("Day 3 - lab: Build a grade classifier and a simple menu system", 25),
            ]),
            SEC("Day 4 \u00b7 Loops & Iteration", [
                R("Day 4 - read: for loops, while loops, break/continue, enumerate, zip", 35,
                  lesson_url("w01", "day-004.md")),
                L("Day 4 - lab: Solve 5 loop challenges (FizzBuzz, primes, patterns)", 25),
            ]),
            SEC("Day 5 \u00b7 Functions", [
                R("Day 5 - read: def, args, *args, **kwargs, return, scope, docstrings", 35,
                  lesson_url("w01", "day-005.md")),
                L("Day 5 - lab: Build a text statistics toolkit (word count, frequency, etc.)", 25),
            ]),
            SEC("Day 6 \u00b7 Strings & String Methods", [
                R("Day 6 - read: f-strings, slicing, methods, regex intro, encoding", 35,
                  lesson_url("w01", "day-006.md")),
                L("Day 6 - lab: Build a text processor (clean, parse, and format data)", 25),
            ]),
            SEC("Day 7 \u00b7 Gate Day", [
                R("Day 7 - read: Review Python foundations", 20,
                  lesson_url("w01", "day-007.md")),
                G("G1 - Python Foundations check", 45),
            ]),
        ],
    })

    # -- Week 2: Data Structures & Comprehensions ----------------------
    s2, e2 = week_dates(2)
    weeks.append({
        "num": 2,
        "start": s2, "end": e2,
        "title": "Data Structures & Comprehensions",
        "gate": "G2", "gate_note": None,
        "planned_a": 7.0, "planned_b": 7.0, "budget_hours": 8.0,
        "resources": [
            ("Python Data Structures (official)", "https://docs.python.org/3/tutorial/datastructures.html"),
        ],
        "sections": [
            SEC("Day 8 \u00b7 Lists & List Comprehensions", [
                R("Day 8 - read: Lists, slicing, methods, list comprehensions", 35,
                  lesson_url("w02", "day-008.md")),
                L("Day 8 - lab: Data filtering pipeline using list comprehensions", 25),
            ]),
            SEC("Day 9 \u00b7 Tuples & Named Tuples", [
                R("Day 9 - read: Tuples, unpacking, named tuples, immutability", 35,
                  lesson_url("w02", "day-009.md")),
                L("Day 9 - lab: Build a record system with named tuples", 25),
            ]),
            SEC("Day 10 \u00b7 Dictionaries", [
                R("Day 10 - read: Dicts, dict comprehensions, defaultdict, Counter", 35,
                  lesson_url("w02", "day-010.md")),
                L("Day 10 - lab: Word frequency analyzer and inventory tracker", 25),
            ]),
            SEC("Day 11 \u00b7 Sets & Frozen Sets", [
                R("Day 11 - read: Sets, set operations, frozenset, practical uses", 35,
                  lesson_url("w02", "day-011.md")),
                L("Day 11 - lab: Deduplication engine and set-based data analysis", 25),
            ]),
            SEC("Day 12 \u00b7 Iterators & Generators", [
                R("Day 12 - read: Iterator protocol, generators, yield, generator expressions", 35,
                  lesson_url("w02", "day-012.md")),
                L("Day 12 - lab: Build a lazy data pipeline for processing large files", 25),
            ]),
            SEC("Day 13 \u00b7 Collections Module & Data Structure Choices", [
                R("Day 13 - read: deque, OrderedDict, ChainMap, choosing the right structure", 35,
                  lesson_url("w02", "day-013.md")),
                L("Day 13 - lab: Implement an LRU cache and a task queue", 25),
            ]),
            SEC("Day 14 \u00b7 Gate Day", [
                R("Day 14 - read: Review data structures", 20,
                  lesson_url("w02", "day-014.md")),
                G("G2 - Data Structures check", 45),
            ]),
        ],
    })

    # -- Week 3: OOP, Modules & Packages -------------------------------
    s3, e3 = week_dates(3)
    weeks.append({
        "num": 3,
        "start": s3, "end": e3,
        "title": "OOP, Modules & Packages",
        "gate": "G3", "gate_note": None,
        "planned_a": 7.0, "planned_b": 7.0, "budget_hours": 8.0,
        "resources": [
            ("Python OOP Tutorial (official)", "https://docs.python.org/3/tutorial/classes.html"),
            ("Python Packaging Guide", "https://packaging.python.org/en/latest/"),
        ],
        "sections": [
            SEC("Day 15 \u00b7 Classes & Objects", [
                R("Day 15 - read: Classes, __init__, self, attributes, methods", 35,
                  lesson_url("w03", "day-015.md")),
                L("Day 15 - lab: Build a BankAccount and Deck-of-Cards class", 25),
            ]),
            SEC("Day 16 \u00b7 Inheritance & Polymorphism", [
                R("Day 16 - read: Inheritance, super(), MRO, polymorphism, ABCs", 35,
                  lesson_url("w03", "day-016.md")),
                L("Day 16 - lab: Build a shape hierarchy with area/perimeter calculations", 25),
            ]),
            SEC("Day 17 \u00b7 Dunder Methods & Protocols", [
                R("Day 17 - read: __repr__, __str__, __eq__, __lt__, __len__, __getitem__", 35,
                  lesson_url("w03", "day-017.md")),
                L("Day 17 - lab: Build a Vector class with arithmetic operator support", 25),
            ]),
            SEC("Day 18 \u00b7 Decorators", [
                R("Day 18 - read: Closures, function decorators, @property, @classmethod, @staticmethod", 35,
                  lesson_url("w03", "day-018.md")),
                L("Day 18 - lab: Write timing, retry, and validation decorators", 25),
            ]),
            SEC("Day 19 \u00b7 Context Managers & Protocols", [
                R("Day 19 - read: with statement, __enter__/__exit__, contextlib, protocols", 35,
                  lesson_url("w03", "day-019.md")),
                L("Day 19 - lab: Build context managers for DB connections and temp files", 25),
            ]),
            SEC("Day 20 \u00b7 Modules, Packages & pip", [
                R("Day 20 - read: import system, __init__.py, pip, venv, requirements.txt", 35,
                  lesson_url("w03", "day-020.md")),
                L("Day 20 - lab: Structure a multi-module project and publish to TestPyPI", 25),
            ]),
            SEC("Day 21 \u00b7 Gate Day", [
                R("Day 21 - read: Review OOP and modules", 20,
                  lesson_url("w03", "day-021.md")),
                G("G3 - OOP & Modules check", 45),
            ]),
        ],
    })

    # -- Week 4: Advanced Python (File I/O, Errors, Functional) --------
    s4, e4 = week_dates(4)
    weeks.append({
        "num": 4,
        "start": s4, "end": e4,
        "title": "Advanced Python",
        "gate": "G4", "gate_note": None,
        "planned_a": 7.0, "planned_b": 7.0, "budget_hours": 8.0,
        "resources": [
            ("Python Functional Programming HOWTO", "https://docs.python.org/3/howto/functional.html"),
            ("Python Logging HOWTO", "https://docs.python.org/3/howto/logging.html"),
        ],
        "sections": [
            SEC("Day 22 \u00b7 File I/O: Text, CSV & JSON", [
                R("Day 22 - read: open(), pathlib, csv module, json module, encoding", 35,
                  lesson_url("w04", "day-022.md")),
                L("Day 22 - lab: Build a config file reader that handles CSV, JSON, and TOML", 25),
            ]),
            SEC("Day 23 \u00b7 Exception Handling", [
                R("Day 23 - read: try/except/else/finally, custom exceptions, exception chaining", 35,
                  lesson_url("w04", "day-023.md")),
                L("Day 23 - lab: Add robust error handling to a file processor", 25),
            ]),
            SEC("Day 24 \u00b7 Regular Expressions", [
                R("Day 24 - read: re module, patterns, groups, lookahead, common recipes", 35,
                  lesson_url("w04", "day-024.md")),
                L("Day 24 - lab: Build a log parser and data extractor with regex", 25),
            ]),
            SEC("Day 25 \u00b7 Functional Programming", [
                R("Day 25 - read: lambda, map, filter, reduce, functools, itertools", 35,
                  lesson_url("w04", "day-025.md")),
                L("Day 25 - lab: Process a dataset using only functional programming patterns", 25),
            ]),
            SEC("Day 26 \u00b7 Type Hints & Dataclasses", [
                R("Day 26 - read: Type annotations, typing module, dataclasses, Pydantic intro", 35,
                  lesson_url("w04", "day-026.md")),
                L("Day 26 - lab: Refactor untyped code with type hints and dataclasses", 25),
            ]),
            SEC("Day 27 \u00b7 Logging, Debugging & Profiling", [
                R("Day 27 - read: logging module, pdb, cProfile, traceback, print debugging", 35,
                  lesson_url("w04", "day-027.md")),
                L("Day 27 - lab: Debug 3 broken scripts and add structured logging", 25),
            ]),
            SEC("Day 28 \u00b7 Gate Day", [
                R("Day 28 - read: Review advanced Python concepts", 20,
                  lesson_url("w04", "day-028.md")),
                G("G4 - Advanced Python check", 45),
            ]),
        ],
    })

    # -- Week 5: NumPy & Pandas ----------------------------------------
    s5, e5 = week_dates(5)
    weeks.append({
        "num": 5,
        "start": s5, "end": e5,
        "title": "NumPy & Pandas",
        "gate": "G5", "gate_note": None,
        "planned_a": 7.0, "planned_b": 7.0, "budget_hours": 8.0,
        "resources": [
            ("NumPy User Guide", "https://numpy.org/doc/stable/user/index.html"),
            ("Pandas Getting Started", "https://pandas.pydata.org/docs/getting_started/index.html"),
        ],
        "sections": [
            SEC("Day 29 \u00b7 NumPy Basics", [
                R("Day 29 - read: Arrays, dtypes, shapes, creation functions", 35,
                  lesson_url("w05", "day-029.md")),
                L("Day 29 - lab: Create and manipulate arrays for image-like data", 25),
            ]),
            SEC("Day 30 \u00b7 NumPy Indexing & Broadcasting", [
                R("Day 30 - read: Fancy indexing, boolean masks, broadcasting rules", 35,
                  lesson_url("w05", "day-030.md")),
                L("Day 30 - lab: Vectorized data cleaning without Python loops", 25),
            ]),
            SEC("Day 31 \u00b7 NumPy Linear Algebra & Math", [
                R("Day 31 - read: np.linalg, matrix operations, random, statistics", 35,
                  lesson_url("w05", "day-031.md")),
                L("Day 31 - lab: Implement linear regression from scratch with NumPy", 25),
            ]),
            SEC("Day 32 \u00b7 Pandas Series & DataFrames", [
                R("Day 32 - read: Series, DataFrame, indexing, loc/iloc, dtypes", 35,
                  lesson_url("w05", "day-032.md")),
                L("Day 32 - lab: Load and explore a real-world dataset (Titanic or similar)", 25),
            ]),
            SEC("Day 33 \u00b7 Pandas Data Cleaning", [
                R("Day 33 - read: NaN handling, dtypes conversion, duplicates, string methods", 35,
                  lesson_url("w05", "day-033.md")),
                L("Day 33 - lab: Clean a messy dataset end-to-end", 25),
            ]),
            SEC("Day 34 \u00b7 Pandas GroupBy, Merge & Pivot", [
                R("Day 34 - read: groupby, agg, merge, join, pivot_table, melt", 35,
                  lesson_url("w05", "day-034.md")),
                L("Day 34 - lab: Analyze sales data with groupby and produce a summary report", 25),
            ]),
            SEC("Day 35 \u00b7 Gate Day", [
                R("Day 35 - read: Review NumPy and Pandas", 20,
                  lesson_url("w05", "day-035.md")),
                G("G5 - NumPy & Pandas check", 45),
            ]),
        ],
    })

    # -- Week 6: Visualization, APIs & Testing -------------------------
    s6, e6 = week_dates(6)
    weeks.append({
        "num": 6,
        "start": s6, "end": e6,
        "title": "Visualization, APIs & Testing",
        "gate": "G6", "gate_note": None,
        "planned_a": 7.0, "planned_b": 7.0, "budget_hours": 8.0,
        "resources": [
            ("Matplotlib Tutorials", "https://matplotlib.org/stable/tutorials/index.html"),
            ("requests Library", "https://docs.python-requests.org/en/latest/"),
            ("pytest Documentation", "https://docs.pytest.org/en/stable/"),
        ],
        "sections": [
            SEC("Day 36 \u00b7 Matplotlib Fundamentals", [
                R("Day 36 - read: Figure, Axes, plot types, styling, subplots", 35,
                  lesson_url("w06", "day-036.md")),
                L("Day 36 - lab: Create a 4-panel dashboard from a dataset", 25),
            ]),
            SEC("Day 37 \u00b7 Seaborn & Advanced Visualization", [
                R("Day 37 - read: Seaborn API, statistical plots, themes, color palettes", 35,
                  lesson_url("w06", "day-037.md")),
                L("Day 37 - lab: Create publication-quality plots for a data analysis", 25),
            ]),
            SEC("Day 38 \u00b7 Working with REST APIs", [
                R("Day 38 - read: HTTP basics, requests library, authentication, pagination", 35,
                  lesson_url("w06", "day-038.md")),
                L("Day 38 - lab: Build a GitHub API client that fetches repo statistics", 25),
            ]),
            SEC("Day 39 \u00b7 Databases with Python", [
                R("Day 39 - read: sqlite3, SQLAlchemy basics, connection patterns", 35,
                  lesson_url("w06", "day-039.md")),
                L("Day 39 - lab: Build a CRUD app with SQLite", 25),
            ]),
            SEC("Day 40 \u00b7 Concurrency & Async", [
                R("Day 40 - read: threading, multiprocessing, asyncio, GIL", 35,
                  lesson_url("w06", "day-040.md")),
                L("Day 40 - lab: Speed up an API scraper with async/threading", 25),
            ]),
            SEC("Day 41 \u00b7 Testing with pytest", [
                R("Day 41 - read: pytest basics, fixtures, parametrize, mocking, coverage", 35,
                  lesson_url("w06", "day-041.md")),
                L("Day 41 - lab: Write a test suite for a previous lab project", 25),
            ]),
            SEC("Day 42 \u00b7 Gate Day", [
                R("Day 42 - read: Review visualization, APIs, and testing", 20,
                  lesson_url("w06", "day-042.md")),
                G("G6 - Visualization & APIs check", 45),
            ]),
        ],
    })

    # -- Week 7: ML Foundations -----------------------------------------
    s7, e7 = week_dates(7)
    weeks.append({
        "num": 7,
        "start": s7, "end": e7,
        "title": "ML Foundations with Scikit-learn",
        "gate": "G7", "gate_note": None,
        "planned_a": 7.0, "planned_b": 7.0, "budget_hours": 8.0,
        "resources": [
            ("Scikit-learn User Guide", "https://scikit-learn.org/stable/user_guide.html"),
            ("Kaggle Learn - Intro to ML", "https://www.kaggle.com/learn/intro-to-machine-learning"),
        ],
        "sections": [
            SEC("Day 43 \u00b7 Intro to ML & Scikit-learn", [
                R("Day 43 - read: ML concepts, sklearn API pattern, estimators, fit/predict", 35,
                  lesson_url("w07", "day-043.md")),
                L("Day 43 - lab: Train your first classifier on the Iris dataset", 25),
            ]),
            SEC("Day 44 \u00b7 Data Preprocessing & Feature Engineering", [
                R("Day 44 - read: Scaling, encoding, imputation, pipelines, ColumnTransformer", 35,
                  lesson_url("w07", "day-044.md")),
                L("Day 44 - lab: Build a preprocessing pipeline for a messy dataset", 25),
            ]),
            SEC("Day 45 \u00b7 Supervised Learning: Classification", [
                R("Day 45 - read: Logistic regression, decision trees, random forest, SVM", 35,
                  lesson_url("w07", "day-045.md")),
                L("Day 45 - lab: Compare classifiers on a binary classification problem", 25),
            ]),
            SEC("Day 46 \u00b7 Supervised Learning: Regression", [
                R("Day 46 - read: Linear regression, Ridge, Lasso, evaluation metrics", 35,
                  lesson_url("w07", "day-046.md")),
                L("Day 46 - lab: Predict house prices with regularized regression", 25),
            ]),
            SEC("Day 47 \u00b7 Model Evaluation & Validation", [
                R("Day 47 - read: Cross-validation, learning curves, hyperparameter tuning, GridSearchCV", 35,
                  lesson_url("w07", "day-047.md")),
                L("Day 47 - lab: Tune a model with GridSearchCV and plot learning curves", 25),
            ]),
            SEC("Day 48 \u00b7 Unsupervised Learning", [
                R("Day 48 - read: K-means, DBSCAN, PCA, dimensionality reduction", 35,
                  lesson_url("w07", "day-048.md")),
                L("Day 48 - lab: Cluster customer data and visualize with PCA", 25),
            ]),
            SEC("Day 49 \u00b7 Gate Day", [
                R("Day 49 - read: Review ML foundations", 20,
                  lesson_url("w07", "day-049.md")),
                G("G7 - ML Foundations check", 60),
            ]),
        ],
    })

    # -- Week 8: AI Engineering in Practice ----------------------------
    s8, e8 = week_dates(8)
    weeks.append({
        "num": 8,
        "start": s8, "end": e8,
        "title": "AI Engineering in Practice",
        "gate": "G8", "gate_note": None,
        "planned_a": 8.0, "planned_b": 8.0, "budget_hours": 9.5,
        "resources": [
            ("Anthropic API Docs", "https://docs.anthropic.com/"),
            ("OpenAI API Docs", "https://platform.openai.com/docs/"),
            ("FastAPI Docs", "https://fastapi.tiangolo.com/"),
            ("ChromaDB Docs", "https://docs.trychroma.com/"),
        ],
        "sections": [
            SEC("Day 50 \u00b7 Working with LLM APIs", [
                R("Day 50 - read: OpenAI & Anthropic APIs, client libraries, structured output", 35,
                  lesson_url("w08", "day-050.md")),
                L("Day 50 - lab: Build a conversational Q&A script with streaming", 25),
            ]),
            SEC("Day 51 \u00b7 Prompt Engineering with Python", [
                R("Day 51 - read: Prompt templates, few-shot, chain-of-thought, output parsing", 35,
                  lesson_url("w08", "day-051.md")),
                L("Day 51 - lab: Build a structured data extractor from unstructured text", 25),
            ]),
            SEC("Day 52 \u00b7 Embeddings & Vector Databases", [
                R("Day 52 - read: Text embeddings, similarity search, ChromaDB, FAISS", 35,
                  lesson_url("w08", "day-052.md")),
                L("Day 52 - lab: Build a semantic search engine over a document collection", 25),
            ]),
            SEC("Day 53 \u00b7 Building a RAG Pipeline", [
                R("Day 53 - read: RAG architecture, chunking strategies, retrieval + generation", 35,
                  lesson_url("w08", "day-053.md")),
                L("Day 53 - lab: Build a RAG chatbot that answers questions from your docs", 35),
            ]),
            SEC("Day 54 \u00b7 Serving AI with FastAPI", [
                R("Day 54 - read: FastAPI basics, Pydantic models, async endpoints, deployment", 35,
                  lesson_url("w08", "day-054.md")),
                L("Day 54 - lab: Wrap your RAG pipeline in a FastAPI service", 30),
            ]),
            SEC("Day 55 \u00b7 MLOps & Production Patterns", [
                R("Day 55 - read: Model versioning, experiment tracking, monitoring, CI/CD for ML", 35,
                  lesson_url("w08", "day-055.md")),
                L("Day 55 - lab: Add logging, metrics, and error handling to your API", 30),
            ]),
            SEC("Day 56 \u00b7 Capstone Gate Day", [
                R("Day 56 - read: Review AI engineering concepts and prepare your capstone", 25,
                  lesson_url("w08", "day-056.md")),
                G("G8 - AI Engineering capstone", 90),
            ]),
        ],
    })

    return weeks


# ---------------------------------------------------------------- reference (Plan tab)

REFERENCE = {
    "budget": [
        ("Setup week", "1.5 h"),
        ("Week 1: Python Foundations (7 days)", "7 h"),
        ("Week 2: Data Structures (7 days)", "7 h"),
        ("Week 3: OOP & Modules (7 days)", "7 h"),
        ("Week 4: Advanced Python (7 days)", "7 h"),
        ("Week 5: NumPy & Pandas (7 days)", "7 h"),
        ("Week 6: Visualization, APIs & Testing (7 days)", "7 h"),
        ("Week 7: ML Foundations (7 days)", "7 h"),
        ("Week 8: AI Engineering (7 days)", "8 h"),
        ("Gates (G1\u2013G8)", "~6.5 h"),
        ("Total planned", "~65 h"),
    ],
    "book": [
        ["Week", "Focus Area", "Key Libraries"],
        ["1", "Python Foundations", "built-ins"],
        ["2", "Data Structures", "collections"],
        ["3", "OOP & Modules", "abc, contextlib"],
        ["4", "Advanced Python", "pathlib, re, typing, dataclasses"],
        ["5", "NumPy & Pandas", "numpy, pandas"],
        ["6", "Viz, APIs & Testing", "matplotlib, seaborn, requests, pytest"],
        ["7", "ML Foundations", "scikit-learn"],
        ["8", "AI Engineering", "openai, anthropic, fastapi, chromadb"],
    ],
    "tracks": [],
    "tracks_note": "",
    "rhythm": [
        "One lesson per day: ~35 min reading + ~25 min lab = ~1 hour.",
        "Gate weeks add 45\u201390 min for the exit test on day 7.",
        "If you miss a day, do it the next day. Don't double up.",
        "Weekend days are included \u2014 adjust pace if you prefer weekdays only.",
    ],
    "gate_rules": [
        "Closed notes, timer on. Official docs allowed.",
        "Grade yourself against the rubric, or use the AI judge.",
        "Fail: one retry next week. Second fail: write a gap note and move on.",
    ],
    "cuts": [
        "Optional extras (E items) first.",
        "Reduce lab time before cutting readings.",
        "Week 8 labs can be simplified to API-call-only versions.",
    ],
    "never_cut": [
        "Gates G1\u2013G5 (core Python & data skills)",
        "NumPy/Pandas labs (foundation for everything after)",
        "Day 50\u201353 (LLM APIs + RAG are the capstone skills)",
    ],
    "posting": [
        "Optional: share your weekly progress or lab results.",
    ],
    "framing_fields": [],
    "drill_note": "",
    "drills": [],
    "drill_trick": "",
    "limits": [
        "Lessons are AI-generated \u2014 verify code examples by running them.",
        "Week 8 requires API keys (OpenAI/Anthropic) \u2014 free tiers available.",
        "ML content is introductory; for depth, continue with a dedicated ML course.",
    ],
}

MODEL_SELECTION_SEED = [
    {
        "data_type": "Text classification",
        "baseline": "Rule-based / regex",
        "model_family": "sklearn (LogisticRegression / SVM)",
        "loss": "Training time + labeled data needed",
        "metric": "F1 score",
        "failure_mode": "Insufficient training data",
        "when_not": "When rules cover >95% of cases",
    },
    {
        "data_type": "Free-text Q&A",
        "baseline": "Keyword search",
        "model_family": "LLM API + RAG",
        "loss": "API cost per query",
        "metric": "Answer relevance (human eval)",
        "failure_mode": "Hallucination on out-of-scope questions",
        "when_not": "When answers are in a structured DB",
    },
]


# ---------------------------------------------------------------- build

def build():
    """Return the full seed payload. Called by server.py."""
    return {
        "weeks": _build_weeks(),
        "gates": [dict(g, week=week_of(GATE_DAY[g["code"]])) for g in GATES],
        "reference": REFERENCE,
        "model_selection": MODEL_SELECTION_SEED,
    }
