from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from courses.routes import courses_bp

    app.register_blueprint(courses_bp, url_prefix='/api/courses')

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(error='Not found'), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(error='Bad request'), 400

    @app.errorhandler(409)
    def conflict(error):
        return jsonify(error='Conflict'), 409

    @app.route('/api/')
    def health_check():
        return jsonify(message='Course Management API is running')

    return app


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)