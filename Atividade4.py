def validar_alfabeto(alfabeto, frase):
    # Converte a frase em conjunto de caracteres
    caracteres_frase = set(frase)
    
    # Remove espaços (opcional, caso não queira considerar espaço como erro)
    caracteres_frase.discard(" ")
    
    # Verifica se todos os caracteres da frase pertencem ao alfabeto
    return caracteres_frase.issubset(alfabeto)


# 🔹 Exemplo 1: Alfabeto binário
alfabeto_binario = {"0", "1"}
frase1 = "10101"
frase2 = "10102"

print("Frase 1 válida?", validar_alfabeto(alfabeto_binario, frase1))
print("Frase 2 válida?", validar_alfabeto(alfabeto_binario, frase2))


# 🔹 Exemplo 2: Letras minúsculas
import string
alfabeto_minusculas = set(string.ascii_lowercase)

frase3 = "linguagem formal"
frase4 = "Linguagem"

print("\nFrase 3 válida?", validar_alfabeto(alfabeto_minusculas, frase3))
print("Frase 4 válida?", validar_alfabeto(alfabeto_minusculas, frase4))
