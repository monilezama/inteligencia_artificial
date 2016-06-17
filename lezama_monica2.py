#MONICA MICHELLE LEZAMA POZOS
#03/JUNIO/2016
#TAREA 1
#IMPLEMENTACION DE LOS ALGORITMOS DE BUSQUEDA NO INFORMADA BPA, BPP
#BPP ALGORITMO QUE BUSCA LA RUTA DESDE UN PUNTO DE INICIO HACIA UNA META, BUSCA EN PROFUNDIDAD, NO SIEMPRE ES LA MAS OPTIMA
ciudades={0:'Avignon', 1:'Bordeaux',2:'Brest',3:'Caen',4:'Calais',5:'Dijon',6:'Grenoble',7:'Limoges',8:'Lyon',9:'Marsella',10:'Montpellier',11:'Nancy',12:'Nantes',13:'Nice',14:'Paris',15:'Rennes',16:'Strasbourg',17:'Toulouse'}

sucesores={0:[6,8,9,10],1:[7,12,17],2:[15],3:[4,14,15],4:[3,14,16],5:[8,11,14,16],6:[0,8],7:[1,8,12,14,17],8:[0,5,6,7],9:[0,13],10:[0,17],11:[4,5,14,16],12:[1,7,15],13:[9],14:[3,4,5,7,11,15],15:[2,3,12,14],16:[5,11],17:[1,7,10]}

distancias = [ [0,0,0,0,0,0,227,0,216,99,91,0,0,0,0,0,0,0],    #0
               [0,0,0,0,0,0,0,220,0,0,0,0,329,0,0,0,0,253],    #1
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,244,0,0],        #2
               [0,0,0,0,120,0,0,0,0,0,0,0,0,0,241,176,0,0],    #3
               [0,0,0,120,0,0,0,0,0,0,0,534,0,0,297,0,0,0],    #4
               [0,0,0,0,0,0,0,0,192,0,0,201,0,0,313,0,335,0],  #5
               [227,0,0,0,0,0,0,0,104,0,0,0,0,0,0,0,0,0],      #6
               [0,220,0,0,0,0,0,0,389,0,0,0,329,0,396,0,0,313],#7
               [216,0,0,0,0,192,104,389,0,0,0,0,0,0,0,0,0,0],  #8
               [99,0,0,0,0,0,0,0,0,0,0,0,0,188,0,0,0,0],       #9
               [91,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,240],       #10
               [0,0,0,0,534,201,0,0,0,0,0,0,0,0,372,0,145,0],  #11
               [0,329,0,0,0,0,0,329,0,0,0,0,0,0,0,107,0,0],    #12
               [0,0,0,0,0,0,0,0,0,188,0,0,0,0,0,0,0,0],        #13
               [0,0,0,241,297,313,0,396,0,0,0,372,0,0,0,348,0,0],#14
               [0,0,244,176,0,0,0,0,0,0,0,0,107,0,348,0,0,0],  #15
               [0,0,0,0,0,335,0,0,0,0,0,145,0,0,0,0,0,0],      #16
               [0,253,0,0,0,0,0,313,0,0,240,0,0,0,0,0,0,0]]    #17




			
	
def ruta(Ce,meta):
        costo=0
	Ruta=[]
	Convertida=[]
	Ruta.append(meta)
	for llave,hijos in Ce.items():
		if Ce.has_key(meta):
			nodo=Ce[meta]
			if nodo is not None:
				costo = costo + distancias[meta][nodo]
				
			Ruta.append(nodo)
			meta=nodo
			
		
			
	Ruta.reverse()
	
	for x in Ruta:
		if ciudades.has_key(x):
			Convertida.append(ciudades[x])
	
	print "Ruta con el algoritmo de BPP", Convertida
	print "costo total",costo
	
	
			
				               
				
	
	
	
	
			

def Busqueda(inicio,meta):
	estado=False 
	Ce ={} 
	Ab=[(inicio,None)]
	Hijos=[]	
	while Ab and not estado:   
		nodo=Ab.pop(0)
		
		Ce[nodo[0]]=nodo[1]
		
		if Ce.has_key(meta):
			estado=True
			ruta(Ce,meta)
			
		else:
				if sucesores.has_key(nodo[0]):
					Hijos=[(y,nodo[0]) for y in sucesores[nodo[0]] if  not Ce.has_key(y)]
				
				for nodo in Hijos:
					Ab.insert(0,nodo)
				
	if not estado:
		print "fracaso"
		

			
			

ciudad=raw_input("Ingrese ciudad de inicio ")
for llave,valor in ciudades.items():
	value=ciudades.get(llave,0)
	if value==ciudad:
		inicio=llave
		
	
destino=raw_input("Ingrese ciudad de destino ")
for llave,valor in ciudades.items():
	value=ciudades.get(llave,0)
	if value==destino:
		meta=llave
		

Busqueda(inicio,meta)


#--------------------------------------------
#Salidas:
#Busquedas de Paris a Strasbourg:
#
#Ingrese ciudad de inicio Paris
#Ingrese ciudad de destino Strasbourg
#Ruta con el algoritmo de BPP ['Paris', 'Rennes', 'Nantes', 'Limoges', 'Toulouse', 'Montpellier', 'Avignon', 'Lyon', 'Dijon', #'Strasbourg']
#costo total 2171
#
#Busqueda Strasbourg a Paris:
#
#Ingrese ciudad de inicio Strasbourg
#Ingrese ciudad de destino Paris
#Ruta con el algoritmo de BPP ['Strasbourg', 'Nancy', 'Paris']
#costo total 517
#
#Busqueda Bordeaux a Lyon:
#
#Ingrese ciudad de inicio Bordeaux
#Ingrese ciudad de destino Lyon
#Ruta con el algoritmo de BPP ['Bordeaux', 'Toulouse', 'Montpellier', 'Avignon', 'Lyon']
#costo total 800
#
#Busqueda Lyon a Bordeaux:
#
#Ingrese ciudad de inicio Lyon
#Ingrese ciudad de destino Bordeaux
#Ruta con el algoritmo de BPP ['Lyon', 'Limoges', 'Toulouse', 'Bordeaux']
#costo total 955
#--------------------------------------------