# Calculadora de Dias

Script em Python que calcula datas futuras ou passadas a partir de hoje criado para resolver um problema real do meu trabalho em um cartório.

## O problema

No cartório, boa parte dos processos tem prazos contados em dias corridos a partir de uma data de entrada (por exemplo, um prazo de 30 dias). Calcular manualmente a data exata em que o prazo vence é fácil de errar e toma tempo. Este script resolve isso: basta informar quantos dias somar ou subtrair, e ele retorna a data exata. Uma resolução simples para um problema simples.

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

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📄 Licença

Este projeto está sob a licença MIT
