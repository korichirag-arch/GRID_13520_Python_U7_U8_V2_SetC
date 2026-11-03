# GRID 13520 – Python Units 7 & 8 (Set C)

A collection of two small Python scripts that practise the **Python standard library**: working with dates and times, maths and random numbers, unique IDs, timing, and file-system operations. Everything uses only modules that ship with Python, so there is **nothing to install**.

| Script | Section | Topics covered |
|--------|---------|----------------|
| [`A_standard_modules.py`](A_standard_modules.py) | **A** | `datetime`, `math`, `random`, `uuid`, `time` |
| [`B_os_demo.py`](B_os_demo.py) | **B** | `os`, `shutil` (directories, files, move, rename, delete) |

> The repository name suggests this is coursework (Units 7 and 8, Set C of a Python course). Each script is organised as a numbered list of small exercises ("1st question", "2nd question", and so on), and each exercise prints a short result.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Requirements](#requirements)
3. [How to Run](#how-to-run)
4. [Section A: `A_standard_modules.py`](#section-a-a_standard_modulespy)
5. [Section B: `B_os_demo.py`](#section-b-b_os_demopy)
6. [Full Expected Output](#full-expected-output)
7. [Quick Reference of Functions Used](#quick-reference-of-functions-used)
8. [Design Notes and Things to Know](#design-notes-and-things-to-know)
9. [Troubleshooting](#troubleshooting)
10. [Possible Improvements](#possible-improvements)
11. [License](#license)

---

## Project Structure

```
GRID_13520_Python_U7_U8_V2_SetC/
├── A_standard_modules.py   # Section A: date/time, math, random, uuid, time (161 lines)
├── B_os_demo.py            # Section B: os and shutil file operations (201 lines)
└── README.md               # This file
```

There are no packages, data files, configuration files or tests. Each script is standalone and independent of the other.

---

## Requirements

- **Python 3.6 or newer** (the scripts use f-strings and numeric literals such as `1_000_000`). They were run successfully on **Python 3.13**.
- **No third-party libraries.** Modules used: `datetime`, `math`, `random`, `uuid`, `time`, `os`, `shutil`.
- Works on Windows, macOS and Linux. Paths are built with `os.path.join`, so the correct separator is used on each system (on Windows you will see `store_data\logs` instead of `store_data/logs`).

---

## How to Run

```bash
# 1. Get the code
git clone https://github.com/korichirag-arch/GRID_13520_Python_U7_U8_V2_SetC.git
cd GRID_13520_Python_U7_U8_V2_SetC

# 2. Run either script (use `python3` if `python` is not available)
python A_standard_modules.py
python B_os_demo.py
```

Neither script asks for input; each prints its results and exits.

**Before running Section B, read the [warning](#warning-section-b-deletes-a-folder-called-store_data) about the folder it deletes.**

---

## Section A: `A_standard_modules.py`

Three groups of exercises. All the "current time" and "random" values are fixed in the code, so **the output is identical on every run** (see [Design Notes](#design-notes-and-things-to-know)).

### Q1. Date and Time (`datetime`)

| # | Exercise | How the code does it | Result |
|---|----------|----------------------|--------|
| 1 | **Leap-year check** | `is_leap_year(year)` applies the full Gregorian rule: divisible by 400 is a leap year; otherwise divisible by 100 is *not*; otherwise divisible by 4 *is*. Run on `[1700, 2016, 2026, 2200, 2032]`. | 1700 `False`, 2016 `True`, 2026 `False`, 2200 `False`, 2032 `True` |
| 2 | **Day of the week** | `datetime.strptime(text, "%Y-%m-%d").strftime("%A")` parses a `YYYY-MM-DD` string, then formats the weekday name. | 2026-05-01 Friday, 2026-10-02 Friday, 2027-03-14 Sunday |
| 3 | **Days between two dates** | Subtracting two `datetime` objects gives a `timedelta`; `.days` is the whole-day count. 10 Mar 2026 to 20 Sep 2026. | `194` |
| 4 | **Formatting** | A fixed moment, 2 Nov 2026 21:45:10, is printed as `%d-%m-%Y` (day first), `%m/%d/%Y` (US style), `%H:%M:%S` (24 hour) and `%I:%M:%S %p` (12 hour with AM/PM). | `02-11-2026 11/02/2026` and `21:45:10 09:45:10 PM` |
| 5 | **Date arithmetic** | Adds `timedelta(weeks=1, days=6, hours=3)` (that is 13 days and 3 hours) to the same moment. The date rolls over midnight into the next day. | `2026-11-16 00:45:10` |

### Q2. `math` and `random`

| # | Exercise | How the code does it | Result |
|---|----------|----------------------|--------|
| 1 | **Buses needed** | `math.ceil(129 / 25)` rounds **up**, because a partly filled bus is still a bus (5.16 becomes 6). | `6` |
| 2 | **Seconds to h:m:s** | `//` (floor division) and `%` (remainder) split 7384 seconds: `7384 // 3600 = 2` hours, `(7384 % 3600) // 60 = 3` minutes, `7384 % 60 = 4` seconds. | `2 3 4` |
| 3 | **Simplify a fraction** | `math.gcd(36, 84)` is 12; dividing both numbers by it gives the lowest terms. Returned as a tuple. | `(3, 7)` |
| 4 | **Height from distance and angle** | Trigonometry: `height = distance x tan(angle)`. `math.radians()` converts 60 degrees to radians first, because `math.tan` expects radians. With distance 120. | `207.85` |
| 5 | **Seeded dice rolls** | `random.seed(31)` makes the "random" numbers repeatable. Five rolls via `random.randint(1, 6)` in a list comprehension, plus their sum. | `[1, 4, 1, 4, 2] 12` |
| 6 | **Shuffle and choose** | `random.shuffle()` reorders the list `1..8` **in place**; `random.choice()` picks one item from rock/paper/scissors. Because the seed from the previous exercise is still active, these are repeatable too. | `[4, 6, 3, 7, 5, 8, 2, 1]` and `rock` |

### Q3. `uuid` and `time`

| # | Exercise | How the code does it | Result |
|---|----------|----------------------|--------|
| 1 | **Stable user IDs** | `uuid.uuid5(uuid.NAMESPACE_DNS, name.lower() + ".example")` builds a **name-based** UUID for each of four names. The same name always gives the same UUID. The first 8 characters are printed, and a set is used to confirm all four are different. | Kavita `57b97b51`, Lalit `29504e7e`, Manoj `2bf224c2`, Nisha `8bdf4049`, then `True` |
| 2 | **UUID v3 vs v5** | Builds both `uuid3` (MD5 based) and `uuid5` (SHA-1 based) for `"example.com"` and shows they differ and report versions 3 and 5. | `True 3 5` |
| 3 | **Timestamp conversion** | Converts the Unix timestamp `1700000000` to UTC three ways: `time.strftime` with `time.gmtime`, `time.asctime`, and `datetime.fromtimestamp(ts, timezone.utc)`. | `2023-11-14 22:13:20`, `Tue Nov 14 22:13:20 2023`, `14 Nov 2023` |
| 4 | **Timing code** | `time.perf_counter()` before and after `sum(range(1_000_000))`. The script prints the sum, the *type* of the elapsed value, and whether it is non-negative. The elapsed time itself is deliberately not printed (it changes every run). | `499999500000 float True` |

---

## Section B: `B_os_demo.py`

Seven exercises on file-system handling, all inside a folder named **`store_data`** that the script creates in the current directory and **deletes at the end**.

The exercises build on each other. Every block first recreates the same starting state (so each block also works when read on its own), then adds one new step.

| # | Exercise | Key calls | What happens |
|---|----------|-----------|--------------|
| 1 | **Create a directory safely** | `os.makedirs(path, exist_ok=True)` | Creates `store_data/logs`, including the parent folder. Called twice to show that `exist_ok=True` makes a repeat call harmless (no `FileExistsError`). |
| 2 | **Create files** | `open(path, "w", encoding="utf-8")` | Writes `p.txt` (`red`, `green`), `q.txt` (`blue`) and `r.csv` (`x,y` header and one row `1,2`) into `logs`. |
| 3 | **List only `.txt` files** | `os.listdir`, `str.endswith`, `sorted` | Filters out `r.csv` and prints `['p.txt', 'q.txt']`. |
| 4 | **Read a file** | `open(path, "r")`, `readlines()` | Reads `p.txt`, prints the line count and the first line stripped of its newline: `2 red`. |
| 5 | **Move a file** | `shutil.move(src, dst)` | Creates `store_data/archive` and moves `p.txt` into it. Listings then show `logs` = `['q.txt', 'r.csv']`, `archive` = `['p.txt']`. |
| 6 | **Rename a file** | `os.replace(src, dst)` | Renames `q.txt` to `old_q.txt`. Prints `os.path.exists(q.txt)` as `False` and `os.path.isfile(old_q.txt)` as `True`. |
| 7 | **Delete everything** | `shutil.rmtree("store_data")` | Removes the whole `store_data` tree and prints `os.path.exists("store_data")` as `False`. |

After a complete run the folder is gone, so the script leaves **no files behind**.

### Warning: Section B deletes a folder called `store_data`

The final step runs `shutil.rmtree("store_data")` on a path **relative to the folder you run the script from**. If you already have a folder named `store_data` there, **all of its contents will be permanently deleted** (and some files inside it are overwritten earlier in the run). Run the script from an empty or scratch directory.

---

## Full Expected Output

### `python A_standard_modules.py`

```text
Section: A - 

Q.1 Date and Time 

1700 False
2016 True
2026 False
2200 False
2032 True
2026-05-01 is a Friday
2026-10-02 is a Friday
2027-03-14 is a Sunday
Number of days: 194
02-11-2026 11/02/2026
21:45:10 09:45:10 PM
2026-11-16 00:45:10


Q2. The math and random modules. 

6
2 3 4
(3, 7)
207.85
[1, 4, 1, 4, 2] 12
[4, 6, 3, 7, 5, 8, 2, 1]
rock


Q3. The uuid and time modules. 

Kavita: 57b97b51
Lalit: 29504e7e
Manoj: 2bf224c2
Nisha: 8bdf4049
True
True 3 5
2023-11-14 22:13:20
Tue Nov 14 22:13:20 2023
14 Nov 2023
499999500000 float True
```

### `python B_os_demo.py`

```text
SECTION B - os MODULE, CUSTOM MODULES AND PACKAGES 

Directory created/verified: store_data/logs
Directory verified again without error: store_data/logs
['p.txt', 'q.txt']
['p.txt', 'q.txt']
2 red
['p.txt', 'q.txt']
2 red
['q.txt', 'r.csv'] ['p.txt']
['p.txt', 'q.txt']
2 red
['q.txt', 'r.csv'] ['p.txt']
False True
['old_q.txt', 'p.txt', 'q.txt']
2 red
['old_q.txt', 'q.txt', 'r.csv'] ['p.txt']
False True
False
```

(These outputs were produced by actually running both scripts on Python 3.13.)

---

## Quick Reference of Functions Used

| Module | Function / class | Purpose |
|--------|------------------|---------|
| `datetime` | `datetime(...)`, `timedelta(...)` | Build a date-time; represent a length of time |
| `datetime` | `strptime(text, fmt)` / `strftime(fmt)` | Parse text into a date / format a date as text |
| `datetime` | `datetime.fromtimestamp(ts, timezone.utc)` | Unix timestamp to an aware UTC date-time |
| `math` | `ceil`, `gcd`, `tan`, `radians` | Round up, greatest common divisor, tangent, degrees to radians |
| `random` | `seed`, `randint`, `shuffle`, `choice` | Repeatable randomness, random integer, in-place shuffle, random pick |
| `uuid` | `uuid3`, `uuid5`, `NAMESPACE_DNS` | Deterministic name-based IDs (MD5 / SHA-1) |
| `time` | `gmtime`, `strftime`, `asctime`, `perf_counter` | UTC time struct, formatting, readable string, high-resolution timer |
| `os` | `makedirs`, `listdir`, `replace`, `path.join`, `path.exists`, `path.isfile` | Folders, listing, rename, portable paths, existence checks |
| `shutil` | `move`, `rmtree` | Move a file; delete a whole directory tree |

Common `strftime` codes used: `%Y` year, `%m` month, `%d` day, `%A` weekday name, `%b` short month name, `%H` 24-hour, `%I` 12-hour, `%M` minutes, `%S` seconds, `%p` AM/PM.

---

## Design Notes and Things to Know

1. **Output is deterministic by design.** Section A uses fixed dates instead of `datetime.now()`, and `random.seed(31)` fixes the random numbers (including the shuffle and the `choice`, which come after the seed). Two runs give identical output. The exact random values can differ between major Python versions, so a different version may print different dice or deck orders.
2. **UUIDs are reproducible.** `uuid5` and `uuid3` are derived from a name, so they are the same on every run and every machine. Use `uuid.uuid4()` if you want a random, unpredictable ID.
3. **Section B repeats its setup in every question.** The directory and file creation code is copied into each block. This makes each block self-contained but is repetitive; a helper function would remove the duplication.
4. **The blocks in Section B are not fully independent.** Because earlier blocks leave files behind (for example `old_q.txt` created in exercise 6), later listings show them. That is why exercise 7 lists `['old_q.txt', 'p.txt', 'q.txt']`.
5. **Mismatch in the Section B heading.** The banner printed by `B_os_demo.py` says "os MODULE, CUSTOM MODULES AND PACKAGES", but the script only contains `os` and `shutil` exercises. There are no custom modules or packages in this repository.
6. **No `if __name__ == "__main__":` guard.** Both scripts run everything as soon as they are executed *or imported*. Importing `B_os_demo` from another file would create and delete `store_data`.
7. **No cleanup on failure.** If Section B crashes before its last step, the `store_data` folder stays on disk.
8. **Strings used as comments.** The `''' 1st question. '''` lines are string literals that Python ignores, so they work as labels but are not real comments or docstrings. (Line 86 of `A_standard_modules.py` has four quote characters, `''''`; it still runs correctly.)
9. **Section A has a long run of blank lines** at the end (lines 146 to 161). They are harmless.
10. **Limited input handling.** `day_of_week` raises `ValueError` for a string that is not in `YYYY-MM-DD` form, and nothing validates other inputs. For these exercises the inputs are fixed, so it never triggers.

---

## Troubleshooting

| Problem | Cause and fix |
|---------|---------------|
| `python: command not found` | Use `python3 A_standard_modules.py`, or install Python from python.org. |
| `SyntaxError` on an f-string or `1_000_000` | Your Python is older than 3.6. Upgrade to a current version. |
| Random numbers differ from the output above | You are on a different Python version. The seeded numbers are only guaranteed to repeat on the same version. |
| `PermissionError` in Section B | Run it from a folder you can write to, and make sure no file inside `store_data` is open in another program (this matters most on Windows). |
| A `store_data` folder of mine disappeared | Section B deletes `store_data` in the current directory. Run it only from an empty folder next time. |
| A `store_data` folder is left behind after a crash | Delete it manually; the script normally removes it in its last step. |
| Paths print with `\` instead of `/` | You are on Windows. This is expected. |

---

## Possible Improvements

- Wrap each section in functions and add `if __name__ == "__main__":` guards.
- In Section B, use `tempfile.TemporaryDirectory()` instead of a fixed `store_data` folder, so no existing data can ever be deleted. Put the cleanup in a `try/finally`.
- Put the repeated setup of Section B in one helper function.
- Use `calendar.isleap()` to cross-check `is_leap_year`.
- Use `pathlib.Path` in place of `os.path.join` for more readable path code.
- Add basic tests (for example with `unittest` or `pytest`) for `is_leap_year`, `day_of_week` and `simplify`.
- Rename or correct the Section B heading so it matches what the script does.

---

## License

No license file is included in this repository yet. Add one (for example MIT) if you want others to reuse the code.
