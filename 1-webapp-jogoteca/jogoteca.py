from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome: str, categoria: str, console: str):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio')
def ola():
    jogo1: Jogo = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2: Jogo = Jogo('God of War', 'Rack n Slash', 'PS2')
    jogo3: Jogo = Jogo('Honkai Star Rail', 'Estratégia', 'PC/PS5/Mobile')
    lista: [str] = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run()
