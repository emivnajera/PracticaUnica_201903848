import re
import json
import os

corriendo = True
donde = False
archivos = []
cuenta = 0
nombres = []
edad = []
activo = []
promedio = []
while(corriendo):
    entrada = input("Digite un Comando:")
    minus = entrada.casefold()
    comando = re.split(r'[,\s]',minus)
    cont = 1
    lim = len(comando)-1
    if(comando[0]=="cargar"):
        while (cont <= lim):
            with open(comando[cont]+".json") as data:
                info = json.load(data)
            archivos.append(info)
            cont = cont+1

    elif(comando[0]=="seleccionar"):
        for i in comando:
            if (i == "donde"):
                donde = True

        if (comando[1]=="*"):
            if(donde):
               if(comando[2]=="donde" and comando[4]=="="):
                print()
                for i in archivos:
                 for j in i:
                     if(str(j[comando[3]])==comando[5]):
                        print(j)
                        print()
            else:
                for i in archivos:
                    for j in i:
                        print(j)
                        print()

        elif(comando[1]!="*" and donde):
            pos1 = 0
            pos2 = 0
            con1 = 1
            while(comando[pos1]!="donde"):
                pos1 = pos1 + 1
            while (comando[pos2]!="="):
                pos2 = pos2 + 1
            while(con1 != pos1):
                for i in archivos:
                    for j in i:
                        if (str(j[comando[pos2-1]])==comando[pos2+1]):
                            print(j[comando[con1]])
                            print()
                con1=con1+1

    elif(comando[0]=="maximo"):
            max =0
            if(comando[1]=="edad"):
                for i in archivos:
                    for j in i:
                        if(int(j["edad"])>max):
                            max = j["edad"]
                print(max)
            elif(comando[1]=="promedio"):
                for i in archivos:
                    for j in i:
                        if(int(j["promedio"])>max):
                            max = j["promedio"]
                print(max)
    elif(comando[0]=="minimo"):
            min = 0
            if(comando[1]=="edad"):
                for i in archivos:
                    for j in i:
                        if(int(j["edad"])>min):
                            min = j["edad"]
                for i in archivos:
                    for j in i:
                        if(j["edad"]<min):
                            min = j["edad"]
                print(min)
            if(comando[1]=="promedio"):
                for i in archivos:
                    for j in i:
                        if (int(j["promedio"]) > min):
                            min = j["promedio"]
                for i in archivos:
                    for j in i:
                        if(j["promedio"]<min):
                            min = j["promedio"]
                print(min)
    elif(comando[0]=="suma"):
        suma = 0
        if(comando[1]=="edad"):
            for i in archivos:
                for j in i:
                    suma = suma + j["edad"]
            print(suma)
        if(comando[1]=="promedio"):
            for i in archivos:
                for j in i:
                    suma = suma + j["promedio"]
            print(suma)

    elif(comando[0]=="cuenta"):
        suma = 0
        for i in archivos:
            for j in i:
                suma = suma +1
        print(suma)
    elif(comando[0]=="reportar"):
        n = int(comando[1])
        for i in archivos:
            for j in i:
                nombres.append(j["nombre"])
                edad.append(j["edad"])
                activo.append(j["activo"])
                promedio.append(j["promedio"])

        if os.path.exists('Reporte.html'):
            if not os.path.isdir('Personas'):
                os.mkdir('Personas')
            with open('Reporte.html', 'r') as file:
                content = file.read()
                tabla = file.read()
            with open('Reporte.html', 'r') as file:
                content = file.read()
                tabla = file.read()
            cont = 0
            while(cont<n):
                content = content.replace('{Datos}',
                                              '<tr>\n<td><p>{Nombre' + str(cont) + '}</p></td>\n<td><p>{Edad' + str(
                                                  cont) + '}</p></td><td><p>{Activo' + str(
                                                  cont) + '}</p></td>\n<td><p>{Promedio' + str(
                                                  cont) + '}</p></td>\n</tr>\n<b>{Datos}</b>')
                cont = cont + 1
            content = content.replace('{Datos}', '')
            con = 0

            while(con<n):
                content = content.replace('{Nombre' + str(con) + '}', nombres[con])
                content = content.replace('{Edad' + str(con) + '}', str(edad[con]))
                content = content.replace('{Activo' + str(con) + '}', str(activo[con]))
                content = content.replace('{Promedio' + str(con) + '}', str(promedio[con]))
                con = con + 1

            with open('Personas/RegistroNuevo' + '.html', 'w') as file:
                file.write(content)
                print('Reporte Generado')
        else:
            print('no existe el archivo')
    elif(comando[0]=="salir"):
        corriendo = False






