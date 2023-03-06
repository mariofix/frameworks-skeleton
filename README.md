# Flask Admin Minimal  
To be used as a flask extension

  
## Install
```bash
$ git clone https://github.com/mariofix/flask-skeleton.git -b flask-admin-minimal admin_folder  
$ rm -rf admin_folder/.git # Remember to remove the git folder  
```  

## how to use
```python
from flask import Flask
from .admin_folder import admin

def create_app():
    app = Flask(__name__)
    admin.init_app(app)

    return app

```