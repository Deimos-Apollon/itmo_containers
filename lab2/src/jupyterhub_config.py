import os

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.hub_connect_ip = '127.0.0.1'

c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
c.DummyAuthenticator.password = '123'

c.JupyterHub.db_url = f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["PGPASSWORD"]}'\
    '@postgres:5432/'

c.Spawner.default_url = '/lab'
