import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    'requirements.txt', 
    '.env', 
    'src/__init__.py', 
    'src/helper.py', 
    'src/prompts.py', 
    'setup.py', 
    'app.py'
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)
    
    # Check if the directory exists
    if filedir != '':
        if os.path.exists(filedir):
            logging.info(f'Directory {filedir} already exists. Proceeding with file creation...')
        else:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f'Created directory: {filedir}...')
    
    # Check if the file exists
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Created file: {filepath}...')
    else:
        logging.info(f'File {filepath} already exists...')