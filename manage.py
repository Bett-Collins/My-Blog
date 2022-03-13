from app import create_app
from  flask_migrate import Migrate, MigrateCommand
from app.models import User
# ...


migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
#......