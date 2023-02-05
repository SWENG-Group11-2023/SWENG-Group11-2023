# Backend Information

## Setting up python virtual environment (Venv) for backend
1. Install python 3.10 if not yet installed and CD to backend directory
2. run `pip install virtualenv`
3. run `virtualenv venv`
4. run `.\venv\Scripts\activate`
5. run `pip install -r requirements.txt`
6. When you have installed a new pip package run: `pip freeze > requirments.txt` from the backend root directory to update requirements file so that everyone can get easily install the new package.

**If you are getting an error on a package not being found run step 8 before trying anything else**

To exit the virtual environnement you can run `deactivate` and to reactivate use same command as step 4
**Make sure to reactivate venv before working in the project again**
