num = 100
contador_pares = 0
contador_impar = 0
while num <= 200:
  if num % 2 == 1:
    contador_impar = contador_impar+1
  else:
    contador_pares = contador_pares+1
  num=num+1
print(contador_impar)
print(contador_pares)