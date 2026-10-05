"""
document_status.py — DocumentStatusService (règle métier §4).

À contenir :
- statut_document(document_type, documents) -> MISSING | VALID | EXPIRED |
  EXPIRING_SOON : on prend le document le plus RÉCENT du type (renouvellement =
  ajout de ligne) ;
- Aucune ligne -> MISSING ; expires_at vide et type sans expiration -> VALID ;
  expires_at < aujourd'hui -> EXPIRED ; <= aujourd'hui + warning_days
  (sinon settings.expiring_soon_days) -> EXPIRING_SOON ; sinon VALID ;
- jour d'expiration INCLUS (valide jusqu'au jour J) ;
- TAXE_CIRCULATION sans document de l'exercice courant -> MISSING (« Impayée »).
JAMAIS stocké en base. Couvert par tests/test_document_status.py.
Réf. : ARCHITECTURE.md §4 et §10.
"""
