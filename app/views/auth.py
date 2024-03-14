from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Verifique se o email e a senha estão presentes no banco de dados
        user = User.query.filter_by(email=email, password=password).first()

        if user:
            # Se o usuário existir, defina uma variável de sessão para indicar que o usuário está logado
            session['user_id'] = user.id

            # Redirecione para a página do dashboard
            return redirect(url_for('dashboard.dashboard'))

        else:
            # Se as credenciais estiverem incorretas, exiba uma mensagem de erro
            return 'Credenciais inválidas. Por favor, tente novamente.'

    return render_template('login.html')

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # Obtenha os dados do formulário
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        if first_name and last_name and email and password and password_confirm:
            # Crie um novo usuário com os dados do formulário
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)

            # Adicione o novo usuário ao banco de dados
            db.session.add(new_user)
            db.session.commit()

            print(f'Nome: {first_name} {last_name}')
            print(f'E-mail: {email}')
            print(f'Senha: {password}')
            print(f'Confirmação de senha: {password_confirm}')

            # Redirecione para uma página de confirmação ou outra página
            return redirect(url_for('auth.login'))
        else:
            return 'Por favor, preencha todos os campos do formulário.'

    return render_template('register.html')
