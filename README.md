# ClientesCRM — Django + SQLite

Sistema de Cadastro de Clientes com Django, rodando localmente com SQLite.

## Requisitos

- Python 3.11+
- Nada mais — o SQLite já vem com o Python.

## Configuração e execução

```bash
# 1. Instalar o Django
pip install -r requirements.txt

# 2. Aplicar as migrations (cria o banco db.sqlite3 automaticamente)
python manage.py migrate

# 3. Criar um usuário para fazer login
python manage.py createsuperuser

# 4. Rodar o servidor
python manage.py runserver
```

Acesse: **http://localhost:8000**

---

## Estrutura do projeto

```
.
├── cliente_crud/        # Configurações do projeto
│   ├── settings.py
│   └── urls.py
├── clientes/            # App principal
│   ├── models.py        # Model Cliente
│   ├── views.py         # Views CRUD + autenticação
│   ├── forms.py         # Formulário
│   ├── urls.py          # Rotas
│   └── admin.py         # Painel admin
├── templates/
│   ├── base.html
│   ├── auth/login.html
│   └── clientes/        # list, detail, form, confirm_delete
├── db.sqlite3           # Banco criado automaticamente
├── requirements.txt
└── manage.py
```

## URLs

| URL | Descrição |
|-----|-----------|
| `/login/` | Login |
| `/clientes/` | Listagem |
| `/clientes/novo/` | Novo cliente |
| `/clientes/<id>/` | Detalhes |
| `/clientes/<id>/editar/` | Editar |
| `/clientes/<id>/excluir/` | Excluir |
| `/admin/` | Painel admin Django |
