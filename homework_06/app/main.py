import os
from flask_bootstrap import Bootstrap
from flask import Flask
from flask_migrate import Migrate
from views.index import index_app
from views.about import about_app
from views.users import users_app
from views.posts import posts_app
from models import db


app = Flask(__name__)

bootstrap = Bootstrap(app)

app.register_blueprint(index_app, url_prefix="/")
app.register_blueprint(about_app, url_prefix="/about")
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(posts_app, url_prefix="/posts")

CONFIG_OBJ_PATH = "config.{}".format(os.getenv("CONFIG", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJ_PATH)

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            debug=app.config["DEBUG"],
            port=app.config["PORT"])