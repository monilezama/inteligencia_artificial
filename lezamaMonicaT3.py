

# Este archivo contiene un programa con varias funciones incompletas, que el 
# usuario tiene que terminar.
# Las configuraciones del tablero son una lista de listas 
# pe meta = [[1,2,3],[8,0,4],[7,6,5]] donde 0 es el blanco
# Ab es una lista de tuple de la forma (node,padre,f(n),g(n))
# g(n) es la longitud del camino al nodo, f(n) = g(n) + h(n)
# donde h puede ser una de 3 funciones heuristicas h1,h2,h3 (nota: h2,h3 falta terminar)
# Ce es un diccionario que contiene el nodo como una tuple de tuples para ser la llave
# y un valor una lista de [padre, f(n), g(n)]
# falta completar h2 (tejas fuera de lugar), h3 (distancia de Manhattan)
# suces, la función que genera los sucesores de un nodo
# moverD, moverA, moverAb
# El codigo es basico y falta pe incluir un interfaz del usuario
# para copiando importamos copy y usamos deepcopy

import copy

# los sucesores estan tomados en el orden I, D, A, Ab
def suces(estado):  
  pos = [(i,j) for i in range(3) for j in range(3) if estado[i][j] == 0]
  fila = pos[0][0]
  col = pos[0][1]
  sucesores = []
  if fila == 0 and col == 0:    
    sucesores.append(moverD(estado, fila, col))
    sucesores.append(moverAb(estado, fila, col))
  elif fila == 0 and col == 2:
        sucesores.append(moverIz(estado,fila,col))
        sucesores.append(moverAb(estado,fila,col))
  elif fila == 0 and col ==1:
      sucesores.append(moverIz(estado,fila,col))
      sucesores.append(moverD(estado, fila, col))
      sucesores.append(moverAb(estado, fila, col))
  elif fila == 1 and col == 0:
      sucesores.append(moverA(estado,fila,col))
      sucesores.append(moverD(estado, fila, col))
      sucesores.append(moverAb(estado,fila,col))
  elif fila==1 and col==1:
      sucesores.append(moverIz(estado,fila,col))
      sucesores.append(moverD(estado, fila, col))
      sucesores.append(moverA(estado,fila,col))
      sucesores.append(moverAb(estado,fila,col))
  elif fila==1 and col==2:
      sucesores.append(moverIz(estado,fila,col))
      sucesores.append(moverA(estado,fila,col))
      sucesores.append(moverAb(estado,fila,col))
  elif fila==2 and col==0:
      sucesores.append(moverD(estado, fila, col))
      sucesores.append(moverA(estado,fila,col))
  elif fila ==2 and col==1:
      sucesores.append(moverIz(estado,fila,col))
      sucesores.append(moverD(estado, fila, col))
      sucesores.append(moverA(estado,fila,col))
  elif fila==2 and col==2:
      sucesores.append(moverIz(estado,fila,col))
      sucesores.append(moverA(estado,fila,col))

  return sucesores

def moverIz(est,fila, col):
  temp = copy.deepcopy(est)
  temp[fila][col], temp[fila][col-1] = temp[fila][col-1], temp[fila][col]
  return temp
def moverD(est,fila, col):
    temp = copy.deepcopy(est)
    temp[fila][col], temp[fila][col+1] = temp[fila][col+1], temp[fila][col]
    return temp    

def moverA(est,fila, col):
  temp = copy.deepcopy(est)
  temp[fila][col], temp[fila-1][col] = temp[fila-1][col], temp[fila][col]
  return temp    

def moverAb(est,fila,col):
  temp = copy.deepcopy(est)
  temp[fila][col], temp[fila+1][col] = temp[fila+1][col], temp[fila][col]
  return temp      


# devuelve 0 a todos los estados (reduce a BPA o costo uniforme)
def h1(est):    
  return 0
# fuera de lugar
def h2(est):
  cont=0
  for i in range(len(meta)):
    for j in range(len(meta)):
      if not meta[i][j]==est[i][j]:
        cont=cont+1
  return cont
     

  
# manhattan
def h3(nodo):
  cont=0
  for i in range(len(meta)):
    for j in range(len(meta)):
      for x in range(len(nodo)):
          for y in range(len(nodo)):
            if meta[i][j]==nodo[x][y]:
              cont=abs(i-x)+abs(j-y)+cont
  return cont
              
             
            
        
        
      
 
      
    
  


def g(est,cam):
  return cam+1

def f(est,cam):
  return cam + h(est)


meta = [[1,2,3],[8,0,4],[7,6,5]]

print "dame el tablero inicial"
print "primer renglon"
a=input("numero: ")
b=input("numero: ")
c=input("numero: ")
print "segundo renglon"
d=input("numero: ")
e=input("numero: ")
f=input("numero: ")
print "tercer renglon"
g=input("numero: ")
h=input("numero: ")
i=input("numero: ")
inicio = [[a,b,c],[d,e,f],[g,h,i]]
print "iniciaremos desde ", inicio

print "Eliga una heuristica"
print "1: Zero heuristica"
print "2:Tejas fuera de lugar"
print "3: Distancia Manhattan"
heur=input()
Ce = {}

if heur == 1:
  h = h1
elif heur == 2:
  h = h2
else:
  h = h3

Ab = [(inicio, None, h(inicio), 0)]
Estado = False

while Ab and not Estado:
  nodo = Ab.pop(0)
  a = tuple([tuple(i) for i in nodo[0]])
  if nodo[1] == None:
    b = None
  else:
    b = tuple([tuple(i) for i in nodo[1]])
  Ce[a] = [b, nodo[2], nodo[3]]
  if nodo[0] == meta:
    print 'encontramos un camino'
    print 'longitud del camino %d' % nodo[3]
    print 'numero de nodos %d' % (len(Ab)+len(Ce))  
    Estado = True
  else:
    hijos = suces(nodo[0]) 
    for hijo in hijos:
      thijo = tuple([tuple(i) for i in hijo])
      abtiene = False
      cetiene = False
      padre = nodo[0]
      g = nodo[3] + 1
      f = g + h(hijo)
      for m in Ab:
        if m[0] == hijo:
          abtiene = True
          if f > m[2]:
            continue
      if Ce.has_key(thijo):
        cetiene = True
        if f > Ce[thijo][2]:
          continue       
      if abtiene:
        Ab = [m for m in Ab if m[0] != hijo]
      if cetiene:
        del Ce[thijo]
      Ab.append([hijo,padre,f,g])
    Ab.sort(key=lambda tup: tup[2])
                  

if not Estado:
        print 'No hay solucion'

 

