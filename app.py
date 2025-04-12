from flask import Flask, render_template, request, redirect, session as flask_session
from database import User, Contato, session
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)



@app.route('/')
def home():
    if 'user_id' not in flask_session:
        return redirect('/login')
    
    user_id = flask_session['user_id']
    contatos = session.query(Contato).filter_by(user_id=user_id).all()
    return render_template('home.html', contatos=contatos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        user = session.query(User).filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flask_session['user_id'] = user.id
            return redirect('/')
        else:
            error = "Login falhou! Verifique suas credenciais ou cadastre-se apertando ok."
            return render_template('login.html', error=error)

    return render_template('login.html')




@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST': 
        username = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        session.add(new_user)
        session.commit()
        return redirect('/login')
    return render_template('registro.html')



@app.route('/salvar_contato', methods=['GET', 'POST'])
def salvar_contato():
    novo_contato = {
        'Nome': request.form['nome'],
        'Email': request.form['email'],
        'Telefone': request.form['telefone'],
        'Tag': request.form['tags']
    }

    contatos.append(novo_contato)

    return redirect('/home')


@app.route('/deletar_contato', methods=['GET', 'POST'])
def deletar_contato():
    email = request.form['email']
    for contato in contatos:
        if contato['Email'] == email:
            contatos.remove(contato)
            break

    return redirect('/home')


@app.route('/editar_contato', methods=['GET', 'POST'])
def editar_contato():
    email = request.form['email']
    for contato in contatos:
        if contato['Email'] == email:
            contato['Nome'] = request.form['nome']
            contato['Telefone'] = request.form['telefone']
            contato['Tag'] = request.form['tags']
            break

    return redirect('/home')

app.run(debug=True)




