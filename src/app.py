from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configurações do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'usuario'
app.config['MYSQL_PASSWORD'] = 'senha'
app.config['MYSQL_DB'] = 'banco_de_dados'

mysql = MySQL(app)

# Rota inicial
@app.route("/")
def pagina_inicial():
    return render_template('index.html')


# Rota para criar um projeto
@app.route('/criar_projeto', methods=['POST'])
def criar_projeto():
    if request.method == 'POST':
        project_name = request.form['projeto_nome']
        # Inserir os dados do projeto no banco de dados

# Rota para criar uma tarefa
@app.route('/criar_task', methods=['POST'])
def criar_task():
    if request.method == 'POST':
        task_name = request.form['task_nome']
        task_points = request.form['task_pontos']
        project_id = request.form['projeto_id']
        # Inserir os dados da tarefa no banco de dados

#Rota para editar uma tarefa 
@app.route('/editar_task', methods=['POST'])
def editar_task():
    if request.method == "POST":
        task_id=request.form["task_id"]

# Rota para marcar uma tarefa como completa
@app.route('/completar_task/<int:task_id>')
def completar_task(task_id):
    return null #?
    # Atualizar o status da tarefa no banco de dados

# Rota para gerar o gráfico burndown
@app.route('/burndown_chart/<int:project_id>')
def burndown_chart(project_id):
        return null #?
    # Consultar dados do banco de dados e gerar o gráfico burndown

if __name__ == '__main__':
    app.run(debug=True)
