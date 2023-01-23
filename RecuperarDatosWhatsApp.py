import os
class RecuperarDatosWhatsApp:
##Metodo que crea el archivo con la información recopilada
    
    @staticmethod
    def  crearArchivo(contenido):
        rutaArchivo='C:\\Users\\rober\\Desktop\\Pruebas.txt'## Escribir la ruta del archivo donde se va a guardar el archivo de la información extraida
        file = open(rutaArchivo, "w",encoding="ANSI") #Creacion del archivo donde se va a guardar los datos recopilados
        for i in contenido:##Lee cada dato extraido en el método anterior
            file.write(i)
        file.close()
    @staticmethod
    def lecturaArchivo(filtro):

        contenido=[] ##Lista donde se guardan los datos recopilados
        try:
            ##Escribir bien la ruta del LOG de Whatsapp
            filepath='C:\\Users\\rober\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ku33nvz3.default-release\\storage\\default\\https+++web.whatsapp.com\\idb\\3166453069wcaw.sqlite'
            
        ##Lee el fichero de datos y filtra la información según los datos a extraer
            palabraClave=""
            with open(filepath,encoding="ANSI") as lectura:
                for line in lectura:
                        
                        if "WANotification" in line:#Independientemente el tipo de mensaje aparece esto si es recibido
                                contenido.append(line)
                        if "getHighestAck" in line: #Independiente del mensaje si es enviado aparece esto#
                                contenido.append(line)
                        if "queryMsgInfo" in line: #Independiente del mensaje si es enviado o recibido aparece esto#
                                contenido.append(line)
                        if "proccessOrphanPeerReceipt" in line: #Independiente del mensaje si es enviado o recibido aparece esto#
                                contenido.append(line)    
                        if filtro=="audio":  
                            if "audio"in line:
                                contenido.append(line)   
                        if filtro=="documento":
                            if "doc"in line:
                                contenido.append(line)
                            if "pdf"in line:
                                contenido.append(line)
                            if "media" in line:
                                contenido.append(line)
                        if filtro=="video":
                            if "mp4"in line:
                                contenido.append(line)
                            if "video"in line:
                                contenido.append(line)
                            if "media" in line:
                                contenido.append(line)
                        if filtro=="imagen":
                            if "png"in line:
                                contenido.append(line)
                            if "jpeg"in line:
                                contenido.append(line)
                            if "image"in line:
                                contenido.append(line)
                            if "media" in line:
                                contenido.append(line)
                        if filtro=="reaccion":
                            if "processReactionOrphanPeerReceipt"in line:
                                contenido.append(line)
                            if "react"in line:
                                contenido.append(line)
                        if filtro=="contacto":
                            if "contact"in line:
                                contenido.append(line)
                            if "vcard"in line:
                                contenido.append(line)
                        if filtro=="ubicacion":
                            if "location"in line:
                                contenido.append(line)
                        if filtro=="busqueda":
                            if palabraClave in line:
                                contenido.append(line)
            RecuperarDatosWhatsApp.crearArchivo(contenido)
            print("Información extraida con éxito")
            print("La información se encuentra en la ruta C:\\Users\\rober\\Desktop\\Pruebas.txt")
        except:
            print("La ruta donde se encuentra el Log es incorrecta revísela")
        
        ##Ejecución del programa##
        
print("***********Introduce el dato a extraer**********")
print( "si necesitas ayuda pulsa help")
filtro=input()
while filtro=="help":
    print ("Según la información que quieres buscar tienes que escribir:  \n audio \n video \n imagen \n ubicacion \n documento \n reaccion \n contacto  \n helpsi lo que quieres es buscar una palabra escribe busqueda")
    filtro=input()
if(filtro=="busqueda"):
    print("Introduve la palabra a buscar :" )
    palabraclave=input();

ejecutar=RecuperarDatosWhatsApp()
ejecutar.lecturaArchivo(filtro)
print("************************************************")

