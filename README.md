
🚀 Task API – FastAPI, Docker & CI/CD

API REST de gestion de tâches développée avec **FastAPI**, conteneurisée avec **Docker** et intégrant un pipeline **CI/CD complet via GitHub Actions**.

Ce projet a été conçu comme un **projet DevOps / Backend de bout en bout**, en environnement Linux natif.

---

🎯 Objectifs du projet

- Concevoir une API REST propre et maintenable
- Mettre en place des tests automatisés
- Conteneuriser l’application avec Docker
- Orchestrer les services avec Docker Compose
- Implémenter un pipeline CI/CD fonctionnel
- Préparer l’application pour un futur déploiement cloud

---

## 🧱 Stack technique

### Backend
- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **SQLite** (facilement remplaçable par PostgreSQL)

### DevOps
- **Docker**
- **Docker Compose**
- **GitHub Actions**
- **GitHub Container Registry (GHCR)**

### Tests
- **Pytest**
- **FastAPI TestClient**

---

## ⚙️ Fonctionnalités

- ✅ API REST fonctionnelle
- ✅ Endpoint racine de vérification de santé
- ✅ Création et listing de tâches
- ✅ Tests automatisés
- ✅ Build Docker reproductible
- ✅ Pipeline CI/CD automatisé
- ✅ Push automatique de l’image Docker vers GHCR

---

## ▶️ Lancer le projet en local (sans Docker)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export DATABASE_URL=sqlite:///./app.db
uvicorn app.main:app --reload
````

Accès API :
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Lancer les tests

```bash
export DATABASE_URL=sqlite:///./test.db
pytest
```

---

## 🐳 Lancer avec Docker

### Build de l’image

```bash
docker build -t task-api .
```

### Lancer le conteneur

```bash
docker run -d \
  --name task_api_container \
  -p 8000:8000 \
  -e DATABASE_URL=sqlite:///./app.db \
  task-api
```

---

## 🐳 Docker Compose

```bash
docker compose up --build
```

---

## 🔄 CI/CD – GitHub Actions

Le pipeline CI/CD se déclenche automatiquement sur :

* `push`
* `pull_request`

### Étapes du pipeline :

1. Installation des dépendances
2. Exécution des tests
3. Build de l’image Docker
4. Push vers GitHub Container Registry (GHCR)

✔️ Le pipeline doit être **vert** avant tout push d’image.

---

## 📦 Image Docker

L’image est publiée automatiquement sur :

```
ghcr.io/CodesVibes229/task-api:latest
```

---

## 🔐 Variables d’environnement

| Variable     | Description               |
| ------------ | ------------------------- |
| DATABASE_URL | URL de la base de données |

---

## 🚀 Évolutions prévues

* PostgreSQL
* Sécurité (authentification JWT)
* Déploiement VPS / Cloud
* Monitoring & logs
* Migration vers Kubernetes

---

## 👤 Auteur

**Pascal**
Projet personnel – DevOps / Backend
Linux • Docker • FastAPI • CI/CD

---

## 📜 Licence

Projet open-source à but pédagogique.

