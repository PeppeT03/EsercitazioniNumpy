import numpy as np


dati= np.random.randint(10,100, size = (6,5))
print("Dati originali: \n",dati)

print("\nShape: ", dati.shape)
print("Tipo di dato", dati.dtype)

print("\nPrima riga: ", dati[0])
print("\nPrima colonna: ", dati[:,0]  )
print("Sub-matrice (prime 2 righe,prime 3 colonne): \n",dati[:2,:3])

view = dati[:2,:2]
copy= dati [:2,:2].copy()
view[0,0]=999
print("\nDopo modifica della view:\n",dati)
print("La copy resta invariata\n",copy)

reshaped= dati.reshape(3,10)
print("\nArray reshaped (3x10): \n", reshaped)

print("\nIterazione su ogni elemento con nditer: ")
for x in np.nditer(dati):
    print(int(x),end=" ")
print()

extra= np.random.randint(10,100,size=(6,2))
unito= np.hstack ((dati,extra))
print("\nArray unito con nuove colonne:\n",unito)

split= np.split(unito,2)
print("\nArray diviso in due blocchi :\n",split[0],"\n",split[1])

mask = dati>50
print("\nValori>50\n", dati[mask])

ordinati= np.sort(dati,axis=1)
print("\nOgni riga ordinata:\n", ordinati)

radici = np.sqrt(dati)
print("\nRadici quadrate di ogni elemento:\n", radici)

StudentiMatrice= np.random.randint(4,10, size= (4,3))
print("Matrice Studenti all'inizio:\n", StudentiMatrice)
StudentiMatriceReshpade= StudentiMatrice.reshape(2,6)
print("Matrice Studenti con il reshape 2x6:\n", StudentiMatriceReshpade)

MascherInsufficienze=StudentiMatrice <6 
print("Insufficienze <6 :\n ", StudentiMatrice[MascherInsufficienze])
ContatoreInsufficienze=len(StudentiMatrice[MascherInsufficienze])
print("Il numero di insufficienze e", ContatoreInsufficienze )

mediaOrizzontale= np.mean(StudentiMatrice,axis=1)
mediaVerticale= np.mean(StudentiMatrice,axis=0)

print("( non arrotondata )La media Orizzontale e': " , mediaOrizzontale)
print("( non arrotondata ) La media Verticale e': " , mediaVerticale)

mediaOrizzontale= np.round(mediaOrizzontale,2)
mediaVerticale= np.round(mediaVerticale,2)

print("La media Orizzontale e': " , mediaOrizzontale.tolist())
print("La media Verticale e': " , mediaVerticale.tolist())


