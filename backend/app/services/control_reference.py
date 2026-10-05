"""
control_reference.py — ControlReferenceService (référence e-PV).

À contenir : génération serveur de la référence unique :
« PV- » si NON CONFORME sinon « CT- » + année + séquence incrémentale
(ex. PV-2026-00482, CT-2026-01941), sous contrainte d'unicité ;
suivi initial : À_TRAITER pour un PV, CLÔTURÉ pour un CT.
Le client ne fournit JAMAIS la référence. Réf. : ARCHITECTURE.md §7/§10.
"""
