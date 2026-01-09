
# 🚀 Task API – FastAPI DevOps Project

Projet backend **professionnel** réalisé sous **Linux (Ubuntu)**, visant à démontrer une chaîne **DevOps complète** :
API REST → Conteneurisation → Orchestration → CI/CD → Cloud-ready.

---

## 🎯 Objectifs du projet

- Construire une **API REST moderne** avec FastAPI
- Utiliser **SQLAlchemy** pour la persistance des données
- Conteneuriser l’application avec **Docker**
- Orchestrer les services avec **Docker Compose**
- Mettre en place une **pipeline CI/CD GitHub Actions**
- Préparer un futur déploiement cloud (AWS / GCP / Azure)

---

## 🛠️ Stack technique

|Domaine | Technologie|
| ------- | -------- | 
| Langage     | Python 3.10+ | 
| Framework API    | FastAPI | 
| Server ASGI   | Uvicorn | 
| ORM    | SQLAlchemy 2.x |
| Base de données    | PostgreSQL |
| Conteneurisation | Docker |
| Orchestration    | Docker Compose |
| CI/CD    | Github Actions |
| OS Cible    | Linux |

```
```
## ⚙️ Prérequis

- Ubuntu Linux
- Python **3.10 ou supérieur**
- Docker Engine
- Docker Compose
- Git

Vérification rapide :
```bash
docker --version
docker compose version
python3 --version
````

---

## 🚀 Lancement du projet (Docker)

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/CodesVibes229/Task_API.git
cd Task_API
```

---

### 2️⃣ Créer le fichier `.env`

```bash
cp .env.example .env
```

Exemple :

```env
POSTGRES_DB=taskdb
POSTGRES_USER=taskuser
POSTGRES_PASSWORD=taskpassword
DATABASE_URL=postgresql://taskuser:taskpassword@db:5432/taskdb
```

---

### 3️⃣ Build & run

```bash
docker compose up --build
```

---

### 4️⃣ Accéder à l’API

* API : [http://localhost:8000](http://localhost:8000)
* Swagger UI : [http://localhost:8000/docs](http://localhost:8000/docs)
* OpenAPI JSON : [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

## 📌 Endpoints disponibles (exemple)

| Méthode | Endpoint | Description             |
| ------- | -------- | ----------------------- |
| GET     | `/tasks` | Lister les tâches       |
| POST    | `/tasks` | Créer une tâche         |
| GET     | `/users` | Lister les utilisateurs |
| POST    | `/users` | Créer un utilisateur    |

---

## 🧪 Lancer les tests

```bash
pytest
```

---

## 🔄 CI/CD (GitHub Actions)

Pipeline automatisée :

* Installation des dépendances
* Linting (`flake8`)
* Tests (`pytest`)
* Vérification du build Docker

Déclenchée sur :

* `push`
* `pull_request`

---

## 🧠 Bonnes pratiques appliquées

✔ Architecture propre
✔ Séparation API / DB
✔ Variables d’environnement
✔ Conteneurs isolés
✔ CI/CD automatisée
✔ Prêt pour production

---

## 🚧 Améliorations futures

* Authentification JWT
* Gestion des rôles (RBAC)
* Migrations Alembic
* Déploiement cloud (EC2 / ECS / GKE)
* Monitoring (Prometheus + Grafana)

---

## 👤 Auteur

**Harold**
Backend / DevOps junior
Passionné par l’infrastructure, l’automatisation et les systèmes distribués.

---

## 📄 Licence

Projet open-source à but pédagogique.
