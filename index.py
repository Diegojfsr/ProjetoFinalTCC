import pickle

import pandas as pd
from flask import Flask, render_template, request

# molezinha, só tem que setar as pastas de template e assets
app = Flask(__name__, template_folder='template', static_folder='template/assets')

# Treina lá, usa cá
modelo_pipeline = pickle.load(open('./models/model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/dados_cliente')
def dados_cliente():
    return render_template("form.html")

# Orden colunas na rede
# 	idade	renda	propriedadeCasa	tempoEmpregado	intensaoInvestimento valorInvestimento	taxaJuros	retornoInvestimento	tempoInvestimento

### Valores para teste ####
# 24,83000,ALUGUEL,8.0,PERSONAL,A,35000,8.9,1,0.42,N,2
# 24,78956,ALUGUEL,5.0,MÉDICO,B,35000,11.11,1,0.44,N,4
# 23,65500,ALUGUEL,4.0,MÉDICO,C,35000,15.23,1,0.53,N,2
# 21,10000,PRÓPRIO,6.0,RISCO,D,1600,14.74,1,0.16,N,3
# 26,108160,ALUGUEL,4.0,EDUCAÇÃO,E,35000,18.39,1,0.32,N,4
# 23,92111,ALUGUEL,7.0,MÉDICO,F,35000,20.25,1,0.32,N,4
# 23,56000,ALUGUEL,8.0,MÉDICO,G,21600,21.21,1,0.39,Y,4
### ----------------- ###

def get_data():
    idade = request.form.get('idade')
    renda = request.form.get('renda')
    propriedadeCasa = request.form.get('propriedadeCasa')
    tempoEmpregado = request.form.get('tempoEmpregado')
    intensaoInvestimento = request.form.get('intensaoInvestimento')
    valorInvestimento = request.form.get('valorInvestimento')
    taxaJuros = request.form.get('taxaJuros')
    retornoInvestimento = request.form.get('retornoInvestimento')
    tempoInvestimento = request.form.get('tempoInvestimento')


    d_dict = {'idade': [idade], 'renda': [renda], 'propriedadeCasa': [propriedadeCasa],
              'tempoEmpregado': [tempoEmpregado], 'intensaoInvestimento': [intensaoInvestimento],
              'valorInvestimento': [valorInvestimento], 'taxaJuros': [taxaJuros], 
              'retornoInvestimento': [retornoInvestimento], 'tempoInvestimento': [tempoInvestimento]}

    return pd.DataFrame.from_dict(d_dict, orient='columns')



@app.route('/send', methods=['POST'])
def show_data():
    df = get_data()
    df = df[['idade', 'renda', 'propriedadeCasa', 'tempoEmpregado', 'intensaoInvestimento',
       'valorInvestimento', 'taxaJuros', 'retornoInvestimento', 'tempoInvestimento']]

    # Acessa o primeiro elemento da previsão
    prediction = modelo_pipeline.predict(df)[0]
    
    if prediction == 0:
        outcome = 'A'
        imagem = 'Conservador.png'
    elif prediction == 1:
        outcome = 'B'
        imagem = 'Conservador.png'
    elif prediction == 2:
        outcome = 'C'
        imagem = 'Moderado.png'
    elif prediction == 3:
        outcome = 'D'
        imagem = 'Moderado.png'
    elif prediction == 4:
        outcome = 'F'
        imagem = 'conservador.png'
    elif prediction == 5:
        outcome = 'G'
        imagem = 'conservador.png'
    elif prediction == 6:
        outcome = 'H'
        imagem = 'conservador.png'
    elif prediction == 7:
        outcome = 'I'
        imagem = 'conservador.png'

    return render_template('result.html', tables=[df.to_html(classes='data', header=True, col_space=10)], 
                           result=outcome, imagem=imagem)


if __name__ == '__main__':
    app.run(debug=True)





    #variavel prediction recebe o modelo treinado, fazendo predicao no df com dados recebidos do form.

#     prediction = modelo_pipeline.predict(df) 
    
#     if prediction == 0:
#         outcome = 'A'
#         imagem = 'Conservador.png'

#     if prediction == 1:
#         outcome = 'B'
#         imagem = 'Conservador.png'

#     if prediction == 2:
#         outcome = 'C'
#         imagem = 'Moderado.png'

#     if prediction == 3:
#         outcome = 'D'
#         imagem = 'Moderado.png'

#     if prediction == 4:
#         outcome = 'E'
#         imagem = 'conservador.png'

#     if prediction == 5:
#         outcome = 'F'
#         imagem = 'conservador.png'

#     if prediction == 6:
#         outcome = 'G'
#         imagem = 'conservador.png'

#     if prediction == 7:
#         outcome = 'H'
#         imagem = 'conservador.png'



#     return render_template('result.html', tables=[df.to_html(classes='data', header=True, col_space=10)], 
#                            result=outcome, imagem=imagem)


# if __name__ == "__main__":
#     app.run(debug=True)
