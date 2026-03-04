import re

# 1️⃣ Conjunto de palavras reservadas
RESERVADAS = {
    "if", "else", "while", "for", "return",
    "int", "System", "out", "print",
    "public", "class"
}

# 2️⃣ Código-fonte (texto de entrada)
codigo = """
public class StarRectangle {
public void printRectangle(int n) {
for (int i = 0; i < n; i++) {
for (int j = 0; j < n; j++) {
System.out.print(" * ");
}
System.out.println();
}
}
public void printBottonLeftTriangle(int n) {
for (int i = 0; i < n; i++) {
for (int j = 0; j <= i; j++) {
System.out.print(" * ");
}
System.out.println();
}
}
public void printTopRightTriangle(int n) {
for (int i = 0; i < n; i++) {
for (int j = 0; j < n; j++) {
if (j < i)
System.out.print(" ");
else
System.out.print(" * ");
}
System.out.println();
}
}
}
"""

# 3️⃣ Extração das palavras (somente letras, números e _)
palavras_extraidas = re.findall(r'\b[A-Za-z_][A-Za-z0-9_]*\b', codigo)

# Transformando em conjunto (remove duplicados)
PALAVRAS = set(palavras_extraidas)

# 4️⃣ Operações de conjuntos
reservadas_encontradas = RESERVADAS.intersection(PALAVRAS)
identificadores = PALAVRAS.difference(RESERVADAS)

# 5️⃣ Exibição dos resultados
print("Palavras reservadas encontradas:")
print(reservadas_encontradas)

print("\nPossíveis identificadores:")
print(identificadores)
