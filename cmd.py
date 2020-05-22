import os

class GenerarClase():
    #Switch para saber si el archivo esta abierto
    sw=False

    #Limpio el archivo del texto
    #nombre (String): Nombre del archivo a limpiar
    def LimpiarArchivo(self, nombre):
        estado=False
        if self.sw == False:
            archivo=open(nombre+".py","w")
            self.sw = True
            if self.sw:
                print("Limpiar archivo :Se activo el switch luego de abrirlo")
                #si se lograr cerrar el archivo devuelve True
                estadoR=self.Cerrar(archivo)
                
                if estadoR:
                    estado=True
                    print("Limpiar archivo :Se limpio el archivo")
        else:
            print("Limpiar archivo: No se pudo limpiar el archivo")
        return estado

    #Cierro el archivo
    #archivo (archivo:IO): variable tipo archivo #archivo=open()
    #Devuelve un estado(boolean):
                                #False: No se pudo cerrar el archivo
                                #True: Se cerro el archivo
    def Cerrar(self, archivo):
        estado=False
        if self.sw==True:
            archivo.close()
            self.sw=False
            estado=True
            print("Cerrar: Se cerro el correctamente el archivo")
        else:
            print("Cerrar: No se cerro el archivo ya que no estaba abierto")
        return estado
            

    #Obtengo el dato NombreC que se usara para nombrar la clase
    def ObtenerNombre(self, dic):
        nombre=""
        try:
            nombre=str(dic['NombreC'])
        except Exception:
            nombre="Error"
        return nombre
    
    #Genero un archivo con terminación .py
    #dic (dict): Se envia un diccionario con los datos
    #Orden de los datos={'NombreC':'Rol', 'atributo':['nombre1','nombre2','nombre3','nombre4'],'tipo':['texto','numero','texto','numero','texto','numero']}
    #retorna una boolean:
                        #False: El archivo no pudo ser creado
                        #True: El archivo se creo
    def CrearArchivo(self, dic):
        nombre=self.ObtenerNombre(dic)
        estado=False
        try:
            #creo el archivo
            os.system("PowerShell 'Borrar' > "+nombre+".py")
            #Limpio el archivo y devuelve True si todo salio bien
            estado=self.LimpiarArchivo(nombre)
            #Lo cierro para guardar los cambios, el sw para a False
            #self.Cerrar(archivo)
            if self.sw==False:
                print("Correcto, Esta cerrado el archivo")
            #edito el archivo
            archivo=self.AbrirArchivo(nombre)
            archivo.write("class "+nombre+"(): \n")
            #cierra el archivo, ¿para qué?, no sé
            archivo.close()
            estado=True
            print("Se creo correctamente el archivo "+ nombre)
        except Exception as e:
            estado=False
            print(str(e))
        return estado

    #Calcula el indice de las clases a crear
    #dic (diccionario)
    def Indice(self, dic):
        indice=len(dic['atributo'])
        return indice
    
    

    #Se utiliza para darle valores a las variables
    #dic (diccionario)
    #respuesta(lista): devulve una lista
    def Inicializar(self,dic):
        respuesta=[]
        nIndice=self.Indice(dic)
        for indice in range(0,nIndice):
            tipo=dic['tipo'][indice]
            atributo=dic['atributo'][indice]
            if tipo =='texto':
                respuesta.append(atributo+" = ''")
            if tipo =='numero':
                respuesta.append(atributo+" = 0")
            if tipo =='boolean':
                respuesta.append(atributo+" = False")
            if tipo == 'float':
                respuesta.append(atributo+" = 0.0")
        return respuesta


    def InicializarInit(self,dic):
        respuesta=""
        numero=0
        nIndice=self.Indice(dic)
        for indice in range(0,nIndice):
            tipo=dic['tipo'][indice]
            atributo=dic['atributo'][indice]
            if numero<=indice:
                if tipo =='texto':
                    respuesta += ","+ atributo+" = ''"
                if tipo =='numero':
                    respuesta += ","+ atributo+" = 0"
                if tipo =='boolean':
                    respuesta += ","+ atributo+" = False"
                if tipo == 'float':
                    respuesta += ","+ atributo+" = 0.0"
                numero+=1
            else:
                if tipo =='texto':
                    respuesta += atributo+" = ''"
                if tipo =='numero':
                    respuesta += atributo+" = 0"
                if tipo =='boolean':
                    respuesta += atributo+" = False"
                if tipo == 'float':
                    respuesta += atributo+" = 0.0"
                numero+=1
        return respuesta

    def CrearSelf(self,dic):
        respuesta=[]
        numero=0
        nIndice=self.Indice(dic)
        for indice in range(0,nIndice):
            atributo=dic['atributo'][indice]
            rSelf=""
            rSelf="      self."+atributo+" = "+atributo
            respuesta.append(rSelf)
            numero+=1
        return respuesta

    #Genera la función __init__
    #respuesta (String): la variable contiene los atributos inicializados y devuelve el titulo
    def CrearInit(self,respuesta):
        salida = ''
        salida ="   def __init__(self"+respuesta+"): \n"
        return salida

    #Agrega al documento el texto
    #texto (String): devuelve un estado boolean con la respuesta
    #devuelve un estado: 
                        #False: No se pudo escribir en el archivo
                        #True: Se escribio en el archivo
    def AgregarTexto(self, texto, nombre):
        estado=False
        archivo=self.AbrirArchivo(nombre)
        archivo.writelines(texto)
        estado=True
        return estado

    #Agrego los self.valor=valor con un for
    def AgregarTextoS(self, nombre,respuesta):
        estado=False
        estadoR=False
        try:
            numero=0
            archivo=self.AbrirArchivo(nombre)
            for Self in range(0,len(respuesta)):
                archivo.writelines(respuesta[numero]+"\n")
                print("Contador :"+str(numero))
                print("Cantidad de :"+str(Self))
                if numero==len(respuesta)-1:
                    estadoR=self.Cerrar(archivo)
                if estadoR:
                    estado=True
                numero +=1
        except Exception as e:
            print(str(e))
        return estado

    

    #Abre el archivo con el nombre
    #nombre (String): nombre del archivo para poder abrirlo
    #devuelve un estado: 
                        #False: No se pudo abrir el archivo
                        #True: Se abrio el archivo
    def AbrirArchivo(self, nombre):
        archivo=open("log.txt","a")
        self.sw=True
        estadoR=self.Log(archivo, nombre)
        if estadoR:
            #if self.sw == False:
            archivo=open(nombre+".py","a")
            self.sw=True
            print("Se logro abrir el archivo para modificarlo")
        return archivo

    #Funcion principal para generar las clases
    #Variable dic tipo Diccionario
    #retorna una estado tipo boolean:
                                    #True: Se genero la clase
                                    #False: No se genero la clase
    def Principal(self, dic):
        estado=False
        estadoR=self.CrearArchivo(dic)
        try:
            if estadoR:
                print("ETAPA 1/6: ARCHIVO CREADO")
                estadoInicializarInit=False
                estadoInicializarInit=self.InicializarInit(dic)
                if estadoInicializarInit !="":
                    print("ETAPA 2/6: CREADO TEXTO PARA INIT")
                    estadoInit=""
                    estadoInit=self.CrearInit(estadoInicializarInit)
                    if estadoInit !="":
                        print("ETAPA 3/6 INIT GENERADO")
                        nombre=self.ObtenerNombre(dic)
                        if nombre !="":
                            print("ETAPA 4/6 NOMBRE DEL ARCHIVO HA SIDO RECUPERADO")
                            estadoAgregar=False
                            estadoAgregar=self.AgregarTexto(estadoInit,nombre)
                            if estadoAgregar:
                                print("ETAPA 5/6 INIT COMPLETO")
                                estadoCrearSelf=[]
                                estadoCrearSelf=self.CrearSelf(dic)
                                print(estadoCrearSelf)
                                print("CANTIDAD DE SELF CREADOS: "+str(len(estadoCrearSelf)))
                                print("ETAPA 6/6 SELF GENERADOS CON :"+str(len(estadoCrearSelf)))
                                if len(estadoCrearSelf)>0:
                                    estadoAgregarS=False
                                    estadoAgregarS=self.AgregarTextoS(nombre,estadoCrearSelf)
                                    if estadoAgregarS:
                                        print("ETAPA 7/6 SELF INSERTADOS EN EL TEXTO")
                                        listadoSet=[]
                                        listadoSet=self.CrearSet(dic)
                                        print("Cantidad Set a generar :"+str(len(listadoSet)))
                                        estadoR=False
                                        estadoR=self.AgregarTextoSet(nombre,listadoSet)
                                        if estadoR:
                                            print("ETAPA 7/6 SE CREARON LAS FUNCIONES SET")
                                            listaGet=self.CrearGet(dic)
                                            if len(listaGet)>0:
                                                estadoR=self.AgregarTextoGet(nombre,listaGet)
                                                if estadoR:
                                                    print("ETAPA 8/8 SE INSERTARON LAS FUNCIONES GET")
                                                    listAtributo=self.getAtributos(dic)
                                                    if len(listAtributo)>0:
                                                        metodoStr=self.CrearSTR(dic)
                                                        if len(metodoStr)>0:
                                                            estadoR=self.AgregarTextoStr(nombre,metodoStr)
                                                            if estadoR:
                                                                print("ETAPA 9/9 SE INSERTO LA FUNCION STR")
                                                                

                                                            estado=True

        
            #print("Se creo el archivo")
        except Exception as e:
            print(str(e))
        return estado

    #Guardare un log de los errores para su posterior comprension
    def Log(self, archivo, nombre):
        estado=False
        estadoR=self.Cerrar(archivo)
        if estadoR:
            estado=True
        else:
            texto="No se logro abrir el archivo con nombre: "+nombre
            self.AgregarError(texto,archivo)
        return estado


    def AgregarError(self, texto, archivo):
        archivo.write(texto)
        #return estado
    #Genera los set
    def CrearSet(self, dic):
        respuesta=[]
        numero=0
        nIndice=self.Indice(dic)
        for indice in range(0,nIndice):
            atributo=dic['atributo'][indice]
            #if indice==0:
            respuesta.append(" ")
            nombreM=""
            nombreM=str(atributo.capitalize())
            respuesta.append("   def set"+nombreM+"(self, "+atributo+"):")
            respuesta.append("      self."+atributo+" = "+atributo)
            numero+=1
        #else:
            #respuesta.append("      self."+atributo+" = "+atributo)    
            numero+=1
        return respuesta
    ######
    #Verion modificada para crear los def setNombre..
    #Agrego los self.valor=valor con un for
    def AgregarTextoSet(self, nombre,respuesta):
        estado=False
        estadoR=False
        try:
            numero=0
            archivo=self.AbrirArchivo(nombre)
            for Self in range(0,len(respuesta)):
                archivo.writelines(respuesta[numero]+"\n")
                print("Contador :"+str(numero))
                print("Cantidad de :"+str(Self))
                if numero==len(respuesta)-1:
                    estadoR=self.Cerrar(archivo)
                if estadoR:
                    estado=True
                numero +=1
        except Exception as e:
            print(str(e))
        return estado

    #Agrega las funciones get al archivo
    def AgregarTextoGet(self, nombre,respuesta):
        estado=False
        estadoR=False
        try:
            numero=0
            archivo=self.AbrirArchivo(nombre)
            for Self in range(0,len(respuesta)):
                archivo.writelines(respuesta[numero]+"\n")
                print("Contador :"+str(numero))
                print("Cantidad de :"+str(Self))
                if numero==len(respuesta)-1:
                    estadoR=self.Cerrar(archivo)
                if estadoR:
                    estado=True
                numero +=1
        except Exception as e:
            print(str(e))
        return estado

    #Genera el texto la funcion
    def CrearGet(self, dic):
        respuesta=[]
        numero=0
        nIndice=self.Indice(dic)
        for indice in range(0,nIndice):
            atributo=dic['atributo'][indice]
            #if indice==0:
            respuesta.append(" ")
            nombreM=""
            nombreM=str(atributo.capitalize())
            respuesta.append("   def get"+nombreM+"(self):")
            respuesta.append("      return self."+atributo)
            numero+=1    
        return respuesta    

    #Genera la funcion __str__
    def CrearSTR(self, dic):
        respuesta=[]
        numero=0
        retorno = ""
        nIndice=self.Indice(dic)
        litadoAtributo=self.getAtributos(dic)
        try:
            if len(litadoAtributo)>0:
                retorno="      return str(self."
                respuesta.append(" ")
                respuesta.append("   def __str__(self):")
                for indice in range(0,nIndice):
                    atributo=litadoAtributo[indice]
                    if indice==0:
                        retorno+=""+atributo+")"
                    if indice > 0 <indice:
                        retorno+=", str(self."+atributo+")" 
                    if indice==nIndice:
                        retorno+=", str(self."+atributo+"))"
                
                numero+=1 
                
                respuesta.append(retorno)
        except Exception as e:
            print("Error en CrearStr :"+str(e))
        return respuesta    

    #Obtengo los atributos de la clase
    def getAtributos(self,dic):
        respuesta=[]
        numero=0
        nIndice=self.Indice(dic)
        for indice in range(0,nIndice):
            atributo=dic['atributo'][indice]
            respuesta.append(atributo)
            numero+=1
        return respuesta

    def AgregarTextoStr(self, nombre,respuesta):
        estado=False
        estadoR=False
        try:
            numero=0
            archivo=self.AbrirArchivo(nombre)
            for Self in range(0,len(respuesta)):
                archivo.writelines(respuesta[numero]+"\n")
                print("Contador :"+str(numero))
                print("Cantidad de :"+str(Self))
                if numero==len(respuesta)-1:
                    estadoR=self.Cerrar(archivo)
                if estadoR:
                    estado=True
                numero +=1
        except Exception as e:
            print("ERROR EN AgregarTextoStr "+str(e))
        return estado





    
    

        
        

    



