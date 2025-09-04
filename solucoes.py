def sao_anagramas(string1, string2):
  s1_normalizada = string1.replace(" ", "").lower()
  s2_normalizada = string2.replace(" ", "").lower()
  
  if len(s1_normalizada) != len(s2_normalizada):
    return False

  return sorted(s1_normalizada) == sorted(s2_normalizada)
print(f"'amor', 'roma' -> {sao_anagramas('amor', 'roma')}")

print(f"'A gentleman', 'Elegant man' -> {sao_anagramas('A gentleman', 'Elegant man')}")

print(f"'gato', 'cabra' -> {sao_anagramas('gato', 'cabra')}")

def cifra_de_cesar(texto, deslocamento):
    resultado = ''

    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += novo_char
        else:
            resultado += char 

    return resultado

mensagem = "Teste de print"
deslocamento = 3

texto_cifrado = cifra_de_cesar(mensagem, deslocamento)

print("Original :", mensagem)
print("Cifrado  :", texto_cifrado)

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