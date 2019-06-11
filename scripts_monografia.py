import pandas as pd
import subprocess
import biblioteca_monografia
import matplotlib.pyplot as plt
import itertools as its
import sklearn.metrics as mt
import numpy as np
import itertools
import operator

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import cross_val_score


# Funcao para identificar elemento mais comum em uma lista
def most_common(_list):
    # get an iterable of (item, iterable) pairs
    sl = sorted((x, i) for i2, x in enumerate(_list))
    # print 'SL:', SL
    groups = itertools.groupby(sl, key=operator.itemgetter(0))
    # auxiliary function to get "quality" for an item
    
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(_list)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        # print 'item %r, count %r, minind %r' % (item, count, min_index)
        return count, -min_index
    # pick the highest-count/earliest item
    return max(groups, key=_auxfun)[0]


# Funcao para remover todas ocorrencias de um elemento passado como parametro em uma lista passada como parametro
def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


# Funcao auxiliar para visualizar a arvore gerada
def visualize_tree(tree, feature_names, class_names, tree_name):
    """Create tree png using graphviz.
    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f, feature_names=feature_names, class_names=class_names, filled=True,
                        rounded=True)

    command = ["dot", "-Tpng", "dt.dot", "-o", tree_name]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to produce visualization")

# Atributos mantidos da base original que serao utilizados na analise
atributosMantidos = [   "cod", "quesm1", "quesm2", "quesm3", "quesm1r", "forum1", "forum2", "forum3", "forum4",
                        "ativcolm1", "ativcolm2", "forum5", "forum6", "forum7", "ativcolm1r", "ativcolm2r",
                        "quesm2r", "forum1r", "forum8", "forum2r", "ativcolm3", "forum9", "forum10", "forum11",
                        "forum12", "forum13", "forum14", "forum15", "ativcolm4", "idade", "sexo", "escolaridade",
                        "estadocivil", "ocupacao", "tempodeservico", "religiao", "contatoanterior", "lidadiretamente",
                        "lida.onde", "materialdidatico", "prazoatividades", "interacaopares", "organizacaocurso",
                        "import.ajud.tutor", "autoavaliacao.x", "part.outrocurso",
                        "pp001", "pp002", "pp003", "pp004", "pp005", "pp006", "pp007", "pp008", "pp009", "pp010",
                        "pp011", "pp012", "pp013", "pp014", "pp015", "pp016", "pp017", "pp018", "pp019", "pp020",
                        "pp021", "pp022", "pp023", "pp024", "pp025", "pp026", "pp027", "pp028", "pp029", "pp030",
                        "pp031", "pp032", "pp033", "pp034", "pp035", "pp036", "pp037",
                        "assignment.view", "course.view", "feedback.view", "folder.view", "forum.add.post",
                        "forum.update.post", "forum.user.report", "forum.view.discussion", "forum.view.forum",
                        "quiz.attempt", "quiz.continue.attempt", "quiz.view", "quiz.view.summary", "resource.view",
                        "url.view", "user.view", "user.view.all", "blog.view", "forum.unsubscribe", "user.update",
                        "discussion.mark.read", "forum.add.discussion", "forum.mark.read", "forum.delete.post",
                        "forum.view.forums", "quiz.review", "forum.subscribe", "forum.search", "quiz.view.all",
                        "user.change.password", "motivopart", "barreiras", "facilitadores", "aprovado"]
                        # "inconsistencia no preenchimento"    ]

# Atributos do Ambiente Virtual de Aprendizado
atributosAVA = [    "assignment.view", "course.view", "feedback.view", "folder.view", "forum.add.post",
                    "forum.update.post", "forum.user.report", "forum.view.discussion", "forum.view.forum",
                    "quiz.attempt", "quiz.continue.attempt", "quiz.view", "quiz.view.summary", "resource.view",
                    "url.view", "user.view", "user.view.all", "blog.view", "forum.unsubscribe", "user.update",
                    "discussion.mark.read", "forum.add.discussion", "forum.mark.read", "forum.delete.post",
                    "forum.view.forums", "quiz.review", "forum.subscribe", "forum.search", "quiz.view.all",
                    "user.change.password"  ]

# Chaves para os tratamentos, se True realiza aquele tratamento
gerarModelos = False
tratarNotas = True
tratarTempoServico = True
tratarValorAusente = True
calcularVizinho = True

# Lê o arquivo
dadosMonografia = pd.read_csv("dadosMonografia.csv")

# Dataframe para armazenar e manipular os dados tratados
dadosTratadosMonografia = pd.DataFrame()

# Atribuindo ao dataframe apenas os atributos selecionados
for c in atributosMantidos:
    dadosTratadosMonografia[c] = dadosMonografia[c]

# print (dadosTratadosMonografia["inconsistencia no preenchimento"])

print("Dimensoes iniciais:")
print(dadosMonografia.shape)

print ("Dimensao apos remover alguns atributos:")
print(dadosTratadosMonografia.shape)

# Exclui registros com 'cod' duplicados
print ("Dimensao apos remover duplicatas por 'cod':")
dadosTratadosMonografia = dadosTratadosMonografia.drop_duplicates(subset="cod")
print(dadosTratadosMonografia.shape)

# Exclui registros com 'idade' nulo
print ("Dimensao apos remover registros com campo idade = NA:")
dadosTratadosMonografia = dadosTratadosMonografia[pd.notnull(dadosTratadosMonografia["idade"])]
print(dadosTratadosMonografia.shape)

# Excluir registros com idade igual a tracinho
print ("Dimensao apos remover registros com campo idade = - :")
dadosTratadosMonografia = dadosTratadosMonografia[dadosTratadosMonografia.idade != "-"]
print(dadosTratadosMonografia.shape)

qtdAprovados = 0
qtdReprovados = 0
for i in dadosTratadosMonografia.index:
    if dadosTratadosMonografia.loc[i]["aprovado"] == "Sim":
        qtdAprovados += 1
    else:
        qtdReprovados += 1

print("\nQuantidade de aprovados: {}\nQuantidade de reprovados: {}".format(qtdAprovados, qtdReprovados))


# Variavel com os atributos referentes às atividades do curso
# Utilizada como auxiliar para a identificação quem fez ou não fez cada atividade
atividades = [ "quesm1", "quesm2", "quesm3", "quesm1r", "forum1", "forum2", "forum3", "forum4",
               "ativcolm1", "ativcolm2", "forum5", "forum6", "forum7", "ativcolm1r", "ativcolm2r",
               "quesm2r", "forum1r", "forum8", "forum2r", "ativcolm3", "forum9", "forum10", "forum11",
               "forum12", "forum13", "forum14", "forum15", "ativcolm4" ]

# Se o campo de algumas das atividades for >= 0, mudar para 1. Senão, mudar para 0.
if tratarNotas:
    print ("\nFormatando os atributos de atividades...")
    for i in dadosTratadosMonografia.index:
        # print ("{}%".format(int( ((i/(len(dadosTratadosMonografia.index)))*100) / (750/100)  )))
        for j in atividades:
            if dadosTratadosMonografia.loc[i][j] >= 0:
                dadosTratadosMonografia.at[i, j] = 1
            else:
                dadosTratadosMonografia.at[i, j] = 0
    print ("Pronto.")

# Padronizar o atributo "idade"
dadosTratadosMonografia.idade = dadosTratadosMonografia.idade.fillna(0)
for i in dadosTratadosMonografia.index:
    idade = dadosTratadosMonografia.loc[i]["idade"]
    dadosTratadosMonografia = biblioteca_monografia.ajustaIdade(idade, dadosTratadosMonografia, i)

# Converte as colunas "idade" e "tempodeservico" para numerico
dadosTratadosMonografia["idade"] = dadosTratadosMonografia["idade"].apply(pd.to_numeric)

print("\nMenor idade: {}".format(dadosTratadosMonografia["idade"].min()))
print("Maior idade: {}".format(dadosTratadosMonografia["idade"].max()))

# Padronizar o atributo "tempodeservico"
dadosTratadosMonografia.tempodeservico = dadosTratadosMonografia.tempodeservico.fillna(0)
for i in dadosTratadosMonografia.index:
    tempo = dadosTratadosMonografia.loc[i]["tempodeservico"]
    dadosTratadosMonografia = biblioteca_monografia.ajustaTempoServico(tempo, dadosTratadosMonografia, i)

# Tratar valor ausente em "tempodeservico" (lembrete: valores ausentes foram colocados como 0 na formatacao a cima)
print ("\nTratanto tempodeservico ausentes...")
if tratarTempoServico:
    for i in dadosTratadosMonografia.index:
        if dadosTratadosMonografia.loc[i]["idade"] == 0:
            print("Idade zero na linha {}".format(i))
        if dadosTratadosMonografia.loc[i]["tempodeservico"] == 0:

            print ("Idade: {} Escolaridade: {} Tempo de servico settado: {}".format(
                dadosTratadosMonografia.loc[i]["idade"],
                dadosTratadosMonografia.loc[i]["escolaridade"],
                biblioteca_monografia.tratarValorAusenteTempoServico(dadosTratadosMonografia, i)))

            dadosTratadosMonografia.at[i, "tempodeservico"] =\
                biblioteca_monografia.tratarValorAusenteTempoServico(dadosTratadosMonografia, i)

# Converte as colunas "idade" e "tempodeservico" para numerico
dadosTratadosMonografia[["idade", "tempodeservico"]] = dadosTratadosMonografia[["idade", "tempodeservico"]].apply(pd.to_numeric)

# # Imprime menor e maior tempo de servico
# print("\nMenor tempodeservico: {}".format(dadosTratadosMonografia["tempodeservico"].min()))
# print("Maior tempodeservico: {}".format(dadosTratadosMonografia["tempodeservico"].max()))

# Normaliza as colunas "idade" e "tempodeservico" (desativei heder)
# dadosTratadosMonografia["idade"]=(dadosTratadosMonografia["idade"]-dadosTratadosMonografia["idade"].min())/\
#                                  (dadosTratadosMonografia["idade"].max()-dadosTratadosMonografia["idade"].min())
# dadosTratadosMonografia["tempodeservico"]=(dadosTratadosMonografia["tempodeservico"]-dadosTratadosMonografia["tempodeservico"].min())/\
#                                  (dadosTratadosMonografia["tempodeservico"].max()-dadosTratadosMonografia["tempodeservico"].min())


# Tratar valor ausente em sexo, so existe um no index 9607 e eh uma mulher
dadosTratadosMonografia.at[9607, "sexo"] = "Feminino"

# Converte a coluna sexo em colunas de numericos (desativei para gerar no BD pro Heder)
novos_dados = pd.get_dummies(dadosTratadosMonografia["sexo"])
dadosTratadosMonografia = pd.concat([dadosTratadosMonografia, novos_dados], axis=1)

# kNN sera utilizado para encontrar vizinhos que auxiliarao tratar valores ausentes
# Preparando os atributos utilizados no kNN
if calcularVizinho:
    print ("\nPreparando a lista de atributos utilizandos no kNN (idade, tempo de servico e sexo)...")
    atributosKNN = [] # lista para guardar atributos levados em consideracao no KNN
    pegaIndex = [] # lista para guardar o index de cada registro
    for i in dadosTratadosMonografia.index:
        aux = [ dadosTratadosMonografia.loc[i]["idade"],
                dadosTratadosMonografia.loc[i]["tempodeservico"],
                dadosTratadosMonografia.loc[i]["Masculino"],
                dadosTratadosMonografia.loc[i]["Feminino"]
                ]
        atributosKNN.append(aux)
        pegaIndex.append(i)

# Tratar motivopart, barreiras e facilitadores
# dadosTratadosMonografia = biblioteca_monografia.tratarMotivopartBarreiraFacilitadores(dadosTratadosMonografia)

# Tratar valores ausentes, levando em consideracao idade, tempo de servico e sexo
qtdVizinhos = 6
if tratarValorAusente:
    print ("\nCalculando os vizinhos mais proximos de cada registro da lista...")
    np.asarray(atributosKNN.copy())
    nbrs = NearestNeighbors(n_neighbors=qtdVizinhos, algorithm='ball_tree').fit(atributosKNN)
    distances, indices = nbrs.kneighbors(atributosKNN)
    print ("Vizinhos calculados.")

    atributosComValoresAusentes = [
        "escolaridade", "estadocivil", "ocupacao", "religiao", "contatoanterior",
                                    "lidadiretamente", "lida.onde", "materialdidatico", "prazoatividades",
                                    "interacaopares", "organizacaocurso", "import.ajud.tutor", "autoavaliacao.x",
                                    "part.outrocurso",
                                    "pp001", "pp002", "pp003", "pp004", "pp005", "pp006", "pp007", "pp008", "pp009", "pp010",
                                    "pp011", "pp012", "pp013", "pp014", "pp015", "pp016", "pp017", "pp018", "pp019", "pp020",
                                    "pp021", "pp022", "pp023", "pp024", "pp025", "pp026", "pp027", "pp028", "pp029", "pp030",
                                    "pp031", "pp032", "pp033", "pp034", "pp035", "pp036", "pp037",
                                    "assignment.view", "course.view", "feedback.view", "folder.view", "forum.add.post",
                                    "forum.update.post", "forum.user.report", "forum.view.discussion", "forum.view.forum",
                                    "quiz.attempt", "quiz.continue.attempt", "quiz.view", "quiz.view.summary", "resource.view",
                                    "url.view", "user.view", "user.view.all", "blog.view", "forum.unsubscribe", "user.update",
                                    "discussion.mark.read", "forum.add.discussion", "forum.mark.read", "forum.delete.post",
                                    "forum.view.forums", "quiz.review", "forum.subscribe", "forum.search", "quiz.view.all",
                                    "user.change.password"
          # "motivopart", "barreiras", "facilitadores"
                                     ]

    print("Settando valores ausentes como -1...")
    # Lista preenchida com valores numericos ou possui valores ausentes
    atributosComAlgunsNumericos = [
        "assignment.view", "course.view", "feedback.view", "folder.view", "forum.add.post",
                                    "forum.update.post", "forum.user.report", "forum.view.discussion", "forum.view.forum",
                                    "quiz.attempt", "quiz.continue.attempt", "quiz.view", "quiz.view.summary", "resource.view",
                                    "url.view", "user.view", "user.view.all", "blog.view", "forum.unsubscribe", "user.update",
                                    "discussion.mark.read", "forum.add.discussion", "forum.mark.read", "forum.delete.post",
                                    "forum.view.forums", "quiz.review", "forum.subscribe", "forum.search", "quiz.view.all",
                                    "user.change.password"]
        #   "motivopart", "barreiras", "facilitadores"]

    for c in atributosComAlgunsNumericos:
        for i in dadosTratadosMonografia.index:
            try:
                if dadosTratadosMonografia.loc[i][c] >= 0:
                    continue
                else:
                    dadosTratadosMonografia.at[i, c] = -1
            except TypeError:
                if len(dadosTratadosMonografia.loc[i][c]) == 0:
                    continue
                else:
                    dadosTratadosMonografia.at[i, c] = -1
    print("Valores ausentes settados como -1.")

if tratarValorAusente:
    print("Tratando valores ausentes...")
    for c in atributosComValoresAusentes:
        for i in dadosTratadosMonografia.index:  # pegaIndex
            if dadosTratadosMonografia.loc[i][c] == "-" or dadosTratadosMonografia.loc[i][c] == -1 or \
                "a".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) < 0:

                indiceAux = pegaIndex.index(i)

                vizinhos = []
                for v in range (1, qtdVizinhos):
                    vizinhos.append(dadosTratadosMonografia.loc[pegaIndex[indices[indiceAux][v]]][c])

                vizinhos[:] = (value for value in vizinhos if value != "-")
                vizinhos[:] = (value for value in vizinhos if value != -1)

                try:
                    valorToSet = most_common(vizinhos)
                except ValueError:
                    valorToSet = 0.0
                except TypeError:
                    valorToSet = "Outros"

                # print("\n\nEndereco: [{},{}] Vizinhos: {}\nValor novo: {}".format(
                #         i, c, vizinhos, valorToSet
                #     ))


                dadosTratadosMonografia.at[i, c] = valorToSet
    print ("Valores ausentes tratados.")

# atributosClassificacao = [  "quesm1", "quesm2", "quesm3", "quesm1r", "forum1", "forum2", "forum3", "forum4",
#                             "ativcolm1", "ativcolm2", "forum5", "forum6", "forum7", "ativcolm1r", "ativcolm2r",
#                             "quesm2r", "forum1r", "forum8", "forum2r", "ativcolm3", "forum9", "forum10", "forum11",
#                             "forum12", "forum13", "forum14", "forum15", "ativcolm4",
#                             "idade", "tempodeservico", "assignment.view", "course.view", "feedback.view", "folder.view", "forum.add.post",
#                             "forum.update.post", "forum.user.report", "forum.view.discussion", "forum.view.forum",
#                             "quiz.attempt", "quiz.continue.attempt", "quiz.view", "quiz.view.summary", "resource.view",
#                             "url.view", "user.view", "user.view.all", "blog.view", "forum.unsubscribe", "user.update",
#                             "discussion.mark.read", "forum.add.discussion", "forum.mark.read", "forum.delete.post",
#                             "forum.view.forums", "quiz.review", "forum.subscribe", "forum.search", "quiz.view.all",
#                             "user.change.password",
#                             "Identificação pessoal com o tema",
#                             "Identificação profissional com o tema",
#                             "Para aquisição de conhecimento na área",
#                             "Pelo fato de o curso ser gratuito",
#                             "Pelo fato de o curso estar vinculado à Universidade",
#                             "Por ser um curso à distância",
#                             "Por ser uma oportunidade de formação continuada",
#                             "Ausência da família",
#                             "Pouca comunicação com os pais",
#                             "Uso de substâncias por familiares",
#                             "Presença de drogas ilícitas no ambiente escolar",
#                             "Proximidade da rede de distribuição de drogas",
#                             "Ausência de limites dos alunos",
#                             "Ausência de colaboração da equipe escolar",
#                             "Ausência de regras no ambiente escolar",
#                             "Possuir alunos interessados na temática",
#                             "Presença de uma equipe para trabalhar a temática",
#                             "Estímulo aos alunos",
#                             "Desenvolvimento de projetos na escola",
#                             "Apoio aos projetos em desenvolvimento",
#                             "Presença de regras no ambiente escolar",
#                             "Promoção de compromisso e confiança",
#                             "Valorização do ambiente escolar",
#                             "Participação da comunidade e dos pais no trabalho de prevenção"    ]

# dadosMonografia = pd.read_csv("/home/thiago/Desktop/dadosTratadosMonografia.csv")
# dadosMonografia = pd.read_csv("dadosMonografia.csv")
# "/home/thiago/Desktop/dadosTratadosMonografia.csv"

atributosClassificacao = ["Masculino", "Feminino", "quesm1", "quesm2", "quesm3", "quesm1r", "forum1", "forum2",
                          "forum3", "forum4", "ativcolm1", "ativcolm2", "forum5", "forum6", "forum7", "ativcolm1r",
                          "ativcolm2r", "quesm2r", "forum1r", "forum8", "forum2r", "ativcolm3", "forum9",
                          "forum10", "forum11", "forum12", "forum13", "forum14", "forum15", "ativcolm4", "idade",
                          "tempodeservico", "assignment.view", "course.view", "feedback.view", "folder.view",
                          "forum.add.post", "forum.update.post", "forum.user.report", "forum.view.discussion", "forum.view.forum", "quiz.attempt", "quiz.continue.attempt", "quiz.view", "quiz.view.summary", "resource.view", "url.view", "user.view", "user.view.all", "blog.view", "forum.unsubscribe", "user.update", "discussion.mark.read", "forum.add.discussion", "forum.mark.read", "forum.delete.post", "forum.view.forums", "quiz.review", "forum.subscribe", "forum.search", "quiz.view.all", "user.change.password", "Identificação pessoal com o tema", "Identificação profissional com o tema", "Para aquisição de conhecimento na área", "Pelo fato de o curso ser gratuito", "Pelo fato de o curso estar vinculado à Universidade", "Por ser um curso à distância", "Por ser uma oportunidade de formação continuada", "Ausência da família", "Pouca comunicação com os pais", "Uso de substâncias por familiares", "Presença de drogas ilícitas no ambiente escolar", "Proximidade da rede de distribuição de drogas", "Ausência de limites dos alunos", "Ausência de colaboração da equipe escolar", "Ausência de regras no ambiente escolar", "Possuir alunos interessados na temática", "Presença de uma equipe para trabalhar a temática", "Estímulo aos alunos", "Desenvolvimento de projetos na escola", "Apoio aos projetos em desenvolvimento", "Presença de regras no ambiente escolar", "Promoção de compromisso e confiança", "Valorização do ambiente escolar", "Participação da comunidade e dos pais no trabalho de prevenção", "Ensino Fundamental Completo( escolaridade )", "Ensino Fundamental Incompleto( escolaridade )", "Ensino Médio Completo( escolaridade )", "Ensino Superior Completo( escolaridade )", "Ensino Superior Incompleto( escolaridade )", "Pós-graduação( escolaridade )", "Casado (a)( estadocivil )", "Divorciado (a)( estadocivil )", "Outros( estadocivil )", "Solteiro (a)( estadocivil )", "União Estável( estadocivil )", "Viúvo (a)( estadocivil )", "Coordenador (a) Pedagógico( ocupacao )", "Diretor (a)( ocupacao )", "Estudante( ocupacao )", "Orientador (a)( ocupacao )", "Outros( ocupacao )", "Professor (a)( ocupacao )", "Supervisor (a)( ocupacao )", "Budismo( religiao )", "Candomblé( religiao )", "Católica( religiao )", "Espírita( religiao )", "Evangélica( religiao )", "Outras( religiao )", "Sem religião( religiao )", "Umbanda( religiao )", "Não( contatoanterior )", "Sim( contatoanterior )", "Não( lidadiretamente )", "Sim( lidadiretamente )", "Amigos( lida.onde )", "Comunidade( lida.onde )", "Escola( lida.onde )", "Família( lida.onde )", "Outros( lida.onde )", "Serviços de atuação( lida.onde )", "Serviços de saúde( lida.onde )", "Adequado( materialdidatico )", "Muito adequado( materialdidatico )", "Pouco adequado( materialdidatico )", "Pouquíssimo adequado( materialdidatico )", "Flexível( prazoatividades )", "Muito flexível( prazoatividades )", "Pouco flexível( prazoatividades )", "Pouquíssimo flexível( prazoatividades )", "Importante( interacaopares )", "Muito importante( interacaopares )", "Pouco importante( interacaopares )", "Pouquíssimo importante( interacaopares )", "Desorganizado( organizacaocurso )", "Muito desorganizado( organizacaocurso )", "Muito organizado( organizacaocurso )", "Organizado( organizacaocurso )", "Nunca( import.ajud.tutor )", "Raramente( import.ajud.tutor )", "Sempre( import.ajud.tutor )", "Às vezes( import.ajud.tutor )", "Não, não considero( autoavaliacao.x )", "Sim, considero( autoavaliacao.x )", "Sim, considero, porém, poderia estar me esforçando mais( autoavaliacao.x )", "Não( part.outrocurso )", "Sim( part.outrocurso )", "pp001", "pp002", "pp003", "pp004", "pp005", "pp006", "pp007", "pp008", "pp009", "pp010",
                          "pp011", "pp012", "pp013", "pp014", "pp015", "pp016", "pp017", "pp018", "pp019", "pp020",
                          "pp021", "pp022", "pp023", "pp024", "pp025", "pp026", "pp027", "pp028", "pp029", "pp030",
                          "pp031", "pp032", "pp033", "pp034", "pp035", "pp036", "pp037"]

atributosSociais = ["Masculino", "Feminino", "idade", "tempodeservico", "Identificação pessoal com o tema", "Identificação profissional com o tema", "Para aquisição de conhecimento na área", "Pelo fato de o curso ser gratuito", "Pelo fato de o curso estar vinculado à Universidade", "Por ser um curso à distância", "Por ser uma oportunidade de formação continuada", "Ausência da família", "Pouca comunicação com os pais", "Uso de substâncias por familiares", "Presença de drogas ilícitas no ambiente escolar", "Proximidade da rede de distribuição de drogas", "Ausência de limites dos alunos", "Ausência de colaboração da equipe escolar", "Ausência de regras no ambiente escolar", "Possuir alunos interessados na temática", "Presença de uma equipe para trabalhar a temática", "Estímulo aos alunos", "Desenvolvimento de projetos na escola", "Apoio aos projetos em desenvolvimento", "Presença de regras no ambiente escolar", "Promoção de compromisso e confiança", "Valorização do ambiente escolar", "Participação da comunidade e dos pais no trabalho de prevenção", "Ensino Fundamental Completo( escolaridade )", "Ensino Fundamental Incompleto( escolaridade )", "Ensino Médio Completo( escolaridade )", "Ensino Superior Completo( escolaridade )", "Ensino Superior Incompleto( escolaridade )", "Pós-graduação( escolaridade )", "Casado (a)( estadocivil )", "Divorciado (a)( estadocivil )", "Outros( estadocivil )", "Solteiro (a)( estadocivil )", "União Estável( estadocivil )", "Viúvo (a)( estadocivil )", "Coordenador (a) Pedagógico( ocupacao )", "Diretor (a)( ocupacao )", "Estudante( ocupacao )", "Orientador (a)( ocupacao )", "Outros( ocupacao )", "Professor (a)( ocupacao )", "Supervisor (a)( ocupacao )", "Budismo( religiao )", "Candomblé( religiao )", "Católica( religiao )", "Espírita( religiao )", "Evangélica( religiao )", "Outras( religiao )", "Sem religião( religiao )", "Umbanda( religiao )", "Não( contatoanterior )", "Sim( contatoanterior )", "Não( lidadiretamente )", "Sim( lidadiretamente )", "Amigos( lida.onde )", "Comunidade( lida.onde )", "Escola( lida.onde )", "Família( lida.onde )", "Outros( lida.onde )", "Serviços de atuação( lida.onde )", "Serviços de saúde( lida.onde )", "Não( part.outrocurso )", "Sim( part.outrocurso )", "pp001", "pp002", "pp003", "pp004", "pp005", "pp006", "pp007", "pp008", "pp009", "pp010",
                    "pp011", "pp012", "pp013", "pp014", "pp015", "pp016", "pp017", "pp018", "pp019", "pp020",
                    "pp021", "pp022", "pp023", "pp024", "pp025", "pp026", "pp027", "pp028", "pp029", "pp030",
                    "pp031", "pp032", "pp033", "pp034", "pp035", "pp036", "pp037"]
#
# atributosSociaisPrevios = [ "Masculino", "Feminino", "idade", "tempodeservico", "Identificação pessoal com o tema", "Identificação profissional com o tema", "Para aquisição de conhecimento na área( motivopart )", "Pelo fato de o curso ser gratuito", "Pelo fato de o curso estar vinculado à Universidade", "Por ser um curso à distância", "Por ser uma oportunidade de formação continuada( motivopart )", "Ausência da família( barreiras )", "Pouca comunicação com os pais", "Uso de substâncias por familiares", "Presença de drogas ilícitas no ambiente escolar", "Proximidade da rede de distribuição de drogas", "Ausência de limites dos alunos", "Ausência de colaboração da equipe escolar", "Ausência de regras no ambiente escolar", "Possuir alunos interessados na temática", "Presença de uma equipe para trabalhar a temática", "Estímulo aos alunos", "Desenvolvimento de projetos na escola", "Apoio aos projetos em desenvolvimento", "Presença de regras no ambiente escolar", "Promoção de compromisso e confiança", "Valorização do ambiente escolar", "Participação da comunidade e dos pais no trabalho de prevenção", "Ensino Fundamental Completo( escolaridade )", "Ensino Fundamental Incompleto( escolaridade )", "Ensino Médio Completo( escolaridade )", "Ensino Superior Completo( escolaridade )", "Ensino Superior Incompleto( escolaridade )", "Pós-graduação( escolaridade )", "Casado (a)( estadocivil )", "Divorciado (a)( estadocivil )", "Outros( estadocivil )", "Solteiro (a)( estadocivil )", "União Estável( estadocivil )", "Viúvo (a)( estadocivil )", "Coordenador (a) Pedagógico( ocupacao )", "Diretor (a)( ocupacao )", "Estudante( ocupacao )", "Orientador (a)( ocupacao )", "Outros( ocupacao )", "Professor (a)( ocupacao )", "Supervisor (a)( ocupacao )", "Budismo( religiao )", "Candomblé( religiao )", "Católica( religiao )", "Espírita( religiao )", "Evangélica( religiao )", "Outras( religiao )", "Sem religião( religiao )", "Umbanda( religiao )", "Não( contatoanterior )", "Sim( contatoanterior )", "Não( lidadiretamente )", "Sim( lidadiretamente )", "Amigos( lida.onde )", "Comunidade( lida.onde )", "Escola( lida.onde )", "Família( lida.onde )", "Outros( lida.onde )", "Serviços de atuação( lida.onde )", "Serviços de saúde( lida.onde )", "Não( part.outrocurso )", "Sim( part.outrocurso )", "Concordo( pp001 )", "Concordo totalmente( pp001 )", "Discordo( pp001 )", "Discordo totalmente( pp001 )", "Nem discordo, nem concordo( pp001 )", "Concordo( pp002 )", "Concordo totalmente( pp002 )", "Discordo( pp002 )", "Discordo totalmente( pp002 )", "Nem discordo, nem concordo( pp002 )", "Concordo( pp003 )", "Concordo totalmente( pp003 )", "Discordo( pp003 )", "Discordo totalmente( pp003 )", "Nem discordo, nem concordo( pp003 )", "Concordo( pp004 )", "Concordo totalmente( pp004 )", "Discordo( pp004 )", "Discordo totalmente( pp004 )", "Nem discordo, nem concordo( pp004 )", "Concordo( pp005 )", "Concordo totalmente( pp005 )", "Discordo( pp005 )", "Discordo totalmente( pp005 )", "Nem discordo, nem concordo( pp005 )", "Concordo( pp006 )", "Concordo totalmente( pp006 )", "Discordo( pp006 )", "Discordo totalmente( pp006 )", "Nem discordo, nem concordo( pp006 )", "Concordo( pp007 )", "Concordo totalmente( pp007 )", "Discordo( pp007 )", "Discordo totalmente( pp007 )", "Nem discordo, nem concordo( pp007 )", "Concordo( pp008 )", "Concordo totalmente( pp008 )", "Discordo( pp008 )", "Discordo totalmente( pp008 )", "Nem discordo, nem concordo( pp008 )", "Concordo( pp009 )", "Concordo totalmente( pp009 )", "Discordo( pp009 )", "Discordo totalmente( pp009 )", "Nem discordo, nem concordo( pp009 )", "Concordo( pp010 )", "Concordo totalmente( pp010 )", "Discordo( pp010 )", "Discordo totalmente( pp010 )", "Nem discordo, nem concordo( pp010 )", "Concordo( pp011 )", "Concordo totalmente( pp011 )", "Discordo( pp011 )", "Discordo totalmente( pp011 )", "Nem discordo, nem concordo( pp011 )", "Concordo( pp012 )", "Concordo totalmente( pp012 )", "Discordo( pp012 )", "Discordo totalmente( pp012 )", "Nem discordo, nem concordo( pp012 )", "Concordo( pp013 )", "Concordo totalmente( pp013 )", "Discordo( pp013 )", "Discordo totalmente( pp013 )", "Nem discordo, nem concordo( pp013 )", "Concordo( pp014 )", "Concordo totalmente( pp014 )", "Discordo( pp014 )", "Discordo totalmente( pp014 )", "Nem discordo, nem concordo( pp014 )", "Concordo( pp015 )", "Concordo totalmente( pp015 )", "Discordo( pp015 )", "Discordo totalmente( pp015 )", "Nem discordo, nem concordo( pp015 )", "Concordo( pp016 )", "Concordo totalmente( pp016 )", "Discordo( pp016 )", "Discordo totalmente( pp016 )", "Nem discordo, nem concordo( pp016 )", "Concordo( pp017 )", "Concordo totalmente( pp017 )", "Discordo( pp017 )", "Discordo totalmente( pp017 )", "Nem discordo, nem concordo( pp017 )", "Concordo( pp018 )", "Concordo totalmente( pp018 )", "Discordo( pp018 )", "Discordo totalmente( pp018 )", "Nem discordo, nem concordo( pp018 )", "Concordo( pp019 )", "Concordo totalmente( pp019 )", "Discordo( pp019 )", "Discordo totalmente( pp019 )", "Nem discordo, nem concordo( pp019 )", "Concordo( pp020 )", "Concordo totalmente( pp020 )", "Discordo( pp020 )", "Discordo totalmente( pp020 )", "Nem discordo, nem concordo( pp020 )", "Concordo( pp021 )", "Concordo totalmente( pp021 )", "Discordo( pp021 )", "Discordo totalmente( pp021 )", "Nem discordo, nem concordo( pp021 )", "Concordo( pp022 )", "Concordo totalmente( pp022 )", "Discordo( pp022 )", "Discordo totalmente( pp022 )", "Nem discordo, nem concordo( pp022 )", "Concordo( pp023 )", "Concordo totalmente( pp023 )", "Discordo( pp023 )", "Discordo totalmente( pp023 )", "Nem discordo, nem concordo( pp023 )", "Concordo( pp024 )", "Concordo totalmente( pp024 )", "Discordo( pp024 )", "Discordo totalmente( pp024 )", "Nem discordo, nem concordo( pp024 )", "Concordo( pp025 )", "Concordo totalmente( pp025 )", "Discordo( pp025 )", "Discordo totalmente( pp025 )", "Nem discordo, nem concordo( pp025 )", "Concordo( pp026 )", "Concordo totalmente( pp026 )", "Discordo( pp026 )", "Discordo totalmente( pp026 )", "Nem discordo, nem concordo( pp026 )", "Concordo( pp027 )", "Concordo totalmente( pp027 )", "Discordo( pp027 )", "Discordo totalmente( pp027 )", "Nem discordo, nem concordo( pp027 )", "Concordo( pp028 )", "Concordo totalmente( pp028 )", "Discordo( pp028 )", "Discordo totalmente( pp028 )", "Nem discordo, nem concordo( pp028 )", "Concordo( pp029 )", "Concordo totalmente( pp029 )", "Discordo( pp029 )", "Discordo totalmente( pp029 )", "Nem discordo, nem concordo( pp029 )", "Concordo( pp030 )", "Concordo totalmente( pp030 )", "Discordo( pp030 )", "Discordo totalmente( pp030 )", "Nem discordo, nem concordo( pp030 )", "Concordo( pp031 )", "Concordo totalmente( pp031 )", "Discordo( pp031 )", "Discordo totalmente( pp031 )", "Nem discordo, nem concordo( pp031 )", "Concordo( pp032 )", "Concordo totalmente( pp032 )", "Discordo( pp032 )", "Discordo totalmente( pp032 )", "Nem discordo, nem concordo( pp032 )", "Concordo( pp033 )", "Concordo totalmente( pp033 )", "Discordo( pp033 )", "Discordo totalmente( pp033 )", "Nem discordo, nem concordo( pp033 )", "Concordo( pp034 )", "Concordo totalmente( pp034 )", "Discordo( pp034 )", "Discordo totalmente( pp034 )", "Nem discordo, nem concordo( pp034 )", "Concordo( pp035 )", "Concordo totalmente( pp035 )", "Discordo( pp035 )", "Discordo totalmente( pp035 )", "Nem discordo, nem concordo( pp035 )", "Concordo( pp036 )", "Concordo totalmente( pp036 )", "Discordo( pp036 )", "Discordo totalmente( pp036 )", "Nem discordo, nem concordo( pp036 )", "Concordo( pp037 )", "Concordo totalmente( pp037 )", "Discordo( pp037 )", "Discordo totalmente( pp037 )", "Nem discordo, nem concordo( pp037 )" ]
#
# atributosSociaisPrevios = [ "Concordo( pp001 )", "Concordo totalmente( pp001 )", "Discordo( pp001 )", "Discordo totalmente( pp001 )", "Nem discordo, nem concordo( pp001 )", "Concordo( pp002 )", "Concordo totalmente( pp002 )", "Discordo( pp002 )", "Discordo totalmente( pp002 )", "Nem discordo, nem concordo( pp002 )", "Concordo( pp003 )", "Concordo totalmente( pp003 )", "Discordo( pp003 )", "Discordo totalmente( pp003 )", "Nem discordo, nem concordo( pp003 )", "Concordo( pp004 )", "Concordo totalmente( pp004 )", "Discordo( pp004 )", "Discordo totalmente( pp004 )", "Nem discordo, nem concordo( pp004 )", "Concordo( pp005 )", "Concordo totalmente( pp005 )", "Discordo( pp005 )", "Discordo totalmente( pp005 )", "Nem discordo, nem concordo( pp005 )", "Concordo( pp006 )", "Concordo totalmente( pp006 )", "Discordo( pp006 )", "Discordo totalmente( pp006 )", "Nem discordo, nem concordo( pp006 )", "Concordo( pp007 )", "Concordo totalmente( pp007 )", "Discordo( pp007 )", "Discordo totalmente( pp007 )", "Nem discordo, nem concordo( pp007 )", "Concordo( pp008 )", "Concordo totalmente( pp008 )", "Discordo( pp008 )", "Discordo totalmente( pp008 )", "Nem discordo, nem concordo( pp008 )", "Concordo( pp009 )", "Concordo totalmente( pp009 )", "Discordo( pp009 )", "Discordo totalmente( pp009 )", "Nem discordo, nem concordo( pp009 )", "Concordo( pp010 )", "Concordo totalmente( pp010 )", "Discordo( pp010 )", "Discordo totalmente( pp010 )", "Nem discordo, nem concordo( pp010 )", "Concordo( pp011 )", "Concordo totalmente( pp011 )", "Discordo( pp011 )", "Discordo totalmente( pp011 )", "Nem discordo, nem concordo( pp011 )", "Concordo( pp012 )", "Concordo totalmente( pp012 )", "Discordo( pp012 )", "Discordo totalmente( pp012 )", "Nem discordo, nem concordo( pp012 )", "Concordo( pp013 )", "Concordo totalmente( pp013 )", "Discordo( pp013 )", "Discordo totalmente( pp013 )", "Nem discordo, nem concordo( pp013 )", "Concordo( pp014 )", "Concordo totalmente( pp014 )", "Discordo( pp014 )", "Discordo totalmente( pp014 )", "Nem discordo, nem concordo( pp014 )", "Concordo( pp015 )", "Concordo totalmente( pp015 )", "Discordo( pp015 )", "Discordo totalmente( pp015 )", "Nem discordo, nem concordo( pp015 )", "Concordo( pp016 )", "Concordo totalmente( pp016 )", "Discordo( pp016 )", "Discordo totalmente( pp016 )", "Nem discordo, nem concordo( pp016 )", "Concordo( pp017 )", "Concordo totalmente( pp017 )", "Discordo( pp017 )", "Discordo totalmente( pp017 )", "Nem discordo, nem concordo( pp017 )", "Concordo( pp018 )", "Concordo totalmente( pp018 )", "Discordo( pp018 )", "Discordo totalmente( pp018 )", "Nem discordo, nem concordo( pp018 )", "Concordo( pp019 )", "Concordo totalmente( pp019 )", "Discordo( pp019 )", "Discordo totalmente( pp019 )", "Nem discordo, nem concordo( pp019 )", "Concordo( pp020 )", "Concordo totalmente( pp020 )", "Discordo( pp020 )", "Discordo totalmente( pp020 )", "Nem discordo, nem concordo( pp020 )", "Concordo( pp021 )", "Concordo totalmente( pp021 )", "Discordo( pp021 )", "Discordo totalmente( pp021 )", "Nem discordo, nem concordo( pp021 )", "Concordo( pp022 )", "Concordo totalmente( pp022 )", "Discordo( pp022 )", "Discordo totalmente( pp022 )", "Nem discordo, nem concordo( pp022 )", "Concordo( pp023 )", "Concordo totalmente( pp023 )", "Discordo( pp023 )", "Discordo totalmente( pp023 )", "Nem discordo, nem concordo( pp023 )", "Concordo( pp024 )", "Concordo totalmente( pp024 )", "Discordo( pp024 )", "Discordo totalmente( pp024 )", "Nem discordo, nem concordo( pp024 )", "Concordo( pp025 )", "Concordo totalmente( pp025 )", "Discordo( pp025 )", "Discordo totalmente( pp025 )", "Nem discordo, nem concordo( pp025 )", "Concordo( pp026 )", "Concordo totalmente( pp026 )", "Discordo( pp026 )", "Discordo totalmente( pp026 )", "Nem discordo, nem concordo( pp026 )", "Concordo( pp027 )", "Concordo totalmente( pp027 )", "Discordo( pp027 )", "Discordo totalmente( pp027 )", "Nem discordo, nem concordo( pp027 )", "Concordo( pp028 )", "Concordo totalmente( pp028 )", "Discordo( pp028 )", "Discordo totalmente( pp028 )", "Nem discordo, nem concordo( pp028 )", "Concordo( pp029 )", "Concordo totalmente( pp029 )", "Discordo( pp029 )", "Discordo totalmente( pp029 )", "Nem discordo, nem concordo( pp029 )", "Concordo( pp030 )", "Concordo totalmente( pp030 )", "Discordo( pp030 )", "Discordo totalmente( pp030 )", "Nem discordo, nem concordo( pp030 )", "Concordo( pp031 )", "Concordo totalmente( pp031 )", "Discordo( pp031 )", "Discordo totalmente( pp031 )", "Nem discordo, nem concordo( pp031 )", "Concordo( pp032 )", "Concordo totalmente( pp032 )", "Discordo( pp032 )", "Discordo totalmente( pp032 )", "Nem discordo, nem concordo( pp032 )", "Concordo( pp033 )", "Concordo totalmente( pp033 )", "Discordo( pp033 )", "Discordo totalmente( pp033 )", "Nem discordo, nem concordo( pp033 )", "Concordo( pp034 )", "Concordo totalmente( pp034 )", "Discordo( pp034 )", "Discordo totalmente( pp034 )", "Nem discordo, nem concordo( pp034 )", "Concordo( pp035 )", "Concordo totalmente( pp035 )", "Discordo( pp035 )", "Discordo totalmente( pp035 )", "Nem discordo, nem concordo( pp035 )", "Concordo( pp036 )", "Concordo totalmente( pp036 )", "Discordo( pp036 )", "Discordo totalmente( pp036 )", "Nem discordo, nem concordo( pp036 )", "Concordo( pp037 )", "Concordo totalmente( pp037 )", "Discordo( pp037 )", "Discordo totalmente( pp037 )", "Nem discordo, nem concordo( pp037 )" ]
#
# atributosPlataforma = [ "assignment.view", "course.view", "feedback.view", "folder.view", "forum.add.post", "forum.update.post", "forum.user.report", "forum.view.discussion", "forum.view.forum", "quiz.attempt", "quiz.continue.attempt", "quiz.view", "quiz.view.summary", "resource.view", "url.view", "user.view", "user.view.all", "blog.view", "forum.unsubscribe", "user.update", "discussion.mark.read", "forum.add.discussion", "forum.mark.read", "forum.delete.post", "forum.view.forums", "quiz.review", "forum.subscribe", "forum.search", "quiz.view.all", "user.change.password" ]

atributosNominais = ["escolaridade", "estadocivil", "ocupacao", "religiao", "contatoanterior",
                     "lidadiretamente", "lida.onde", "materialdidatico", "prazoatividades",
                     "interacaopares", "organizacaocurso", "import.ajud.tutor", "autoavaliacao.x",
                     "part.outrocurso"]

atributosOrdinarios = ["pp001", "pp002", "pp003", "pp004", "pp005", "pp006", "pp007", "pp008", "pp009", "pp010",
                       "pp011", "pp012", "pp013", "pp014", "pp015", "pp016", "pp017", "pp018", "pp019", "pp020",
                       "pp021", "pp022", "pp023", "pp024", "pp025", "pp026", "pp027", "pp028", "pp029", "pp030",
                       "pp031", "pp032", "pp033", "pp034", "pp035", "pp036", "pp037"]

# Atividades
# "quesm1", "quesm2", "quesm3", "quesm1r", "forum1", "forum2",
# "forum3", "forum4", "ativcolm1", "ativcolm2", "forum5", "forum6", "forum7", "ativcolm1r",
# "ativcolm2r", "quesm2r", "forum1r", "forum8", "forum2r", "ativcolm3", "forum9",
# "forum10", "forum11", "forum12", "forum13", "forum14", "forum15", "ativcolm4",

atributosTempo1 = ["quesm1", "forum1", "forum2", "forum3", "forum4", "ativcolm1", "forum5"]

atributosTempo2 = ["quesm1", "forum1", "forum2", "forum3", "forum4", "ativcolm1", "forum5", "forum6", "forum7",
                   "forum8", "quesm2", "ativcolm2"]

atividadesRecuperacao = ["quesm1r", "ativcolm1r", "ativcolm2r", "quesm2r", "forum1r", "forum2r"]

# Gerar binarizacao do questionario social de preconceito
if True:
    for c in atributosOrdinarios:
        novos_dados = pd.get_dummies(dadosTratadosMonografia[c])

        for i in novos_dados.columns:
            # if i == "Outros" or i == "Outras" or i == "-" or "Sim" or "Nao":
            try:
                novoNome = i + " (" + c + ")"
                novos_dados.rename(columns={i: novoNome}, inplace=True)
                atributosClassificacao.append(novoNome)
            except TypeError:
                print(i, c)
            # else:
            #     atributosClassificacao.append(i)

        dadosTratadosMonografia = pd.concat([dadosTratadosMonografia, novos_dados], axis=1)

# # (desativei gerar tabela R para o Heder)
# if True:
#     for c in atributosNominais:
#         novos_dados = pd.get_dummies(dadosTratadosMonografia[c])
#
#         for i in novos_dados.columns:
#             # if i == "Outros" or i == "Outras" or i == "-" or "Sim" or "Nao":
#             try:
#                 novoNome = i + "( " + c + " )"
#                 novos_dados.rename(columns={i: novoNome}, inplace=True)
#                 atributosClassificacao.append(novoNome)
#             except TypeError:
#                 print(i, c)
#             # else:
#             #     atributosClassificacao.append(i)
#
#         dadosTratadosMonografia = pd.concat([dadosTratadosMonografia, novos_dados], axis=1)
#
#     for c in atributosOrdinarios:
#         for i in dadosTratadosMonografia.index:
#             if dadosTratadosMonografia.loc[i][c] >= "Discordo totalmente":
#                 dadosTratadosMonografia.at[i, c] = 0
#             elif dadosTratadosMonografia.loc[i][c] >= "Discordo":
#                 dadosTratadosMonografia.at[i, c] = 1
#             elif dadosTratadosMonografia.loc[i][c] >= "Nem discordo, nem concordo":
#                 dadosTratadosMonografia.at[i, c] = 2
#             elif dadosTratadosMonografia.loc[i][c] >= "Concordo":
#                 dadosTratadosMonografia.at[i, c] = 3
#             elif dadosTratadosMonografia.loc[i][c] >= "Concordo totalmente":
#                 dadosTratadosMonografia.at[i, c] = 4

# Printar as respostas unicas dos campos outros
# print(dadosMonografia["estadocivil.outros"].unique())
# print(dadosMonografia["ocupacao.outra"].unique())
# print(dadosMonografia["religiao.outra"].unique())
# print(dadosMonografia["lida.outros"].unique())
# print(dadosMonografia["motivo.outros"].unique())

# Salva a nova tabela de dados
dadosTratadosMonografia.to_csv("dadosTratadosMonografia_(versao para o R).csv")
print("\nNova tabela de dados salva.")

# Lê a tabela de dados tratada, pos-tratamento comeca aqui, por exemplo, gerar as arvores, desfazer a normalizacao da
# idade, gerar matriz de confusao, gerar os graficos para descobrir os melhores parametros
dadosTratadosMonografia = pd.read_csv("dadosTratadosMonografia_(versao para o R).csv")

print(dadosTratadosMonografia.shape)

dadosTratadosMonografia["idade"] = round(dadosTratadosMonografia["idade"] * 70)
dadosTratadosMonografia["tempodeservico"] = round(dadosTratadosMonografia["tempodeservico"] * 48)

# print(dadosTratadosMonografia["idade"])

print("Atributos utilizados na classificacao:")
for a in atributosClassificacao:
    print("\"{}\"".format(a), end=", ")

# gerarModelos
# Arvore de decisao
if gerarModelos: # Controle para gerar ou não os modelos ao executar
    profundidade = 4
    profundidades = [] # Auxiliar para plottar gráficos de acurácia

    acuraciaTodos=[]
    acuraciaSociais=[]
    acuraciaPlataforma=[]
    acuraciaPrevios=[]
    acuraciaTempo1=[]
    acuraciaTempo2=[]


    aux = ["Reprovado", "Aprovado"]
    y = dadosTratadosMonografia ["aprovado"]

    #todos atributos
    X = dadosTratadosMonografia [atividadesRecuperacao]

    dt = DecisionTreeClassifier(max_depth=profundidade) #, random_state=99
    dt.fit(X, y)
    scores = cross_val_score(dt, X, y, cv=10)

    # scores = cross_validate.StratifiedKFold(dt, X, y, cv=10)
    print("\n\nqtd vizinhos: {} profundidade: {}".format(qtdVizinhos, profundidade))
    print("Accuracy todos atributos: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    acuraciaTodos.append(scores.mean())
    visualize_tree(dt, atividadesRecuperacao, aux, "Arvores/" + "atividadesRecuperacao.png")
    # visualize_tree(dt, atributosTempo1, aux, "Arvores/"+str(profundidade)+"atributosTempo1.png")

    # # Matriz de confusao
    # # calcula e imprime a matriz de confusao
    # predito = dt.predict(X)
    # matriz = mt.confusion_matrix(y, predito)
    # # mt.accuracy_score()
    #
    # print(matriz)
    # print("acuracia: ", mt.accuracy_score(y, predito))
    # # print("avg precision score: ", mt.average_precision_score(y, predito))
    # # normaliza a matriz de confusao e gera grafico
    # matriz = matriz / matriz.sum(axis=1)[:, np.newaxis]
    # cmap = plt.cm.Blues
    # plt.imshow(matriz, interpolation='nearest', cmap=cmap)
    # plt.colorbar()
    #
    # # iclasses = np.arange(len(iris.target_names))
    # iclasses = np.arange(2)
    #
    # aux = ["Reprovado", "Aprovado"]
    #
    # plt.xticks(iclasses, aux, rotation=45)
    # plt.yticks(iclasses, aux)
    # limiarCor = matriz.max() / 2.
    # for i, j in its.product(range(matriz.shape[0]), range(matriz.shape[1])):
    #     plt.text(j, i, format(matriz[i, j], '.2f'),
    #              horizontalalignment="center",
    #              color="white" if matriz[i, j] > limiarCor else "black")
    # plt.tight_layout()
    # plt.ylabel('Valores Esperados')
    # plt.xlabel('Valores Preditos')
    # plt.show()

    #atributos sociais
    X = dadosTratadosMonografia [atributosSociais]

    dt = DecisionTreeClassifier(min_samples_split=20) #, random_state=99
    dt.fit(X, y)
    scores = cross_val_score(dt, X, y, cv=10)
    print("Accuracy atributos sociais: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    acuraciaSociais.append(scores.mean())
    visualize_tree(dt, atributosSociais, aux, "Arvores/"+"minSamples20_AtributosSociais.png")
    # visualize_tree(dt, atributosSociais, aux, "Arvores/" + str(profundidade) + "atributosTempo2.png")

    # # Matriz de confusao
    # # calcula e imprime a matriz de confusao
    predito = dt.predict(X)
    matriz = mt.confusion_matrix(y, predito)
    print(matriz)
    print("acuracia: ", mt.accuracy_score(y, predito))
    # normaliza a matriz de confusao e gera grafico
    matriz = matriz / matriz.sum(axis=1)[:, np.newaxis]
    cmap = plt.cm.Blues
    plt.imshow(matriz, interpolation='nearest', cmap=cmap)
    plt.colorbar()

    iclasses = np.arange(2)

    aux = ["Reprovado", "Aprovado"]

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
    plt.savefig("Arvores/minSamples20_AtributosSociais_matrizConfusao.png")

    #atributos plataforma
    # X = dadosTratadosMonografia [atributosPlataforma]
    #
    # # dt = DecisionTreeClassifier(min_samples_split=20) #, random_state=99
    # dt.fit(X, y)
    # scores = cross_val_score(dt, X, y, cv=10)
    # print("Accuracy atributos plataforma: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    # acuraciaPlataforma.append(scores.mean())
    # visualize_tree(dt, atributosPlataforma, aux, "Arvores/"+str(profundidade)+"atributosPlataforma.png")

    # Matriz de confusao
    # # calcula e imprime a matriz de confusao
    # predito = dt.predict(X)
    # matriz = mt.confusion_matrix(y, predito)
    # print(matriz)
    # print("acuracia: ", mt.accuracy_score(y, predito))
    # # normaliza a matriz de confusao e gera grafico
    # matriz = matriz / matriz.sum(axis=1)[:, np.newaxis]
    # cmap = plt.cm.Blues
    # plt.imshow(matriz, interpolation='nearest', cmap=cmap)
    # plt.colorbar()
    #
    # # iclasses = np.arange(len(iris.target_names))
    # iclasses = np.arange(2)
    #
    # aux = ["Reprovado", "Aprovado"]
    #
    # plt.xticks(iclasses, aux, rotation=45)
    # plt.yticks(iclasses, aux)
    # limiarCor = matriz.max() / 2.
    # for i, j in its.product(range(matriz.shape[0]), range(matriz.shape[1])):
    #     plt.text(j, i, format(matriz[i, j], '.2f'),
    #              horizontalalignment="center",
    #              color="white" if matriz[i, j] > limiarCor else "black")
    # plt.tight_layout()
    # plt.ylabel('Valores Esperados')
    # plt.xlabel('Valores Preditos')
    # plt.show()

    # atributos previos
    # X = dadosTratadosMonografia[atributosSociaisPrevios]
    #
    # # dt = DecisionTreeClassifier(min_samples_split=20) #, random_state=99
    # dt.fit(X, y)
    # scores = cross_val_score(dt, X, y, cv=10)
    # print("Accuracy atributos plataforma: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    # acuraciaPrevios.append(scores.mean())
    # visualize_tree(dt, atributosSociaisPrevios, aux, "Arvores/" + str(profundidade) + "atributosSociaisPrevios.png")

    # profundidades.append(profundidade)
    # profundidade += 1
    # final do loop

    # Plottar gráfico de acurácia de acordo com variações de parâmetro - BEGIN
    # profundidades = [1,2,3,4]#,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    # from matplotlib.legend_handler import HandlerLine2D
    #
    # axes = plt.gca()
    # axes.set_ylim([0, 1])
    # line1, = plt.plot(4, acuraciaTodos, 'b', label="atributosTempo1")
    # plt.plot(profundidades, acuraciaSociais, 'r', label="atributosTempo2")
    # # plt.plot(profundidades, acuraciaPlataforma, 'g', label="Atributos de uso da plataforma")
    # # plt.plot(profundidades, acuraciaPrevios, 'y', label="Atributos previos")
    # plt.ylabel("Acurácia")
    # plt.xlabel("max_leaf_nodes")
    # plt.legend(handler_map={line1: HandlerLine2D(numpoints=2)})
    # plt.show()
    # Plottar gráfico de acurácia de acordo com variações de parâmetro - END

    # plt.title("idade")
    # plt.boxplot(dadosTratadosMonografia["idade"])
    # plt.show()
    #
    # plt.title("tempodeservico")
    # plt.boxplot(dadosTratadosMonografia["tempodeservico"])
    # plt.show()

    # for c in atributosPlataforma:
    #     plt.clf()
    #     plt.title(c)
    #     plt.boxplot(dadosTratadosMonografia[c])
    #     plt.show()
