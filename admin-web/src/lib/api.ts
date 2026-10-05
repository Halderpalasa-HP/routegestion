/**
 * api.ts — client HTTP typé de l'admin (le contrat OpenAPI).
 * À contenir : instance axios/fetch avec baseURL de l'API + /api/v1, en-tête
 * Authorization Bearer (jeton stocké côté navigateur), intercepteurs 401 ->
 * redirection login, helpers typés par groupe d'endpoints (auth, vehicles,
 * owners, qr, documents, controls, users, dashboard, settings, audit, exports),
 * gestion du format d'erreur { detail }. Réf. : ARCHITECTURE.md §7.
 */
