from flask import Flask
from app.routes import init_app
from app.config import TEMPLATES, STATIC


app = Flask(
    __name__,
    template_folder=TEMPLATES,
    static_folder=STATIC
)

if __name__ == "__main__":
    init_app(app)
    print(app.url_map)
    app.run(debug=True)
