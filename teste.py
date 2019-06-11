import pandas as pd

# Lê o arquivo
dadosTratadosMonografia = pd.read_csv("dadosTeste.csv")

# # Dataframe para armazenar e manipular os dados tratados
# dadosTratadosMonografia = pd.DataFrame()

# motivopart
dadosTratadosMonografia["Identificação pessoal com o tema (motivopart)"] = 0
dadosTratadosMonografia["Identificação profissional com o tema (motivopart)"] = 0
dadosTratadosMonografia["Para aquisição de conhecimento na área (motivopart)"] = 0
dadosTratadosMonografia["Pelo fato de o curso ser gratuito (motivopart)"] = 0
dadosTratadosMonografia["Pelo fato de o curso estar vinculado à Universidade (motivopart)"] = 0
dadosTratadosMonografia["Por ser um curso à distância (motivopart)"] = 0
dadosTratadosMonografia["Por ser uma oportunidade de formação continuada (motivopart)"] = 0

# barreiras
dadosTratadosMonografia["Ausência da família (barreiras)"] = 0
dadosTratadosMonografia["Pouca comunicação com os pais (barreiras)"] = 0
dadosTratadosMonografia["Uso de substâncias por familiares (barreiras)"] = 0
dadosTratadosMonografia["Presença de drogas ilícitas no ambiente escolar (barreiras)"] = 0
dadosTratadosMonografia["Proximidade da rede de distribuição de drogas (barreiras)"] = 0
dadosTratadosMonografia["Ausência de limites dos alunos (barreiras)"] = 0
dadosTratadosMonografia["Ausência de colaboração da equipe escolar (barreiras)"] = 0
dadosTratadosMonografia["Ausência de regras no ambiente escolar (barreiras)"] = 0

# facilitadores
dadosTratadosMonografia["Possuir alunos interessados na temática (facilitadores)"] = 0
dadosTratadosMonografia["Presença de uma equipe para trabalhar a temática (facilitadores)"] = 0
dadosTratadosMonografia["Estímulo aos alunos (facilitadores)"] = 0
dadosTratadosMonografia["Desenvolvimento de projetos na escola (facilitadores)"] = 0
dadosTratadosMonografia["Apoio aos projetos em desenvolvimento (facilitadores)"] = 0
dadosTratadosMonografia["Presença de regras no ambiente escolar (facilitadores)"] = 0
dadosTratadosMonografia["Promoção de compromisso e confiança (facilitadores)"] = 0
dadosTratadosMonografia["Valorização do ambiente escolar (facilitadores)"] = 0
dadosTratadosMonografia["Participação da comunidade e dos pais no trabalho de prevenção (facilitadores)"] = 0

for i in dadosTratadosMonografia.index:
    if "Pelo fato de o curso ser gratuito".find(str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
        dadosTratadosMonografia.at[i, "Identificação pessoal com o tema (motivopart)"] = 1

    if "Identificação profissional com o tema".find(str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
        dadosTratadosMonografia.at[i, "Identificação profissional com o tema (motivopart)"] = 1

    if "Para aquisição de conhecimento na área".find(str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
        dadosTratadosMonografia.at[i, "Para aquisição de conhecimento na área (motivopart)"] = 1

    if "Pelo fato de o curso ser gratuito".find(str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
        dadosTratadosMonografia.at[i, "Pelo fato de o curso ser gratuito (motivopart)"] = 1

    if "Pelo fato de o curso estar vinculado à Universidade".find(
            str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
        dadosTratadosMonografia.at[i, "Pelo fato de o curso estar vinculado à Universidade (motivopart)"] = 1

    if "Por ser um curso à distância".find(str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
        dadosTratadosMonografia.at[i, "Por ser um curso à distância (motivopart)"] = 1

    if "Por ser uma oportunidade de formação continuada".find(
            str(dadosTratadosMonografia.loc[i]["motivopart"])) >= 0:
        dadosTratadosMonografia.at[i, "Por ser uma oportunidade de formação continuada (motivopart)"] = 1

    if "Ausência da família".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
        dadosTratadosMonografia.at[i, "Ausência da família (barreiras)"] = 1

    if "Pouca comunicação com os pais".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
        dadosTratadosMonografia.at[i, "Pouca comunicação com os pais (barreiras)"] = 1

    if "Uso de substâncias por familiares".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
        dadosTratadosMonografia.at[i, "Uso de substâncias por familiares (barreiras)"] = 1

    if "Presença de drogas ilícitas no ambiente escolar".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
        dadosTratadosMonografia.at[i, "Presença de drogas ilícitas no ambiente escolar (barreiras)"] = 1

    if "Proximidade da rede de distribuição de drogas".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
        dadosTratadosMonografia.at[i, "Proximidade da rede de distribuição de drogas (barreiras)"] = 1

    if "Ausência de limites dos alunos".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
        dadosTratadosMonografia.at[i, "Ausência de limites dos alunos (barreiras)"] = 1

    if "Ausência de colaboração da equipe escolar".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
        dadosTratadosMonografia.at[i, "Ausência de colaboração da equipe escolar (barreiras)"] = 1

    if "Ausência de regras no ambiente escolar".find(str(dadosTratadosMonografia.loc[i]["barreiras"])) >= 0:
        dadosTratadosMonografia.at[i, "Ausência de regras no ambiente escolar (barreiras)"] = 1

    if "Possuir alunos interessados na temática".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
        dadosTratadosMonografia.at[i, "Possuir alunos interessados na temática (facilitadores)"] = 1

    if "Presença de uma equipe para trabalhar a temática".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
        dadosTratadosMonografia.at[i, "Presença de uma equipe para trabalhar a temática (facilitadores)"] = 1

    if "Estímulo aos alunos".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
        dadosTratadosMonografia.at[i, "Estímulo aos alunos (facilitadores)"] = 1

    if "Desenvolvimento de projetos na escola".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
        dadosTratadosMonografia.at[i, "Desenvolvimento de projetos na escola (facilitadores)"] = 1

    if "Apoio aos projetos em desenvolvimento".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
        dadosTratadosMonografia.at[i, "Apoio aos projetos em desenvolvimento (facilitadores)"] = 1

    if "Presença de regras no ambiente escolar".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
        dadosTratadosMonografia.at[i, "Presença de regras no ambiente escolar (facilitadores)"] = 1

    if "Promoção de compromisso e confiança".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
        dadosTratadosMonografia.at[i, "Promoção de compromisso e confiança (facilitadores)"] = 1

    if "Valorização do ambiente escolar".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
        dadosTratadosMonografia.at[i, "Valorização do ambiente escolar (facilitadores)"] = 1

    if "Participação da comunidade e dos pais no trabalho de prevenção".find(str(dadosTratadosMonografia.loc[i]["facilitadores"])) >= 0:
        dadosTratadosMonografia.at[i, "Participação da comunidade e dos pais no trabalho de prevenção (facilitadores)"] = 1

dadosTratadosMonografia.to_csv("dadosTesteTratados.csv")