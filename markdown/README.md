# Markdown

This folder contains runnable / viewable notes for **Markdown syntax** and the conventions I use in GitHub-flavored Markdown (GFM).

## What’s in here

- `basics.md` — a small “kitchen sink” note that demonstrates common Markdown building blocks:
  - Headings (`#`, `##`, `###`)
  - Paragraphs and emphasis (`*italic*`, `**bold**`, `~~strikethrough~~`, `==highlight==`*)
  - Lists (bulleted + numbered) and task lists (`- [x]`, `- [ ]`)
  - Blockquotes (`> ...`)
  - Links (`[text](url)`) and inline code (`` `command` ``)
  - Fenced code blocks (```python ... ```)
  - Horizontal rules (`---`)
  - Tables (placeholder section included)
  - Footnotes (`[^1]`)**
  - Images (`![alt text](image.jpg)`)

\* Note: `==highlight==` is not part of “core” Markdown and only renders as highlight in some renderers.
GitHub generally does **not** render highlight with `==...==`.

\** Footnotes are supported in many Markdown renderers, including GitHub-flavored Markdown in many contexts.

## About README.md files (what they’re for)

A `README.md` is the default “front page” for a repository (and often for folders inside a repo) on GitHub.
It’s typically used to answer:

- **What is this?** (short description / purpose)
- **What’s inside?** (directory structure, key files)
- **How do I use it?** (commands, examples, expected output)
- **How do I contribute or extend it?** (optional)

In this repo, each directory-level `README.md` is meant to be a lightweight index so future-me can
quickly find the right note/script and remember how to run/view it.

## Viewing the notes

- On GitHub: open `basics.md` in the web UI to see how it renders.
- Locally: you can view Markdown in many editors (VS Code preview, Obsidian, Typora, etc.).

## Notes / TODO

- The image example in `basics.md` should use the exact syntax below (no spaces):
  - `![alt text](image.jpg)`
- The code block in `basics.md` is labeled `python` but contains JSON-like content; consider using
  `json` as the fence label instead if you want highlighting to match.
