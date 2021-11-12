# Stock-Quote-Alert

O objetivo do sistema é auxiliar um investidor nas suas decisões de comprar/vender ativos. Para tal, ele deve registrar periodicamente a cotação atual de ativos da B3 e também avisar, via e-mail, caso haja oportunidade de negociação.

## Requisitos

Os seguintes requisitos funcionais são necessários:

- Obter periodicamente as cotações de alguma fonte pública qualquer e armazená-las, em uma periodicidade configurável, para consulta posterior

- Expor uma interface web para permitir consultar os preços armazenados, configurar os ativos a serem monitorados e parametrizar os túneis de preço de cada ativo

- Enviar e-mail para o investidor sugerindo Compra sempre que o preço de um ativo monitorado cruzar o seu limite inferior, e sugerindo Venda sempre que o preço de um ativo monitorado cruzar o seu limite superior

## Configurações

Para instalar as dependências necessárias, execute o comando abaixo dentro do diretório do projeto:

```
pip install -r requirements.txt
```

O serviço de e-mail exige as seguintes configurações presentes no arquivo `settings.py`:

```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') 
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

Portanto, é necessário criar um arquivo `.env` no diretório raiz do projeto com as seguintes variáveis ambiente:

```
EMAIL_HOST_USER=seuemail@email.com
EMAIL_HOST_PASSWORD=suasenha
```

## Login

Foi criado um super usuário para acessar a Admin Interface. Veja a seguir as credenciais:

```
Username: InoaAdmin
Senha: admin#ino@
```
