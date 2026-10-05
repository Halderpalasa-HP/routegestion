# RouteGestion — Schéma de la base de données

> Scaffold vide : ce document doit être rempli à partir de `docs/ARCHITECTURE.md` §4.

## Sections à rédiger
1. **Diagramme des relations** — provinces 1-N owners, roles 1-N users, owners 1-N
   vehicles, vehicles 1-N qr_codes/documents/controls, document_types 1-N
   documents/control_items, controls 1-N control_items, users 1-N controls/api_tokens.
2. **Les 14 tables** — colonnes, types MySQL, contraintes (colonnes du tableau §4).
3. **Intégrité** — ON DELETE RESTRICT partout, uniques (plaque, VIN, email, code QR,
   badge, reference), colonne générée active_vehicle_id + index UNIQUE.
4. **Index** — documents(vehicle_id, document_type_id, expires_at), controls(agent_id,
   controlled_at)…
5. **Règle des statuts** — jamais de colonne status sur documents (calculé, §4).
6. **Seeds** — 26 provinces, 4 types de documents, settings, rôles, utilisateurs démo.

