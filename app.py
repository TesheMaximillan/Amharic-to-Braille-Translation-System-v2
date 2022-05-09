from routers.route import configure_routes
from flask import Flask


_author_ = 'Teshome Kurabachew'

app = Flask(__name__)
app.secret_key = 'super secret key'


configure_routes(app)

if __name__ == '__main__':
    app.run()