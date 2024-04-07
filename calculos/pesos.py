from .tf_idf import  idf, tf

def calcula_idf_palavras( qtd_doc_total , frequencia_palavras ):
    idf_p = {}
    for palavra_info in frequencia_palavras:
        qtd_doc_total_com_palavra = palavra_info["ocorrencias"]
        idf_p[palavra_info['palavra']] = idf(qtd_doc_total_com_palavra,qtd_doc_total)
    
    return idf_p

def calcula_pesos_docs(infos: dict):

    # Preparando a estrutura de dados de saída
    pesos_docs = {doc["caminho"]: [] for palavra in infos["indice"] for doc in palavra["documentos"]}

    # Número total de documentos
    qtd_doc_total = infos["qtdDoc"]

    # Iterar sobre cada palavra para calcular IDF
    idf_p = calcula_idf_palavras(qtd_doc_total, infos["indice"])

    for palavra_info in infos["indice"]:
       
    # Iterar sobre cada documento onde a palavra aparece
        for doc in palavra_info["documentos"]:
            peso_tf_idf = tf(doc['ocorrencias']) * idf_p[palavra_info['palavra']]
            palavra_info['palavra']
            pesos_docs[doc["caminho"]].append({'palavra': palavra_info['palavra'] ,'tf_idf' : round(peso_tf_idf , 4)})
    
    # gera arquivo de pesos dos docs
    with open("pesos.txt", "w") as arquivo_saida:
        for nome_arquivo, pontuacoes in pesos_docs.items():
                # Escrevemos o nome do arquivo
                arquivo_saida.write(f"{nome_arquivo}: ")
                # Para cada par palavra-TF_IDF, escrevemos no arquivo
                for item in pontuacoes:
                    if item['tf_idf'] > 0:
                        arquivo_saida.write(f"{item['palavra']},{item['tf_idf']}  ")   
                # Adicionamos uma quebra de linha após cada lista de pontuações
                arquivo_saida.write("\n")

    # retorna o dicionário com os pesos tf-idf de cada documento ( { 'caminho1': [ {palavra: 'w', tf_idf: 0.0}, {palavra: 'y', tf_idf: 0.0}], 'caminho2': [ {palavra: 'w', tf_idf: 0.0}, {palavra: 'y', tf_idf: 0.0}]})
    return pesos_docs

def calcula_pesos_consulta(palavras , infos: dict): 

    qtd_doc_total = infos["qtdDoc"]
    pesos_consulta = {'consulta' : []}
    idf_p = calcula_idf_palavras(qtd_doc_total, infos["indice"])
    palavras_dict = {item['palavra']: item['frequencia'] for item in palavras}

    for palavra in idf_p:
        if palavra in palavras_dict:
            # Calcula o TF-IDF se a palavra está presente
            peso_tf_idf = tf(palavras_dict[palavra]) * idf_p[palavra]
            pesos_consulta['consulta'].append({'palavra': palavra, 'tf_idf': round(peso_tf_idf, 4)})
        else:
            # Atribui 0.0 se a palavra não estiver presente
            pesos_consulta['consulta'].append({'palavra': palavra, 'tf_idf': 0.0})

    # gera array de pesos da consulta ( [ {palavra: 'w', tf_idf: 0.0}, {palavra: 'y', tf_idf: 0.0}])
    return pesos_consulta