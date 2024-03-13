from flask_sqlalchemy import SQLAlchemy

# Crie uma instância do SQLAlchemy
db = SQLAlchemy()

# Defina o modelo de dados para a tabela de Ordens de Serviço
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    # Adicione mais colunas conforme necessário

    def __repr__(self):
        return f"Order('{self.title}')"

# Função para inicializar o banco de dados
def init_db(app):
    # Configura a aplicação Flask para usar o SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Altere o nome do banco de dados conforme necessário
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializa o SQLAlchemy com a aplicação Flask
    db.init_app(app)
    
    # Cria as tabelas no banco de dados, se elas não existirem
    with app.app_context():
        db.create_all()
