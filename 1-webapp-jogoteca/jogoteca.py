from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome: str, categoria: str, console: str):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1: Jogo = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2: Jogo = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3: Jogo = Jogo('Honkai Star Rail', 'Estratégia', 'PC/PS5/Mobile')
listaJogos: [Jogo] = [jogo1, jogo2, jogo3]


class Usuario:
    def __init__(self, nome: str, nickname: str, senha: str):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario1: Usuario = Usuario('Gentil Silva', 'Denv3r', 'honkai')
usuario2: Usuario = Usuario('Camily Beleza', 'Mily', 'paozinho')
usuario3: Usuario = Usuario('Guilherme Louro', 'Cake', 'python_eh_vida')
listaUsuarios: dict = {usuario1.nickname: usuario1, usuario2.nickname: usuario2, usuario3.nickname: usuario3}


app = Flask(__name__)
app.secret_key = 'alura'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=listaJogos)


@app.route('/novo')
def formulario():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('formulario')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/cadastrar', methods=['POST', ])
def cadastrar():
    nome: str = request.form['nome']
    categoria: str = request.form['categoria']
    console: str = request.form['console']
    jogo: Jogo = Jogo(nome, categoria, console)
    listaJogos.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima: str = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in listaUsuarios:
        usuario = listaUsuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina: str = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Usuario não logado')
            return redirect(url_for('login'))
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado']: session = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)
