import spacy

# consulta_w = {'palavra': 'w' , 'frequencia' : 1 }

def consulta(caminho : str):
    nlp = spacy.load("pt_core_news_lg")

    with open(caminho, "r") as file:
        BaseCaminho  = file.readlines()

    consulta_list = []

    basetext = ""
    for item  in BaseCaminho: 
        basetext += item
    
    doc = nlp(basetext)

    indice_invertido_sem_value = sorted(set([ t.lemma_ for t in doc if not (t.is_stop or t.is_punct or t.is_space)]))

    for t in indice_invertido_sem_value:
        consulta_list.append({'palavra': t , 'frequencia' : basetext.count(t)})

    return(consulta_list)