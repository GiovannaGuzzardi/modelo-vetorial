# Sistema de Busca e Indexação de Documentos
Este projeto implementa um sistema de busca de texto que utiliza indexação invertida e TF-IDF (Term Frequency-Inverse Document Frequency) para recuperar documentos relevantes a partir de consultas de texto. O sistema é composto por três componentes principais: a criação de um índice invertido, o cálculo de pesos TF-IDF para termos nos documentos, e a execução de consultas para encontrar documentos relevantes.

## Rodando 
python modelo_vetorial.py base.txt consulta2.txt

## Componentes
1. Índice Invertido
O índice invertido é gerado a partir de um conjunto de documentos e mapeia cada palavra única para os documentos em que aparece. Este índice é crucial para a eficiência do sistema de busca, permitindo rápidas recuperações de documentos baseadas em termos de consulta.

### Funcionalidades:

Processamento e normalização de texto: tokenização, remoção de stopwords.
Geração do índice: cada termo é associado a uma lista de documentos e quantidade de vezes que aparece em cada um.

## 2. Cálculo de Pesos TF-IDF
Para cada documento e termo, calcula-se um peso TF-IDF que indica a importância do termo no documento em relação ao corpus inteiro. O TF-IDF ajuda a determinar quais documentos são mais relevantes para uma consulta, dando preferência a documentos que contêm termos mais raros ou significativos.

### Funcionalidades:

Cálculo do TF (Term Frequency): Mede a frequência de cada termo em um documento.
Cálculo do IDF (Inverse Document Frequency): Mede a importância do termo no corpus inteiro.
Geração de um arquivo de pesos: Armazena os pesos TF-IDF para rápida referência durante as consultas.

## 3. Resposta a Consultas
O sistema permite que os usuários realizem consultas de texto e retorna uma lista de documentos ordenados por relevância, com base nos pesos TF-IDF e na similaridade do cosseno entre os vetores de consulta e documentos.

### Funcionalidades:

Processamento de consultas: Aplicação dos mesmos métodos de processamento de texto usados na indexação.
Cálculo de similaridade: Uso da similaridade do cosseno para comparar a consulta com cada documento.
Ordenação de documentos por relevância: Documentos são retornados em ordem decrescente de relevância.