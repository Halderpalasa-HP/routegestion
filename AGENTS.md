# RouteGestion — Mémoire de projet

Assistant : consulte ce fichier à chaque nouvelle session pour retrouver le contexte. Mets-le à jour quand l'état change.

## Le projet

**Portail national de contrôle des véhicules — République Démocratique du Congo.**
Gestion de véhicules, pièces justificatives (carte grise, assurance, contrôle technique, taxe de circulation) et contrôles de terrain par des agents équipés d'un scanneur QR. Contexte académique/compétition, démo numérique.

- **4 maquettes PNG** (référence visuelle) : `Maquette/` — Tableau de bord, Véhicules & cartes grises, Contrôles & infractions, Paramètres documentaires. Style dark, données RDC (26 provinces, cinquantenaire…), statuts Conforme / À surveiller / Non conforme, e-PV `PV-2026-00482` / `CT-2026-01941`.
- **Architecture validée** : `docs/ARCHITECTURE.md` — **document de référence, lire en premier** (14 sections : stack, BD 14 tables, API 40 endpoints, règles métier, sécurité, plan).

## Stack (validée avec l'utilisateur)

| Couche | Choix |
|---|---|
| Backend | **Python 3.12 + FastAPI + SQLAlchemy 2 + Alembic + Pydantic v2** — MySQL 8 |
| Admin web | **Next.js + React + TypeScript + Tailwind** (App Router) |
| Mobile | **React Native (Expo)** — **réalisé par l'utilisateur lui-même** ; l'API REST §7 d'ARCHITECTURE.md est son contrat |
| QR | `segno` (SVG pur Python) ; e-PV PDF : `reportlab` ; auth : **jeton opaque hashé** (esprit Sanctum, révocable) |

**PHP/ÉMISÉ** : l'utilisateur a explicitement refusé PHP/Laravel/Vue — ne plus proposer. (Herd PHP d'ailleurs cassé en local : `auto_prepend_file` manquant, composer inutilisable — sans importance car non requis.)

## État réel (mise à jour du 05/10/2026)

- ✅ Architecture rédigée : `docs/ARCHITECTURE.md` (stack finale : FastAPI/Next/RN).
- ✅ **Scaffold créé : 120 fichiers + 34 dossiers** (backend, admin-web, mobile-app) — arborescence = §3 de l'archi.
- ✅ **Docstrings ajoutées dans les 117 fichiers scaffold** (seuls les `.gitkeep` restent vides) : chaque fichier explique son rôle et son contenu attendu. **Aucun code écrit** (docstrings uniquement).
- ❌ Aucun code exécutable, aucune dépendance installée, aucune BD, aucun commit git.

### App mobile (créée le 05/10/2026)
- **App React Native active : `mobile/mobile-app/`** (copie du dossier `Desktop\Maquette\mobile-app` — original conservé sur le Bureau, à resynchroniser à chaque changement) : 63 fichiers documentés + `ARCHITECTURE_MOBILE.md` (maquettes ↔ écrans, écrans ↔ endpoints §7, flux scan→constat→e-PV, décisions en attente dont les stats de l'accueil agent).
- `mobile/` contient aussi les **4 maquettes mobiles PNG** ; `mobile-app/` (racine) = squelette de **référence** (16 fichiers documentés, 4 écrans).
- Aucun code mobile écrit : la doc de chaque fichier indique ce qu'il devra contenir.

### Dépôt GitHub
- **`routegestion` (public)** : tout le projet dans un seul dépôt (backend, admin-web, mobile-app, mobile/, Maquette/, docs/).

### Session 05/10/2026 — leçons de méthode
- L'utilisateur a demandé **l'architecture d'abord, puis le squelette** — ne pas écrire le code de lui-même ni lancer `pip/npm install` sans demande explicite.
- Réponse à « va y cree » après architecture = **dossiers + fichiers avec docstring d'attente**, jamais de scaffold exécutable.
- Les docstrings sont la source de vérité « ce que doit contenir ce fichier » — les respecter quand on écrira le code.

## Règles métier essentielles (détail §4-§5-§10 de l'archi)

- **Statuts documents calculés, jamais stockés** : MISSING / VALID / EXPIRED / EXPIRING_SOON (doc le plus récent par type ; renouvellement = ajout de ligne).
- **Statut global** : NON CONFORME (obligatoire EXPIRED/MISSING) > À SURVEILLER (EXPIRING_SOON) > CONFORME. Types non obligatoires n'influencent pas.
- **4 types seed** : CARTE_GRISE (sans échéance), ASSURANCE 30j, CONTROLE_TECHNIQUE 30j, TAXE_CIRCULATION 15j (impayée = document manquant de l'exercice courant). Tout modifiable par l'admin.
- **QR** : `VEH-8F29A73`, 7 chars aléatoires non séquentiels, 1 seul actif par véhicule (index unique MySQL), révocable.
- **POST /controls** : le serveur recalcule tout (jamais faire confiance au client) ; référence e-PV générée serveur (PV- si non conforme, CT- sinon) ; `control_items` fige le constat.
- **Rôles** : ADMIN (tout) / AGENT (scan + ses seuls contrôles) — permissions serveur, jamais seulement UI.

## Décisions en attente (§14 de l'archi — sinon défauts retenus)

1. Nom du propriétaire visible agent (ni téléphone ni adresse) — défaut oui.
2. Seuils 30j/30j/15j par type — défaut oui.
3. Types indépendants de la catégorie véhicule — défaut oui.
4. Laragon/XAMPP/Herd sans Docker — défaut oui.
5. e-PV PDF généré à la demande (reportlab) — défaut oui.
6. Lieu du contrôle : saisie manuelle (défaut) ou GPS auto (`expo-location`).
7. MySQL : `pymysql` synchrone (défaut) ou async `asyncmy`.

## Prochaine étape (plan §13 de l'archi)

**Étape 3 : migrations Alembic + seeds** (26 provinces, 4 types de documents, settings, données démo) → puis auth/roles, CRUD, `DocumentStatusService` avec tests pytest. Respecter l'ordre du plan et l'API §7 (contrat immuable pour le mobile de l'utilisateur).

## Environnement local

- Python **3.12.8** (`C:\Users\halder\AppData\Local\Programs\Python\Python312`) + pip 26 — OK pour FastAPI.
- Node **v24.13.0** + npm 11.6 — OK pour Next.js/Expo.
- MySQL 8 : à vérifier (Laragon/XAMPP/Herd) — pas encore branché.
- PHP : inutilisé (voir plus haut).

## Commandes (à valider une fois le code écrit)

- Backend : `pip install -r requirements.txt` puis `uvicorn app.main:app --reload`
- Docs API : `http://127.0.0.1:8000/docs` (Swagger OpenAPI = contrat mobile)
- Tests : `pytest`
- Admin web : `npm run dev` (port 3000)
- Mobile : `npx expo start`

## Pièges

- Ne pas confondre avec le projet **Cross Road** (`Desktop/Cross Road/AGENTS.md`) : simulateur de trafic RL, sujet totalement différent.
- `basculer_mode_scenario`, `weights_only=True` etc. de Cross Road **ne concernent pas** ici.
- Chaque fichier du scaffold contient **une docstring d'attente** (« À contenir : … ») : le code écrit doit suivre cette consigne, l'architecture et la doc ne doivent pas diverger.
