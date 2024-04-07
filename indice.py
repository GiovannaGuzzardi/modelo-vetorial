import spacy

def indice_func(base: str):
    # carrega o modelo do spaCy
    nlp = spacy.load("pt_core_news_lg")

    #obtem o caminho de todos os arquivos
    with open(base, "r") as file:
        BaseCaminho  = file.readlines()


    # array com base estruturada onde é separada em caminho e texto de cada documento
    documentos = []


    for i, doc in enumerate(BaseCaminho, start=1):
        caminho_arquivo = doc.strip()
        temp =  open( caminho_arquivo, "r" ).read()
        documentos.append({"documento": i , "caminho": caminho_arquivo,  "texto": temp})

    basetext = ""

    for doc in documentos:
        basetext += doc["texto"]
    doc = nlp(basetext)


    indice_invertido_sem_value = sorted(set([ t.lemma_ for t in doc if not (t.is_stop or t.is_punct or t.is_space)]))

    # cria arquivo de indice invertido
    indice_invertido = []
    # cria array de indice completa
    indice_format = {'indice' :[] , "qtdDoc": documentos.__len__()}

    for t in indice_invertido_sem_value:
        current_term_info = {"palavra": t, "ocorrencias": 0, 'documentos': []}
        indice_invertido.append({t: ""})
        for j in documentos:

            format = nlp(j['texto'])
            temp_format = sorted([ y.lemma_ for y in format if not (y.is_stop or y.is_punct or y.is_space)])

            if t in temp_format:
                # adiciona a quantidade de vezes que a palavra aparece no documento e em cada documento
                current_term_info["ocorrencias"] += 1
                current_term_info["documentos"].append({'doc': str(j['documento']), 'caminho' : j['caminho'] , 'ocorrencias': temp_format.count(t)})

                # adiciona o documento e a quantidade de vezes que a palavra aparece no documento de acordo com a formatação necessária no arquivo
                indice_invertido[-1][t] +=str(j['documento'])
                indice_invertido[-1][t] += ","
                indice_invertido[-1][t] +=str(temp_format.count(t))
            else :
                current_term_info["documentos"].append({'doc': str(j['documento']),'caminho' : j['caminho'],  'ocorrencias': 0})
        indice_format['indice'].append(current_term_info)

    with open("indice.txt", "w") as arquivo_saida:
        for entrada in indice_invertido:
            palavra = list(entrada.keys())[0]
            indice = entrada[palavra]
            arquivo_saida.write(f"{palavra}: {indice}")
            arquivo_saida.write("\n")
    
    return indice_format
            







    







