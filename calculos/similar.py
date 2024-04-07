from math import sqrt

def calcula_similaridade(pesos_docs: dict[ str, list], pesos_consulta :  dict[str, list]):

    array_sim = []
    for chave, valor in pesos_docs.items():
        temp = 0 
        sim = 0
        quadradod = 0
        quadradoc = 0
        total_palavras = len(valor)
        for item in valor:
            doctemp = item['tf_idf']
            quadradotempo = doctemp ** 2
            quadradod += quadradotempo
            if(temp < total_palavras):
                contemp = pesos_consulta['consulta'][temp]['tf_idf']
                simtemp = doctemp * contemp
                raiztemp = contemp ** 2
                quadradoc += raiztemp
                sim += simtemp
            temp += 1


        result = sim / (sqrt(quadradod) * sqrt(quadradoc))
        # Adiciona o resultado da similaridade no array de similaridade
        array_sim.append({'doc': chave, 'sim': round(result, 4)})
        
    return array_sim