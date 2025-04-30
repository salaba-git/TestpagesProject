### how to setup project with pyCharm
# 1. clone the project from git
Git > Clone
# 2. within project settings select Python interpreter (this will create .venv folder)
Settings > Pythin interpreter > Add interpreter > Add Local interpreter

### how to setup project using terminal
# 1. clone the project from git repository
git clone <Project A> # Cloning project repository
# 2. create virtual environment within the cloned project (remember to use the desired python3 version)
cd <Project A> # Enter to project directory
python3 -m venv my_venv # If not created, creating virtualenv

### working with virtualenv and managing requirements
# 3. activate virtualenv
source ./my_venv/bin/activate # Activating virtualenv
# 4. install dependencies from requirements.txt file (if exists)
(my_venv)$ pip3 install -r ./requirements.txt # Installing dependencies
# 5. deactivate virtualenv
(my_venv)$ deactivate # When you want to leave virtual environment

### how to create requirements.txt using terminal
(my_venv)$ pip3 freeze > requirements.txt