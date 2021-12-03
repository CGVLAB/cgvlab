Script to automatically check consistency of the papers database
================================================================

This script automatically check that each paper in the database has:
 - A valid image
 - A valid PDF
 - No duplicate

It also checks that all PDF files in the folder correspond to a paper and are not unrelated to any bibtex entry.

How it works?
-------------

1. Run the script with `python3 main.py`
2. It will display a list of warnings and errors

References
----------

### BibTex Python Lib

Source on GitHub: https://github.com/aclements/biblib

```bash
$ git clone https://github.com/aclements/biblib.git
```

### Virtual environment

This script needs the package fuzzywuzzy

```bash
$ python3 -m venv --system-site-packages ./venv
$ source ./venv/bin/activate
$ pip install --upgrade pip
$ pip install python-Levenshtein fuzzywuzzy
```
