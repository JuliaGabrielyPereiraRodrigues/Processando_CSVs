import pandas as pd
import os 
import time
from multiprocessing import Pool, cpu_count

start = time.time()

def normalizar_ramo(ramo_original, sigla_tribunal):
    ramo_original = ramo_original.strip()
    sigla_tribunal = sigla_tribunal.strip().upper()

    if ramo_original == 'Tribunais Superiores':
        if sigla_tribunal == 'STJ':
            return 'Superior Tribunal da Justiça'
        elif sigla_tribunal == 'TST':
            return 'Tribunal Superior do Trabalho'
        else:
            return 'Tribunais Superiores'

    mapping = {
        'Justiça Estadual': 'Justiça Estadual',
        'Justiça Federal': 'Justiça Federal',
        'Justiça do Trabalho': 'Justiça do Trabalho',
        'Justiça Militar da União': 'Justiça Militar da União',
        'Justiça Militar Estadual': 'Justiça Militar Estadual',
        'Justiça Eleitoral': 'Tribunal Superior Eleitoral'
    }
    return mapping.get(ramo_original, ramo_original)

def calcular_meta1(df, ramo):
    ramos_validos = [
        'Justiça Estadual', 
        'Justiça do Trabalho', 
        'Justiça Federal',
        'Justiça Militar da União', 
        'Justiça Militar Estadual',
        'Tribunal Superior Eleitoral', 
        'Tribunal Superior do Trabalho', 
        'Superior Tribunal da Justiça'
    ]

    if ramo not in ramos_validos:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 1 definida.")
        return 'NA'

    try:
        julgados = df['julgados_2025'].sum()
        casos_novos = df['casos_novos_2025'].sum()
        dessobrestados = df['dessobrestados_2025'].sum()
        suspensos = df['suspensos_2025'].sum()
        denom = casos_novos + dessobrestados - suspensos

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * 100, 2)
    except Exception as e:
        print(f"Erro ao calcular a Meta 1: {e}")
        return 'NA'


def calcular_meta2A(df, ramo):
    fatores = {
        'Justiça Estadual': 1000 / 8,
        'Justiça do Trabalho': 1000 / 9.4,
        'Justiça Federal': 1000 / 8.5,
        'Justiça Militar da União': 1000 / 9.5,
        'Justiça Militar Estadual': 1000 / 9,
        'Tribunal Superior Eleitoral': 1000 / 7,
        'Superior Tribunal da Justiça': 1000 / 9.5
    }

    if ramo not in fatores:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 2A definida.")
        return 'NA'

    try:
        julgados = df['julgm2_a'].sum()
        distribuidos = df['distm2_a'].sum()
        suspensos = df['suspm2_a'].sum()
        denom = distribuidos - suspensos
        fator = fatores[ramo]

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)
    except Exception as e:
        print(f"Erro ao calcular a Meta 2A: {e}")
        return 'NA'


def calcular_meta2B(df, ramo):
    fatores = {
        'Justiça Estadual': 1000 / 9,
        'Justiça Federal': 100,
        'Justiça Militar da União': 1000 / 9.9,
        'Justiça Militar Estadual': 1000 / 9.5,
    }

    if ramo not in fatores:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 2B definida.")
        return 'NA'

    try:
        julgados = df['distm2_b'].sum()
        distribuidos = df['julgm2_b'].sum()
        suspensos = df['suspm2_b'].sum()
        denom = distribuidos - suspensos
        fator = fatores[ramo]

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)
    except Exception as e:
        print(f"Erro ao calcular a Meta 2B: {e}")
        return 'NA'


def calcular_meta2C(df, ramo):
    if ramo != 'Justiça Estadual':
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 2C definida.")
        return 'NA'

    try:
        julgados = df['julgm2_c'].sum()
        distribuidos = df['distm2_c'].sum()
        suspensos = df['suspm2_c'].sum()
        denom = distribuidos - suspensos
        fator = 1000 / 9

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)
    except Exception as e:
        print(f"Erro ao calcular a Meta 2C: {e}")
        return 'NA'


def calcular_meta2ANT(df, ramo):
    ramos_validos = [
        'Justiça Estadual', 
        'Justiça do Trabalho', 
        'Justiça Federal',
        'Justiça Militar da União', 
        'Justiça Militar Estadual',
        'Justiça Eleitoral', 
        'Tribunal Superior do Trabalho'
    ]

    if ramo not in ramos_validos:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 2ANT definida.")
        return 'NA'

    try:
        julgados = df['julgm2_ant'].sum()
        distribuidos = df['distm2_ant'].sum()
        suspensos = df['suspm2_ant'].sum()
        denom = distribuidos - suspensos

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * 100, 2)
    except Exception as e:
        print(f"Erro ao calcular a Meta 2ANT: {e}")
        return 'NA'


def calcular_meta4A(df, ramo):
    fatores = {
        'Justiça Estadual': 1000 / 6.5,
        'Justiça Federal': 1000 / 7,
        'Justiça Militar da União': 1000 / 9.5,
        'Justiça Militar Estadual': 1000 / 9.5,
        'Justiça Eleitoral': 1000 / 9,
        'Superior Tribunal da Justiça': 1000 / 9
    }

    if ramo not in fatores:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 4A definida.")
        return 'NA'
    
    try:
        julgados = df['julgm4_a'].sum()
        distribuidos = df['distm4_a'].sum()
        suspensos = df['suspm4_a'].sum()
        denom = distribuidos - suspensos
        fator = fatores[ramo]

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)
    except Exception as e:
        print(f"Erro ao calcular a Meta 4A: {e}")
        return 'NA'


def calcular_meta4B(df, ramo):
    fatores = {
        'Justiça Estadual': 100,
        'Justiça Federal': 100,
        'Justiça Militar da União': 1000 / 9.9,
        'Justiça Militar Estadual': 1000 / 9.9,
        'Justiça Eleitoral': 1000 / 5,
        'Superior Tribunal da Justiça': 100
    }

    if ramo not in fatores:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 4B definida.")
        return 'NA'

    try:
        julgados = df['julgm4_b'].sum()
        distribuidos = df['distm4_b'].sum()
        suspensos = df['suspm4_b'].sum()
        denom = distribuidos - suspensos
        fator = fatores[ramo]

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)
    except Exception as e:
        print(f"Erro ao calcular a Meta 4B: {e}")
        return 'NA'


def calcular_meta6(df, ramo):
    fatores = {
        'Justiça Estadual': 100,
        'Justiça Federal': 1000 / 3.5,
        'Superior Tribunal da Justiça': 1000 / 7.5
    }

    if ramo not in fatores:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 6 definida.")
        return 'NA'

    try:
        julgados = df['julgm6_a'].sum()
        distribuidos = df['distm6_a'].sum()
        suspensos = df['suspm6_a'].sum()
        denom = distribuidos - suspensos
        fator = fatores[ramo]

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)
    except Exception as e:
        print(f"Erro ao calcular a Meta 6: {e}")
        return 'NA'

def calcular_meta7A(df, ramo):
    fatores_por_ramo = {
        'Justiça Estadual': 1000 / 5,
        'Justiça Federal': 1000 / 3.5,
        'Superior Tribunal da Justiça': 1000 / 7.5
    }

    if ramo not in fatores_por_ramo:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 7A definida.")
        return 'NA'

    try:
        julgados = df['julgm7_a'].sum()
        distribuidos = df['distm7_a'].sum()
        suspensos = df['suspm7_a'].sum()
        denom = distribuidos - suspensos
        fator = fatores_por_ramo[ramo]

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)

    except Exception as e:
        print(f"Erro ao calcular a Meta 7A: {e}")
        return 'NA'

def calcular_meta7B(df, ramo):
    fatores_por_ramo = {
        'Justiça Estadual': 1000 / 5,
        'Justiça Federal': 1000 / 3.5,
        'Superior Tribunal da Justiça': 1000 / 7.5
    }

    if ramo not in fatores_por_ramo:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 7B definida.")
        return 'NA'
    
    try:
        julgados = df['julgm7_b'].sum()
        distribuidos = df['distm7_b'].sum()
        suspensos = df['suspm7_b'].sum()
        denom = distribuidos - suspensos
        fator = fatores_por_ramo[ramo]

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)

    except Exception as e:
        print(f"Erro ao calcular a Meta 7B: {e}")
        return 'NA'

def calcular_meta8(df, ramo):
    if ramo != 'Superior Tribunal da Justiça':
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 8 definida.")
        return 'NA'

    try:
        julgados = df['julgm8_a'].sum()
        distribuidos = df['distm8_a'].sum()
        suspensos = df['suspm8_a'].sum()
        denom = distribuidos - suspensos
        fator = 1000 / 10

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)
    except Exception as e:
        print(f"Erro ao calcular a Meta 8: {e}")
        return 'NA'


def calcular_meta8a(df, ramo):
    ramos_com_meta8a = [
        'Justiça Estadual'
    ]

    if ramo not in ramos_com_meta8a:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 8A definida.")
        return 'NA'

    try:
        julgados = df['julgm8_a'].sum()
        distribuidos = df['distm8_a'].sum()
        suspensos = df['suspm8_a'].sum()

        denom = distribuidos - suspensos
        fator = 1000 / 7.5

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)

    except Exception as e:
        print(f"Erro ao calcular a Meta 8A: {e}")
        return 'NA'


def calcular_meta8b(df, ramo):
    ramos_com_meta8b = [
        'Justiça Estadual',
        'Superior Tribunal da Justiça'
    ]

    if ramo not in ramos_com_meta8b:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 8B definida.")
        return 'NA'

    try:
        julgados = df['julgm8_b'].sum()
        distribuidos = df['distm8_b'].sum()
        suspensos = df['suspm8_b'].sum()

        denom = distribuidos - suspensos
        fator = 1000 / 9

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)

    except Exception as e:
        print(f"Erro ao calcular a Meta 8B: {e}")
        return 'NA'

def calcular_meta10(df, ramo):
    if ramo != 'Superior Tribunal da Justiça':
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 10 definida.")
        return 'NA'

    try:
        julgados = df['julgm10_a'].sum()
        distribuidos = df['distm10_a'].sum()
        suspensos = df['suspm10_a'].sum()

        denom = distribuidos - suspensos
        fator = 1000 / 10

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)
    except Exception as e:
        print(f"Erro ao calcular a Meta 10: {e}")
        return 'NA'

def calcular_meta10A(df, ramo):
    fatores_por_ramo = {
        'Justiça Estadual': 1000 / 9,
        'Justiça Federal': 100
    }

    if ramo not in fatores_por_ramo:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 10A definida.")
        return 'NA'

    try:
        julgados = df['julgm10_a'].sum()
        distribuidos = df['distm10_a'].sum()
        suspensos = df['suspm10_a'].sum()
        fator = fatores_por_ramo[ramo]
        denom = distribuidos - suspensos

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2) 

    except Exception as e:
        print(f"Erro ao calcular a Meta 10A: {e}")
        return 'NA'

def calcular_meta10B(df, ramo):
    fatores_por_ramo = {
        'Justiça Estadual': 1000 / 10
    }

    if ramo not in fatores_por_ramo:
        print(f"Ramo de Justiça '{ramo}' não tem a Meta 10B definida.")
        return 'NA'

    try:
        julgados = df['julgm10_b'].sum()
        distribuidos = df['distm10_b'].sum()
        suspensos = df['suspm10_b'].sum()
        fator = fatores_por_ramo[ramo]

        denom = distribuidos - suspensos

        if denom == 0:
            return 'NA'
        else:
            return round((julgados / denom) * fator, 2)

    except Exception as e:
        print(f"Erro ao calcular a Meta 10B: {e}")
        return 'NA'

def processar_arquivo(caminho_csv):
    try:
        df = pd.read_csv(caminho_csv)
        
        tribunal = df['sigla_tribunal'].iloc[0]
        ramo_raw = df['ramo_justica'].iloc[0]
        ramo = normalizar_ramo(ramo_raw, tribunal)

        print(f"Processando tribunal {tribunal} do ramo: {ramo} (original: {ramo_raw}).")

        meta1 = calcular_meta1(df, ramo)
        meta2a = calcular_meta2A(df, ramo)
        meta2b = calcular_meta2B(df, ramo)
        meta2c = calcular_meta2C(df, ramo)
        meta2ant = calcular_meta2ANT(df, ramo)
        meta4a = calcular_meta4A(df, ramo)
        meta4b = calcular_meta4B(df, ramo)
        meta6 = calcular_meta6(df, ramo)
        meta7a = calcular_meta7A(df, ramo)
        meta7b = calcular_meta7B(df, ramo)
        meta8 = calcular_meta8(df, ramo)
        meta8a = calcular_meta8a(df, ramo)
        meta8b = calcular_meta8b(df, ramo)
        meta10 = calcular_meta10(df, ramo)
        meta10a = calcular_meta10A(df, ramo)
        meta10b = calcular_meta10B(df, ramo)

        return {
            'tribunal': tribunal,
            'ramo_justica': ramo,
            'meta1': meta1,
            'meta2A': meta2a,
            'meta2B': meta2b,
            'meta2C': meta2c,
            'meta2ANT': meta2ant,
            'meta4A': meta4a,
            'meta4B': meta4b,
            'meta6': meta6,
            'meta7A': meta7a,
            'meta7B': meta7b,
            'meta8': meta8,
            'meta8A': meta8a,
            'meta8B': meta8b,
            'meta10': meta10,
            'meta10A': meta10a,
            'meta10B': meta10b
        }
    except Exception as e:
        print(f"Erro ao processar arquivo {caminho_csv}: {e}")
        return None

def consolidar_dados(pasta):
    todos_arquivos = [os.path.join(pasta, f) for f in os.listdir(pasta) if f.endswith('.csv')]

    with Pool(cpu_count()) as pool:
        lista_dfs = pool.map(pd.read_csv, todos_arquivos)
    
    df_consolidado = pd.concat(lista_dfs, ignore_index=True)
    df_consolidado.to_csv('Consolidado.csv', index=False)
    print("Consolidado.csv: arquivo gerado com sucesso.")
    return todos_arquivos

def main():
    pasta = 'Dados'
    
    todos_arquivos = consolidar_dados(pasta)

    with Pool(cpu_count()) as pool:
        lista_resultados = pool.map(processar_arquivo, todos_arquivos)
    
    lista_resultados = [r for r in lista_resultados if r is not None]
    
    df_resultados = pd.DataFrame(lista_resultados)
    df_resultados.to_csv('ResumoMetas.csv', index=False)
    print("ResumoMetas.csv: arquivo gerado com sucesso.")
    
    end = time.time()
    print(f"Tempo total de execução: {end - start:.2f} segundos")

if __name__ == '__main__':
    main()