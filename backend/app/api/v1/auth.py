"""
auth.py — endpoints AUTH.

À contenir : POST /auth/login (slowapi ≈5/min anti brute-force, crée le jeton
opaque, met last_login_at), POST /auth/logout (révoque le jeton courant),
GET /auth/me (profil de l'utilisateur connecté). Réf. §7 (AUTH).
"""
