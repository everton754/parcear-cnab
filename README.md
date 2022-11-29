# CNAB Transactions

Este projeto de back-end é responsável por parsear e receber arquivos CNAB, e foi desenvolvida em Python, utilizando do Django como framework.

# 👨‍🏫 Passo a Passo

1. Crie seu ambiente virtual:

> python -m venv venv

2. Ative seu venv:

#### windows

> .\venv\Scripts\activate

#### linux

> source venv/bin/activate

3. Instale todas as dependências:

> pip install -r requirements.txt

4. Rode as migrações:

> python manage.py migrate

5. Execute a população da tabela de tipos:

> python manage.py create_types

<br>

# 🚴‍♂️ Rotas da aplicação

```
GET: /api/upload/
```

Endpoint, sem a necessidade de autorização, onde mostra o banco de dados, ao usuário em uma página html com as transações, onde o mesmo pode fazer envios.

```
POST: /api/upload/
```

Mostra o armazenamento, além de fazer a leitura das informações no banco de dados assim que o botão enviar for acionado, não há necessidade de autorização.

<hr></hr>

## Documentação do CNAB 📃

![alt text](https://conteudo-kenzie-fullstack.vercel.app/modulo_6/desafio_backend/img/documentacao_cnab.png)

## Documentação sobre os tipos das transações 📃

![alt text](https://conteudo-kenzie-fullstack.vercel.app/modulo_6/desafio_backend/img/tipo_transacao.png)

<hr></hr>
<br></br>
