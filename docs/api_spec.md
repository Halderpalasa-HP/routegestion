# RouteGestion — Spécification de l'API REST

> Scaffold vide : référence contractuelle = `ARCHITECTURE.md` §7 (+ Swagger /docs en direct).

## Sections à rédiger
1. **Convention générale** — préfixe /api/v1, auth Bearer (jeton opaque), format
   d'erreur { detail }, pagination (items/total/page/size), codes HTTP.
2. **AUTH** — POST /auth/login, /auth/logout, GET /auth/me.
3. **PROVINCES, VÉHICULES, PROPRIÉTAIRES** — params et réponses.
4. **QR CODES** — création/révocation/image SVG/lookup agent (vue réduite).
5. **TYPES DOC + DOCUMENTS** — multipart, MIME, statuts calculés.
6. **CONTRÔLES** — POST /controls (corps minimal, recalcul serveur), filtres,
   e-PV PDF, suivi (admin).
7. **ADMIN** — dashboard, users, settings, audit, exports CSV.
8. **Tableau écran -> endpoints** — le mobile n'utilise qu'un sous-ensemble (§7).

