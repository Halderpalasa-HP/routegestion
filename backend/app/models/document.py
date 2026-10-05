"""
document.py — table documents (pièces d'un véhicule).

Colonnes : id, vehicle_id (FK), document_type_id (FK), document_number,
issued_at, expires_at (nullable), file_path, file_mime, file_size, created_by.
ATTENTION : PAS de colonne « status » — le statut est CALCULÉ (services).
Renouvellement = ajout d'une ligne, jamais écrasement. Réf. §4.
"""
