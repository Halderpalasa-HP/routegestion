"""
test_auth.py — authentification et jetons.
À contenir : login OK / mauvais mot de passe (401), GET /auth/me avec et sans
jeton (401), logout -> jeton révoqué (réutilisation = 401), rate limiting
login (429), expiration de jeton, agent désactivé = jetons révoqués.
"""
