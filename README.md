🏆 Sistema de Premiação de Vendedores (ConstruTech)

Este projeto foi desenvolvido para o departamento de RH, com o objetivo de automatizar o cálculo de bônus de performance baseado em produtividade mensal.

## 📌 Diferenciais desta Versão (3.0)
Nesta versão final, implementei uma lógica de decisão robusta que separa o **desempenho constante** da **gratificação total**:
- **Decisão por Média:** O status do vendedor (Top Player, Bronze ou Alerta) é decidido pela sua média mensal de vendas.
- **Bônus sobre o Montante:** A gratificação financeira é aplicada sobre o valor total vendido no período analisado.
- **Integridade de Dados:** Tratamento de valores decimais e acumuladores dinâmicos com listas.

## 🚀 Regras de Negócio Aplicadas
| Média Mensal | Status | Bônus |
| :--- | :--- | :--- |
| Acima de R$ 5.000,00 | Top Player | 10% sobre o total |
| Entre R$ 2.000,00 e R$ 5.000,00 | Vendedor Bronze | 5% sobre o total |
| Abaixo de R$ 2.000,00 | Alerta de Performance | Sem bônus |
