"""
control.py — schemas contrôles (les plus sensibles).

À contenir :
- ControlCreate = STRICTEMENT { code, notes, location } (+ photos éventuelles) :
  aucun statut ni référence côté client (le serveur recalcule tout, §7) ;
- ControlOut (reference, global_status, agent, dates, location, notes, items) ;
- ControlItemOut (constat figé pièce par pièce) ;
- ControlListParams (agent_id, result, follow_up, province_id, q, from, to, page) ;
- FollowUpUpdate (suivi e-PV, ADMIN seul).
Réf. : ARCHITECTURE.md §7 et §10.
"""
