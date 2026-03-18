import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# ENTRADAS
capital = float(input('Capital inicial: '))
aporte  = float(input('Aporte mensal: '))
meses  = float(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual %: ')) / 100
perc_cdb = float(input('Percentual do CDI - CDB (%): ')) / 100
perc_lci = float(input('Percentual do CDI - LCI (%): ')) / 100
taxa_fii = float(input('Rentabilidade do FII (%): ')) / 100
meta = float(input('Meta financeira (R$): '))

# conversao CDI
cdi_mensal = math.pow((1 + cdi_anual), 1/12) - 1

# total investido
total_investido = capital + (aporte * meses)

# CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1 + taxa_cdb), meses)) + (aporte * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

# LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses)) + (aporte * meses)

# poupanca
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1 + taxa_poupanca), meses)) + (aporte * meses)

# --- CÁLCULOS FII ---
# Gerando a lista de evolução mensal para as estatísticas
# Cada item da lista representa o montante acumulado até aquele mês
valores_fii = [(capital + i * aporte) * math.pow(1 + taxa_fii, meses - i) for i in range(int(meses) + 1)]
montante_fii = valores_fii[-1]  # O último valor da lista é o montante final

# Estatísticas do FII usando o módulo statistics
media_fii = statistics.mean(valores_fii)
mediana_fii = statistics.median(valores_fii)
# Desvio padrão precisa de pelo menos 2 pontos de dados
desvio_fii = statistics.stdev(valores_fii) if len(valores_fii) > 1 else 0.0

# --- DATAS ---
data_simulacao = datetime.datetime.now()
# Calculando resgate aproximado (meses * 30 dias)
data_resgate = data_simulacao + datetime.timedelta(days=int(meses) * 30)

# --- INDICADOR DE META ---
atingiu_meta = montante_fii >= meta

# --- RELATÓRIO FINAL OBRIGATÓRIO ---
print("\n" + "="*60)
print("SISTEMA DE SIMULAÇÃO DE INVESTIMENTOS - RELATÓRIO FINAL")
print("="*60)
print(f"Data da simulação:           {data_simulacao.strftime('%d/%m/%Y %H:%M')}")
print(f"Data estimada de resgate:    {data_resgate.strftime('%d/%m/%Y')}")
print(f"Total investido:             {locale.currency(total_investido, grouping=True)}")
print("-" * 60)
print(f"Valor final CDB (Líquido):   {locale.currency(montante_cdb_liquido, grouping=True)}")
print(f"Valor final LCI:             {locale.currency(montante_lci, grouping=True)}")
print(f"Valor final Poupança:        {locale.currency(montante_poupanca, grouping=True)}")
print(f"Valor final FII:             {locale.currency(montante_fii, grouping=True)}")
print("-" * 60)
print(f"ESTATÍSTICAS FII:")
print(f" > Média:                    {locale.currency(media_fii, grouping=True)}")
print(f" > Mediana:                  {locale.currency(mediana_fii, grouping=True)}")
print(f" > Desvio Padrão:            {locale.currency(desvio_fii, grouping=True)}")
print("-" * 60)
print(f"META FINANCEIRA ATINGIDA?    {atingiu_meta}")
print("="*60)

# --- REPRESENTAÇÃO GRÁFICA OBRIGATÓRIA ---
# Regra: Cada bloco █ representa R$ 1.000. 
# Construção por multiplicação de strings (sem laços for).

print("\nDESEMPENHO POR MODALIDADE (█ = R$ 1.000)")

# Calculamos a quantidade de blocos usando divisão inteira (//)
blocos_cdb = int(montante_cdb_liquido // 1000)
blocos_lci = int(montante_lci // 1000)
blocos_poup = int(montante_poupanca // 1000)
blocos_fii = int(montante_fii // 1000)

print(f"CDB:      {blocos_cdb * '█'} ({locale.currency(montante_cdb_liquido, grouping=True)})")
print(f"LCI:      {blocos_lci * '█'} ({locale.currency(montante_lci, grouping=True)})")
print(f"POUPANÇA: {blocos_poup * '█'} ({locale.currency(montante_poupanca, grouping=True)})")
print(f"FII:      {blocos_fii * '█'} ({locale.currency(montante_fii, grouping=True)})")
print("="*60)
