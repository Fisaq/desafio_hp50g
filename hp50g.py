
def ehIncognita(valor):
  if valor.isdigit():
    return False
  return True

oposto = {
  '+': '-',
  '-': '+',
  '*': '/',
  '/': '*'
}

def hp50g(expressao):
  
  # decompor a expressão em duas partes
  partes = expressao.split("=")

  esquerda = partes[0].strip()
  direita = partes[1].strip()

  # identificar o operador da equação
  operadores = ["+","-","*","/"]
  op = ""
  res = 0
  
  for operador in operadores:
    if operador in expressao:
      op = operador

  partes_direita = direita.split(op)

  a = partes_direita[0].strip()
  b = partes_direita[1].strip()
  
  if (ehIncognita(esquerda)):
    
    a = float(a)
    b = float (b)
    
  elif (ehIncognita(a)):
    
    a = float(esquerda)
    b = float(b)
    op = oposto[op]
    
  elif (ehIncognita(b)):
    if (op == '-' or op == '/'):
      a = float(a)
      b = float(esquerda)
    else:
      a = float(a)
      b = float(esquerda)
      op = oposto[op]

  if op == '+':
    res = a + b
  elif op == '-':
    res = a - b
  elif op == '*':
    res = a * b
  elif op == '/':
    res = a / b

  print(f'O resultado da expressão {expressao} é: {res}')
  
if __name__ == '__main__':

  cont = 0

  while (cont < 1):
    print("Informe uma expressão do tipo 'V = D op T':\n")
    exp = str(input('R: '))
    print('\n')
    hp50g(exp)
    cont += 1

  print("\nFim do programa!")

  '''
  Saída:
    Informe uma expressão do tipo 'V = D op T':
    R: 10 = 2 / d
    O resultado da expressão 10 = 2 / d é: 0.2
    Fim do programa!
  '''
