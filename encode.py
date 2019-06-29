def possuiSubsetSum(listaElementos, numeroElementos, valorASerEncontrado) : 
  if (numeroElementos == 0 and valorASerEncontrado != 0):
    return False
  
  if (valorASerEncontrado == 0): 
    return True
  
  elementoAtual = numeroElementos-1

  if (listaElementos[elementoAtual] > valorASerEncontrado):
    return possuiSubsetSum(listaElementos, elementoAtual, valorASerEncontrado) 

  if (possuiSubsetSum(listaElementos, elementoAtual, valorASerEncontrado)):
    return True

  if (possuiSubsetSum(listaElementos, elementoAtual, valorASerEncontrado-listaElementos[elementoAtual])):
    return True
  
  return False


def testesUnitarios(listaElementos):
  print(">> Iniciando testes unitários...")

  if (possuiSubsetSum(listaElementos, len(listaElementos), 37)):
    print('Erro.')
  if (possuiSubsetSum(listaElementos, len(listaElementos), 38)):
    print('Erro.')
  if (possuiSubsetSum(listaElementos, len(listaElementos), 39)):
    print('Erro.')
  if (possuiSubsetSum(listaElementos, len(listaElementos), 20) == False):
    print('Erro.')
  if (possuiSubsetSum(listaElementos, len(listaElementos), 20011111111) == False):
    print('Erro.')
  if (possuiSubsetSum(listaElementos, len(listaElementos), 20011111112) == False):
    print('Erro.')
  if (possuiSubsetSum(listaElementos, len(listaElementos), 20011111113) == False):
    print('Erro.')

  print(">> Testes unitários concluídos.")


if __name__=='__main__':
  listaElementos = [10011110000, 10000001111, 1011001100, 1000110011, 110101010,101010101, 10000000,20000000,1000000,2000000,100000,200000,10000,20000,1000,2000,100,200,10,20,1,2]
  
  valorASerEncontrado = 37

  if (possuiSubsetSum(listaElementos, len(listaElementos), valorASerEncontrado)):
    print("Foi encontrado um SubsetSum para o valor informado.")     
  else:     
    print("Não foi encontrado um SubsetSum para o valor informado.") 

  testesUnitarios(listaElementos)