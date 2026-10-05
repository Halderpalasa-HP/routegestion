"""
router.py — assemblage de tous les routeurs v1.

À contenir : api_router = APIRouter(prefix="/api/v1") + include_router de :
auth, provinces, vehicles, owners, qr_codes, document_types, documents, controls,
users, dashboard, settings, audit, exports (avec leur tags et préfixes).
Inclus depuis app/main.py. Aucune logique métier ici : appeler services/.
Réf. : ARCHITECTURE.md §7.
"""
