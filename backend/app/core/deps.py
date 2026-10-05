"""
deps.py — dépendances FastAPI (le cœur des permissions).

À contenir :
- get_db() : session SQLAlchemy par requête, commit/rollback propre ;
- get_current_user() : lit Authorization: Bearer, hash le jeton, vérifie
  api_tokens (non révoqué, non expiré), met à jour last_used_at ;
- require_role("ADMIN"|"AGENT") : c'est la VRAIE protection serveur (§6) ;
- paramètres de pagination courants (page, size bornés).
Réf. : ARCHITECTURE.md §6 et §11.
"""
