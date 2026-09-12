# codeforces-solutions
My very own journey into codeforces. This repo contains my accepted solutions to various problems on **Codeforces**, implemented primarily in **Python**.

## Repository Structure

```text
codeforces-solutions/
│
├── .gitignore              # Ignores temporary input/output data
├── README.md               # Repository documentation
├── templates/
│   └── template.py         # Standard Python template with Fast I/O
└── codeforces/
    ├── practice/           # Random problem-set solutions (named by Problem ID)
    └── contests/           # Solutions grouped by specific live contests
```

## Setup & Workflow

### Running Locally
To test solutions locally without manually typing inputs every time, I pipe the sample cases from an `input.txt` file into the script using the terminal:

```powershell
python codeforces/practice/4A.py < input.txt
```

### Python Template (Fast I/O)
To avoid **Time Limit Exceeded (TLE)** errors, solutions use `sys.stdin.readline` for optimal performance:

```python
import sys

# Optimize standard input
input = sys.stdin.readline

def solve():
    # Problem logic goes here
    pass

if __name__ == '__main__':
    t = 1
    # t = int(input()) # Uncomment if problem has multiple test cases
    for _ in range(t):
        solve()
```

## Progression - <1000 Problem Set 
- **Language:** Python 3
- **Goal:** Improve problem-solving speed, data structure mastery, and algorithmic thinking.
