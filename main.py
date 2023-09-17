from flask import Flask, render_template

app = Flask(__name__)

# Dados fictícios de serviços de ar condicionado
servicos_ar_condicionado = [
    {
        'titulo': 'Instalação de Ar Condicionado',
        'descricao': 'Instalação de unidades de ar condicionado em residências e escritórios.'
    },
    {
        'titulo': 'Manutenção Preventiva',
        'descricao': 'Serviços regulares de manutenção para garantir o desempenho ideal do ar condicionado.'
    },
    {
        'titulo': 'Reparo de Ar Condicionado',
        'descricao': 'Reparo de unidades de ar condicionado com problemas.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', servicos=servicos_ar_condicionado)


if __name__ == '__main__':
    app.run(debug=True)
