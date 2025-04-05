from flask import Flask, render_template

app = Flask(__name__)

contatos = [
    {'Nome': 'Ana Silva', 'Email': 'ana.silva@email.com', 'Telefone': '(85) 99999-1111', 'Tag': 'família'},
    {'Nome': 'Pedro Souza', 'Email': 'pedro.souza@email.com', 'Telefone': '(85) 98888-2222', 'Tag': 'trabalho'},
    {'Nome': 'Carla Rocha', 'Email': 'carla.rocha@email.com', 'Telefone': '(85) 97777-3333', 'Tag': 'amigos'},
    {'Nome': 'Lucas Mendes', 'Email': 'lucas.mendes@email.com', 'Telefone': '(85) 96666-4444', 'Tag': 'família'},
    {'Nome': 'Mariana Costa', 'Email': 'mariana.costa@email.com', 'Telefone': '(85) 95555-5555', 'Tag': 'trabalho'},
    {'Nome': 'Rafael Pereira', 'Email': 'rafael.pereira@email.com', 'Telefone': '(85) 94444-6666', 'Tag': 'amigos'},
    {'Nome': 'Juliana Lima', 'Email': 'juliana.lima@email.com', 'Telefone': '(85) 93333-7777', 'Tag': 'família'},
    {'Nome': 'Bruno Oliveira', 'Email': 'bruno.oliveira@email.com', 'Telefone': '(85) 92222-8888', 'Tag': 'trabalho'},
    {'Nome': 'Fernanda Santos', 'Email': 'fernanda.santos@email.com', 'Telefone': '(85) 91111-9999', 'Tag': 'amigos'},
    {'Nome': 'Gustavo Rodrigues', 'Email': 'gustavo.rodrigues@email.com', 'Telefone': '(85) 98765-4321', 'Tag': 'família'},
    {'Nome': 'Letícia Alves', 'Email': 'leticia.alves@email.com', 'Telefone': '(85) 91234-5678', 'Tag': 'trabalho'},
    {'Nome': 'Ricardo Gomes', 'Email': 'ricardo.gomes@email.com', 'Telefone': '(85) 99876-5432', 'Tag': 'amigos'},
    {'Nome': 'Patrícia Nunes', 'Email': 'patricia.nunes@email.com', 'Telefone': '(85) 92345-6789', 'Tag': 'família'},
    {'Nome': 'Marcelo Castro', 'Email': 'marcelo.castro@email.com', 'Telefone': '(85) 98765-9876', 'Tag': 'trabalho'},
    {'Nome': 'Camila Fernandes', 'Email': 'camila.fernandes@email.com', 'Telefone': '(85) 93456-7890', 'Tag': 'amigos'},
    {'Nome': 'Eduardo Vieira', 'Email': 'eduardo.vieira@email.com', 'Telefone': '(85) 97654-3210', 'Tag': 'família'},
    {'Nome': 'Isabela Barbosa', 'Email': 'isabela.barbosa@email.com', 'Telefone': '(85) 94567-8901', 'Tag': 'trabalho'},
    {'Nome': 'Thiago Martins', 'Email': 'thiago.martins@email.com', 'Telefone': '(85) 96543-2109', 'Tag': 'amigos'},
    {'Nome': 'Renata Cavalcante', 'Email': 'renata.cavalcante@email.com', 'Telefone': '(85) 95678-9012', 'Tag': 'família'},
    {'Nome': 'Vinicius Rocha', 'Email': 'vinicius.rocha@email.com', 'Telefone': '(85) 97890-1234', 'Tag': 'trabalho'}
]

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/home')
def home_page():
    return render_template('home.html',
                           contatos=contatos)



app.run(debug=True)




