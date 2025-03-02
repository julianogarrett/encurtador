# Encurtador de URLs

Um encurtador de URLs simples e eficiente, desenvolvido com Flask e Python. 
Este projeto permite encurtar URLs longas e redirecionar para a URL original usando um servidor local.

# Como usar

## Pré-requisitos

- Python 3.8 ou superior.
- Pip (gerenciador de pacotes do Python).

## Instalação

### 1. Clone o repositório:

   ```bash
   git clone https://github.com/julianogarrett/encurtador.git
   ```
### 2. Instale o Postman
Baixe e instale o Postman: [https://www.postman.com/downloads/](https://www.postman.com/downloads/).

### 3. Execute o projeto
Inicie o servidor Flask:
```bash
python app.py
```
O servidor estará rodando em http://localhost:5000.

### 4. Use o Postman para executar a API
Abra o Postman.

Crie uma nova requisição clicando em New > Request.
Dê um nome à requisição (ex.: "Encurtar URL") e salve em uma coleção (ou crie uma nova).

####Configure a requisição:
Método HTTP: Selecione POST.

URL: Digite http://localhost:5000/shorten.
Headers: Adicione um cabeçalho para indicar que você está enviando JSON:
Chave: Content-Type
Valor: application/json

#### Envie o corpo da requisição (body):
Clique na aba Body.
Selecione raw e escolha JSON no menu suspenso.
Digite o JSON com a URL que você quer encurtar:

```bash
{
  "url": "https://www.exemplo.com"
}
```
Clique em Send.

A resposta será exibida na parte inferior da tela. Você deve receber algo como:
```bash
{
  "short_url": "http://localhost:5000/abc123"
}
```
#### Copie o url gerado e cole em seu navegador. Você será redirecionado automaticamente.

## Endpoints da API

Encurtar uma URL
Método: POST

URL: http://localhost:5000/shorten

Corpo da requisição (JSON):
```bash
{
  "url": "https://www.exemplo.com"
}
```

Resposta (JSON):
```bash
{
  "short_url": "http://localhost:5000/abc123"
}
```
Acessar a URL original
Método: GET

URL: http://localhost:5000/<short_code>

Substitua <short_code> pelo código gerado (ex.: abc123).

Resposta: Redirecionamento automático para a URL original.

# S2 BRUNO

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
