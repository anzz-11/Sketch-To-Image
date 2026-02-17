import subprocess
import webbrowser
import time
import os

# === PATHS (edit only if your folders change) ===
BACKEND_DIR = r"C:\Users\VIVOBOOK 14\Desktop\cp\backend"
VENV_PYTHON = os.path.join(BACKEND_DIR, "venv", "Scripts", "python.exe")

HTML_DRAW = r"C:\Users\VIVOBOOK 14\Desktop\cp\frontend\draw.html"
HTML_RES = r"C:\Users\VIVOBOOK 14\Desktop\cp\frontend\result.html"

# === Start FastAPI backend ===
subprocess.Popen(
    [VENV_PYTHON, "-m", "uvicorn", "main:app", "--reload"],
    cwd=BACKEND_DIR,
    shell=True
)

# Wait a bit for server to start
time.sleep(3)

# === Open frontend HTML files ===
webbrowser.open(f"file:///{HTML_DRAW}")
time.sleep(1)  # small delay so browsers don't fight
webbrowser.open(f"file:///{HTML_RES}")

print("✅ Backend started and both frontend pages opened")