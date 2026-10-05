"""
qr_code.py — QrCodeService (génération et révocation des QR).

À contenir :
- génération de code « VEH- » + 7 caractères aléatoires sans 0/O ni 1/I,
  NON séquentiels (pas de VEH-000025 devinable) via secrets ;
- rendu SVG via segno (endpoint image) ;
- révocation : ancien -> REVOKED, nouveau -> ACTIVE (index unique garantit
  l'unicité de l'actif) ; le code seul ne donne rien sans jeton (§8).
Réf. : ARCHITECTURE.md §8.
"""
