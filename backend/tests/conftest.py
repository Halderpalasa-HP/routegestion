"""
conftest.py — fixtures pytest partagées.

À contenir : application FastAPI de test (client httpx ASGI), base de test
(éphémère, isolée de la MySQL de dev), seeds minimaux (provinces, 4 types de
documents, admin + agent), fixtures de jeton d'authentification (admin/agent),
helpers de création de véhicule/documents. Réf. : ARCHITECTURE.md §12 (pytest).
"""
