# from os import system
# system('cls')
# diccionario = dict {'nombre':'Eugenio',
#             'edad': 23,
#             'Localidad':'Puerto del Rosario',
#             'coches':{'marca':'toyota',
#                         'matricula':'2567 opu'}}

# for alto in dict.item():
#     print (alto)

# for clave,valor in dict.item():
    
#     if type(valor)==dict:
#         print(f'Para la clave {clave} los valores son la marca{valor['marca']} y la matrícula es {valor['matricula']}')
#     else:
#         print(f'Para la clave {clave} el valor es {valor}')

dicc = {'nombre':'Karen',
        'apelldio':'Jurgens',
        'edad': 35,
        'ocupacion':'Peridodista'}

dicc['pais']='Alemania'

for cl, v in dicc.items():
    print(cl,v)