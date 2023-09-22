# Arquivo criado somente para a criação do banco de dados, pode excluir no final

from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()