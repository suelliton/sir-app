#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.models import Coleta
import time
import serial


comport = serial.Serial('/dev/ttyUSB0',9600)     
coleta = Blueprint('coleta', __name__)
liga = Blueprint('liga',__name__) 
desliga = Blueprint('desliga',__name__)
@coleta.route('/')
@coleta.route('/home')

def home():
    return "Welcome to the Catalog Home."
 
 
class ColetaView(MethodView): 
    def get(self, id=None, page=1):            
        try:
            
            #comport = serial.Serial('/dev/ttyUSB0',9600)
            time.sleep(1.5)      
            PARAM_COLETA='t'            
            PARAM_ASCII_COLETA=str(chr(116))           
            comport.write(PARAM_COLETA)
            comport.write(PARAM_ASCII_COLETA)          
            VALUE_SERIAL=str(comport.readline())
            VALUE_TEMPERATURA, VALUE_UMIDADE = VALUE_SERIAL.split(":")
            #comport.close()                         
                            

            return jsonify({"temperatura" : VALUE_TEMPERATURA,"umidade" :VALUE_UMIDADE})
        except Exception as e:
            return str(e) 
 
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
       
        try:
            #comport = serial.Serial('/dev/ttyUSB0',9600)
            time.sleep(1.5)      
            PARAM_LIGAR='1'           
            PARAM_ASCII_LIGAR=str(chr(49))           
            comport.write(PARAM_LIGAR)
            comport.write(PARAM_ASCII_LIGAR)                                  
            #comport.close()  
            return "Ligado"                   
        except Exception as e:
            return str(e)    

liga_view =  LigaView.as_view('liga_view')
app.add_url_rule(
    '/liga/', view_func=liga_view, methods=['GET', 'POST']
)
        


class desligaView(MethodView): 
    def get(self, id=None, page=1):    
       
        try:
            #comport = serial.Serial('/dev/ttyUSB0',9600)
            time.sleep(1.5)      
            PARAM_DESLIGAR='2'           
            PARAM_ASCII_DESLIGAR=str(chr(50))           
            comport.write(PARAM_DESLIGAR)
            comport.write(PARAM_ASCII_DESLIGAR)                                  
            #comport.close()     
            return "Desligado"                
        except Exception as e:
            return str(e)    

desliga_view =  desligaView.as_view('desliga_view')
app.add_url_rule(
    '/desliga/', view_func=desliga_view, methods=['GET', 'POST']
)

