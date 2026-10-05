"""
qr_codes.py — endpoints QR CODES.

À contenir : POST /vehicles/{id}/qr-codes (génère VEH-XXXXXXXX et révoque
l'ancien actif), GET /vehicles/{id}/qr-codes (historique),
GET /qr-codes/{id}/image?format=svg (segno), POST /qr-codes/{id}/revoke,
GET /qr-codes/{code} = vérification AGENT (vue réduite, requiert jeton).
QR révoqué/inconnu -> 404 explicite. Réf. : ARCHITECTURE.md §7/§8.
"""
