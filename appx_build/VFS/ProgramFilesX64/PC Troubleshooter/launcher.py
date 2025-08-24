#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def main():
    # Get the directory where this launcher is located
    launcher_dir = Path(__file__).parent
    main_script = launcher_dir / "main.py"
    
    if main_script.exists():
        # Change to the application directory
        os.chdir(launcher_dir)
        
        # Execute the main script
        subprocess.run([sys.executable, str(main_script)])
    else:
        print(f"Error: main.py not found in {launcher_dir}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
