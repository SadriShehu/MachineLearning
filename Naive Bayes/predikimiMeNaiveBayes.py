# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:54:46 2018

@author: ssheh

Testimi i algoritmit te naiveBayes.py
"""
import csv

from naiveBayes import naiveBayes

reader = csv.DictReader(open('DataFrameTest.csv'))

k = naiveBayes(shteguDataBaze = "DataFrame.csv", AtributiKlase = "AQI Category" )

k.kalkulo_propabilitetin_AtributitKlase()

for row in reader:
    k.hipoteza = row
    k.Kalkulo_propabilitetin_kushtezues(k.hipoteza)
    k.klasifiko()		
    print("\n\n")