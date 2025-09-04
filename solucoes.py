def sao_anagramas(string1, string2):
    #TODO
    pass

def cifra_de_cesar(texto, deslocamento):
    #TODO
    pass

import string

def encontrar_maior_palavra(frase):
  """
  Encontra a maior palavra em uma frase, ignorando a pontuação.

  Args:
    frase: A string de entrada contendo a frase.

  Returns:
    A maior palavra encontrada na frase. Se houver empate, retorna a primeira.
  """

  for pontuacao in string.punctuation:
    frase = frase.replace(pontuacao, '')

  palavras = frase.split()

  maior_palavra = ""
  maior_comprimento = 0

  for palavra in palavras:
    if len(palavra) > maior_comprimento:
      maior_comprimento = len(palavra)
      maior_palavra = palavra

  return maior_palavra


print(f"'O rato roeu a roupa do rei de Roma' -> '{encontrar_maior_palavra('O rato roeu a roupa do rei de Roma')}'")
print(f"'A jornada de mil milhas começa com um único passo.' -> '{encontrar_maior_palavra('A jornada de mil milhas começa com um único passo.')}'")
print(f"'Seja forte e corajoso' -> '{encontrar_maior_palavra('Seja forte e corajoso')}'")