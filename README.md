# Frameworks-Skeleton  
Branch **flask-admin-minimal**: Flask, Flask-Admin. as extension  
Branch **flask-admin**: Flask, Flask-Admin, Flask-Migrate, Flask-Security  
Branch **flask-admin-celery**: Flask, Flask-Admin, Flask-Migrate, Flask-Security, Celery (Not Available)  
Branch **flask-admin-async**: Quart, Flask-Admin (Not Available)  
Branch **django-code**: Django, Django Baton, Celery (Not Available)  

  
## Install
```bash
$ git clone https://github.com/mariofix/flask-skeleton.git -b branch my-project  
$ cd my-project  
$ rm .git/ -rfiv # Careful with this command, you can erase YOUR .git folder.
$ poetry install --with dev 
```  
Optional:
```bash
$ git remote rename origin github
```

## Run
```bash
$ poetry run flask run
```