from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json


# pip install flask-cors
app = Flask("Minha API")
CORS(app)  # Ativa cors

def carregar_arquivos():
    caminho_arquivo = os.path.join("data", "clientes.json")

    print(f"Verificando caminho: {caminho_arquivo}")

    try:
        with open(caminho_arquivo, "r") as arq:
            return json.load(arq)

    except Exception:
        return "Falha ao carregar o arquivo"

@app.route("/consulta", methods=["GET"])
def consulta_cadastro():
    documento = request.args.get("doc")
    registro = dados(documento)
    return registro

@app.route("/cadastro", methods=["POST"])
def cadastrar():
    payload = request.json
    cpf = payload.get("cpf")
    if existe_registro(cpf):
        return jsonify(True)
    reg = payload.get("dados")
    salvar_dados(cpf, reg)
    return jsonify(False)

def dados(cpf):
    dados_pessoas = carregar_arquivos()
    print(dados_pessoas)
    vazio = {
        "nome": "Nao encontrado",
        "data_nascimento": "Nao encontrado",
        "email": "Nao encontrado",
    }
    chave = dados_pessoas.get(cpf, vazio)
    return chave

def gravar_arquivo(dados):
    caminho_arquivo = os.path.join("data", "clientes.json")

    try:
        with open(caminho_arquivo, "w") as arq:
            json.dump(dados, arq, indent=4)
            return "Dados armazenados"
    except Exception:
        return "Falha ao carregar o arquivo"

def salvar_dados(cpf, reg):
    dados_pessoas = carregar_arquivos()
    dados_pessoas[cpf] = reg
    gravar_arquivo(dados_pessoas)
    ordena_json()

def ordena_json():
    arquivo_json = carregar_arquivos()
    sorted_items = sorted(arquivo_json.items(), key=chave_nome)
    dicionario_ordenado = dict(sorted_items)
    gravar_arquivo(dicionario_ordenado)

def chave_nome(itens):
    return itens[1]["nome"]

def existe_registro(cpf):
    dados_pessoas = carregar_arquivos()
    return cpf in dados_pessoas.keys()





if __name__ == "__main__":
    app.run()
    