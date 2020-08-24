# Flask-Skeleton
Branch **base**: Flask, Peewee, Blueprints  
Branch **base-api**: Flask, Peewee, Flask-Restful  
Branch **cms-core**: Flask, Peewee, Flask-Security  
Branch **cms**: **cms-core**, Flask-Admin
  
## Install
```bash
$ git clone git@github.com:mariofix/flask-skeleton.git my-project  
$ cd my-project  
$ git ch [-b] [base|base-api]  
$ git pull github [base|base-api]  
$ poetry install  
```  
Optional:
```bash
$ git remote rename origin github
```

## Run
```bash
$ poetry run flask run
```