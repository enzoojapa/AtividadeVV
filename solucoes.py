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

def valida_cpf(cpf_string):
    #TODO
    pass