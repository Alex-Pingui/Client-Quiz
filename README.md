# Client Questionnaires

## Groupe

### Alexandre GUIHARD
### Sileye FRANCHET

## Installation

### Serveur
Pour utiliser le serveur avec lequel les clients vont pouvoir communiquer, 
il faut tout d'abord installer les dépendances avec les commandes suivantes:

```bash
cd api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Client
Pour lancer un client, vous devez, dans un premier temps installer les dépendances avec la commande suivante
```bash
cd client
npm install
```

## Utilisation

### Serveur
Pour lancer le serveur, il faut exécuter les commandes suivantes
```bash
cd api
source .venv/bin/activate
flask run
```

### Client
Pour lancer un client dans un navigateur, il faut exécuter la commande suivante
```bash
cd client
npm run dev
```

Après cela, rendez-vous sur votre navigateur à [cet adresse]

[cet adresse]: http://localhost:5173