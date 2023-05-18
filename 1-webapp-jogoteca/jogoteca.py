from flask import Flask, render_template, request

app = Flask(__name__)


class Jogo:
    def __init__(self, nome: str, categoria: str, console: str):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1: Jogo = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2: Jogo = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3: Jogo = Jogo('Honkai Star Rail', 'Estratégia', 'PC/PS5/Mobile')
lista: [str] = [jogo1, jogo2, jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/formulario')
def formulario():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/cadastrar', methods=['POST', ])
def cadastrar():
    nome: str = request.form['nome']
    categoria: str = request.form['categoria']
    console: str = request.form['console']
    jogo: Jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run(debug=True)
