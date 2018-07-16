# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:54:46 2018

@author: ssheh

Testimi i algoritmit te naiveBayes.py
"""
import csv

from naiveBayes import naiveBayes

reader = csv.DictReader(open('TestOrigins.csv'))

k = naiveBayes(shteguDataBaze = "Origins.csv", AtributiKlase = "Buys_Computer" )

k.kalkulo_propabilitetin_AtributitKlase()

for row in reader:
    k.hipoteza = row
    k.Kalkulo_propabilitetin_kushtezues(k.hipoteza)
    k.klasifiko()		
    print("\n\n")