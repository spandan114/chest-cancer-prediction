"""
Project Structure Generator Script

This script sets up the initial project structure for a CNN Classifier project.
It creates a standardized directory structure and required empty files for 
the ML project development.

Features:
    - Configures logging with timestamp and log level
    - Creates project directories and files if they don't exist
    - Establishes standard ML project structure including:
        * GitHub workflows
        * Source code directory with components, utils, config, etc.
        * Configuration files (config.yaml, params.yaml, dvc.yaml)
        * Setup and requirements files
        * Research and template directories
    - Logs the creation of directories and files
    - Skips existing files to prevent overwriting

The script uses pathlib for cross-platform path handling and ensures
all parent directories are created as needed.
"""

import os

from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File: {filepath} already exists")
