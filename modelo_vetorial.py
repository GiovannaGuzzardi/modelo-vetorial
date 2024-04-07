import sys
from indice import indice_func
from calculos.pesos import calcula_pesos_docs, calcula_pesos_consulta
from consulta import consulta
from calculos.similar import calcula_similaridade
# Trabalho feito por:
# Giovanna Sara Lemos Guzzardi
# matrícula: 12121bsi261

# em caso de não fornecerem um argumento como entrada
if len(sys.argv) != 3:
    print("Por favor, forneça um caminho que leve a base de dados e um que leve a consulta.")
    sys.exit(1)

base_arquivo = sys.argv[1]
consulta_arquivo = sys.argv[2]

# chamando a função indice_func do arquivo indice.py
indice_array = indice_func(base_arquivo)
consulta_array = consulta(consulta_arquivo)

# calculo do tf-idf

pesos_docs = calcula_pesos_docs(indice_array)

pesos_consulta = calcula_pesos_consulta(consulta_array , indice_array)

# calculo da similaridade entre os documentos e a consulta

similaridade = calcula_similaridade(pesos_docs, pesos_consulta)

sorted_docs = sorted(similaridade, key=lambda x: x['sim'], reverse=True)

with open("resposta.txt", "w") as arquivo_saida:
    cont = 0
    for item in sorted_docs:
        if item['sim'] >= 0.001:
            cont += 1
    arquivo_saida.write(f"{cont}\n")
    for item in sorted_docs:
        if item['sim'] >=  0.001:
            arquivo_saida.write(f"{item['doc']} {item['sim']}\n") 

