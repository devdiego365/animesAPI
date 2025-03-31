from flask import Flask, jsonify, request
from flask_cors import CORS
from random import choice
api = Flask(__name__)
CORS(api)

animes = ['Naruto','Pokemon','OnePiece','Solo Leveling','Sakura Card Captors','Dragon Ball','Spy x Family']

@api.route('/animes', methods = ['GET'])
def getAnimes():
    if len(animes)==0: return jsonify({"erro":"Nenhum anime entrado"}),404

    resposta ={
        "contagem":len(animes),
        "animes":animes
    }
    return jsonify(resposta),200

@api.route('/animes/ramdom', methods = ['GET'])
def getRandomAnime():
    if len(animes) == 0:return jsonify({"erro":"Nenhum anime encontrado"}),404

    resposta = {
        "anime":choice(animes)
    }
    return jsonify(resposta),200

@api.route('/animes/<int:id>', methods = ['GET'])
def getAnimeBtId(id:int):
    if (len(animes)==0) or (id < 0) or (id >=len(animes)):
        return jsonify({"erro":"Nenhum anime encontrado"}),404
    
    resposta = {
        "animes":animes[id]
    }
    return jsonify(resposta),200

@api.route('/anime/create', methods = ['POST'])
def addAnime():
    data = request.get_json()
    if ("anime" not in data): return jsonify({"erro":"você precisa fornecer um anime..."}),400
        
    anime = data["anime"].strip
    if(anime in animes):return jsonify({"erro":"esse anime ja existe"}),400

    animes.append(anime)
    print(f"{anime} foi inserido na base com sucesso")
    #animes.sort()
    return jsonify({"status":"success","message":f"O anime {anime} foi inserido com sucesso"}), 200

@api.route("/animes/update/<int:id>", methods = ["PUT"])
def updateAnime(id:int):
    if(len(animes)== 0) or (id < 0) or (id >= len(animes)):
        return jsonify({"erro":"nenhum anime encontrado"}),404
    data = request.get_json()
    if("anime" not in data ): return jsonify({"erro":"voce precisa fornecer o nome de um anime..."}),400

    animeAntigo = animes[id]
    animeNovo= data["anime"]
    animes[id] = animeNovo
    return jsonify ({"status":"success","message":f"O anime de id {id} foi alterado de {animeAntigo} para {animeNovo}"}), 200

@api.route("/animes/delete/<int:id>", methods = ["DELETE"])
def deleteAnime(id:int):
    if (len(animes)==0) or (id < 0) or (id >- len(animes)):
        return jsonify({"erro":"nenhum anime encontrado"}),404
    
    anime = animes[id]
    animes.remove(anime)
    return jsonify({"status": "success","message":f"O Anime {anime} de id {id} foi removido do sitema"}),200
