import mysql.connector

# Configurações de conexão com o banco de dados
config = {
    'user': 'root',
    'password': 'Lafera97',
    'host': 'localhost',
    'database': 'teste',
    'raise_on_warnings': True
}

# Cria a conexão
conn = mysql.connector.connect(**config)

# Executa uma consulta
cursor = conn.cursor()
cursor.execute("SELECT * FROM agendamentos")
rows = cursor.fetchall()

# Processa os resultados
for row in rows:
    print(row)

# Fecha a conexão
cursor.close()
conn.close()



from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    dia = request.form['dia']
    horario = request.form['horario']
    mensagem = f"Olá! Gostaria de agendar um horário para {dia} às {horario}. Aguardo confirmação. Obrigado!"
    numero_barbeiro = "55(62)99433-3220"
    link_whatsapp = f"https://api.whatsapp.com/send?phone={urllib.parse.quote(numero_barbeiro)}&text={urllib.parse.quote(mensagem)}"
    return redirect(link_whatsapp)

if __name__ == '__main__':
    app.run()
 