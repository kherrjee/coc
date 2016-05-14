from imagebattle import app
from imagebattle import db


if __name__ == '__main__':
    app.run(debug=True)

db.create_all()