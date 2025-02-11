import os
import sys
import subprocess
import venv

# If not in a virtual environment, create one and re-launch the script.
if sys.prefix == sys.base_prefix:
    venv_dir = os.path.join(os.path.dirname(__file__), 'venv')
    if not os.path.exists(venv_dir):
        print("Creating virtual environment...")
        builder = venv.EnvBuilder(with_pip=True)
        builder.create(venv_dir)
    # Determine interpreter path according to OS.
    if os.name == 'nt':
        new_python = os.path.join(venv_dir, 'Scripts', 'python.exe')
    else:
        new_python = os.path.join(venv_dir, 'bin', 'python')
    print(f"Re-launching script using virtual environment interpreter: {new_python}")
    subprocess.check_call([new_python] + sys.argv)
    sys.exit()

# --- Now running inside the virtual environment ---

import pkg_resources  # Part of setuptools
import importlib.metadata  # For Python 3.8+

def install_packages():
    # List only external packages.
    # csv, json, and os are built-in and don't need installation.
    # Use the correct package name (e.g., "google-genai") for the genai library.
    required_packages = {"httpx", "python-dotenv", "google-genai", "pyodbc","google"}
    try:
        # Retrieve installed packages (names normalized to lower-case).
        installed = {pkg.key for pkg in pkg_resources.working_set}
    except Exception:
        installed = set()
    missing = required_packages - installed
    if missing:
        print("Installing missing packages:", ", ".join(missing))
        subprocess.check_call([sys.executable, "-m", "pip", "install", *list(missing)])
    else:
        print("All required packages are already installed.")

# Install packages if needed
install_packages()

# ...existing code...

def main():
    print("Running inside the virtual environment with required packages installed!")
    # ...existing code...

if __name__ == '__main__':
    main()
