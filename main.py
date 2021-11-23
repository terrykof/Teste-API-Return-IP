from socket import *


def insertSite(site):
    # adiciona via jason
    nome = site
    ip = gethostbyname(nome)

    return {"site": nome, "Ip": ip}
