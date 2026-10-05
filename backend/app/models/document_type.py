"""
document_type.py — table document_types (configurable par l'admin).

Colonnes : id, code (unique), name, is_required, has_expiry, warning_days
(nullable : 30 assurance/technique, 15 taxe), diagnostic_hint, is_active.
Seed des 4 types : CARTE_GRISE, ASSURANCE, CONTROLE_TECHNIQUE, TAXE_CIRCULATION.
Réf. : ARCHITECTURE.md §5.
"""
