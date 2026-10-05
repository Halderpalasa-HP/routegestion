"""
compliance.py — ComplianceService (statut global + compteurs).

À contenir :
- global_status(statuts par type) -> NON CONFORME (au moins un OBLIGATOIRE
  EXPIRED/MISSING) > A_SURVEILLER (obligatoire EXPIRING_SOON) > CONFORME
  (tous les obligatoires VALID) ; les types non obligatoires n'influencent pas ;
- compteur « 3 / 4 » (pièces valides parmi les obligatoires) ;
- agrégations SQL des mêmes règles pour le dashboard (compteurs 14 820 / 11 415…).
Réf. : ARCHITECTURE.md §4 et §10.
"""
