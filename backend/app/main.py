"""
main.py — point d'entrée de l'application FastAPI (RouteGestion).

À contenir :
- création de l'instance FastAPI (titre, version, /docs Swagger, /redoc) ;
- chargement de la config (app.core.config) + moteur SQLAlchemy (lifespan) ;
- CORS restreint aux origines admin-web et mobile ;
- inclusion du routeur unique préfixé /api/v1 (app.api.v1.router) ;
- endpoint de santé GET /health (démarrage, tests).
Aucune logique métier ici : elle vit dans services/ (ARCHITECTURE.md §1, §7).
"""
