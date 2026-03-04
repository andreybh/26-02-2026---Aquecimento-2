# Conjuntos de interesses
Usuario_A = {"Python", "Jogos", "Música", "IA"}
Usuario_B = {"Java", "IA", "Música", "Caminhada"}

# 1️⃣ Interesses em comum (Interseção)
interesses_em_comum = Usuario_A.intersection(Usuario_B)

# 2️⃣ Sugestões para o Usuário A (Diferença)
sugestoes_para_A = Usuario_B.difference(Usuario_A)

# Exibição dos resultados
print("Interesses em comum:")
print(interesses_em_comum)

print("\nSugestões para o Usuário A:")
print(sugestoes_para_A)
