
import os 
os.system('clear')
os.system('date')
#Première partie 
""" Dans cette première partie on souhaite créer une fonction qui permet
 de calculer le nombre d'occurrence de chaque caractère présent dans le texte fourni en argument.
"""

texteACompresser = "un homme averti en vaut deux"
dictionnaire = {} # Création d'un dictionnaire vide
def findFrequences(txt): 
        lettre="abcdefghijklmnopqrstuvwxyz " # Definition des cas possibles càd toutes les lettres de l'alphabet et l'espace 
        for key in lettre:        #On parcourt l'alphabet (espace y compris) afin de calculer pour le nbre de chaque caractère 
            #print(key, txt.count(key))
            if(txt.count(key)!= 0):  #Cette condition permet de prendre que les caractère de l'alphabet présents dans la chaine de caracètre que l'on veut exploiter, les autres caractères qui ne sont pas présents ne seront pas pris en compte 
                dictionnaire[key]=txt.count(key)/len(txt) # On ajoute au dictionnaire le item (key,value), qui représente  Key : le caractère et value : le nombre d'occurrence 
        #print(dictionnaire)                               # On affiche le résultat (dictionnaire)
        return dictionnaire



#Deuxième partie : 
"""
Dans cette partie on crée une classe appelée Noeud 

"""



class Noeud:
    def __init__(self,caractere,freq,gauche=None,droite=None):
        self.caractere=caractere # on recupérer le caractère et on le stocke dans self.caractere 
        self.freq=freq 
        self.next={'gauche':gauche,'droite':droite}  # on crée un dictionnaire avec les valeurs gauche et droite qu'on utilisera par la suite dans l'étiquetage 
        self.codage=""                                #ce dictionnaire nous permettra d'encoder le caractère   

    def getCaractere(self):     # méthode permettant d'avoir le caractère 
        return self.caractere

    def getFreq(self):          #méthode permettant d'avoir la fréquence 
        return self.freq



    def __str__(self): #méthode permettant d'afficher le noeud à l'aide de la fonction Print()
        temp = "Caractere {}  Frequence : {} ".format(self.getCaractere(),self.getFreq())  # dans ce cas on utilise les deux fonction définie au préalable 
        #Ces deux méthode permettent de conserver et de respecter le principe d'encapsulation 
        return temp 
"""
Dans cette partie on s'intéresse à la classe Arbre 

La classe Arbre prend en parametre un dictionnaire 
"""

class Arbre : 
    def __init__(self,dicoFreq): # On initialise le constructeur qui prend en paramètre un dictionnaire qui contient un item (key,value) 
        #qui représentent réspectivement(Caractère,fréquence), ce item par la suite on l'aura grace à la fonction définie au préalable findFrequences 
        self.codes={} # cet attribut va contenir le code qu'on va mettre pour chaque caractère 
        self.dicoFreq=dicoFreq
        self.ListeNoeuds= []
        """
        On crée un noeud pour chaque caractère et on les mets dans l'attribut ListeNoeuds 
        et cela se fait en parcourant le dictionnaire dicoFreq 
        pour chaque élement on crée un noeud en instanciant la classe Noeud(i,fréquence(i)), qui prend en paramètre le caractère et sa fréquence 
        """
        for i in dicoFreq:  
             self.ListeNoeuds.append(Noeud(i,self.dicoFreq[i])) 

        self.run() # c'est une méthode qui nous permet de trouver les minimums de la ListeNoeud (dans notre cas n1 et n2) de les supprimer 
        # et créer un nouveau noeud en additionnant leurs deux fréquence et en concaténant les caractères 
             

        """
        Fonction permettant d'ajouter un Noeud 
        """
    def addNoeud(self,node):
            self.ListeNoeuds.append(node)  # ListeNeouds est une liste ce qui fait qu'on va directement utiliser append(node) pour ajouter node à la liste 

    
    """
    Fonction permettant de trouver le min 
    """
    def findMin(self):  
        m=1 
        for i in self.ListeNoeuds:  # On parcourt la liste de Noeuds et on défini au préalable une constante =1 (on sait pertinnement que la fréquence ne pourra pas être égale à 1 pour un caractère )
            if(i.getFreq() < m):  # On compare la fréquence des élement de la liste de noeud avec m, si elle est inférieur (dans le premier cas c'est une évidence )
                #la variable m prendre la fréquence inférieur 
                m=i.getFreq() 
                minn=self.ListeNoeuds.index(i)  # On fait apelle à l'index de i 
            
        #print (self.ListeNoeuds[p])
        return self.ListeNoeuds[minn]

    """
    Fonction permettant d'enlever un noeud (on utilise la fonction pop )
    """
    def removeNoeud(self,node):
        self.ListeNoeuds.pop(node) 
    """
    Définition de la méthode run() permettant de trouver les minimums de la ListeNoeud (dans notre cas n1 et n2) de les supprimer 
        # et créer un nouveau noeud en additionnant leurs deux fréquence et en concaténant les caractères 
        cette méthode a été appelé dans le constructure 
    """
    def run(self): 
        while(len(self.ListeNoeuds) > 1 ): 
            noeud1=self.findMin()
            x=noeud1
            self.removeNoeud(self.ListeNoeuds.index(self.findMin()))
            noeud2=self.findMin()
            y=noeud2
            self.removeNoeud(self.ListeNoeuds.index(self.findMin()))    
            newfreq= x.freq + y.freq 
            newcar = x.getCaractere() + y.getCaractere() 
            self.addNoeud(Noeud(newcar,newfreq,x,y))

    def etiquetage(self,node): 
        for direct,nF in node.next.items():
            if nF==None:
                self.codes[node.caractere]=node.codage
                return
            else:
                if direct=='gauche':
                    nF.codage="{}0".format(node.codage)
                else:
                    nF.codage="{}1".format(node.codage)
            self.etiquetage(nF)


    def compress(self,text): 
        alpha= " "
        for i in text : 
            alpha += self.codes[i]
        return alpha 
    
    def uncompress(self,textComb):
        origin=""
        s=1
        taille=len(textComb)
        for i in range(1,taille+1): 
            for cle,valeur in self.codes.items():
                if(textComb[s:i]==valeur): 
                    origin += cle
                    s=i
                    
        return origin
        

            

                
texteACompresser = "un homme averti en vaut deux"
dicoFreq = findFrequences(texteACompresser)
G = Arbre(dicoFreq)

G.etiquetage(G.ListeNoeuds[0]) # On passe en argument le nœud racine pour etiqueter tout l’arbre 

texteCompresse=G.compress(texteACompresser)
#print(texteCompresse)
# Affichage taux de compression
#print('Taux de compression : ',100*(len(texteACompresser)*8-len(texteCompresse))/(len(texteACompresser)*8))
texte = G.uncompress(texteCompresse) 
print(texte)
if texte == texteACompresser:
    print('Bravo cela fonctionne correctement !') 
else:
    print('Encore un petit effort, vous y êtes presque !')


with open("VictorHugo.txt","r",encoding="Latin-1") as f:
    content=f.read()
    fichier=content.lower()
    
    
    dic=findFrequences(fichier)
    F=Arbre(dic)
    F.etiquetage(F.ListeNoeuds[0])
    print (fichier)
    tex=F.compress(fichier)
    print(tex)    

    """tex2=F.uncompress(tex)
    #print(tex2)    
    if tex2 == texteACompresser:
        print('Bravo cela fonctionne correctement !') 
    else:
        print('Encore un petit effort, vous y êtes presque !')"""

    
          