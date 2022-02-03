# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o reposiório.
2. Crie um virtualenv com python 3.9
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
    cd workspace
    git clone git@github.com:wt3c/wttd.git
    mkvirtual -p /opt/pyenv/versions/3.9.9/bin/python wttd
    workon wttd
    pip install -r requiements-dev.txt
    cp contrib/env-sample .env
    python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância para o heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET_KEY segura para instância.
4. Define DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku  create minhainstancia
heroku config:push
heroku config:set SECRET_KEY = `python contrib/secret_gen.py` -- https://gist.github.com/henriquebastos/11cf99c1bbc70bacf73a
heroku config:set DEBUG=False
# Configuro email
git push heroku master --force
```

AGORA VAI
