import math

def tf ( frequencia: int): 
    if frequencia >= 1:
        return 1 + math.log10(frequencia)
    else:
        return 0

def idf ( qtd_doc_total_com_palavra: int , qtd_doc_total: int): 
    return math.log10(qtd_doc_total / qtd_doc_total_com_palavra)

