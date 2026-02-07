# Graphing Calculator

A simple graphing calculator application built with Python and tkinter. It
plots functions of `x`, provides a small calculator, and can be packaged as a
Windows executable.

<<<<<<< HEAD
## Features

- Plot mathematical expressions f(x) with configurable axis ranges
- Quick expression calculator for single-value evaluations
- Uses `numpy` + `matplotlib` for plotting and `tkinter` for the GUI

## Quickstart

Option A — Run from source (development)

1. Install Python 3.7+.
2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python test.py
```

Option B — Create a Windows executable (recommended for distributing to
users)

1. Make sure dependencies are installed (`requirements.txt` is optional for
the build, but needed for testing locally).
2. Use the included helper script (Windows):

```powershell
cd "path\to\repo"
.\setup.bat
```

This will install PyInstaller (if needed) and create `dist\GraphingCalculator.exe`.

You can also run PyInstaller manually:

```powershell
python -m pip install pyinstaller
python -m PyInstaller --onefile --windowed --name "GraphingCalculator" test.py
```

Then run the executable in `dist\GraphingCalculator.exe`.

## Distributing the .exe (recommended: GitHub Releases)

- Option 1 — Add the `.exe` directly to the repository (works, but inflates
  repo size).
- Option 2 — Use GitHub Releases: create a release and upload `GraphingCalculator.exe`.

## .gitignore recommendations

Add the following to `.gitignore` to avoid committing build artifacts:

```
build/
dist/
*.spec
__pycache__/
*.pyc
```

## Troubleshooting

- If `pip` is not recognized, run installers using `python -m pip` instead:

```powershell
python -m pip install -r requirements.txt
python -m pip install --upgrade pip
```

- If the `setup.bat` reports it cannot find files, make sure you run it from
  the repository folder (the script does `cd /d "%~dp0"` so double-clicking
  it is usually sufficient).

- When packaging with PyInstaller, rebuild cleanly if you change `test.py`:

```powershell
Remove-Item -Path .\build, .\dist, .\GraphingCalculator.spec -Recurse -Force -ErrorAction SilentlyContinue
python -m PyInstaller --onefile --windowed --name "GraphingCalculator" test.py
```

## Example functions to try

- `x**2`
- `sin(x)`
- `1/x` (note: discontinuity at zero)
- `sqrt(x)` (use x >= 0)

## Contact

If you want improvements (more functions, saving images, interactive zoom),
open an issue or PR.
=======
- Python 3.7 or higher
- numpy
- matplotlib
=======
coming soon
>>>>>>> e3f20a72f1f13b775c0958f053d8ed5ccc6ed465

>>>>>>> 262a5b306370ba96e2f868bfa6932056068e6725

