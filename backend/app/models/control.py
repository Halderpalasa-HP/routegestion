"""
control.py — table controls (contrôles effectués + e-PV).

Colonnes : id, vehicle_id (FK), agent_id (FK users), qr_code_id (FK),
reference (unique, PV-2026-00482 / CT-2026-01941), controlled_at, location,
global_status, follow_up (A_TRAITER/EN_REVUE/CLOTURE), notes.
Index : (vehicle_id, controlled_at), (agent_id, controlled_at), (follow_up).
Réf. : ARCHITECTURE.md §4 et §10.
"""
