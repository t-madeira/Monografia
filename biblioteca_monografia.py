import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import itertools as its

import sklearn.metrics as mt
from sklearn import tree
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.utils import  shuffle
from sklearn.model_selection import cross_val_score




def isNumeric(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def ajustaIdade (idade, dadosTratadosMonografia, i):
    if idade == "cinquenta  anos":
        dadosTratadosMonografia.at[i, "idade"] = 50
    elif idade == "DEZENOVE":
        dadosTratadosMonografia.at[i, "idade"] = 19
    elif idade == "trinta dois anos":
        dadosTratadosMonografia.at[i, "idade"] = 32
    elif idade == "cinquenta anos":
        dadosTratadosMonografia.at[i, "idade"] = 50
    elif idade == "quarenta e nove anos":
        dadosTratadosMonografia.at[i, "idade"] = 49
    elif idade == "cinquenta e quatro":
        dadosTratadosMonografia.at[i, "idade"] = 54
    elif idade == "trinta e um anos":
        dadosTratadosMonografia.at[i, "idade"] = 31
    elif idade == "cinquenta e quatro":
        dadosTratadosMonografia.at[i, "idade"] = 54
    elif idade == "quarenta e dois anos":
        dadosTratadosMonografia.at[i, "idade"] = 42
    elif idade == "cinquenta anos":
        dadosTratadosMonografia.at[i, "idade"] = 50
    elif idade == "quarenta e nove-49":
        dadosTratadosMonografia.at[i, "idade"] = 49
    elif idade == "Cinquenta anos":
        dadosTratadosMonografia.at[i, "idade"] = 50
    elif idade == "quarenta e quatro anos":
        dadosTratadosMonografia.at[i, "idade"] = 44
    elif idade == "quarenta e 8 anos":
        dadosTratadosMonografia.at[i, "idade"] = 48
    elif idade == "cinquenta e um":
        dadosTratadosMonografia.at[i, "idade"] = 51
    elif idade == "quarenta e seis anos":
        dadosTratadosMonografia.at[i, "idade"] = 46
    elif idade == "quarenta e três anos":
        dadosTratadosMonografia.at[i, "idade"] = 43
    elif idade == "QUARENTA E DOIS  anos":
        dadosTratadosMonografia.at[i, "idade"] = 42
    elif idade == "quarenta e quatro":
        dadosTratadosMonografia.at[i, "idade"] = 44
    elif idade == "sessenta anos":
        dadosTratadosMonografia.at[i, "idade"] = 60
    elif idade == "23/09/1969":
        dadosTratadosMonografia.at[i, "idade"] = 44
    elif idade == "22- 11-1967":
        dadosTratadosMonografia.at[i, "idade"] = 46
    else:
        if idade == "1972":
            dadosTratadosMonografia.at[i, "idade"] = 41
        elif idade == "1961":
            dadosTratadosMonografia.at[i, "idade"] = 52
        elif idade == "1971":
            dadosTratadosMonografia.at[i, "idade"] = 42
        elif idade == "1954":
            dadosTratadosMonografia.at[i, "idade"] = 59
        elif idade == "1973":
            dadosTratadosMonografia.at[i, "idade"] = 40
        elif idade == "1969":
            dadosTratadosMonografia.at[i, "idade"] = 44
        elif idade == "1958":
            dadosTratadosMonografia.at[i, "idade"] = 55
        elif idade == "1961":
            dadosTratadosMonografia.at[i, "idade"] = 52
        elif idade == "1977":
            dadosTratadosMonografia.at[i, "idade"] = 36
        elif idade == "1963":
            dadosTratadosMonografia.at[i, "idade"] = 50
        else:
            dadosTratadosMonografia.at[i, "idade"] = idade[:2]

    return dadosTratadosMonografia

def ajustaTempoServico(tempo, dadosTratadosMonografia, i):
    if tempo == "dois":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "28 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 28

    elif tempo == "11anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 11

    elif tempo == "12anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "06 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 6

    elif tempo == "7anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "21 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 21

    elif tempo == "21 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 21

    elif tempo == "3 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "15 Anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "3anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "29 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 29

    elif tempo == "09 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 9

    elif tempo == "6 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 6

    elif tempo == "12 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "2 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "20 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "20anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "07 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "6 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 6

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "20 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "dois":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "oito anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "22 anos e 3 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "17 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "1 ano e 6 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "29 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 29

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "34 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 34

    elif tempo == "4 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "4 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "10anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "42 anos /      6 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 42

    elif tempo == "5 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "6 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 6

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "21 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 21

    elif tempo == "27 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 27

    elif tempo == "quase 5 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "15 escola e 3 meses Ong":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "1 ano":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "18 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 18

    elif tempo == "mais de 31 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 32

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "7 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "18 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 18

    elif tempo == "quatorze":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 14

    elif tempo == "8 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "14 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 14

    elif tempo == "6 anos incompleto":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 6

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "4 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "18 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 18

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "8 Anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "18 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 18

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "4 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "3 anos e 5 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "1 ano e 6 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "5 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "18 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 18

    elif tempo == "11 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 11

    elif tempo == "21 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 21

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "27 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 27

    elif tempo == "5 anos  e 1 ano na escola":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "5 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "14 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 14

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "9 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 9

    elif tempo == "9 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 9

    elif tempo == "05, anos como gestora, 16 anos  de regência.":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 21

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "menos de 1 ano.":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "01- 02- 2010":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "20 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "5 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "24 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 24

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "17 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "13 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 13

    elif tempo == "doze anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "7 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "cinco anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "6 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 6

    elif tempo == "12 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "17 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "13 (O)   e 20 (P)":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 33

    elif tempo == "quinze anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "15 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "20 (vinte)":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "20 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "mais ou menos 19 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 19

    elif tempo == "28 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 28

    elif tempo == "32 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 32

    elif tempo == "15   anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "26 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 26

    elif tempo == "23anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "quatro":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "32 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 32

    elif tempo == "4 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "24 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 24

    elif tempo == "12 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "22anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22

    elif tempo == "12 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "31 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 31

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "três anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "29 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 29

    elif tempo == "18 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 18

    elif tempo == "4 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "nan":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "22 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22

    elif tempo == "20 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "dez anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "10 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "12 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "quinze anos de serviço,":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "14 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 14

    elif tempo == "2 anos e 10 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "dezesseis":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "28 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 28

    elif tempo == "4 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "19 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 19

    elif tempo == "7 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "12 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "21 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 21

    elif tempo == "32 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 32

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "13 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 13

    elif tempo == "dezesete anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "24 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 24

    elif tempo == "2 anos na escola e 8 anos na prefeitura":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "20 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "20 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "13 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 13

    elif tempo == "24 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 24

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "13 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 13

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "dois anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "2ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "11 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 11

    elif tempo == "vinte e sete anos -27":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 27

    elif tempo == "vinte anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "27 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 27

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "7 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "11 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 11

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "24 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 24

    elif tempo == "27 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 27

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "27 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 27

    elif tempo == "7 anos    e   3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "5 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "vinte anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "22 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22

    elif tempo == "17 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "vinte e três anos de serviço":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "4 anos como professora":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "35 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 35

    elif tempo == "27 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 27

    elif tempo == "17 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "9 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 9

    elif tempo == "vinte dois":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22

    elif tempo == "35 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 35

    elif tempo == "sete ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "24 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 24

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "dois anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "25 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 25

    elif tempo == "29 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 29

    elif tempo == "26 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 26

    elif tempo == "22 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22

    elif tempo == "dezesete anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "5 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "22 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "quatro-04":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "11 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 11

    elif tempo == "25 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 25

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "20 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "quatro anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "15, 1":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "9 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 9

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "Aproximadamente 22":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22

    elif tempo == "22 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22

    elif tempo == "13 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 13

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "Quinze anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "30 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 30

    elif tempo == "22 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "meio ano":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "14 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 14

    elif tempo == "11 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 11

    elif tempo == "vinte anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "1 ano":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "20  e 32":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 32

    elif tempo == "1 ano e 6 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "3 anos e 6 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "+ 30":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 31

    elif tempo == "1 ano":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "9 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 9

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "5 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "28 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 28

    elif tempo == "um":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "32 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 32

    elif tempo == "14 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 14

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "05 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 5

    elif tempo == "aqui 7 anos, total 23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "4 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "10 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "1 ano e 3 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "15 anos de idade":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "14 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 14

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "Aproximadamente 20 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "2 (vinte sete) anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 27

    elif tempo == "trinta":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 30

    elif tempo == "12 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "17 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "aproximadamente doze anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "1 ano":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "ATB(15 anos) Professora (3 ANOS)":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 18

    elif tempo == "4 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "26 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 26

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "MAIS DE 40 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 41

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "9125 anos ou 25 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 25

    elif tempo == "18 meses como professora e 10 anos como secretária Escolar":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 11

    elif tempo == "1ano":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "sete anos na mesma escola":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "15 anos e seis meses.":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "27anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 27

    elif tempo == "14 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 14

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "6 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 6

    elif tempo == "vinte e oito anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 28

    elif tempo == "2 anos e 10 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "16 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 16

    elif tempo == "31 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 31

    elif tempo == "17 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "11 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 11

    elif tempo == "24 e 12 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "SETE ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "Na Escola Municipal Antônio Joaquim Vieira  , tenho 10 anos e na Escola do Estado tenho 16 anos de Magistério":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 26

    elif tempo == "18 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "30 dias":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "21 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 21

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "15anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "19 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 19

    elif tempo == "15 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "3 mêses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "25 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 25

    elif tempo == "1 ano e 1 mês":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "6meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "7 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "4 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "vinte sete":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 27

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "6 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 6

    elif tempo == "15 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "mais de 10 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 11

    elif tempo == "18 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 18

    elif tempo == "7 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 7

    elif tempo == "1 ano":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 1

    elif tempo == "2 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "19 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 19

    elif tempo == "3 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "10 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "23 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "6 (seis) anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 6

    elif tempo == "12 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 12

    elif tempo == "4 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 4

    elif tempo == "-":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    elif tempo == "vinte e tres":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 23

    elif tempo == "8 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 8

    elif tempo == "02 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "17 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "2 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "10 ANOS":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "13 anos e 1 mês":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 13

    elif tempo == "3 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 3

    elif tempo == "Na função de Supervisora 7 anos e como professora já aposentada 29 anos e 6 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 37

    elif tempo == "20 anos":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 20

    elif tempo == "9 anos e 6 meses":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 10

    elif tempo == "2011":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 2

    elif tempo == "1996":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 17

    elif tempo == "1998":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 15

    elif tempo == "1991":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 22
    elif tempo == " ":
        dadosTratadosMonografia.at[i, "tempodeservico"] = 0

    return dadosTratadosMonografia

def tratarValorAusenteTempoServico (dadosTratadosMonografia, i):
    idade = int(dadosTratadosMonografia.loc[i]["idade"])
    escolaridade = dadosTratadosMonografia.loc[i]["escolaridade"]
    media = 0
    contador = 1
    for j in dadosTratadosMonografia.index:
        if int(dadosTratadosMonografia.loc[j]["idade"]) > idade-5 and \
                int(dadosTratadosMonografia.loc[j]["idade"]) < idade+5 and \
                int(dadosTratadosMonografia.loc[j]["idade"]) != 0 and \
                dadosTratadosMonografia.loc[j]["escolaridade"] == escolaridade:
           # print (dadosTratadosMonografia.loc[j]["tempodeservico"], j)
           media += int(dadosTratadosMonografia.loc[j]["tempodeservico"])
           contador += 1
           # print("Idade:{} IdadeRange: {} Escolaridade: {} Tempo de servico: {}".format(idade, dadosTratadosMonografia.loc[j]["idade"],
           #                                                         dadosTratadosMonografia.loc[j]["escolaridade"], dadosTratadosMonografia.loc[j]["tempodeservico"]))
    return int(media/contador)

def ajustaColunasNominais(dadosTratadosMonografia):
    atributosNominais = ["sexo", "escolaridade"]
    # , "escolaridade", "estadocivil", "ocupacao", "religiao", "contatoanterior", "lidadiretamente",
    #                   "lida.onde", "materialdidatico", "prazoatividades", "interacaopares", "organizacaocurso",
    #                   "import.ajud.tutor", "autoavaliacao.x", "part.outrocurso",
    #                   "pp001", "pp002", "pp003", "pp004", "pp005", "pp006", "pp007", "pp008", "pp009", "pp010",
    #                   "pp011", "pp012", "pp013", "pp014", "pp015", "pp016", "pp017", "pp018", "pp019", "pp020",
    #                   "pp021", "pp022", "pp023", "pp024", "pp025", "pp026", "pp027", "pp028", "pp029", "pp030",
    #                   "pp031", "pp032", "pp033", "pp034", "pp035", "pp036", "pp037",
    #                   "motivopart", "barreiras", "facilitadores", "aprovado"

    for c in atributosNominais:
        novos_dados = pd.get_dummies(dadosTratadosMonografia[c])
        dadosTratadosMonografia = pd.concat([dadosTratadosMonografia, novos_dados], axis=1)

    # Converte colunas nominais em colunas de numericos
    for c in atributosNominais:
        le = LabelEncoder()
        le.fit(dadosTratadosMonografia[c].astype(str))
        dadosTratadosMonografia[c] = le.transform(dadosTratadosMonografia[c].astype(str))

    return dadosTratadosMonografia

def tratarValorAusenteEscolaridade(dadosTratadosMonografia):
    print("Registros com escolaridade ausente:")
    for i in indices:
        if dadosTratadosMonografia.loc[pegaIndex[i[0]]]["escolaridade"] == 0:
            aux = [dadosTratadosMonografia.loc[pegaIndex[i[1]]]["escolaridade"],
                   dadosTratadosMonografia.loc[pegaIndex[i[2]]]["escolaridade"]
                   ]
            np.asarray(aux)
            valorToSet = np.bincount(aux).argmax()
            print("\tRegistro: {} Vizinhos mais proximos: {}  Mais frequente: {}".format(
                dadosTratadosMonografia.loc[pegaIndex[i[0]]]["escolaridade"], aux, valorToSet))
            dadosTratadosMonografia.at[pegaIndex[i[0]], "escolaridade"] = valorToSet
    print("Escolaridades ausentes tratadas.")

    print("Adicionando atributo escolaridade à lista de atributos do KNN...")
    for a, i in zip(atributosKNN, dadosTratadosMonografia.index):
        a.append(dadosTratadosMonografia.loc[i]["escolaridade"])

    return dadosTratadosMonografia

def tratarMotivopartBarreiraFacilitadores(dadosTratadosMonografia):
    # motivopart
    dadosTratadosMonografia["Identificação pessoal com o tema"] = 0
    dadosTratadosMonografia["Identificação profissional com o tema"] = 0
    dadosTratadosMonografia["Para aquisição de conhecimento na área"] = 0
    dadosTratadosMonografia["Pelo fato de o curso ser gratuito"] = 0
    dadosTratadosMonografia["Pelo fato de o curso estar vinculado à Universidade"] = 0
    dadosTratadosMonografia["Por ser um curso à distância"] = 0
    dadosTratadosMonografia["Por ser uma oportunidade de formação continuada"] = 0

    # barreiras
    dadosTratadosMonografia["Ausência da família"] = 0
    dadosTratadosMonografia["Pouca comunicação com os pais"] = 0
    dadosTratadosMonografia["Uso de substâncias por familiares"] = 0
    dadosTratadosMonografia["Presença de drogas ilícitas no ambiente escolar"] = 0
    dadosTratadosMonografia["Proximidade da rede de distribuição de drogas"] = 0
    dadosTratadosMonografia["Ausência de limites dos alunos"] = 0
    dadosTratadosMonografia["Ausência de colaboração da equipe escolar"] = 0
    dadosTratadosMonografia["Ausência de regras no ambiente escolar"] = 0

    # facilitadores
    dadosTratadosMonografia["Possuir alunos interessados na temática"] = 0
    dadosTratadosMonografia["Presença de uma equipe para trabalhar a temática"] = 0
    dadosTratadosMonografia["Estímulo aos alunos"] = 0
    dadosTratadosMonografia["Desenvolvimento de projetos na escola"] = 0
    dadosTratadosMonografia["Apoio aos projetos em desenvolvimento"] = 0
    dadosTratadosMonografia["Presença de regras no ambiente escolar"] = 0
    dadosTratadosMonografia["Promoção de compromisso e confiança"] = 0
    dadosTratadosMonografia["Valorização do ambiente escolar"] = 0
    dadosTratadosMonografia["Participação da comunidade e dos pais no trabalho de prevenção"] = 0

    for i in dadosTratadosMonografia.index:
        if "Pelo fato de o curso ser gratuito".find(str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
            dadosTratadosMonografia.at[i, "Identificação pessoal com o tema"] = 1

        if "Identificação profissional com o tema".find(str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
            dadosTratadosMonografia.at[i, "Identificação profissional com o tema"] = 1

        if "Para aquisição de conhecimento na área".find(str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
            dadosTratadosMonografia.at[i, "Para aquisição de conhecimento na área"] = 1

        if "Pelo fato de o curso ser gratuito".find(str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
            dadosTratadosMonografia.at[i, "Pelo fato de o curso ser gratuito"] = 1

        if "Pelo fato de o curso estar vinculado à Universidade".find(
                str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
            dadosTratadosMonografia.at[i, "Pelo fato de o curso estar vinculado à Universidade"] = 1

        if "Por ser um curso à distância".find(str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
            dadosTratadosMonografia.at[i, "Por ser um curso à distância"] = 1

        if "Por ser uma oportunidade de formação continuada".find(
                str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
            dadosTratadosMonografia.at[i, "Por ser uma oportunidade de formação continuada"] = 1

        if "Ausência da família".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
            dadosTratadosMonografia.at[i, "Ausência da família"] = 1

        if "Pouca comunicação com os pais".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
            dadosTratadosMonografia.at[i, "Pouca comunicação com os pais"] = 1

        if "Uso de substâncias por familiares".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
            dadosTratadosMonografia.at[i, "Uso de substâncias por familiares"] = 1

        if "Presença de drogas ilícitas no ambiente escolar".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
            dadosTratadosMonografia.at[i, "Presença de drogas ilícitas no ambiente escolar"] = 1

        if "Proximidade da rede de distribuição de drogas".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
            dadosTratadosMonografia.at[i, "Proximidade da rede de distribuição de drogas"] = 1

        if "Ausência de limites dos alunos".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
            dadosTratadosMonografia.at[i, "Ausência de limites dos alunos"] = 1

        if "Ausência de colaboração da equipe escolar".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
            dadosTratadosMonografia.at[i, "Ausência de colaboração da equipe escolar"] = 1

        if "Ausência de regras no ambiente escolar".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
            dadosTratadosMonografia.at[i, "Ausência de regras no ambiente escolar"] = 1

        if "Possuir alunos interessados na temática".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
            dadosTratadosMonografia.at[i, "Possuir alunos interessados na temática"] = 1

        if "Presença de uma equipe para trabalhar a temática".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
            dadosTratadosMonografia.at[i, "Presença de uma equipe para trabalhar a temática"] = 1

        if "Estímulo aos alunos".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
            dadosTratadosMonografia.at[i, "Estímulo aos alunos"] = 1

        if "Desenvolvimento de projetos na escola".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
            dadosTratadosMonografia.at[i, "Desenvolvimento de projetos na escola"] = 1

        if "Apoio aos projetos em desenvolvimento".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
            dadosTratadosMonografia.at[i, "Apoio aos projetos em desenvolvimento"] = 1

        if "Presença de regras no ambiente escolar".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
            dadosTratadosMonografia.at[i, "Presença de regras no ambiente escolar"] = 1

        if "Promoção de compromisso e confiança".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
            dadosTratadosMonografia.at[i, "Promoção de compromisso e confiança"] = 1

        if "Valorização do ambiente escolar".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
            dadosTratadosMonografia.at[i, "Valorização do ambiente escolar"] = 1

        if "Participação da comunidade e dos pais no trabalho de prevenção".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
            dadosTratadosMonografia.at[i, "Participação da comunidade e dos pais no trabalho de prevenção"] = 1

    return dadosTratadosMonografia


def criaMatrizConfusao(x, y, modelo):
    # Matriz de confusao

    # calcula e imprime a matriz de confusao
    predito = modelo.predict(x)
    matriz = mt.confusion_matrix(y, predito)

    # normaliza a matriz de confusao e gera grafico
    matriz = matriz / matriz.sum(axis=1)[:, np.newaxis]
    print(matriz)
    # Matriz de confusao
    # calcula e imprime a matriz de confusao
    predito = modelo.predict(x)
    matriz = mt.confusion_matrix(y, predito)

    # normaliza a matriz de confusao e gera grafico
    matriz = matriz / matriz.sum(axis=1)[:, np.newaxis]
    print(matriz)
    cmap = plt.cm.Blues
    plt.imshow(matriz, interpolation='nearest', cmap=cmap)
    plt.colorbar()

    # iclasses = np.arange(len(iris.target_names))
    iclasses = np.arange(2)

    aux = ["~BP", "BP"]

    plt.xticks(iclasses, aux, rotation=45)
    plt.yticks(iclasses, aux)
    limiarCor = matriz.max() / 2.
    for i, j in its.product(range(matriz.shape[0]), range(matriz.shape[1])):
        plt.text(j, i, format(matriz[i, j], '.2f'),
                 horizontalalignment="center",
                 color="white" if matriz[i, j] > limiarCor else "black")
    plt.tight_layout()
    plt.ylabel('Valores Esperados')
    plt.xlabel('Valores Preditos')
    plt.show()
    plf.clf()


