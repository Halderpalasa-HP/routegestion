"""
qr_code.py — table qr_codes (codes QR des véhicules).

Colonnes : id, vehicle_id (FK), code (unique, ex. VEH-8F29A73), status
(ACTIVE/REVOKED), created_by, revoked_at + colonne générée active_vehicle_id
(= vehicle_id si ACTIF sinon NULL) avec index UNIQUE MySQL : garantit UN SEUL
QR actif par véhicule côté base, pas côté code. Réf. : ARCHITECTURE.md §4/§8.
"""
