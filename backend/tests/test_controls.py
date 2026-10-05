"""
test_controls.py — enregistrement des contrôles (contrat mobile).
À contenir : POST /controls avec { code, notes, location } renvoie référence +
global_status recalculés ; un corps client truqué (statut « conforme ») est
ignoré/refusé ; référence PV- pour non conforme, CT- sinon ; suivi initial
cohérent ; control_items figés ; l'agent ne voit que SES contrôles dans la
liste ; PV/CT PDF générés ; AGENT ne peut pas clôturer (403).
Réf. : ARCHITECTURE.md §7/§9/§10.
"""
