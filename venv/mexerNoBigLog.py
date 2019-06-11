import pandas as pd

# Lê o arquivo
log = pd.read_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/log.csv", sep='\t')

logAbril = pd.DataFrame()
logMaio = pd.DataFrame()
logJunho = pd.DataFrame()
logJulho = pd.DataFrame()
logAgosto = pd.DataFrame()
logSetembro = pd.DataFrame()
logOutubro = pd.DataFrame()
logNovembro = pd.DataFrame()
logDezembro = pd.DataFrame()

# logAbril = logAbril.append(log["abril" in log["17 dezembro 2014, 21:27"]])



for i in log.index:
    if (i%5000 == 0):
        print (i)
        logAbril.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logAbril.csv")

        logMaio.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logMaio.csv")

        logJunho.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logJunho.csv")

        logJulho.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logJulho.csv")

        logAgosto.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logAgosto.csv")

        logSetembro.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logSetembro.csv")
        logOutubro.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logOutubro.csv")
        logNovembro.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logNovembro.csv")
        logDezembro.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logDezembro.csv")

    if "abril" in log.loc[i]["17 dezembro 2014, 21:27"]:
        logAbril = logAbril.append(log.loc[i])
    elif "maio" in log.loc[i]["17 dezembro 2014, 21:27"]:
        logMaio = logMaio.append(log.loc[i])
    elif "junho" in log.loc[i]["17 dezembro 2014, 21:27"]:
        logJunho = logJunho.append(log.loc[i])
    elif "julho" in log.loc[i]["17 dezembro 2014, 21:27"]:
        logJulho = logJulho.append(log.loc[i])
    elif "agosto" in log.loc[i]["17 dezembro 2014, 21:27"]:
        logAgosto = logAgosto.append(log.loc[i])
    elif "setembro" in log.loc[i]["17 dezembro 2014, 21:27"]:
        logSetembro = logSetembro.append(log.loc[i])
    elif "outubro" in log.loc[i]["17 dezembro 2014, 21:27"]:
        logOutubro = logOutubro.append(log.loc[i])
    elif "novembro" in log.loc[i]["17 dezembro 2014, 21:27"]:
        logNovembro = logNovembro.append(log.loc[i])
    elif "dezembro" in log.loc[i]["17 dezembro 2014, 21:27"]:
        logDezembro = logDezembro.append(log.loc[i])

logAbril.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logAbril.csv")

logMaio.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logMaio.csv")

logJunho.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logJunho.csv")

logJulho.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logJulho.csv")

logAgosto.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logAgosto.csv")

logSetembro.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logSetembro.csv")
logOutubro.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logOutubro.csv")
logNovembro.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logNovembro.csv")
logDezembro.to_csv("/home/thiago/Desktop/ead-senad/preditores/logs/log.txt/logDezembro.csv")