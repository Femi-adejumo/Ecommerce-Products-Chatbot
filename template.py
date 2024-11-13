#create a project directory structure
import os
from pathlib import Path

project_name = "Jumia"

list_of_project_files = [
f"{project_name}/__init__.py",
f"{project_name}/DATA_CONVERSION",
f"{project_name}/DATA_INGESTION",
f"{project_name}/DATA_RETRIVAL_GENERAION",
"static/style.css",
"template/chat.html"
"SETUP.py",
"app.py",
"requirements.txt",
".env"
]

for filepath in list_of_project_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath, "w") as f:
            pass


