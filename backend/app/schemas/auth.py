"""
auth.py — schémas d'authentification.

À contenir : LoginRequest (email, password), TokenResponse (jeton opaque + user),
UserMe (nom, email, badge_number, rôle). Sortie = liste blanche de champs
(jamais password_hash). Réf. : ARCHITECTURE.md §7 (AUTH).
"""
