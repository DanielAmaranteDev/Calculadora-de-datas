# Calculadora de Dias

Script em Python que calcula datas futuras ou passadas a partir de hoje criado para resolver um problema real do meu trabalho em um cartório.

## O problema

No cartório onde trabalhei, grande parte dos processos possui prazos contados em dias corridos a partir da data do protocolo. Para calcular esses prazos, precisávamos fazer a contagem manualmente, consultando o calendário. Além de consumir tempo, esse método estava sujeito a erros. Esse script resolveu esse problema de forma simples: basta informar a quantidade de dias que deseja adicionar ou subtrair e ele retorna a data exata. Uma solução simples para um problema simples.

## Como funciona

- Escolha entre calcular uma data **futura** (F) ou **passada** (P).
- Informe a quantidade de dias.
- O programa mostra a data exata correspondente, no formato `dd/mm/aaaa`.
- Repete quantas vezes quiser até você optar por sair.

## Como executar

### Opção 1 — Executável pronto (Windows)
Baixe o `.exe` mais recente na aba [Releases](https://github.com/DanielAmaranteDev/Calculadora-de-datas/releases) e dê dois cliques. Não precisa instalar Python nem dependências.

### Opção 2 — Rodando o código-fonte
```bash
pip install -r requirements.txt
python contador-de-dias.py
```
## Exemplo de uso

```
CALCULADORA DE DIAS
Calcula dias futuros ou passados com base na data atual

Você quer calcular dias futuros ou passados? (F/P): F
Quantos dias você quer calcular no futuro? 30
calculando...
Hoje é 22/08/2026 e daqui a 30 dias será 21/09/2026.

Deseja sair? (S/N): S
Programa encerrado!
```

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📄 Licença

Este projeto está sob a licença MIT
