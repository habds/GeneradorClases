from cmd import GenerarClase
dic={'NombreC':'Rol', 'atributo':['nombre','casado','edad','altura'],'tipo':['texto','boolean','numero','float']}
#indice=len(dic['atributo'])
#print(indice)
estado=False
clase = GenerarClase()
estado = clase.InicializarInit(dic)
print(estado)
