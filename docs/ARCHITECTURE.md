# RouteGestion — Architecture technique

**Portail national de contrôle des véhicules — République Démocratique du Congo**

Sources : les 4 maquettes (`../Maquette/`) + l'analyse d'architecture en 14 points (validée).

**Stack retenue (validée avec le porteur du projet)**
- **Backend : Python 3.12 + FastAPI + SQLAlchemy 2 + Pydantic v2**
- **Admin web : Next.js (App Router) + React + TypeScript + Tailwind CSS**
- **Mobile : React Native (Expo)** — développé séparément, l'API REST est le contrat d'interface
- **Base : MySQL 8** — aucune dépendance PHP/Node côté API

---

## 1. Architecture générale

Trois applications indépendantes parlent à une seule API :

```
Admin web (Next.js)  ──┐
                       ├──HTTPS/JSON──►  API REST (FastAPI)  ──►  MySQL 8
Mobile (React Native)  ┘                   logique métier
```

- **L'API est le seul point d'accès à la base.** Ni le web ni le mobile ne parlent à MySQL directement.
- **Toute la logique métier reste dans le backend** : calcul des statuts, statut global, permissions, références e-PV. Les clients n'affichent que.
- **Un seul backend pour deux clients.** Une règle métier corrigée une fois vaut pour les deux.
- Le mobile étant réalisé à part, **le document §7 (API REST) fait foi** ; `GET /api/v1/docs` (OpenAPI généré par FastAPI) documente le contrat automatiquement.

## 2. Architecture technique et technologies

| Couche | Choix | Pourquoi |
|---|---|---|
| Base de données | **MySQL 8** (InnoDB, utf8mb4) | Imposé. Clés étrangères, transactions, colonnes générées. |
| Backend | **Python 3.12 + FastAPI** | Typage fort (Pydantic), validation + documentation OpenAPI générées, async, écosystème mûr. |
| ORM | **SQLAlchemy 2.0** + Alembic | Requêtes paramétrées (anti-injection SQL), migrations versionnées. |
| Authentification API | **Jeton opaque aléatoire (256 bits), stocké hashé en base** — table `api_tokens` | Même philosophie que Laravel Sanctum : révocation **immédiate** (déconnexion, téléphone perdu, agent désactivé). Pas de JWT impossible à révoquer. |
| Admin web | **Next.js + TypeScript + Tailwind** | App Router, composants React typés, les 4 maquettes se transposent page par page (`/dashboard`, `/vehicles`, `/controls`, `/settings`). |
| Mobile | **React Native (Expo)** | Choix du projet. Scan QR, stockage sécurisé, navigation. |
| QR Code | **`segno`** (SVG) | Pur Python, zéro dépendance système (pas de GD ni de lib C), SVG imprimable sans perte. |
| e-PV (PDF) | **`reportlab`** | Génération à la demande du constat (*Consulter / Télécharger l'e-PV*), accents français gérés. |
| Tests | **pytest** + httpx (client ASGI) | Tests unitaires des services et tests d'intégration de l'API. |
| Rate limiting | **slowapi** | Limitation de débit sur `/auth/login` et endpoints coûteux. |

## 3. Arborescence

```
RouteGestion/
├── backend/                          # FastAPI (Python 3.12)
│   ├── app/
│   │   ├── main.py                   # création de l'App, CORS, inclusion des routeurs /api/v1
│   │   ├── core/                     # config (.env), security (hash/jetons), deps (rôles, DB)
│   │   ├── models/                   # SQLAlchemy 2 : tables (Base, vehicles, controls…)
│   │   ├── schemas/                  # Pydantic : entrées (validation) et sorties (liste blanche des champs)
│   │   ├── api/v1/                   # routers : auth, provinces, vehicles, owners, qr_codes,
│   │   │                             #   document_types, documents, controls, users, dashboard,
│   │   │                             #   exports, settings, audit
│   │   └── services/                 # DocumentStatusService, ComplianceService, QrCodeService,
│   │                                 #   ControlReferenceService, PvPdfService
│   ├── alembic/                      # migrations
│   ├── tests/                        # pytest
│   ├── requirements.txt
│   └── .env.example
├── admin-web/                        # Next.js (App Router) — 4 écrans des maquettes
│   └── src/app/{dashboard,vehicles,controls,settings}/page.tsx
│       src/lib/api.ts                # client fetch typé (contrat OpenAPI)
│       src/types/                    # types générés/manuels du contrat API
│       src/components/
├── mobile-app/                       # squelette mobile de référence (docstrings)
│   └── src/ (api/, auth/, navigation/, features/{scanner,vehicle_check,control_save,history}/)
├── mobile/                           # copie du dossier Maquette (bureau)
│   ├── Mobile — *.png                # 4 maquettes mobiles
│   └── mobile-app/                   # app React Native active (9 écrans, ARCHITECTURE_MOBILE.md)
├── Maquette/                         # PNG portail (existant)
└── docs/                             # ARCHITECTURE.md, schéma BD, spécification API
```

Les règles métier vivent dans `services/` (fonctions pures, testables avec pytest), jamais dans les routeurs.

## 4. Modèle de base de données

**Relations principales**

- `provinces` 1─N `owners`
- `roles` 1─N `users`
- `owners` 1─N `vehicles`
- `vehicles` 1─N `qr_codes`, `documents`, `controls`
- `document_types` 1─N `documents`, `control_items`
- `controls` 1─N `control_items`
- `users` (agents) 1─N `controls`
- `users` 1─N `api_tokens`

**Tables** (adaptées aux maquettes)

| Table | Colonnes clés | Rôle |
|---|---|---|
| `provinces` | id, name (unique) | Les 26 provinces RDC (seed). Filtres des écrans. |
| `roles` | id, name (unique : ADMIN, AGENT) | Les rôles. |
| `users` | id, role_id (FK), name, email (unique), password_hash (bcrypt/argon2), badge_number (unique, nullable, ex. `AGT-2026-042`), is_active, last_login_at | Admins et agents. |
| `api_tokens` | id, user_id (FK), token_hash (SHA-256 du jeton), expires_at, revoked_at, last_used_at, ip | Jetons d'accès ; révocation immédiate par `revoked_at`. Le jeton en clair n'existe qu'à la création. |
| `owners` | id, first_name, last_name, province_id (FK), phone, address (nullable) | Titulaires. Province affichée dans la liste. Pas de pièce d'identité (donnée sensible inutile). |
| `vehicles` | id, owner_id (FK), plate_number (unique), brand, model, color, year, vin (unique, nullable), category (nullable, ex. SUV), usage (nullable, ex. Privé), status (ACTIVE/INACTIVE) | Véhicules. `category`/`usage` : affichage du dossier, pas logique documentaire. |
| `qr_codes` | id, vehicle_id (FK), code (unique, ex. `VEH-8F29A73`), status (ACTIVE/REVOKED), created_by, revoked_at | Plusieurs codes dans le temps, **un seul actif**. |
| `document_types` | id, code (unique), name, is_required, has_expiry, warning_days (nullable), diagnostic_hint (nullable), is_active | Configurable par l'admin. Seed des 4 types (§5). |
| `documents` | id, vehicle_id (FK), document_type_id (FK), document_number, issued_at, expires_at (nullable), file_path, file_mime, file_size, created_by | **Pas de colonne `status`** (statut calculé). |
| `controls` | id, vehicle_id (FK), agent_id (FK), qr_code_id (FK), reference (unique, ex. `PV-2026-00482` / `CT-2026-01941`), controlled_at, location, global_status, follow_up (À_TRAITER/EN_REVUE/CLÔTURÉ), notes | Un contrôle effectué + son e-PV. |
| `control_items` | id, control_id (FK), document_type_id (FK), document_id (FK, nullable), status, expires_at | Constat figé pièce par pièce : l'historique reste vrai après renouvellement. |
| `settings` | key (PK), value | `expiring_soon_days = 30`, `show_alerts = 1`, `show_missing = 1`. |
| `audit_logs` | id, user_id (FK, nullable), action, entity_type, entity_id, old_values (JSON), new_values (JSON), ip, created_at | Journal (dont « Journal des modifications »). |

**Intégrité**

- **`ON DELETE RESTRICT` partout** : pas de suppression d'un véhicule ayant des contrôles → désactivation, historique intact.
- **Un seul QR actif par véhicule** : colonne générée `active_vehicle_id` (égale à `vehicle_id` si ACTIF, sinon NULL) + index UNIQUE — garanti par MySQL, pas par le code applicatif.
- **Uniques** : plaque, VIN, email, code QR, badge, `controls.reference`.
- **Index** : `documents(vehicle_id, document_type_id, expires_at)`, `documents(expires_at)`, `controls(vehicle_id, controlled_at)`, `controls(agent_id, controlled_at)`, `controls(follow_up)`, `owners(province_id)`, `api_tokens(token_hash)`.

**Statut des documents : calculé, jamais stocké.** `MISSING` ne peut pas être stocké (absence de ligne), et un statut stocké deviendrait faux le jour de l'expiration.

Pour chaque type, on prend le document le plus récent (un renouvellement **ajoute** une ligne) :

| Situation | Statut |
|---|---|
| Aucun document pour ce type | MISSING |
| `expires_at` vide et type sans expiration | VALID |
| `expires_at` < aujourd'hui | EXPIRED |
| `expires_at` ≤ aujourd'hui + seuil | EXPIRING_SOON |
| Sinon | VALID |

- Seuil = `warning_days` du type, sinon `settings.expiring_soon_days` (30 par défaut).
- Un document est valide **jusqu'au jour d'expiration inclus**.
- **Taxe de circulation** : pas de document pour l'exercice courant = MISSING → affiché « **Impayée** ».
- Le dashboard réutilise **la même règle en SQL** (via SQLAlchemy) pour les compteurs (14 820 / 11 415 / 3 405).

## 5. Types de documents — seed (maquette « Paramètres documentaires »)

Quatre types pré-remplis, **entièrement modifiables par l'admin** (aucune liste officielle codée en dur) :

| code | name | is_required | has_expiry | warning_days | diagnostic_hint |
|---|---|---|---|---|---|
| `CARTE_GRISE` | Carte grise | ✅ | ❌ | — | « À vérifier si absente » |
| `ASSURANCE` | Assurance automobile | ✅ | ✅ | 30 | « Expirée après échéance » |
| `CONTROLE_TECHNIQUE` | Contrôle technique | ✅ | ✅ | 30 | « Expirée après échéance » |
| `TAXE_CIRCULATION` | Taxe de circulation | ✅ | ✅ | 15 | « Impayée sans règlement » |

La maquette montre deux seuils (30 j assurance/technique, 15 j taxe) : ils vivent dans `warning_days`, éditables dans *Seuils & affichage*.

## 6. Rôles et permissions

| Action | Admin | Agent |
|---|---|---|
| Véhicules, propriétaires, types de documents, documents (créer/modifier) | ✅ | ❌ |
| Consulter un véhicule via QR (vue réduite) | ✅ | ✅ |
| Enregistrer un contrôle | ✅ | ✅ |
| Voir tous les contrôles | ✅ | ❌ (uniquement les siens) |
| Suivi e-PV (clôturer / en revue) | ✅ | ❌ |
| Gérer les utilisateurs, QR Codes, paramètres | ✅ | ❌ |
| Journal d'audit, dashboard, exports | ✅ | ❌ |

Appliqué côté serveur par des **dépendances FastAPI** (`require_role("ADMIN")` sur les routeurs/endpoints). Masquer un bouton n'est pas une protection.

## 7. Endpoints REST — `/api/v1` (contrat API, fait foi pour le mobile)

```
AUTH        POST /auth/login  POST /auth/logout  GET /auth/me
PROVINCES   GET /provinces                                    (filtres des écrans)
VÉHICULES   GET /vehicles?search=&status=&province_id=&page=
            POST /vehicles    GET|PATCH /vehicles/{id}    PATCH /vehicles/{id}/status
PROPRIÉT.   GET|POST /owners   GET|PATCH /owners/{id}     GET /owners/{id}/vehicles
QR CODES    POST /vehicles/{id}/qr-codes          (génère ; révoque l'ancien s'il existe)
            GET /vehicles/{id}/qr-codes           (historique)
            GET /qr-codes/{id}/image?format=svg   (affichage / impression)
            POST /qr-codes/{id}/revoke
            GET /qr-codes/{code}                  (vérification agent → vue réduite)
TYPES DOC   GET|POST /document-types   PATCH /document-types/{id}
DOCUMENTS   GET|POST /vehicles/{id}/documents     (POST multipart)
            GET|PATCH|DELETE /documents/{id}      GET /documents/{id}/file
CONTRÔLES   POST /controls   { code, notes, location }   ← le serveur recalcule TOUT
            GET /controls?agent_id=&result=&follow_up=&province_id=&q=&from=&to=&page=
            GET /controls/{id}
            GET /controls/{id}/pv.pdf                            (e-PV, reportlab)
            PATCH /controls/{id}/follow-up                       (admin : suivi)
UTILISAT.   GET|POST /users  GET|PATCH /users/{id}  POST /users/{id}/reset-password
            POST /users/{id}/deactivate                          (révoque les jetons)
ADMIN       GET /dashboard/stats                (KPIs, conformes/non conformes, provinces)
            GET /dashboard/activity?from=&to=&province_id=       (courbe des contrôles)
            GET /dashboard/anomalies?from=&to=                   (répartition par type)
            GET|PUT /settings                GET /audit-logs
EXPORTS     GET /exports/dashboard|vehicles|controls?format=csv  (boutons « Exporter »)
```

- JSON, format d'erreur uniforme (`detail` + code HTTP), listes paginées, codes standards (401/403/404/422/429). Validation Pydantic → 422 automatique.
- `POST /controls` reçoit **uniquement** `code`, `notes`, `location` (+ photos éventuelles). **Le serveur recalcule tous les statuts** : un client modifié ne peut pas déclarer « conforme ».
- La référence e-PV est **générée côté serveur** (`ControlReferenceService`) : `PV-` si non conforme, `CT-` sinon, + année + séquence. `follow_up` initial : `À_TRAITER` pour un PV, `CLÔTURÉ` pour un CT.
- Séparation maintenue : `GET /qr-codes/{code}` = vérification agent (vue réduite) ; `GET /vehicles/{id}` = fiche admin complète.
- **Documentation live** : `GET /docs` (Swagger) et `GET /redoc` — c'est la référence contractuelle pour le mobile.

## 8. Fonctionnement du QR Code

1. **Création.** L'admin génère un code du type `VEH-8F29A73` : 7 caractères (`secrets.choice`) sans 0/O ni 1/I, **non séquentiel** (`VEH-000025` laisserait deviner `VEH-000026`).
2. **Contenu.** Le QR encode uniquement ce texte.
3. **Affichage/impression.** Endpoint SVG (`segno`, `format='svg'`).
4. **Utilisation.** L'agent scanne → `GET /qr-codes/{code}` avec son jeton → réponse.
5. **Perte/fraude.** L'admin révoque puis régénère : l'ancien = REVOKED (scan → « QR invalide »), le nouveau devient actif.

Le code seul ne révèle rien : sans jeton d'agent valide, le scanner d'un inconnu ne donne aucune information.

## 9. Flux de communication

```
Agent scanne le QR ("VEH-8F29A73")
  → Mobile : GET /api/v1/qr-codes/VEH-8F29A73   (Authorization: Bearer <jeton>)
  → API : vérifie jeton (hash en base, non révoqué), rôle, code actif
  → MySQL : véhicule, propriétaire, documents par type
  → Service : calcule statuts + statut global (+ compteur « 3 / 4 »)
  → Mobile : affiche vert / orange / rouge
Agent appuie sur « Enregistrer le contrôle »
  → Mobile : POST /api/v1/controls { code, notes, location }
  → API : recalcule tout, génère la référence, écrit controls + control_items
  → Réponse : référence e-PV + statut global → écran de confirmation
Admin web : même circuit via ses endpoints (dashboard, fiches, exports, e-PV).
```

## 10. Règles métier

**Statut global** (identique web et mobile, imposé par les maquettes) :

- **NON CONFORME** : au moins un type **obligatoire** est EXPIRED ou MISSING (ex. assurance expirée, taxe impayée).
- **CONFORME – À SURVEILLER** : aucun expiré/manquant, mais au moins un obligatoire EXPIRING_SOON (ex. « Assurance à J-12 »).
- **CONFORME** : tous les obligatoires VALID (« 4 pièces valides »).
- Types **non obligatoires** : affichés, n'influencent pas le global.
- Véhicule INACTIF ou QR révoqué/inconnu : **erreur explicite**, pas un statut de conformité.

Autres règles : renouvellement = ajout, jamais écrasement ; véhicule/utilisateur désactivés, jamais supprimés ; agent désactivé = jetons révoqués immédiatement.

**Suivi e-PV** (écran Contrôles) : `À_TRAITER` → `EN_REVUE` → `CLÔTURÉ`, modifiable uniquement par l'admin. Chaque contrôle conserve le figeage documentaire (`control_items`) au moment du constat.

## 11. Sécurité

- **Jeton opaque stocké hashé** (SHA-256) avec `expires_at` + `revoked_at` : révocation immédiate (logout, téléphone perdu, agent désactivé). Pas de JWT non révocable. Côté mobile : stockage Keychain/Keystore (`expo-secure-store` ou `react-native-keychain`).
- **Mots de passe** bcrypt/argon2 (`passlib` ou `argon2-cffi`) + politique de complexité.
- **Rate limiting** (`slowapi`) : `/auth/login` ≈ 5/min contre le brute-force.
- **Validation** de toute entrée par des schemas Pydantic (422 automatique) ; SQLAlchemy = requêtes paramétrées ; **les schemas de sortie listent explicitement les champs** (pas de `SELECT *` vers le client).
- **Minimisation côté agent** : plaque, marque, modèle, couleur, année, statuts, nom du propriétaire (si validé). **Jamais** téléphone, adresse, fichiers.
- **Fichiers** : PDF/JPG/PNG uniquement, taille limitée, vrai type MIME vérifié, nom aléatoire (`secrets`), stockage **hors dossier public**, téléchargement via endpoint authentifié.
- **HTTPS** en production, CORS restreint (origines Next.js + mobile), en-têtes de sécurité.
- **Journalisation** (`audit_logs`) : connexions, créations/modifications, révocations QR, changements de paramètres, changements de suivi e-PV.

## 12. Dépendances

**Environnement local** : Python 3.12, Node.js 20+, MySQL 8 (Laragon/XAMPP/Herd sous Windows). **Aucun PHP requis.**

**Backend (`requirements.txt`)** :
- `fastapi`, `uvicorn[standard]`, `sqlalchemy>=2`, `alembic`, `pymysql` (ou `asyncmy` si async)
- `pydantic`, `pydantic-settings`
- `passlib[bcrypt]`, `python-multipart` (upload fichiers), `segno`, `reportlab`
- `slowapi`, `python-dotenv`
- Tests : `pytest`, `httpx`

**Admin web (`package.json`)** : `next`, `react`, `react-dom`, `typescript`, `tailwindcss`, `axios` (ou fetch natif), `zustand` ou `@tanstack/react-query` (cache serveur), `recharts` (courbes du tableau de bord).

**Mobile (React Native / Expo)** — indicatif :
- Expo SDK (`expo-camera` scan QR, `expo-secure-store` jeton, `expo-router`/React Navigation, `expo-location` lieu du contrôle)
- `axios`, `@tanstack/react-query`, `expo-print`/`expo-file-system` (e-PV)

## 13. Plan de développement

1. ✅ Maquettes (4 PNG) + **validation de cette architecture**.
2. ✅ Environnement + 3 projets (backend, admin-web, mobile-app).
3. Migrations Alembic + seeds (26 provinces, 4 types de documents, settings, données démo).
4. Auth (login, jetons, rôles), dépendances de permissions.
5. CRUD propriétaires et véhicules.
6. Documents + **DocumentStatusService avec tests pytest** (règles §4/§10).
7. QR Codes : génération, SVG, révocation.
8. Vérification agent + `POST /controls` (référence e-PV, suivi).
9. Admin web : 4 écrans des maquettes (dashboard, véhicules, contrôles, paramètres).
10. Application mobile React Native (scan, résultat, enregistrement, historique).
11. Dashboard agrégé, exports CSV, journal d'audit, e-PV PDF.
12. Tests, revue de sécurité, documentation, démonstration.

## 14. Décisions

**Prises**
- ✅ **Backend = Python 3.12 + FastAPI + SQLAlchemy 2** (PHP/Laravel écartés).
- ✅ **Admin web = Next.js + React + TypeScript + Tailwind** (Vue écarté).
- ✅ **Mobile = React Native (Expo)**, développé par le porteur — l'API (§7) est le contrat.
- ✅ Auth = jeton opaque hashé révocable (esprit Sanctum).
- ✅ Maquettes = les 4 PNG existants (pas de Figma nécessaire).
- ✅ Suivi e-PV, références PV/CT, filtres provinces : intégrés au modèle et à l'API.

**À valider (sinon valeurs par défaut)**
1. Nom du propriétaire visible par l'agent (ni téléphone ni adresse).
2. Seuils par type : assurance/technique 30 j, taxe 15 j (défauts des maquettes), modifiables.
3. Types de documents indépendants de la catégorie de véhicule (pas de table `vehicle_categories`).
4. Environnement local Laragon/XAMPP/Herd, sans Docker.
5. e-PV = PDF **généré à la demande** (reportlab) — alternative : fichier stocké à l'enregistrement.
6. Lieu du contrôle : **saisie manuelle** par l'agent (défaut) ou **GPS auto** (`expo-location`).
7. MySQL en local via `mysqlclient`/`pymysql` — async optionnel (`asyncmy` + `create_async_engine`).
