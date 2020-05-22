import time
# mombreRol="Persona"
# nombreRol=""
# atributo=[]
# tipo=[]
#dic={'NombreC':'Rol','atributo':['nombre','casado','edad','altura'],'tipo':['texto','boolean','numero','float']}
#dic={'NombreC':nombreRol,'atributo':atributo,'tipo':tipo}

#dic={'NombreC':'Rol', 'atributo':['nombre','casado','edad','altura'],'tipo':['texto','boolean','numero','float']}

#dic={'NombreC':[nombreRol,{'atributo':atributos,'tipo':tipos}]}

####
##  NOMBREC[0:ROL,1:PERSONA]
##  ATRIBUTO[0:[0:NOMBRE,1:CASADO,2:EDAD,3:ALTURA]]
##  TIPO[0:[0:TEXTO,1:BOOLEAN,2:NUMERO,3:FLOAT]]


# nombreClases=['Persona','Mujer','Animal']
# atributos=['nombre','casado','edad','altura']
# tipos=['texto','boolean','numero','float']nh
#                 0         1       2                             =3
nombreClases=['TiendaTipo','Metodo_Pago','Tipos_Pop_Anuncio','Coordenadas','Tienda','Map_Settings_Coordenadas',]

atributos=[['idTiendaTipo','TiendaTipo'],['code','TiendaTipo'],['descripcion','TiendaTipo'],
           ['idMetodo','Metodo_Pago'],['code','Metodo_Pago'],['descripcion','Metodo_Pago'],
           ['idTipo','Tipos_Pop_Anuncio'],['code','Tipos_Pop_Anuncio'],['descripcion','Tipos_Pop_Anuncio'],
           ['idCor','Coordenadas'],['longitud','Coordenadas'],['latitud','Coordenadas'],['estatus','Coordenadas'],
           ['idTienda','Tienda'],['nombre','Tienda'],['direccion','Tienda'],['email','Tienda'],['telefono','Tienda'],['ciudad','Tienda'],
           ['idMapS','Map_Settings_Coordenadas'],['categoria','Map_Settings_Coordenadas'],['estatus','Map_Settings_Coordenadas']]

tipos=[['numero','TiendaTipo','idTiendaTipo'],['texto','TiendaTipo','code'],['texto','TiendaTipo','descripcion'],
        ['numero','Metodo_Pago','idMetodo'],['texto','Metodo_Pago','code'],['texto','Metodo_Pago','descripcion'],
        ['numero','Tipos_Pop_Anuncio','idTipo'],['texto','Tipos_Pop_Anuncio','code'],['texto','Tipos_Pop_Anuncio','descripcion'],
        ['numero','Coordenadas','idCor'],['texto','Coordenadas','longitud'],['texto','Coordenadas','latitud'],['texto','Coordenadas','estatus'],
        ['numero','Tienda','idTienda'],['texto','Tienda','nombre'],['texto','Tienda','direccion'],['texto','Tienda','email'],['numero','Tienda','telefono'],['texto','Tienda','ciudad'],
        ['numero','Map_Settings_Coordenadas','idMapS'],['texto','Map_Settings_Coordenadas','categoria'],['texto','Map_Settings_Coordenadas','estatus'],]



#diccionario={'nombre':['matias',{'atributo':['apellido',{'tipo':'texto'},'edad',{'tipo':'int'}]},'vannia',{'atributo':['sexo',{'tipo':'bool'},'altura',{'tipo':'float'}]}}
diccionario={'nombres':nombreClases,'atributos':atributos,'tipos':tipos}

#diccionario={'nombre':['matias',{'atributo':['apellido',{'tipo':'texto'}]},'vannia',{'atributo':['sexo',{'tipo':'bool'}]}]}

#def Creador(nombre,)


