"""
documents.py — endpoints DOCUMENTS (pièces justificatives).

À contenir : GET|POST /vehicles/{id}/documents (POST multipart : PDF/JPG/PNG
uniquement, taille limitée, vrai MIME vérifié, nom aléatoire, stockage hors
public), GET|PATCH|DELETE /documents/{id}, GET /documents/{id}/file
(téléchargement authentifié). Le statut n'est jamais écrit ici (calculé, §4).
Réf. : ARCHITECTURE.md §7 et §11.
"""
