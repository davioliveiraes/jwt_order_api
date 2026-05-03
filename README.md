# JWT Order API

## Finalidade

API REST de pedidos com autenticação e autorização via JWT. Permite que usuários se registrem, autentiquem-se e gerenciem seus próprios pedidos, garantindo que cada usuário acesse apenas os dados que lhe pertencem.

A aplicação foi estruturada seguindo o padrão MVC, com camadas bem definidas (models, controllers, drivers, routes), injeção de dependências via composer e cobertura completa de testes unitários.

## Tecnologias Utilizadas

- **Python 3.12**
- **Flask** — framework HTTP
- **SQLite** — banco de dados
- **PyJWT** — geração e validação de tokens JWT
- **bcrypt** — hashing de senhas
- **python-dotenv** — gerenciamento de variáveis de ambiente
- **pytest** — testes unitários

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/davioliveiraes/jwt_order_api.git
cd jwt_order_api
```

### 2. Criar e ativar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Criar um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
JWT_KEY=sua_chave_secreta_aqui_com_no_minimo_32_caracteres
JWT_ALGORITHM=HS256
JWT_HOURS=2
```

### 5. Inicializar o banco de dados

```bash
python init/init_db.py
```

### 6. Rodar a aplicação

```bash
python run.py
```

Servidor disponível em `http://127.0.0.1:5000`.

### 7. Rodar os testes

```bash
pytest -v
```

## Endpoints

### Públicos

#### `POST /register`

Cria um novo usuário.

**Body:**
```json
{
    "username": "davi",
    "password": "senha123"
}
```

**Respostas:**
- `201 Created` — Usuário criado
- `400 Bad Request` — Usuário já existe

---

#### `POST /login`

Autentica o usuário e retorna o token JWT.

**Body:**
```json
{
    "username": "davi",
    "password": "senha123"
}
```

**Resposta de sucesso (200 OK):**
```json
{
    "user_id": 1,
    "username": "davi",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Resposta de erro (401 Unauthorized):**
```json
{
    "error": "Usuário ou senha incorreto"
}
```

---

### Protegidos (requerem token JWT)

Todas as rotas abaixo exigem o header:
```
Authorization: Bearer <token>
```

#### `POST /orders`

Cria um novo pedido para o usuário autenticado.

**Body:**
```json
{
    "description": "Pedido de notebook"
}
```

**Respostas:**
- `201 Created` — Pedido criado
- `400 Bad Request` — Descrição obrigatória
- `401 Unauthorized` — Token inválido ou ausente

---

#### `GET /orders`

Lista todos os pedidos do usuário autenticado.

**Resposta de sucesso (200 OK):**
```json
{
    "orders": [
        {
            "id": 1,
            "description": "Pedido de notebook",
            "created_at": "2026-05-02 10:00:00"
        },
        {
            "id": 2,
            "description": "Pedido de teclado",
            "created_at": "2026-05-02 11:00:00"
        }
    ]
}
```

**Resposta de erro (401 Unauthorized):**
```json
{
    "error": "Token não fornecido"
}
```

---

## Desenvolvido na trilha de Python da Rocketseat

**Nível 6:** Autenticação JWT e Segurança
