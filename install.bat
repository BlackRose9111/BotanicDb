rm \rf venv
python -m venv venv
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\pip.exe install -r requirements.txt
venv\Scripts\pip cache purge
venv\Scripts\python.exe manage.py makemigrations
venv\Scripts\python.exe manage.py migrate
echo "Installation is completed, run start.bat to start the application."
pause
