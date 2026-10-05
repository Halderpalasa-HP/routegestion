"""
vehicle.py — table vehicles.

Colonnes : id, owner_id (FK), plate_number (unique), brand, model, color, year,
vin (unique, nullable), category/usage (affichage seulement), status
(ACTIVE/INACTIVE). ON DELETE RESTRICT : jamais de suppression, désactivation.
Réf. : ARCHITECTURE.md §4.
"""
