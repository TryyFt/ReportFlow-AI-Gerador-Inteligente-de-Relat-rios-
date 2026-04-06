from flask import Flask, render_template, request

app = Flask(__name__)


def gerar_relatorio(texto):
    palavras = len(texto.split())
    linhas = len(texto.splitlines())
    resumo = texto[:200] + '...' if len(texto) > 200 else texto

    return {
        'palavras': palavras,
        'linhas': linhas,
        'resumo': resumo,
        'insight': 'O texto possui boa densidade de conteúdo para análise inicial.'
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    relatorio = None
    if request.method == 'POST':
        conteudo = request.form['conteudo']
        relatorio = gerar_relatorio(conteudo)
    return render_template('index.html', relatorio=relatorio)


if __name__ == '__main__':
    app.run(debug=True)