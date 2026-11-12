# Python for AI Engineering

A self-paced, 8-week course to learn Python from scratch with a focus on AI/ML engineering. Built on a local learning tracker UI that lets you follow your progress, check off lessons, and test yourself with gate assessments.

## What is this?

This is a structured Python curriculum designed for someone who wants to use Python professionally in AI engineering roles. It covers everything from `print("hello")` to building RAG pipelines with LLM APIs.

The course runs inside a local web app (the **Learning Tracker**) that shows your weekly plan, tracks completed items, logs study hours, and hosts readable lesson content — all offline, no account needed.

## Course overview

| Week | Topic | What you learn |
|------|-------|---------------|
| 0 | Setup | Python, VS Code, venv, pip, git — and *why* each matters |
| 1 | Python Foundations | Variables, types, control flow, functions, strings |
| 2 | Data Structures | Lists, dicts, sets, tuples, generators, comprehensions |
| 3 | OOP & Modules | Classes, inheritance, decorators, context managers, packages |
| 4 | Advanced Python | File I/O, exceptions, regex, type hints, dataclasses, logging |
| 5 | NumPy & Pandas | Arrays, DataFrames, data cleaning, groupby, merge |
| 6 | Viz, APIs & Testing | Matplotlib, Seaborn, REST APIs, SQLite, concurrency, pytest |
| 7 | ML Foundations | Scikit-learn: classification, regression, clustering, evaluation |
| 8 | AI Engineering | LLM APIs, prompt engineering, embeddings, RAG, FastAPI, MLOps |

**56 lessons** with real, runnable code examples. **8 gate assessments** to test your understanding. **~65 hours** of total content at ~1 hour/day.

## Quick start

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd python-learning

# 2. Make sure Python 3.12+ is installed
python3 --version

# 3. Start the tracker
./run.sh

# Opens http://127.0.0.1:8765 in your browser
```

If you need a fresh start (reset all progress):

```bash
rm -f tracker.db
./run.sh
```

## Project structure

```
python-learning/
├── seed.py              # Course curriculum definition (weeks, items, gates)
├── lessons/             # Markdown lesson files (56 lessons)
│   ├── w00/             # Week 0: Setup guide
│   ├── w01/             # Week 1: Python Foundations (day-001 to day-007)
│   ├── w02/             # Week 2: Data Structures (day-008 to day-014)
│   ├── w03/             # Week 3: OOP & Modules (day-015 to day-021)
│   ├── w04/             # Week 4: Advanced Python (day-022 to day-028)
│   ├── w05/             # Week 5: NumPy & Pandas (day-029 to day-035)
│   ├── w06/             # Week 6: Viz, APIs & Testing (day-036 to day-042)
│   ├── w07/             # Week 7: ML Foundations (day-043 to day-049)
│   └── w08/             # Week 8: AI Engineering (day-050 to day-056)
├── server.py -> ...     # Symlink to learning-ui scaffold (web server)
├── static/ -> ...       # Symlink to learning-ui scaffold (frontend assets)
├── run.sh -> ...        # Symlink to learning-ui scaffold (start script)
├── tracker.db           # SQLite database (auto-created, stores your progress)
└── README.md            # This file
```

## Features

- **Built-in lesson reader** — click any lesson in the tracker to read it in a clean, distraction-free reader with syntax-highlighted code blocks
- **Progress tracking** — check off items as you complete them; see completion percentages per week and overall
- **Gate assessments** — self-tests at the end of each week with rubrics; optionally graded by a local AI judge (Ollama)
- **Study hour logging** — log how much time you spend each day; track against the planned budget
- **Streak counter** — see your consecutive-days streak to stay motivated
- **Decision log** — record tool/approach decisions as you learn (Decisions tab)
- **Fully offline** — everything runs locally, no internet required (except for Week 8 API lessons)

## How each day works

Each day has two items:

1. **Reading (~35 min)** — a lesson covering one concept with explanations, code examples, and tables
2. **Lab (~25 min)** — a hands-on exercise where you write code to practice what you just learned

Gate days (day 7, 14, 21, ...) replace the lab with an assessment.

## Maintaining the course

### Reset progress

```bash
rm -f tracker.db
./run.sh
```

### Edit curriculum

All curriculum data lives in `seed.py`. You can:

- Change dates by updating `START` and `PLAN_DATES`
- Reorder or rename weeks in `_build_weeks()`
- Add/remove lessons, labs, or gates
- Modify gate rubrics in the `GATES` list

After editing, delete `tracker.db` and restart — or just restart and the tracker will auto-merge changes while preserving your existing progress.

### Add or edit lessons

Lessons are markdown files in `lessons/wNN/`. To add a new lesson:

1. Create a `.md` file in the appropriate week folder
2. Link it in `seed.py` using `lesson_url("wNN", "filename.md")`
3. Restart the server

The reader supports: headings, paragraphs, lists, task lists, fenced code blocks, tables, blockquotes, bold/italic, and links.

### The scaffold (learning-ui)

The web UI comes from a separate scaffold project (`../learning-ui/`). The files `server.py`, `static/`, and `run.sh` are symlinked from there. **Do not modify the scaffold** — it's designed to be reusable across different courses.

## Requirements

- Python 3.12+
- A modern web browser
- No external Python packages needed for the tracker itself

For course labs, you'll install libraries progressively:
- Week 5: `numpy`, `pandas`
- Week 6: `matplotlib`, `seaborn`, `requests`, `pytest`
- Week 7: `scikit-learn`
- Week 8: `openai`, `anthropic`, `fastapi`, `uvicorn`, `chromadb`

## License

Personal learning project.
