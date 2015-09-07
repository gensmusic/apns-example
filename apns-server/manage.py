import os
from app import create_app, db
from app.models import Identity
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('APNS_SERVER_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, Identity=Identity)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()