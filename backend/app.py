from flask import Flask
from flask_cors import CORS
from extensions import db
from route.routes import api
from config import Config, TestConfig

app = Flask(__name__, static_folder="../frontend/src", template_folder="../frontend/index.html")
app.config.from_object(TestConfig)
app.config.from_object(Config)
# Enable CORS
CORS(app)

# Initialize the database
db.init_app(app)

# Register the API blueprint
app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")
    app.run(debug=True)