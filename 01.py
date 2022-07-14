from random import randint, seed
seed()

qty_row_colum = int(input())

def origin_square(row, colum):
  origin = []
  for r in range(row):
    inside = []
    for c in range(colum):
     inside.append(randint(0,20))
    origin.append(inside)
  
  return origin





##FUNCAO PROBLEMÁTICA.... def minor_row_position(n):
    minor = []
    menor = 9999
    position = 0
    for c in range(len(n)):
      for d in n[c]:
        if d < menor:
          menor = d
          position = n.index(min(d))

    print(n)    
    return menor   


ch1 = origin_square(qty_row_colum, qty_row_colum)

ch2 = minor_row_position(ch1)


      




