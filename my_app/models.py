#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_app import db
 
class Coleta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float(asdecimal=True))
    umidade = db.Column(db.Float(asdecimal=True))
 
    def __init__(self, temperatura, umidade):
        self.temperatura = temperatura
        self.umidade = umidade
 
    def __repr__(self):
        return '<Coleta %d>' % self.id