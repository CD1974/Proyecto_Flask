import os

from flask import Flask, request, url_for, redirect, abort, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )

    from . import db
    
    # Inicializar la aplicación con los comandos personalizados
    db.init_app(app)
    
    @app.route('/hola')
    def hola():
        return 'Hello Moto'
    return app