# Week 0 - Environment Setup: Why Every Tool Matters

**Module:** Setup | **Time:** ~45 min

> Before you write a single line of Python, you need a workspace that won't fight you.
> Every tool below exists for a reason — this guide explains *what* each one does,
> *why* you need it, and *how* to set it up. Skipping this step is the #1 reason
> beginners get stuck later.

## By the end of this guide you will

- Have Python installed and running on your machine
- Understand what a virtual environment is and why it prevents disasters
- Have a code editor that actually helps you write Python
- Know what each tool in the AI/ML Python ecosystem does
- Have a working project folder ready for Week 1

---

## 1. Python itself

### What is Python?

Python is a programming language — a way to give instructions to your computer. You type
commands in English-like syntax, and Python translates them into actions the computer
understands.

### Why Python for AI?

Almost every AI/ML tool is built in Python or has a Python interface:
- **ChatGPT, Claude, Gemini** — all accessed through Python libraries
- **scikit-learn, PyTorch, TensorFlow** — the big ML frameworks are Python-first
- **NumPy, Pandas** — data manipulation tools used by every data scientist
- **FastAPI** — the standard way to serve AI models as web services

Python isn't the fastest language, but it has the richest ecosystem for AI. That's why
you're learning it.

### How to install

**macOS:**

```bash
# Option A: Download from python.org (simplest)
# Go to https://www.python.org/downloads/ and download the latest 3.12+

# Option B: Use Homebrew (if you have it)
brew install python@3.12

# Option C: Use pyenv (recommended for managing multiple versions later)
brew install pyenv
pyenv install 3.12.7
pyenv global 3.12.7
```

**Verify it works:**

```bash
python3 --version
# Should print: Python 3.12.x (or newer)
```

**Why 3.12+?** Each Python version adds features. 3.12 added better error messages
(crucial for beginners!), faster performance, and `match-case` support has matured.
Older versions work but give you worse error messages when things go wrong.

### What about Python 2?

Python 2 is dead (end-of-life since 2020). Never use it. If you see `python` vs
`python3` on your system, always use `python3`. On some systems, `python` still
points to Python 2.

---

## 2. The code editor (VS Code)

### What is a code editor?

A code editor is where you write your code. You *could* use Notepad or TextEdit, but
that's like hammering nails with your shoe — it works, but a real hammer is better.

### Why VS Code?

| Feature | Why it matters |
|---------|---------------|
| **Syntax highlighting** | Colors your code so you can see structure at a glance |
| **Auto-completion** | Suggests what to type next — huge time saver |
| **Error underlining** | Shows mistakes *before* you run the code |
| **Integrated terminal** | Run Python right inside the editor |
| **Debugger** | Step through code line-by-line to find bugs |
| **Extensions** | Add extra powers (Python support, Git, AI assistants) |

### How to install

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install and open it
3. Install the **Python extension**:
   - Click the Extensions icon in the sidebar (or press `Cmd+Shift+X`)
   - Search "Python"
   - Install the one by Microsoft (it has millions of downloads)

### What the Python extension gives you

- **IntelliSense** — as you type `"hello".`, it shows you every string method
- **Linting** — warns you about bad style or likely bugs
- **Run button** — click the green play button to run your file
- **Jupyter support** — run notebook cells right in VS Code

### Other editors (alternatives)

- **PyCharm** — more powerful but heavier. Good if you like IDEs.
- **Cursor** — VS Code fork with built-in AI. Great for AI-assisted coding.
- **Vim/Neovim** — for terminal lovers. Steep learning curve.

Stick with VS Code for this course. It's free, fast, and the most popular choice in
the Python/AI community.

---

## 3. Virtual environments

### The problem they solve

Imagine you're working on two projects:
- Project A needs `numpy version 1.24`
- Project B needs `numpy version 1.26`

If you install both globally, one project breaks. This is called a **dependency conflict**,
and it's one of the most common headaches in Python.

### What is a virtual environment?

A virtual environment is a **self-contained folder** that has its own copy of Python and
its own installed packages. Each project gets its own environment, so they never
interfere with each other.

Think of it like having separate toolboxes for separate projects.

### How to create one

```bash
# Navigate to your project folder
cd ~/upskilling/python-learning

# Create a virtual environment called .venv
python3 -m venv .venv

# Activate it
source .venv/bin/activate    # macOS/Linux
# .venv\Scripts\activate     # Windows

# Your prompt should now show (.venv) at the start:
# (.venv) $
```

### How to know it's working

```bash
# With venv activated:
which python
# Should show: /path/to/your/project/.venv/bin/python

# WITHOUT venv, it would show:
# /usr/bin/python3  or  /usr/local/bin/python3
```

### Key commands

| Command | What it does |
|---------|-------------|
| `python3 -m venv .venv` | Create a new virtual environment |
| `source .venv/bin/activate` | Activate it (start using it) |
| `deactivate` | Deactivate it (go back to system Python) |
| `pip install <package>` | Install a package *into the active venv* |
| `pip list` | See what's installed in this venv |
| `pip freeze > requirements.txt` | Save your installed packages to a file |

### Why `.venv` as the name?

The dot makes it a hidden folder (on macOS/Linux), so it doesn't clutter your
file listing. The name `venv` is a convention — everyone knows what it means.

### VS Code integration

VS Code detects `.venv` automatically. When you open a Python file, look at the
bottom-right status bar — it should say `Python 3.12.x ('.venv')`. If not,
click it and select the `.venv` interpreter.

---

## 4. pip — the package manager

### What is pip?

`pip` is Python's package manager. It downloads and installs libraries from
[PyPI](https://pypi.org/) (Python Package Index) — a repository of 500,000+ packages
created by the Python community.

### Why you need it

Python comes with a "standard library" (built-in tools), but AI/ML requires
external libraries. You install them with pip:

```bash
# Make sure your venv is activated first!
pip install numpy
```

### Essential commands

```bash
# Install a specific package
pip install numpy

# Install a specific version
pip install numpy==1.26.4

# Install multiple packages at once
pip install numpy pandas matplotlib

# Upgrade a package
pip install --upgrade numpy

# See what's installed
pip list

# Save your environment (so others can recreate it)
pip freeze > requirements.txt

# Install from a requirements file
pip install -r requirements.txt
```

### What is requirements.txt?

It's a simple text file listing every package your project needs:

```
numpy==1.26.4
pandas==2.2.0
matplotlib==3.8.2
```

Anyone can run `pip install -r requirements.txt` to get the exact same setup.
This is how teams share environments and how you deploy to servers.

---

## 5. IPython & Jupyter — interactive Python

### What is IPython?

IPython is an **enhanced Python shell**. The regular Python shell (`python3` in
your terminal) is basic — IPython adds auto-completion, syntax highlighting,
history search, and magic commands.

```bash
pip install ipython
ipython
```

### Why use it?

When you're learning, you'll want to try things quickly:

```python
# In IPython, just type and see results immediately:
In [1]: 2 + 2
Out[1]: 4

In [2]: "hello".upper()
Out[2]: 'HELLO'

In [3]: [x**2 for x in range(5)]
Out[3]: [0, 1, 4, 9, 16]
```

It's like a scratchpad — perfect for experimenting before writing full scripts.

### What is Jupyter?

Jupyter Notebook is a **document that mixes code, output, and text**. You write
code in "cells," run them one at a time, and see results (including charts!)
right below the code.

```bash
pip install jupyter
jupyter notebook
# Opens in your browser
```

### Why Jupyter matters for AI

- **Data exploration** — see your data as tables and charts inline
- **Experimentation** — run code cells in any order, tweak and re-run
- **Sharing** — notebooks are the standard format for ML tutorials and papers
- **Kaggle** — the biggest ML competition site runs everything in notebooks

For this course, we'll mostly write `.py` files, but you'll use Jupyter for data
exploration in Weeks 5-8.

### VS Code alternative

You don't need the browser-based Jupyter. VS Code can open `.ipynb` files directly
with the Python extension. Many people prefer this because you get all VS Code
features inside the notebook.

---

## 6. Git — version control

### What is Git?

Git tracks every change you make to your code. Think of it as an unlimited
**undo history** for your entire project.

### Why you need it

- **Safety net** — broke something? Go back to when it worked.
- **Experimentation** — try something risky on a "branch" without affecting your main code.
- **Portfolio** — your GitHub profile shows employers what you can build.
- **Collaboration** — every team and open-source project uses Git.

### How to set up

```bash
# Check if git is installed
git --version

# If not installed (macOS):
xcode-select --install
# Or: brew install git

# Configure your identity (one-time setup)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize a repo in your project folder
cd ~/upskilling/python-learning
git init
```

### Create a .gitignore

Some files should NOT be tracked by git. Create a `.gitignore` file:

```
# Virtual environment
.venv/

# Python cache files
__pycache__/
*.pyc

# Jupyter checkpoints
.ipynb_checkpoints/

# OS files
.DS_Store

# Secrets (API keys) — NEVER commit these
.env

# Data files (too large for git)
*.csv
*.parquet
data/
```

### Why .gitignore matters for AI

- **API keys** — you'll use OpenAI/Anthropic keys in Week 8. If you commit them to
  GitHub, bots will find and steal them within minutes. Always use `.env` files and
  `.gitignore`.
- **Data files** — ML datasets can be gigabytes. Git isn't designed for large files.
- **Model files** — trained models can be hundreds of MB. Use specialized tools
  (MLflow, DVC) for those.

---

## 7. The libraries you'll install throughout this course

You don't need to install everything now — we'll install each library when we first
use it. But here's the roadmap so you know *why* each one exists:

### Weeks 1-4: Core Python (no extra libraries needed)

Python's built-in standard library covers everything:
- `os`, `pathlib` — file and folder operations
- `json`, `csv` — reading/writing data formats
- `re` — regular expressions (text pattern matching)
- `logging` — recording what your program does
- `typing`, `dataclasses` — writing cleaner, safer code

### Week 5: Data manipulation

| Library | What it does | Why you need it |
|---------|-------------|-----------------|
| **NumPy** | Fast math on arrays of numbers | Foundation of ALL ML — every model uses NumPy arrays internally |
| **Pandas** | Tables of data (like Excel but powerful) | Loading, cleaning, and analyzing datasets |

```bash
pip install numpy pandas
```

### Week 6: Visualization, APIs & Testing

| Library | What it does | Why you need it |
|---------|-------------|-----------------|
| **Matplotlib** | Create charts and plots | Visualizing data, model performance, training progress |
| **Seaborn** | Beautiful statistical plots | Built on matplotlib, easier for common ML visualizations |
| **Requests** | Make HTTP requests | Calling web APIs (including AI model APIs) |
| **pytest** | Run automated tests | Verifying your code works correctly |

```bash
pip install matplotlib seaborn requests pytest
```

### Week 7: Machine Learning

| Library | What it does | Why you need it |
|---------|-------------|-----------------|
| **Scikit-learn** | Classical ML algorithms | Classification, regression, clustering, preprocessing |

```bash
pip install scikit-learn
```

### Week 8: AI Engineering

| Library | What it does | Why you need it |
|---------|-------------|-----------------|
| **openai** | OpenAI API client (GPT models) | Calling ChatGPT/GPT-4 from Python |
| **anthropic** | Anthropic API client (Claude models) | Calling Claude from Python |
| **FastAPI** | Build web APIs | Serving your AI models as HTTP endpoints |
| **ChromaDB** | Vector database | Storing and searching text embeddings for RAG |
| **uvicorn** | ASGI server | Running your FastAPI app |

```bash
pip install openai anthropic fastapi uvicorn chromadb
```

---

## 8. Your project folder structure

Here's what your workspace should look like:

```
python-learning/
├── .venv/              # Virtual environment (don't edit manually)
├── .gitignore          # Files git should ignore
├── lessons/            # Course lesson files (already here)
│   ├── w00/
│   ├── w01/
│   └── ...
├── seed.py             # Course curriculum (already here)
├── server.py           # Learning tracker UI (symlinked)
├── static/             # UI assets (symlinked)
├── run.sh              # Start the tracker (symlinked)
└── labs/               # YOUR work goes here — create this!
    ├── week1/
    ├── week2/
    └── ...
```

Create the labs folder:

```bash
mkdir -p labs/week1 labs/week2 labs/week3 labs/week4 \
         labs/week5 labs/week6 labs/week7 labs/week8
```

This is where you'll write your lab exercises. Keeping them separate from the
lessons keeps things organized.

---

## 9. Verify everything works

Run this checklist in your terminal:

```bash
# 1. Python version
python3 --version
# Expected: Python 3.12.x or newer

# 2. Virtual environment
cd ~/upskilling/python-learning
source .venv/bin/activate
which python
# Expected: .../python-learning/.venv/bin/python

# 3. pip works
pip --version
# Expected: pip 24.x from .../python-learning/.venv/...

# 4. Install IPython and test it
pip install ipython
python3 -c "print('Hello, AI Engineer!')"
# Expected: Hello, AI Engineer!

# 5. Git is ready
git --version
# Expected: git version 2.x.x

# 6. VS Code opens the project
code .
# Expected: VS Code opens with your project folder
```

If all six steps work, you're ready for Week 1!

---

## 10. Choose your daily study slot

This course is designed for **~1 hour per day**. Pick a consistent time:

- **Morning** — fresh brain, fewer distractions
- **Lunch break** — split into 35 min read + 25 min lab later
- **Evening** — wind down with focused learning

The best time is whatever time you'll actually stick to. Put it in your calendar.

---

## Common setup mistakes

- **Installing packages globally instead of in a venv** — always activate your venv first. If you see `WARNING: pip is configured with locations that require TLS/SSL`, you're probably using system Python.
- **Using Python 2** — if `python --version` says 2.x, use `python3` instead.
- **Not creating .gitignore before your first commit** — add it immediately so you never accidentally commit `.venv/` or API keys.
- **Installing too much at once** — only install what you need for the current week. Fewer packages = fewer conflicts.

## Check yourself

- [ ] `python3 --version` shows 3.12+
- [ ] You have a `.venv` folder and know how to activate it
- [ ] VS Code is installed with the Python extension
- [ ] You can run `python3 -c "print('ready')"` and see output
- [ ] Git is initialized in your project folder
- [ ] You have a `.gitignore` file
- [ ] You've chosen a daily study time
