import json

from mongodb import PyMongo

# Juan Jose Navarrete Garibay  NC:18420470

vars = {}
vars["host"] = "localhost"
vars ["user"] = ""
vars ["password"] = ""
#El nombre de la base de datos es opensource
vars ["bd"] = "opensource"
vars["port"] = "27017"
vars["timeout"] = 1000


res={}
def consultar_materias():
    obj_PyMongo = PyMongo(vars)

    ctrl = input("Dame el número de control: ")

    filtro = {"control": ctrl}
    atributos_est = {"_id": 0, "nombre": 1}
    atributos_mat = {"_id": 0, "materia": 1, "calificacion": 1}

    obj_PyMongo.conectar_mongodb()
    respuesta1 = obj_PyMongo.consulta_mongodb('estudiantes', filtro, atributos_est)
    respuesta2 = obj_PyMongo.consulta_mongodb('kardex', filtro, atributos_mat)

    obj_PyMongo.desconectar_mongodb()
    print()
    diccionario={}
    if respuesta1["status"] and respuesta2["status"]:
        h=respuesta1["resultado"][0]["nombre"]


        diccionario["Estudiante"]= h

        arreglo=[]
        for mat in respuesta2["resultado"]:
            diccionario2 = {}
            diccionario2["Materia"] = mat["materia"]
            diccionario2["Calificacion"]=mat["calificacion"]
            arreglo.append(diccionario2)

        diccionario["Materias"]=arreglo
    else:
        print("No encontrado")

    jsontext=json.dumps(diccionario,indent=4)
    print(jsontext)

consultar_materias()