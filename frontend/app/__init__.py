from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)

app.config.from_object('config')

csrf = CSRFProtect(app)
csrf.init_app(app)


from .views import movimentacoes_view