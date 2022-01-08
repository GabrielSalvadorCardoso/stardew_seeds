import pandas as pd

SEMENTES_LABEL = "SEMENTES"
QUALIDADE_LABEL = "QUALIDADE"
VALOR_DE_COMPRA_LABEL = "VALOR DE COMPRA (OUROS)"
DIAS_CRESCER_LABEL = "TEMPO PARA CRESCER (DIAS)"
VALOR_VENDA_LABEL = "VALOR DE VENDA (OUROS)"
LUCRO_LABEL = "LUCRO (OUROS)"
QUANTIDADE_COLHEITAS_LABEL = "QUANTIDADE DE COLHEITAS"

ESTACAO = "PRIMAVERA"
data = pd.read_excel("STARDEW-VALLEY-ANOTACOES.xlsx", sheet_name=ESTACAO)

QUANTIDADE_COLHEITAS_ALVO = "1 VEZ"
QUALIDADE_ALVO = "NORMAL"
print("QUANTIDADE DE COLHEITAS", QUANTIDADE_COLHEITAS_ALVO)

def get_by_min_days():
    result_ftd_by_qtde_colheitas = data[ (data[QUANTIDADE_COLHEITAS_LABEL] == QUANTIDADE_COLHEITAS_ALVO) ]
    result_ftd_by_qtde_colheitas = result_ftd_by_qtde_colheitas[ result_ftd_by_qtde_colheitas[QUALIDADE_LABEL] == QUALIDADE_ALVO]

    TEMPO_ALVO = min(result_ftd_by_qtde_colheitas[DIAS_CRESCER_LABEL])
    result_ftd_by_days = result_ftd_by_qtde_colheitas[ (result_ftd_by_qtde_colheitas[DIAS_CRESCER_LABEL] == TEMPO_ALVO) ]

    LUCRO_ALVO = max(result_ftd_by_days[LUCRO_LABEL])
    result_ftd_by_lucro = result_ftd_by_days[ (result_ftd_by_days[LUCRO_LABEL] == LUCRO_ALVO) ]
    return result_ftd_by_lucro

def get_by_max_lucro():
    result_ftd_by_qtde_colheitas = data[(data[QUANTIDADE_COLHEITAS_LABEL] == QUANTIDADE_COLHEITAS_ALVO)]
    result_ftd_by_qtde_colheitas = result_ftd_by_qtde_colheitas[result_ftd_by_qtde_colheitas[QUALIDADE_LABEL] == QUALIDADE_ALVO]

    LUCRO_ALVO = max(result_ftd_by_qtde_colheitas[LUCRO_LABEL])
    result_ftd_by_lucro = result_ftd_by_qtde_colheitas[(result_ftd_by_qtde_colheitas[LUCRO_LABEL] == LUCRO_ALVO)]

    TEMPO_ALVO = min(result_ftd_by_lucro[DIAS_CRESCER_LABEL])
    result_ftd_by_days = result_ftd_by_lucro[(result_ftd_by_lucro[DIAS_CRESCER_LABEL] == TEMPO_ALVO)]
    return result_ftd_by_days

if __name__ == "__main__":
    print()
    print(f"O QUE PLANTAR NA ESTAÇÃO '{ESTACAO}'...")
    print()
    show_columns = [SEMENTES_LABEL, QUALIDADE_LABEL, DIAS_CRESCER_LABEL, LUCRO_LABEL]
    result_by_min_days = get_by_min_days()
    print("PRIORIZANDO MENOR TEMPO DE COLHEITA")
    print(result_by_min_days[show_columns])
    print()
    print("PRIORIZANDO MAIOR LUCRO")
    result_by_max_lucro = get_by_max_lucro()
    print(result_by_max_lucro[show_columns])

# result = data[ (data[QUANTIDADE_COLHEITAS_LABEL] == QUANTIDADE_COLHEITAS_ALVO) & (data[DIAS_CRESCER_LABEL] == TEMPO_ALVO) & (data[LUCRO_LABEL] == LUCRO_ALVO) ]