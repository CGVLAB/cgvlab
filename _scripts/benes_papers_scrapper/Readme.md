Script to automatically rename papers from Professor Bedrich Benes
==================================================================

This script automatically retrieve papers from Bedrich Benes' website and rename them to follow the naming convention.

How it works?
-------------

1. Update the file `benes_original_references.bib` with his reference bibtex library
2. Run the script with `python3 main.py > reference.bib`
3. Take care of any error output by the script
4. Copy the curated bibtex list from `reference.bib` to the main file in `_bibliography/references.bib`


References
----------

### BibTex Python Lib

Source on GitHub: https://github.com/aclements/biblib

```bash
$ git clone https://github.com/aclements/biblib.git
```
