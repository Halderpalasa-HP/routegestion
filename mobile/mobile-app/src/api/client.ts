/**
 * client.ts — client HTTP unique de l'app (axios).
 *
 * À contenir :
 * - instance axios avec baseURL = API_BASE_URL (.env) + préfixe éventuel ;
 * - intercepteur requête : en-tête Authorization: Bearer <jeton> (voir auth/tokenStorage) ;
 * - intercepteur réponse : 401/403 -> déconnexion propre et navigation vers Login ;
 *   401/422/429 -> traduits en erreurs lisibles (api/errors.ts) ;
 * - helpers typés get/post/patch/delete alignés sur types/api.ts.
 *
 * Contrat : ARCHITECTURE.md §7 — l'app ne parle jamais à MySQL, seulement à l'API.
 */
