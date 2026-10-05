"""
vehicles.py — endpoints VÉHICULES (rôle ADMIN pour l'écriture).

À contenir : GET /vehicles (search, status, province_id, page) ;
POST /vehicles ; GET|PATCH /vehicles/{id} ; PATCH /vehicles/{id}/status
(désactivation au lieu de suppression, ON DELETE RESTRICT).
GET /vehicles/{id} = fiche complète admin ; l'agent passe par /qr-codes/{code}.
Réf. : ARCHITECTURE.md §7 et §10.
"""
