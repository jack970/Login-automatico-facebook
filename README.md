<h1 align="center">Login Automático no Facebook</h1>

🚀 Aplicação que navega até o site facebook, usando navegador Chrome, e realiza login automático. Feito em Python.

### 1. 🎲 Instale as dependências
```bash
$ pip install requirements.txt
```

### 2. Configure as credenciais para logar no Facebook
1. Vá para `/configs`
2. O arquivo `.env.example` deve se chamar `.env`
3. E Coloque suas credenciais de login do Facebook em `/configs/.env`
```bash
USUARIO= # Coloque seu usuário de login aqui
SENHA= # Coloque sua senha de login aqui
```

### 3. Executando a aplicação
```bash
$ python logar_facebook.py
```

### 🛠 Tecnologias usadas:
  - [Python3](https://www.python.org)
  - [Selenium](https://pypi.org/project/selenium)
  - [WebDriver Manager](https://pypi.org/project/webdriver-manager)
  - [Python Dotenv](https://pypi.org/project/python-dotenv)