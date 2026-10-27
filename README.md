# Estudos de Consumo de APIs com Python

Este repositório reúne exercícios práticos que desenvolvi durante meus estudos de Python, com foco no consumo de APIs REST utilizando a biblioteca `requests`.

O objetivo é compreender como funciona a comunicação entre aplicações por meio de requisições HTTP, como enviar dados, consultar informações e tratar possíveis erros durante as requisições.

## Tecnologias utilizadas

- **Python** — linguagem utilizada nos exercícios.
- **Requests** — biblioteca para realizar requisições HTTP.
- **JSON** — formato utilizado para receber e enviar dados.
- **Git e GitHub** — versionamento e organização do projeto.
- **JSONPlaceholder** — API de testes utilizada para praticar as requisições.

## O que pratiquei

Durante o desenvolvimento dos exercícios, pratiquei:

- **GET:** consultar e listar usuários.
- **POST:** enviar dados para simular a criação de um usuário.
- **PUT:** enviar dados para simular a atualização completa de um usuário.
- **PATCH:** enviar dados para simular uma atualização parcial.
- **DELETE:** enviar uma solicitação de exclusão.
- **Parâmetros de consulta:** filtrar usuários por informações como `username`.
- **JSON:** interpretar os dados retornados pela API.
- **Códigos de status HTTP:** verificar o resultado das requisições.
- **Tratamento de erros:** utilizar `try/except` e `timeout` para lidar com possíveis falhas de comunicação.

## Organização dos arquivos

| Arquivo | Descrição |
|---|---|
| `primeiro_get.py` | Primeiro exercício de consulta de usuários com GET. |
| `buscar_usuario.py` | Exercício de busca de usuários. |
| `buscar_usuario_filtro.py` | Busca de usuários utilizando parâmetros de consulta. |
| `criar_usuario.py` | Envio de dados com POST. |
| `atualizar_usuario.py` | Atualização de dados com PUT. |
| `atualizar_parcial.py` | Atualização parcial com PATCH. |
| `delete_usuario.py` | Solicitação de exclusão com DELETE. |

## Como executar os exercícios

**1. Clone o repositório:**

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço do repositório no GitHub.

**2. Entre na pasta do projeto:**

```bash
cd api_estudos
```

**3. Instale a biblioteca utilizada:**

```bash
python -m pip install requests
```

**4. Execute o exercício desejado:**

```bash
python buscar_usuario_filtro.py
```

Você também pode executar os demais arquivos Python individualmente.

## API utilizada

Os exercícios utilizam a [JSONPlaceholder](https://jsonplaceholder.typicode.com/), uma API pública de testes que permite praticar operações comuns de uma API REST.

**Importante:** as operações de criação, atualização e exclusão do JSONPlaceholder são simuladas. Os exemplos não representam alterações persistentes em um banco de dados real.

## Objetivo de aprendizado

Este projeto faz parte da minha jornada de aprendizado em Python e desenvolvimento back-end. Estou construindo uma base prática para avançar na criação de APIs próprias, integração com bancos de dados e desenvolvimento de aplicações.

## Autor

Estudante de Análise e Desenvolvimento de Sistemas, com interesse em Python, desenvolvimento back-end, APIs REST e bancos de dados.
