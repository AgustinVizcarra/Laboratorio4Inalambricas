with open("TU_NOMBRE_DE_ARCHIVO.txt", "r") as f:
    lineas = f.readlines()
    info = []
    counter = 0
    bloques = 0
    cadena_Bloques = []
    k = 1
    bloque = []
    cadena_diccionarios = []
    mapeo = {}
    for linea in lineas:
        info=linea.split(" ")
        if(info[3] == "local"  ):
            #añado al contador
            counter += 1 
            if (counter <5):
                mapeo[info[2].strip("]")] = info[9]
        if(info[3] != "local"):
            #añado lineas
            bloque.append(info)
        if(counter == 5):
            cadena_diccionarios.append(mapeo)
            mapeo = {}
            counter = 1 #reseteo el contador
            cadena_Bloques.append(bloque)
            bloque = []
            mapeo[info[2].strip("]")] = info[9]
        k+=1
        if(k == len(lineas)):
            # he llegado al final del archivo
            cadena_Bloques.append(bloque)
            cadena_diccionarios.append(mapeo)
    #Itero
    j = 0
    cadena_Referencia = ["20.0-21.0","21.0-22.0","22.0-23.0","23.0-24.0","24.0-25.0"]
    #cadena_Referencia = ["25.0-26.0","26.0-27.0"]
    dataFinal = []
    for i in cadena_Bloques:
        matches = []
        for asociacion in cadena_diccionarios[j]:
            valoresMedidos = []
            match = []
            for arreglo in i:
                if(arreglo[3] in cadena_Referencia and arreglo[2].strip(']')== asociacion):
                    try:
                        valoresMedidos.append(float(arreglo[10]))
                    except:
                        try:
                            valoresMedidos.append(float(arreglo[9]))
                        except:
                            valoresMedidos.append(float(arreglo[7]))
            valor_Promedio = sum(valoresMedidos)/len(valoresMedidos)
            if valor_Promedio > 14:
                match = [asociacion, cadena_diccionarios[j][asociacion],valor_Promedio/1000]
            else:
                match = [asociacion, cadena_diccionarios[j][asociacion],valor_Promedio]
            matches.append(match)
        dataFinal.append(matches)
        j += 1
for data in dataFinal:
    suma = 0
    for valor in data:
        match valor[1] :
            case "10.0.0.1":
                print("El nodo 1 tiene througputh: "+str(valor[2]))
                suma += valor[2]
            case "10.0.0.2":
                print("el nodo 2 tiene throughput: "+str(valor[2]))
                suma += valor[2]
            case "10.0.0.3":
                print("el nodo 3 tiene throughput: "+str(valor[2]))
                suma += valor[2]
            case "10.0.0.4":
                print("el nodo 4 tiene throughput: "+str(valor[2]))
                suma += valor[2]
            case _:
                print("Algo malo ocurre")
    print("El throughput total es "+ str(suma))
    print("-----Siguiente iteracion------------")
            