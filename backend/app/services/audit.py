"""
audit.py — AuditService (journalisation).

À contenir : write(user, action, entity_type, entity_id, old, new, ip) ->
insertion dans audit_logs. Appelé sur connexions, créations/modifications,
révocations QR, changements de paramètres et de suivi e-PV. Ne jamais journaliser
de mot de passe ni de jeton en clair. Réf. : ARCHITECTURE.md §4/§11.
"""
