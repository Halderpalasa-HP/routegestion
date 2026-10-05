# RouteGestion Mobile — Architecture de l'application

**Application « Contrôle Véhicule » — React Native (Expo) — République Démocratique du Congo**

Companion mobile du portail **RouteGestion** (`C:\Users\halder\Desktop\RouteGestion`).
Sources : les 4 maquettes PNG (`../Mobile — *.png`) + `RouteGestion/docs/ARCHITECTURE.md`.

> **Statut : architecture seule.** Tous les fichiers de ce dossier sont **vides volontairement** (0 octet) :
> aucun code, aucune dépendance installée. Ce document est le seul fichier rédigé.
> Le code sera écrit plus tard, écran par écran, sur demande.

---

## 1. Lien avec RouteGestion

```
Mobile (cette app)  ──HTTPS/JSON──►  API REST FastAPI (RouteGestion/backend)  ──►  MySQL 8
                                      contrat : ARCHITECTURE.md §7 (/api/v1)
```

- **L'API est le seul point d'accès aux données.** L'app ne parle jamais à MySQL directement.
- **Le contrat d'interface est `ARCHITECTURE.md` §7** (et Swagger `GET /docs` du backend une fois lancé).
- Base URL configurable dans `.env.example` → `API_BASE_URL=http://127.0.0.1:8000/api/v1`.
- **Toute la logique métier reste côté serveur** : statuts des documents, statut global, permissions,
  référence e-PV. Le mobile n'affiche et n'envoie que :
  `POST /controls { code, notes, location }` — le serveur **recalcule tout**.

## 2. Correspondance maquette → écran → fichier

| # | Maquette PNG | Écran | Fichier |
|---|---|---|---|
| — | *(pas de maquette)* | Connexion agent | `src/features/login/LoginScreen.tsx` |
| 1 | Mobile — Accueil de service | Accueil | `src/features/home/HomeScreen.tsx` |
| 2 | Mobile — Scanner QR | Scanner (QR + plaque) | `src/features/scanner/ScannerScreen.tsx`, `PlateEntrySheet.tsx` |
| — | *(découlent du scan)* | Dossier véhicule (4 pièces) | `src/features/vehicle_check/VehicleCheckScreen.tsx` |
| 3 | Mobile — Assurance expirée | Détail d'une pièce | `src/features/vehicle_check/DocumentDetailScreen.tsx` |
| 4 | Mobile — Enregistrement du contrôle | Constat / e-PV | `src/features/control_save/ControlSaveScreen.tsx` |
| — | *(confirmation)* | Succès + référence e-PV | `src/features/control_save/ControlSuccessScreen.tsx` |
| — | tab bar « Historique » | Historique des contrôles | `src/features/history/HistoryScreen.tsx` |
| — | *(clic sur un contrôle)* | Détail contrôle + e-PV PDF | `src/features/history/ControlDetailScreen.tsx` |

**Tab bar (3 onglets, maquette) :** `Accueil` · `Scanner` · `Historique` → `src/navigation/MainTabs.tsx`.

## 3. Arborescence et rôle de chaque dossier

```
mobile-app/
├── App.tsx                 # entrée : providers (auth, draft, thème) + navigation racine
├── app.json                # config Expo : nom, icônes, permission caméra, splash
├── package.json            # dépendances (§6) — aucun install tant que le code n'est pas écrit
├── tsconfig.json           # TypeScript strict
├── babel.config.js         # preset babel-preset-expo
├── .env.example            # API_BASE_URL (copier en .env)
├── .gitignore              # node_modules, .env, expo, build
├── assets/                 # icônes, splash, polices, images (à ajouter)
├── ARCHITECTURE_MOBILE.md  # ce document
│
└── src/
    ├── api/                # accès réseau
    │   ├── client.ts       #   instance axios : baseURL, header Bearer, interceptor 401 → logout
    │   ├── endpoints.ts    #   toutes les routes /api/v1 en constantes (une seule source de vérité)
    │   └── errors.ts       #   format d'erreur uniforme du backend (detail + code HTTP)
    ├── auth/               # session agent
    │   ├── AuthContext.tsx #   état : connecté / non, restore au démarrage (GET /auth/me)
    │   ├── useAuth.ts      #   hook de consommation
    │   └── tokenStorage.ts #   jeton opaque en SecureStore (Keychain/Keystore) — jamais en clair ailleurs
    ├── components/         # UI réutilisable, style des maquettes (dark + cyan)
    │   ├── Theme.ts        #   palette, typographie, espacements, rayons
    │   ├── Button.tsx      #   bouton primaire cyan (Scanner, Consulter, Enregistrer…)
    │   ├── Card.tsx        #   carte sombre + variante claire (attestation d'assurance)
    │   ├── StatusBadge.tsx #   pastilles : Conforme / À surveiller / Non conforme / Service
    │   ├── AppHeader.tsx   #   titre + sous-titre + retour + menu « ⋯ »
    │   ├── SectionTitle.tsx · FormField.tsx · CheckboxRow.tsx · StatTile.tsx
    │   └── EmptyState.tsx · LoadingView.tsx · ErrorView.tsx   # états vides / chargement / erreurs
    ├── features/           # un dossier par écran (source de vérité des écrans)
    │   ├── login/  home/  scanner/  vehicle_check/  control_save/  history/
    ├── navigation/         # structure de navigation
    │   ├── RootNavigator.tsx   # switch : non connecté → Auth, connecté → Main
    │   ├── AuthNavigator.tsx   # pile Login
    │   ├── MainTabs.tsx        # tabs Accueil / Scanner / Historique
    │   ├── ScannerStack.tsx    # Scanner → Dossier → Pièce → Constat → Succès
    │   ├── HistoryStack.tsx    # Historique → Détail contrôle
    │   └── types.ts            # RootStackParamList, MainTabParamList (typage des routes)
    ├── services/           # 1 fichier = 1 groupement d'endpoints §7 (appels API typés)
    ├── hooks/              # logique réutilisable liée aux données/caméra
    ├── store/              # ControlDraftContext : brouillon de constat partagé (scan → e-PV)
    ├── types/              # api.ts (réponses/pagination) · models.ts (Vehicle, Document…) · enums.ts
    ├── utils/              # dates (J-x, « depuis 8 jours ») · status · format · validation
    └── __tests__/          # tests des utils/services (Jest)
```

**Règle de placement :** un écran = un fichier dans `features/` ; un appel API = `services/` +
`api/endpoints.ts` ; un style réutilisable = `components/` ; jamais de logique métier dans les écrans
(ses résultats viennent déjà calculés du serveur).

## 4. Écran → endpoints appelés

| Écran | Méthode & endpoint | Remarque |
|---|---|---|
| Login | `POST /auth/login` · `GET /auth/me` · `POST /auth/logout` | jeton opaque, rôle AGENT/ADMIN |
| Accueil | `GET /controls?agent_id=…` (stats + dernier contrôle) | ⚠️ voir §7 |
| Scanner (QR) | `GET /qr-codes/{code}` | vue réduite agent, requiert jeton |
| Scanner (plaque) | `GET /vehicles?search={plaque}` | repli si QR illisible |
| Dossier véhicule | `GET /vehicles/{id}` · `GET /vehicles/{id}/documents` | statuts **calculés par le serveur** |
| Détail pièce | `GET /documents/{id}` · `GET /documents/{id}/file` | aperçu éventuel |
| Constat | `POST /controls { code, notes, location }` | **le serveur recalcule tout** |
| Succès e-PV | réponse de `POST /controls` (référence PV-/CT-) | référence générée serveur |
| Historique | `GET /controls?agent_id=&page=` | agent = ses seuls contrôles |
| Détail contrôle | `GET /controls/{id}` · `GET /controls/{id}/pv.pdf` | e-PV via `expo-print` |

## 5. Règles serveur à ne jamais dupliquer côté client

1. **Statuts calculés, jamais stockés** : `MISSING / VALID / EXPIRED / EXPIRING_SOON` — le mobile
   affiche ce que renvoie l'API, il ne les recalcule pas.
2. **Statut global imposé par les maquettes** : NON CONFORME > À SURVEILLER > CONFORME ;
   seuls les types **obligatoires** l'influencent.
3. **`POST /controls` n'envoie que** `code`, `notes`, `location` (+ photos) — aucun statut dans le corps.
   La référence e-PV (`PV-` non conforme / `CT-` conforme) est générée **côté serveur**.
4. **Permissions** : l'agent ne voit que ses contrôles (vérifié serveur, pas seulement en masquant un bouton).
5. **Minimisation** : jamais de téléphone/adresse/fichiers du propriétaire côté agent (§11 de l'archi).
6. **QR** : le code seul (`VEH-8F29A73`) ne donne rien sans jeton ; QR révoqué/inconnu ou
   véhicule INACTIF → **erreur explicite** (`ErrorView`), pas un statut de conformité.

## 6. Dépendances prévues (`package.json` — à installer au moment du code)

| Besoin | Paquet |
|---|---|
| Framework | `expo`, `react`, `react-native`, `typescript` |
| Navigation | `@react-navigation/native`, `@react-navigation/native-stack`, `@react-navigation/bottom-tabs`, `react-native-screens`, `react-native-safe-area-context` |
| Scan QR | `expo-camera` |
| Jeton sécurisé | `expo-secure-store` |
| Réseau | `axios` (+ `@tanstack/react-query` optionnel pour le cache) |
| e-PV PDF | `expo-print`, `expo-file-system` |
| Lieu du contrôle | `expo-location` *(si décision GPS, sinon saisie manuelle)* |
| Tests | `jest`, `jest-expo`, `@types/jest` |

## 7. Décisions / points à trancher avec le backend

1. **Stats de l'accueil agent** (maquette : « 12 contrôles réalisés / 3 non conformes ») :
   `GET /dashboard/stats` est un endpoint **admin**. Solutions possibles :
   a) endpoint agent dédié côté backend, b) agrégation mobile depuis `GET /controls?agent_id=`.
   → à confirmer avec RouteGestion avant d'écrire l'accueil.
2. **Lieu du contrôle** : saisie manuelle (défaut, maquette 4) ou GPS auto (`expo-location`) —
   décision en attente §14 de l'ARCHITECTURE.md.
3. **Emplacement** : cette app vit dans `mobile/mobile-app/` (copie du dossier
   `Desktop\Maquette\mobile-app`) ; `mobile-app/` à la racine du dépôt = squelette
   de référence (16 fichiers, 4 écrans).

## 8. Ordre d'implémentation recommandé

1. Config : `package.json`, `app.json`, `tsconfig`, `.env` + installation Expo.
2. Socle : `Theme`, `client.ts`, `types/`, `auth/` + `LoginScreen`.
3. Navigation : `RootNavigator` → `MainTabs`.
4. **Scanner** (maquette 2) + `GET /qr-codes/{code}`.
5. **Dossier véhicule** + **Détail pièce** (maquettes 1 & 3).
6. **Constat + Succès** (maquette 4) via `ControlDraftContext`.
7. **Accueil** puis **Historique**.
8. Tests (`utils/`, `services/`) + revue sécurité (stockage jeton, erreurs 401/403).
