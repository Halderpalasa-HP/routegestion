"""
test_document_status.py — règles de statut (le plus important).
À contenir : MISSING sans ligne, VALID, EXPIRED la veille de/à l'expiration,
jour d'expiration inclus (valide), EXPIRING_SOON à J-30/J-0, seuil par type
(30/30/15), taxe sans exercice courant -> MISSING (« Impayée »), renouvellement
= ligne récente priment, statut global NON CONFORME > À SURVEILLER > CONFORME,
types non obligatoires sans effet.
Réf. : ARCHITECTURE.md §4 et §10.
"""
