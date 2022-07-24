from random import randint, seed
seed()

qty_row_colum = int(input())

def origin_square(row, colum):
  origin = []
  for r in range(row):
    inside = []
    for c in range(colum):
     inside.append(int(input()))
    origin.append(inside)
  return origin



def minor_row_position(n):
  minor_linha = []
  menor_linha = 9999
  for c in range(len(n)):
    for d in n[c]:
      if d < menor_linha:
        menor_linha = d
        position = n.index(n[c])
  minor_linha.append(position)
  return tuple(minor_linha)



def larger_row_position(n):
  larger_linha = []
  maior_linha = -999999
  for k in range(len(n)):
    for m in n[k]:
      if m > maior_linha:
        maior_linha = m
        position = n.index(n[k])
  larger_linha.append(position)
  return tuple(larger_linha)



def minor_colum_position(n):
  minor_colum = []
  minor = 999999
  for c in range(len(n)):
    for d in n[c]:
      if d < minor:
        minor = d
        position = n[c].index(d)
  minor_colum.append(position)
  return tuple(minor_colum)

  

def larger_colum_position(n):
  larger_colum = []
  larger = -99999
  for c in range(len(n)):
    for g in n[c]:
      if g > larger:
        larger = g
        position = n[c].index(g)
  larger_colum.append(position)
  return tuple(larger_colum)

def row_and_colum_minor(a, b):
  c = a + b
  return c

def row_and_colum_larger(c, d):
  y = c + d
  return y



ch1 = origin_square(qty_row_colum, qty_row_colum)

ch2 = minor_row_position(ch1)

ch3 = minor_colum_position(ch1)

ch4 = larger_row_position(ch1)

ch5 = larger_colum_position(ch1)

ch6 = row_and_colum_minor(ch2, ch3)

ch7 = row_and_colum_larger(ch4, ch5)



print(ch7)
print(ch6)



