# create_structure.py

import os

folders = [
    "data/raw/weo",
    "data/raw/ifs",
    "data/raw/gfs",
    "data/raw/worldbank",
    "data/raw/manual_labels",
    "data/processed",
    "notebooks",
    "src/data_ingestion",
    "src/data_cleaning",
    "src/merging",
    "src/modeling",
    "src/llm",
    "src/utils",
    "models",
    "dashboard",
    "tests"
]

files = [
    "config.yaml",
    "requirements.txt",
    ".gitignore",
    ".env",
    "README.md",
    "dashboard/app.py",
    "dashboard/components.py"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        f.write("# " + file)

print("✅ Project structure created!")
