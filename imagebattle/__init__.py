from flask import Flask

app = Flask(__name__)
app.config.from_object('imagebattle.config')

from . import hooks  # noqa
from .import views  # noqa

<<<<<<< HEAD
db = SQLAlchemy(app)
=======
db = SQLAlchemy(app)
>>>>>>> 7e16aa5c71b24291e38f062f37d728ad4a14b646
