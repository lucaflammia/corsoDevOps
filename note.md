# Corso DevOps for developers

## Docker e Docker Compose
```
docker build --tag devops:1.0 -f devops/Dockerfile .
docker run -it devops:1.0 

docker-compose -f devops/docker-compose.yml  up -d --build
docker exec -it devops_website_1 /bin/bash 
```

## Docker Hub
```
docker images
docker tag a1c6014b2ec5 devops_api:firsttry
docker push alessandrocuccienergee3 devops_api:firsttry
```

## Jenkins
```
docker build -t jenkins-docker . 
docker run --name jenkins-docker -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker
```

recuperare password amministratore e installare plugin consigliati
finire configurazione e installare plugin docker pipeline

aggiungere credenziali per dockerhub con user e password e deploy key per github

```
docker exec -ti jenkins-docker /bin/sh
ssh-keygen -t rsa -b 4096 -C "alessandro.cucci@energee3.com"
```
creare chiavi per connettersi a github

se da errore di connessione a Docker
```
docker exec -ti -u root jenkins-docker /bin/bash
chmod 666 /var/run/docker.sock
```

## Github Webhook

- aggiungere github webhook
- https://webhookrelay.com/v1/installation/cli
- installare, registrarsi e creare token

```
relay login -k token-key-here -s token-secret-here
export RELAY_KEY=token-key
export RELAY_SECRET=token-secret
relay forward http://localhost:8080/github-webhook/ 
```

## Test API insert 
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"partecipanti":"4"}' \
  http://localhost/insert

```
