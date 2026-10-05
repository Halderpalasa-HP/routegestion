"""
config.py — settings de l'application (pydantic-settings + .env).

À contenir :
- DATABASE_URL (MySQL 8, utf8mb4), CORS_ORIGINS, ENV (dev/prod) ;
- durée de vie des jetons, dossier de stockage des fichiers HORS du public ;
- pagination par défaut (page size max) ; aucun secret en dur (voir .env.example).
Réf. : ARCHITECTURE.md §11.
"""
