# 1. Используем явную версию
FROM jupyterhub/jupyterhub:3.1.1

# 2. Оптимизируем слои. Часто меняющиеся библиотеки питона выделены в отдельный слой.
#     В идеале, конечно, использовать requirements.txt для библиотек питона.
# 3. Очищаем кэш менеджеров пакетов. 
RUN apt update \
    && apt -y install git postgresql-client\
    && apt clean
RUN pip install --no-cache-dir \
    notebook \
    psycopg2-binary \
    jupyterhub-dummyauthenticator

WORKDIR /jupyter

# Изменили ENTRYPOINT на JSON формат.
ENTRYPOINT ["jupyterhub", "--log-level=DEBUG"]
