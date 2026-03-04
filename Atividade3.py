# Conjuntos de permissões por cargo
RH = {"ver_salario", "editar_perfil"}
TI = {"acesso_servidor", "editar_perfil"}

# 1️⃣ Função que retorna o total de permissões
# quando o funcionário acumula dois cargos
def calcular_permissoes_totais(*cargos):
    permissoes_totais = set()
    for cargo in cargos:
        permissoes_totais = permissoes_totais.union(cargo)
    return permissoes_totais

# Funcionário com RH e TI
permissoes_funcionario = calcular_permissoes_totais(RH, TI)

print("Permissões totais do funcionário:")
print(permissoes_funcionario)


# 2️⃣ Verificar se o usuário pode abrir arquivo confidencial

# Conjunto de permissões necessárias
PERMISSOES_ARQUIVO_CONFIDENCIAL = {
    "ver_salario",
    "acesso_servidor",
    "editar_perfil"
}

def pode_abrir_arquivo(permissoes_usuario, permissoes_necessarias):
    return permissoes_necessarias.issubset(permissoes_usuario)

# Verificação
if pode_abrir_arquivo(permissoes_funcionario, PERMISSOES_ARQUIVO_CONFIDENCIAL):
    print("\nAcesso autorizado ao arquivo confidencial.")
else:
    print("\nAcesso negado ao arquivo confidencial.")
