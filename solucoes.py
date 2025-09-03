def sao_anagramas(string1, string2):
    #TODO
    pass

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

def valida_cpf(cpf_string):
    #TODO
    pass