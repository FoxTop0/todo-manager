@echo off

git clone https://github.com/FoxTop0/todo-manager.git
cd todo-manager

mkdir tests
echo. > main.py
echo. > storage.py
echo. > task_manager.py
echo. > validator.py
echo. > logger.py
echo. > tests\__init__.py
echo. > tests\test_storage.py
echo. > tests\test_task_manager.py
echo. > tests\test_validator.py

echo # Python > .gitignore
echo __pycache__/ >> .gitignore
echo *.pyc >> .gitignore
echo venv/ >> .gitignore
echo *.log >> .gitignore
echo tasks.json >> .gitignore

echo pytest>=7.0.0 > requirements.txt
echo pytest-cov>=4.0.0 >> requirements.txt

echo # Todo List Manager > README.md

git add .
git commit -m "Initial commit: project structure"
git push origin main

git checkout -b feature/validator
git push origin feature/validator
git checkout main

git checkout -b feature/logger
git push origin feature/logger
git checkout main

git checkout -b feature/storage
git push origin feature/storage
git checkout main

git checkout -b feature/task-manager
git push origin feature/task-manager
git checkout main

git checkout -b feature/user-interface
git push origin feature/user-interface
git checkout main

echo Все ветки созданы!
pause