import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s: %(levelname)s]:%(message)s")

while True:
    project_name = input("Enter project name ")
    if project_name != '':
        break
    
logging.info(f"create project by name:{project_name}")

#list of files:

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh", ## to setup conda environment
    "requirements.txt",
    "requirements_dev.txt", ## for installing requirements for tests
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split((filepath))
    if filedir != "":
        os.makedirs(filedir, exist_ok =True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename} ")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file at: {filepath} for file: {filename}")
    else:
        logging.info(f"file is already present at: {filepath}")