/**
 * page.tsx — « Paramètres documentaires » (maquette Portail - Paramètres).
 * À contenir : table des types de documents (GET /document-types) avec édition
 * (is_required, has_expiry, warning_days 30/30/15, diagnostic_hint) via PATCH ;
 * « Seuils & affichage » (GET|PUT /settings : expiring_soon_days, show_alerts,
 * show_missing) ; gestion des utilisateurs (GET|POST /users, reset-password,
 * deactivate) ; lien vers le journal (GET /audit-logs). Réf. §5 et §7.
 */
