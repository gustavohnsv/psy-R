import sys
import os
from pathlib import Path

def get_base_path() -> Path:
    """
    Get the base path of the application.
    
    If running as a frozen application (PyInstaller), returns the directory of the executable.
    If running as a script, returns the parent directory of the 'src' folder (project root).
    """
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return Path(sys.executable).parent
    else:
        # Running as script
        # This file is in src/app/utils/paths.py
        # We want the project root, which is 3 levels up from here (app/utils/paths.py -> app/utils -> app -> src -> root)
        # Actually, let's target the 'src' parent to be consistent with how we want to find 'data'
        # If we are in src/app/utils/paths.py:
        # .parent = src/app/utils
        # .parent.parent = src/app
        # .parent.parent.parent = src
        # .parent.parent.parent.parent = project root
        
        # Let's align with how main_controller was doing it:
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # documents_dir = os.path.abspath(os.path.join(current_dir, '..', 'data', 'documents'))
        
        # If we want the folder where 'data' is located:
        # In dev: project_root/src/app/data (or project_root/data? The previous code looked for ../data/documents relative to controller)
        # Controller is in src/app/controllers. ../data is src/app/data.
        
        # So we want the directory that contains 'app'.
        # In dev: src/
        # In frozen: dist/ (where the executable is)
        
        # Wait, the user wants: "creates a temp folder, i would want it the same folder as the app is and then create a template folder, the same as the final document, it should create a separate folder on the same as the app."
        
        # So:
        # Frozen: /path/to/dist/psy-r (executable)
        # Documents: /path/to/dist/documents
        # Templates: /path/to/dist/templates
        
        # Dev: /path/to/project/src/main.py
        # Documents: /path/to/project/data/documents (or src/app/data/documents?)
        
        # Let's look at the previous code in main_controller.py:
        # documents_dir = os.path.abspath(os.path.join(current_dir, '..', 'data', 'documents'))
        # current_dir is src/app/controllers
        # .. is src/app
        # ../data is src/app/data
        
        # So in dev, we want to target src/app/data? Or project root?
        # The user said "same folder as the app is".
        
        # Let's define get_base_path as the folder where we should store user-visible files.
        return Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

def get_app_dir() -> Path:
    """
    Returns the directory where the application executable or entry point script resides.
    This is where we want to create 'documents' and 'templates' folders in production.
    """
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    else:
        # In dev, use the project root
        return Path(__file__).resolve().parents[3]
