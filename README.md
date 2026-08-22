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

```bash
python calculadora_de_dias.py
```

Requer apenas Python 3 — usa somente bibliotecas padrão (`datetime` e `time`), sem necessidade de instalar nada.

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
