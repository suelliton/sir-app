#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.models import Coleta
import time
import serial
import os
from bs4 import BeautifulSoup
import requests
import threading

          
coleta = Blueprint('coleta', __name__)
#comport = serial.Serial('/dev/ttyUSB2', 9600) 
liga = Blueprint('liga',__name__) 
@coleta.route('/')
@coleta.route('/home')

#executa script para dar permissoes a porta usbdo arduino
#a = os.system("/home/suelliton/sir.sh") 
#abre tunel http e https
#b = os.system("/home/suelliton/ngrok http 80")  
#fa requisicao a pagina localhost do ngrok para pegar a url

#page = requests.get("http://127.0.0.1:4040/status")
#trata a requisicao http em html
#soup = BeautifulSoup(page.content, 'html.parser')  
#transfrma a resposta html em string
#html_string = str(soup)
#extrai da string apenas os elementos pertencentes a url 
#http = html_string[3106:3130]
#print http
#requests.post("https://suelliton.pythonanywhere.com/url/",data={'url':http})




def home():
    return "Welcome to the Catalog Home."
 
 
<<<<<<< HEAD
class ColetaView(MethodView):
 
    def get(self, id=None, page=1):   
        


        
        try:
            comport = serial.Serial('/dev/ttyUSB0', 9600)    
            time.sleep(0.5) # Entre 1.5s a 2s      
=======
class ColetaView(MethodView): 
    def get(self, id=None, page=1):            
        try:
			
            comport = serial.Serial('/dev/ttyUSB0',9600)
            time.sleep(1.5)      
>>>>>>> 608589248e223e7cb29eae12dc6ece6e20fc6fd0
            PARAM_UMIDADE='t'            
            PARAM_ASCII_UMIDADE=str(chr(116))           
            comport.write(PARAM_UMIDADE)
            comport.write(PARAM_ASCII_UMIDADE)     		
            VALUE_SERIAL=str(comport.readline())
            VALUE_TEMPERATURA, VALUE_UMIDADE = VALUE_SERIAL.split(":")
            comport.close()                         

		                    

            return jsonify({"temperatura" : VALUE_TEMPERATURA,"umidade" :VALUE_UMIDADE})
        except Exception as e:
<<<<<<< HEAD

            return str(e)    
=======
            return str(e) 
>>>>>>> 608589248e223e7cb29eae12dc6ece6e20fc6fd0
 
    def post(self):       
        """ name = request.form.get('name')
        price = request.form.get('price')
        product = Product(name, price)
        db.session.add(product)
        db.session.commit()
        return jsonify({product.id: {
            'name': product.name,
            'price': str(product.price),
        }})"""
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return
 
    def delete(self, id):
        # Delete the record for the provided id.
        return
 
 
coleta_view =  ColetaView.as_view('coleta_view')
app.add_url_rule(
    '/coleta/', view_func=coleta_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/coleta/<int:id>', view_func=coleta_view, methods=['GET']
)


class LigaView(MethodView):
 
    def get(self, id=None, page=1):        
                   
       
        
        

        t = threading.Thread(target=liga_desliga_led,args=(1,))
        t.start()        
        return "funcionou"


liga_view =  LigaView.as_view('liga_view')
app.add_url_rule(
    '/liga/', view_func=liga_view, methods=['GET', 'POST']
)
            
<<<<<<< HEAD





def liga_desliga_led(v):


    if os.name == 'nt':
        try:
            # Criando a conexão com a controladora.
            conexao = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)
        except Exception as e:
            # Exibindo uma mensagem de erro genérica caso a conexão falhe.
            print('[!] Verifique se a porta COM está correta [!]')
        else:
        # Exibindo uma mensagem caso a conexão seja bem-sucedida e
        # exibindo em qual porta foi realizada a conexão.
            print('Conexão realizada na', conexao.name)
        # Caso o código não esteja sendo executado no Windows.
    else:
        try:
        # Verifique em qual porta a sua microcontroladora foi reconhecida.
            conexao = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)
        except Exception as e:
            print('[!] Verifique se a porta tty está correta [!]')
        else:
            print('Conexão realizada na', conexao.name)
    '''Método liga desliga led
    Este método cria um looping infinito onde são exibidas algumas
    opções (menu) ao usuário.

    Dependendo da escolha o código ligará ou desligará o LED
    do pino 13 e o led onboard da placa.

    :return: Nada é retornado.
    '''
    # Laço de repetição
    
    
            # menu que será exibido ao usuário.
    menu = """
    Opções disponíveis:
    1 - Ligar LED
    2 - Desligar LED
    3 - Sair
    """
        # Exibindo o menu no terminal.
    print(menu)

        # Input do usuário (entrada de dados),
        # Entrada de dados está sendo convertida para bytes porque
        # estamos utilizando Python 3.
    valor = v
        # Verificando se o valor digitado foi 1 ou 2.
        # Repare que no código do Arduino estamos utilizando esses valores
        # Para determinar se o sinal será **HIGH** ou **LOW**.
    if valor == b'1' or valor == b'2':
            # Enviando o valor digitado pelo usuário através da conexão serial.
            # Este valor será recebido na variável **leitura** do código do Arduino.
        conexao.write(valor)

            # Capturando o **Serial.print()** que é enviado do código do Arduino.
        resposta = conexao.readline()

            # Exibindo no terminal o que foi retornando pelo **Serial.print()**.
            # Estamos utilizando o **decode**, porque os dados recebidos estão em byte.
        print('Arduino retornou:', resposta.decode('utf-8'))

        # Se o valor digitado for 3 o programa é encerado.
    elif valor == b'3':
        print('[!] Programa finalizado [!]')
        sys.exit()

        # Qualquer valor diferente dos que estão no menu vem para o else.
    else:
        print('[!] Digite uma opção válida [!]')

    
=======
>>>>>>> 608589248e223e7cb29eae12dc6ece6e20fc6fd0
