# Собираем кастомный образ

`docker build -f ./src/Dockerfile . -t jupyterhub `

![1741206670037](image/README/1741206670037.png)

Отправляем его в minikube:

`minikube image load jupyterhub_custom:latest`

# Настройка minikube

Применяем манифесты

`kubectl create -f jupyterhub.yml`

`kubectl create -f postgresql.yml`

Проверяем

`kubectl logs deployment/jupyterhub`

![1741206807685](image/README/1741206807685.png)

Заходит в jupyterhub извне:

`kubectl port-forward service/jupyterhub-service 8000:8000`

![1741206873911](image/README/1741206873911.png)

# Инфраструктура

## Postgres

* ConfigMap, с переменной названия БД
* Secrets, с переменными для подключения к БД
* Service
* Deployment
* init-container
* livenessProbe

  ![1741207446493](image/README/1741207446493.png)

## Jupyterhub

* Secrets, с начальным скриптом инициализации
* Service
* Deployment
