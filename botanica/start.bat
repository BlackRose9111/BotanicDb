start "" http://localhost:8000/
..\venv\Scripts\python.exe manage.py makemigrations
..\venv\Scripts\python.exe manage.py migrate
..\venv\Scripts\python.exe manage.py runserver 8000
pause