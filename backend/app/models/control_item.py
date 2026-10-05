"""
control_item.py — table control_items (constat figé pièce par pièce).

Colonnes : id, control_id (FK), document_type_id (FK), document_id (FK nullable),
status, expires_at. Figé au moment du contrôle : l'historique reste vrai même
après renouvellement. Réf. : ARCHITECTURE.md §4 et §10.
"""
