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
    #TODO
    pass

def valida_cpf(cpf_string):
    #TODO
    pass