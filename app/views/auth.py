from flask import Blueprint, render_template, request, redirect, url_for
from ..models  import User, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        # Crie um novo objeto de usuário com as informações do formulário
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)

        # Adicione o novo usuário ao banco de dados
        db.session.add(new_user)
        db.session.commit()

        # Redirecione o usuário para a página de login após o registro bem-sucedido
        return redirect(url_for('auth.login'))

    # Renderize o template de registro
    return render_template('register.html')