import os

# --- FUNÇÕES QUE CALCULAM AS COLUNAS DA PLANILHA ---

def calc_coluna_e_material(peso):
    return peso * 0.10

def calc_coluna_f_maquina(horas):
    return horas * 0.60

def calc_coluna_g_trabalho(minutos):
    valor_hora = 20.00
    return (minutos / 60) * valor_hora

def calc_coluna_h_custo_total(mat, maq, trab):
    return mat + maq + trab

def calc_coluna_i_venda(custo_total):
    return custo_total * 2.5

# --- NOVA FUNÇÃO: TAXAS EXTRAS ---
def calc_taxas_plataforma(preco_base):
    print("\n--- ONDE VOCÊ VAI VENDER? ---")
    print("1. Presencial / WhatsApp (Sem taxas)")
    print("2. Shopee (19% + R$ 4.00 de taxa fixa)")
    print("3. Mercado Livre (17% + R$ 6.00 de taxa fixa)")
    
    escolha = input("Escolha o local de venda: ")
    
    if escolha == "2":
        # Cálculo: (Preço / 0.81) + 4 -> Para garantir que sobre o valor desejado
        return (preco_base / 0.81) + 4.00
    elif escolha == "3":
        return (preco_base / 0.83) + 6.00
    else:
        return preco_base

# --- BANCO DE DADOS EM MEMÓRIA ---
produtos = []

def menu():
    while True:
        print("\n--- GESTÃO DE IMPRESSÃO 3D: ---")
        print("1. Cadastrar Novo Produto")
        print("2. Listar Produtos")
        print("3. Ver Detalhes de um Produto")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            peso = float(input("Peso em gramas: "))
            horas = float(input("Horas de impressão: "))
            minutos = float(input("Minutos de trabalho manual: "))

            c_material = calc_coluna_e_material(peso)
            c_maquina = calc_coluna_f_maquina(horas)
            c_trabalho = calc_coluna_g_trabalho(minutos)
            custo_total = calc_coluna_h_custo_total(c_material, c_maquina, c_trabalho)
            
            # Primeiro calcula o preço de venda base
            preco_base = calc_coluna_i_venda(custo_total)
            
            # Agora ajusta conforme a plataforma
            preco_final_ajustado = calc_taxas_plataforma(preco_base)

            produto = {
                "nome": nome,
                "peso": peso,
                "horas": horas,
                "minutos": minutos,
                "c_material": c_material,
                "c_maquina": c_maquina,
                "c_trabalho": c_trabalho,
                "custo_total": custo_total,
                "preco_venda": preco_final_ajustado
            }
            produtos.append(produto)
            print(f"\n {nome} cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- PRODUTOS CADASTRADOS ---")
            if not produtos: print("Nenhum produto na lista.")
            for i, p in enumerate(produtos):
                print(f"{i} - {p['nome']}")

        elif opcao == "3":
            try:
                indice = int(input("Digite o número do produto: "))
                if 0 <= indice < len(produtos):
                    p = produtos[indice]
                    print(f"\n--- DETALHES: {p['nome']} ---")
                    print(f"B. Peso: {p['peso']}g | C. Tempo: {p['horas']}h | D. Trabalho: {p['minutos']}min")
                    print("-" * 35)
                    print(f"E. Custo Plástico:      R$ {p['c_material']:.2f}")
                    print(f"F. Custo Máquina:       R$ {p['c_maquina']:.2f}")
                    print(f"G. Mão de Obra:         R$ {p['c_trabalho']:.2f}")
                    print(f"H. CUSTO TOTAL:         R$ {p['custo_total']:.2f}")
                    print("-" * 35)
                    print(f"I. PREÇO FINAL (C/ TAXAS): R$ {p['preco_venda']:.2f}")
                else:
                    print(" Produto não encontrado.")
            except ValueError:
                print(" Digite apenas números.")

        elif opcao == "4":
            print("Saindo... Bons negócios!")
            break

if __name__ == "__main__":
    menu()