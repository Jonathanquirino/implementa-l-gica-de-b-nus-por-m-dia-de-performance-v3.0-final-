"""
A empresa quer premiar os vendedores

O que o programa deve fazer:

Entrada: Pergunte o nome do vendedor e quantos meses de vendas serão analisados.

O Loop (for): Peça o valor total de vendas de cada mês.

O Processamento:

Calcule a Média Mensal de vendas.

A Regra de Ouro (Condicionais):

Se a média for maior que R$ 5.000,00: O vendedor ganha o status de "Top Player" e um bônus de 10% sobre o total vendido.

Se a média estiver entre R$ 2.000,00 e R$ 5.000,00: Status "Vendedor Bronze" e bônus de 5%.

Se a média for menor que R$ 2.000,00: Status "Alerta de Performance" e não ganha bônus.

Saída (Relatório): Mostre o nome, a média de vendas, o status alcançado e o valor do bônus (se houver).
"""
print('--- Sistema de Premiação ---')

print('Seja bem vindo!')
nome = input('Qual o nome do vendedor? ')
meses_sobre_analise = int(input('Quantos meses quer analisar? '))
resultado = 0
contagem = []
total_vendas = 0
status = ""

for venda in range(1, meses_sobre_analise+1):
    cauculo = float(input(f'Qual o valor do {venda}º mês? '))
    contagem.append(cauculo)
    total_vendas = sum(contagem)
    media = total_vendas/meses_sobre_analise
if media >= 5000:
    status = 'Vendedor Top Player'
    bonus = total_vendas * 0.10
    resultado = total_vendas + bonus
elif media >= 2000:
    status = 'Vendedor Bronze'
    bonus = total_vendas * 0.05
    resultado = total_vendas + bonus
else:
    status = 'Alerta de Performance'
    resultado = total_vendas


print(f'O vendedor {nome}, vendeu {contagem} em {meses_sobre_analise} meses com média de {media}, no total de {total_vendas}, o status é {status} valor final é R${resultado:.2f}')