# static-site-project

A tiny, no-framework static site generator that turns Markdown content into a fast, portable website using a minimal HTML template. Designed for simplicity: predictable folder structure, zero magic, and build scripts you can actually read.

> Why this exists: to learn and demonstrate static-site generation fundamentals (parsing, templating, routing, and asset handling) without hiding everything behind a framework. This project was also used as a means to learn and advance my python knowledge and experience.

---

## Features

- **Markdown → HTML** pipeline with a single **`template.html`** layout  
- **Content-first structure**: drop posts/pages in `content/` and build  
- **Asset passthrough**: everything in `static/` is copied as-is  
- **Deterministic builds** via simple shell entrypoints (`main.sh`, `test.sh`)  
- **Tiny footprint**: Python (mostly standard library) and a few readable scripts  

---

## Project structure

.

├─ content/ → *Your Markdown and/or HTML content lives here*

├─ src/ → *Python build scripts (parser, renderer, copier, utils)*

├─ static/ → *Images, CSS, JS (copied 1:1 to the output)*

├─ template.html → *Base HTML template used for every page*

├─ main.sh → *Build orchestration (dev/build helper)*

├─ test.sh → *Basic checks/tests for the pipeline*

└─ README.md

---

## Quick start

### Prerequisites
- Python 3.10+ (earlier may work, but not guaranteed)  
- macOS/Linux shell (Windows users can use WSL or Git Bash)  

### 1) Clone

```bash
git clone https://github.com/Mon-arc/static-site-project.git
cd static-site-project
```

### 2) Build the site
Use the helper script (optional)
```bash
chmod +x main.sh
./main.sh
```
If you prefer calling Python directly, check the scripts in src/ and wire them as you like. The point is: the build is transparent and hackable.

### 3) Preview Locally
```bash
python -m http.server --directory dist 8080
# open http://localhost:8080
```
