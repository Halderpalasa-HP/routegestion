"""
user.py — table users (admins et agents).

Colonnes : id, role_id (FK roles), name, email (unique), password_hash,
badge_number (unique, nullable, ex. AGT-2026-042), is_active, last_login_at.
Relations : 1-N api_tokens, 1-N controls. Jamais de suppression : désactivation.
Réf. : ARCHITECTURE.md §4.
"""
