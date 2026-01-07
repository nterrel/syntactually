# syntactualize

A personal “syntax notebook” repo: short, runnable examples and reminders for languages/tools I use.
Each folder contains small scripts that double as notes.

## Structure

- `bash/` — shell scripting notes + common CLI tools (grep, awk, …)
- `perl/` — Perl basics
- `python/` — Python basics (and some package usage notes); see below for venv setup
- `markdown/` — Markdown patterns and snippets

## Usage

Make scripts executable (if applicable) and run to see some basic notes.

To create a Python virtual environment, run:
```bash
make setup
```

This will help with running scripts that rely on non-standard libraries. 

And to run scripts do:
```bash
./run_scripts.sh [bash, python, ...]
```


