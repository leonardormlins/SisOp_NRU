##Implementation of a _Not _Recently _Used algorithm (NRU)

import random

MAX_ITERATIONS = 8
possibilities = [0,1]
pages = [
  [1,1],
  [1,0],
  [1,0],
  [0,1],
  [1,1],
  [1,0]
]
founded = False

#Cabecalho
print(" r ,m ")

#Funcao zerarR
def zerarR():
  for page in pages: 
        page[0] = 0

#Funcao main
def verifyCadidate():
  it = 0
  while True:
    for page in pages: 
      if page == [0,0]:
        page = str(page)+"*"
        print(page)
        founded = True
        return
      else: print(page)
    print("----(ITERACAO", it,")")
    if it > MAX_ITERATIONS : zerarR()
    it+=1
    for page in pages: 
      page[0] = random.choice(possibilities)
  if founded == True: return


#|Definindo:
verifyCadidate()

