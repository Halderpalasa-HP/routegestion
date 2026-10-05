"""
api_token.py — table api_tokens (jetons d'accès opaque hashés).

Colonnes : id, user_id (FK), token_hash (SHA-256, unique, index), expires_at,
revoked_at, last_used_at, ip. Le jeton en clair n'existe qu'à la création ;
révocation immédiate (logout, téléphone perdu, agent désactivé) via revoked_at.
Réf. : ARCHITECTURE.md §2/§4/§11.
"""
