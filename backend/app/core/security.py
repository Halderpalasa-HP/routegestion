"""
security.py — primitives d'authentification.

À contenir :
- hash/verify de mots de passe (passlib bcrypt ou argon2-cffi) ;
- création de jeton opaque (256 bits, token_urlsafe) : en clair JAMAIS stocké,
  seule sa hash SHA-256 va dans api_tokens ;
- vérification d'expiration (expires_at) et de révocation (revoked_at).
Réf. : ARCHITECTURE.md §2 (auth esprit Sanctum) et §11.
"""
