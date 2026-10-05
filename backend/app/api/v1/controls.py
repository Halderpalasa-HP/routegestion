"""
controls.py — endpoints CONTRÔLES (le cœur métier).

À contenir :
- POST /controls { code, notes, location } : le serveur RECALCULE tout
  (statuts via DocumentStatusService, statut global via ComplianceService),
  génère la référence (PV-/CT-) via ControlReferenceService, écrit controls +
  control_items ; suivi initial À_TRAITER (PV) ou CLÔTURÉ (CT) ;
- GET /controls (filtres : agent_id, result, follow_up, province_id, q, from, to,
  page) — l'agent n'obtient QUE les siens (dépendance serveur, §6) ;
- GET /controls/{id} ; GET /controls/{id}/pv.pdf (reportlab, à la demande) ;
- PATCH /controls/{id}/follow-up (ADMIN seul).
Réf. : ARCHITECTURE.md §7, §9, §10.
"""
