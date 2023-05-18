# os-backend docker guide

docker projekt je sestavljen iz treh slih:

- backend (Django)
- db (PostgreSQL)
- nginx (Nginx)

Backend je sam Django projekt serviran z GUnicorn, DB je podatkovna baza na katero se poveze Django, nginx se pa
uporablja za serviranje staticnih in media datotek.

## standalone docker file

Da ustvarimo Django sliko lahko zazenemo:

```
$ docker build -f Dockerfile.standalone -t os-backend:standalone .
```

Preverimo ce je slika bila ustvarjena:

```
$ docker images

REPOSITORY       TAG           IMAGE ID       CREATED         SIZE
os-backend       standalone    4a53ceed404b   5 seconds ago   136MB
```

Uporabi sliko da zazenemo kontejner:

```
$ docker run -p 8000:8000 os-backend:standalone
```

Spletni servis je nato aktiven na [http://localhost:8000](http://localhost:8000). Preverimo lahko z cURL:

```
curl http://localhost:8000/api/
```

Pri tem se moramo zavedat, da Django ne bo deloval pravilno zaradi tega ker nima dostopa do podatkovne baze.
Staticni in media file-u tudi ne bodo delali.

## docker compose

Da ustvarimo Docker compose paket:

```
$ docker-compose -f docker-compose.prod.yml build
```

Da zazenemo Docker Compose servise:

```
$ docker-compose -f docker-compose.prod.yml up
```

Preverimo ce delajo:

```
curl http://localhost/api/
```