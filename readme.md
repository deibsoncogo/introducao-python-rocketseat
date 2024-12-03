# Introdução ao Python | Rocketseat

🚀 Explorando novas possibilidades com Python! 🐍

Recentemente tive meu primeiro contato com Python durante o curso "Introdução ao Python" realizado pela Rocketseat.

Foi uma experiência incrível aprender os fundamentos dessa linguagem tão versátil e também explorar o framework Flask e o banco de dados SQLite.

No projeto final, desenvolvemos um sistema onde o usuário pode adicionar produtos a um carrinho de compras, integrando conceitos de backend com Python, rotas criadas com Flask e armazenamento eficiente com SQLite.

Foi uma oportunidade fantástica para consolidar conhecimentos e expandir minhas habilidades como desenvolvedor.

Estou animado para continuar explorando o universo Python e aplicar esses aprendizados em novos desafios! 🎯

👉 Se você também é fã de Python ou trabalha com Flask, adoraria trocar ideias. Vamos compartilhar experiências!

#Python #DesenvolvimentoWeb #Rocketseat #Flask #SQLite #Backend #DevFullStack #Programação #Tech #Inovação

# Execução do projeto

Este projeto não está sendo executado em nenhum servidor online, mas você pode seguir os seguintes passo para rodar ele em sua maquina.

## Instalação

Primeiramente instale as dependências utilizando o `PIP3`:

```bash
pip3 install -r requirements.txt
```

Agora é a hora de executar o banco de dados `MSQLite` utilizando um terminal junto da criação de um usuário administrador:

```bash
flask shell
```

```bash
db.create_all()
```

```bash
user = User(userName="admin", password="123")
```

```bash
db.session.add(user)
```

```bash
db.session.commit()
```

```bash
exit()
```

Por fim basta executar o servidor utilizando seu editor de código.
