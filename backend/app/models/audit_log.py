"""
audit_log.py — table audit_logs (journal d'audit).

Colonnes : id, user_id (FK nullable), action, entity_type, entity_id,
old_values (JSON), new_values (JSON), ip, created_at. Trace connexions,
créations/modifications, révocations QR, changements de paramètres/suivi e-PV.
Réf. : ARCHITECTURE.md §4 et §11.
"""
