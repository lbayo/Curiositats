import copy

def ss(p):
    for x in p:
        return x 

def dsp():
    print (" Acertijo de Einstein")
    for i in range (len(p)):
        print ("La casa %1d  es de color %s, vive un %s, que bebe %s, fuma %s y tiene un %s"%(i+1, ss(p[i][0]),ss(p[i][1]),ss(p[i][2]),ss(p[i][3]),ss(p[i][4])))
  

def recuadrar(p):
    for c in Colors:
        n=0
        for  i in range (len(p)):
            if c in p[i][0]:
                n+=1
                k=i
        if n==1:
            p[k][0]={c}
            
    for c in Nacion:
        n=0
        for  i in range (len(p)):
            if c in p[i][1]:
                n+=1
                k=i
        if n==1:
            p[k][1]={c}
            
    for c in Bebida:
        n=0
        for  i in range (len(p)):
            if c in p[i][2]:
                n+=1
                k=i
        if n==1:
            p[k][2]={c}
            
    for c in Tabaco:
        n=0
        for  i in range (len(p)):
            if c in p[i][3]:
                n+=1
                k=i
        if n==1:
            p[k][3]={c}
            
    for c in Mascot:
        n=0
        for  i in range (len(p)):
            if c in p[i][4]:
                n+=1
                k=i
        if n==1:
            p[k][4]={c}

    for fila in range (5):
        for col in range (5)            :
            n=len(p[col][fila])
            if n==1:
                s=p[col][fila]
                for j in range (5):
                    if j!=col:
                        p[j][fila]-=p[col][fila]
#                p[col][fila]=s

def pasada(p):

    #noruego primera casa
    for i in range(1,len(p)):
        p[i][1]-={"noruego"}
    p[0][1]={"noruego"}
    recuadrar(p)

    #El noruego vive al lado de la casa azul.
    for i in range(len(p)):
        if i==0:
            if not ("azul" in p[i+1][0]):  
                p[i][1]-={"noruego"}
            if not ("noruego" in p[i+1][1]):  
                p[i][0]-={"azul"}
        elif i==4:
            if not ("noruego" in p[i-1][1]):  
                p[i][0]-={"azul"}
            if not ("azul" in p[i-1][0]):  
                p[i][1]-={"noruego"}
        else:
            if not (("noruego" in p[i-1][1]) or (("noruego" in p[i+1][1]))):  
                p[i][0]-={"azul"}
            if not (("azul" in p[i-1][0]) or (("azul" in p[i+1][0]))):  
                p[i][1]-={"noruego"}
    recuadrar(p)

    #El hombre que vive en la casa del centro bebe leche.
    for i in range(len(p)):
        p[i][2]-={"leche"}
    p[2][2]={"leche"}
    recuadrar(p)
    
    # britanico en casa roja
    for i in range(len(p)):
        if not ("britanico" in p[i][1]):  # si no britanico => no rojo
            p[i][0]-={"rojo"}
        if not ("rojo" in p[i][0]):  # si no rojo => no britanico
            p[i][1]-={"britanico"}
    recuadrar(p)

    #sueco tiene perro           
    for i in range(len(p)):
        if not ("sueco" in p[i][1]):  # si no sueco => no perro
            p[i][4]-={"perro"}
        if not ("perro" in p[i][4]):  # si no perro => no sueco
            p[i][1]-={"sueco"}
    recuadrar(p)

    #danes toma te
    for i in range(len(p)):
        if not ("danes" in p[i][1]):  
            p[i][2]-={"te"}
        if not ("te" in p[i][2]):  
            p[i][1]-={"danes"}
    recuadrar(p)

    #aleman fuma prince           
    for i in range(len(p)):
        if not ("aleman" in p[i][1]):  
            p[i][3]-={"prince"}
        if not ("prince" in p[i][3]):  
            p[i][1]-={"aleman"}
    recuadrar(p)

    #casa verde inmediatamente a la izquierda casa blanca
    p[4][0]-={"verde"}   # extrem dret no pot ser verd
    p[0][0]-={"blanco"}  # extrem esquerra no pot ser blanc
    for i in range(len(p)-1):
        if not ("verde" in p[i][0]):
            p[i+1][0]-={"blanco"}
    for i in range(1,len(p)):
        if not ("blanco" in p[i][0]):
            p[i-1][0]-={"verde"}
    recuadrar(p)
    
    # dueño casa verde bebe cafe
    for i in range(len(p)):
        if not ("verde" in p[i][0]):  
            p[i][2]-={"cafe"}
        if not ("cafe" in p[i][2]):  
            p[i][0]-={"verde"}
    recuadrar(p)

    #El dueño de la casa amarilla fuma Dunhill.
    for i in range(len(p)):
        if not ("amarillo" in p[i][0]):  
            p[i][3]-={"dunhill"}
        if not ("dunhill" in p[i][3]):  
            p[i][0]-={"amarillo"}
    recuadrar(p)
            
    #El hombre que tiene un caballo vive al lado del que fuma Dunhill.
    for i in range(len(p)):
        if i==0:
            if not ("caballo" in p[i+1][4]):  
                p[i][3]-={"dunhill"}
            if not ("dunhill" in p[i+1][3]):  
                p[i][4]-={"caballo"}
        elif i==4:
            if not ("dunhill" in p[i-1][3]):  
                p[i][4]-={"caballo"}
            if not ("caballo" in p[i-1][4]):  
                p[i][3]-={"dunhill"}
        else:
            if not (("dunhill" in p[i-1][3]) or (("dunhill" in p[i+1][3]))):  
                p[i][4]-={"caballo"}
            if not (("caballo" in p[i-1][4]) or (("caballo" in p[i+1][4]))):  
                p[i][3]-={"dunhill"}
    recuadrar(p)

    #El propietario que fuma Bluemaster toma cerveza.
    for i in range(len(p)):
        if not ("bluemaster" in p[i][3]):  
            p[i][2]-={"cerveza"}
        if not ("cerveza" in p[i][2]):  
            p[i][3]-={"bluemaster"}
    recuadrar(p)
            
    #El vecino que fuma Blends vive al lado del que toma agua.
    for i in range(len(p)):
        if i==0:
            if not ("agua" in p[i+1][2]):  
                p[i][3]-={"blends"}
            if not ("blends" in p[i+1][3]):  
                p[i][2]-={"agua"}
        elif i==4:
            if not ("blends" in p[i-1][3]):  
                p[i][2]-={"agua"}
            if not ("agua" in p[i-1][2]):  
                p[i][3]-={"blends"}
        else:
            if not (("blends" in p[i-1][3]) or (("blends" in p[i+1][3]))):  
                p[i][2]-={"agua"}
            if not (("agua" in p[i-1][2]) or (("agua" in p[i+1][2]))):  
                p[i][3]-={"blends"}
    recuadrar(p)

    #El propietario que fuma Pall Mall cría pájaros.
    for i in range(len(p)):
        if not ("pallmall" in p[i][3]):  
            p[i][4]-={"pajaro"}
        if not ("pajaro" in p[i][4]):  
            p[i][3]-={"pallmall"}
    recuadrar(p)

    #El vecino que fuma Blends vive al lado del que tiene un gato.
    for i in range(len(p)):
        if i==0:
            if not ("blends" in p[i+1][3]):  
                p[i][4]-={"gato"}
            if not ("gato" in p[i+1][4]):  
                p[i][3]-={"blends"}
        elif i==4:
            if not ("gato" in p[i-1][4]):  
                p[i][3]-={"blends"}
            if not ("blends" in p[i-1][3]):  
                p[i][4]-={"gato"}
        else:
            if not (("blends" in p[i-1][3]) or (("blends" in p[i+1][3]))):  
                p[i][4]-={"gato"}
            if not (("gato" in p[i-1][4]) or (("gato" in p[i+1][4]))):  
                p[i][3]-={"blends"}
    recuadrar(p)


    return




Colors={"rojo","verde","amarillo","blanco","azul"}
Nacion={"britanico","sueco","danes","noruego","aleman"}
Bebida={"te","cafe","leche","cerveza","agua"}
Tabaco={"prince","pallmall","dunhill","blends","bluemaster"}
Mascot={"perro","pajaro","gato","caballo","koala"}

casa=[Colors,Nacion,Bebida,Tabaco,Mascot]
p=[]
for i in range(5):
    p+=copy.deepcopy([casa])
nmax=5
while nmax!=1:
    pasada (p)
    nmax=0
    for i in range (5):
        for j in range(5):
            nmax=max(len(p[i][j]), nmax)
dsp()
