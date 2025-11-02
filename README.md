# Projeto To-Do List com Django

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

Um projeto simples de aplicação "To-Do List" (Lista de Tarefas) desenvolvido com o framework web Django.

## 🎯 Objetivo do Projeto

O principal objetivo deste repositório foi **educacional**. Ele foi desenvolvido como um exercício prático durante meu período de estágio, com o intuito de:

* **Familiarização com o Django:** Entender a estrutura de um projeto Django (models, views, templates, URLs).
* **Aprendizado de CRUD:** Praticar as operações fundamentais de um banco de dados (Create, Read, Update, Delete).
* **Fundamentos do Padrão MVT:** Aplicar na prática o padrão Model-View-Template.

## 🚀 Tecnologias Utilizadas

* **Django:** O principal framework web utilizado.
* **Python:** A linguagem de programação base.
* **HTML/CSS:** Para a estrutura e estilização básica do front-end.


## 🔧 Funcionalidades

A aplicação permite ao usuário:

* Adicionar novas tarefas.
* Visualizar todas as tarefas pendentes.
* Marcar tarefas como "concluídas".
* Excluir tarefas da lista.

## ⚙️ Como Executar Localmente

Para executar este projeto em sua máquina, siga os passos abaixo:

```bash
# 1. Clone o repositório
git clone [https://github.com/Victorlave333/Projeto_to_do_New.git](https://github.com/Victorlave333/Projeto_to_do_New.git)

# 2. Navegue até a pasta do projeto
cd to_do

# 3. (Recomendado) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate

# 4. Instale as dependências (crie um requirements.txt se não tiver)
pip install django
# (Se houver um requirements.txt: pip install -r requirements.txt)

# 5. Aplique as migrações do banco de dados
python manage.py migrate

# 6. Inicie o servidor local
python manage.py runserver

# 7. Abra seu navegador em [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
