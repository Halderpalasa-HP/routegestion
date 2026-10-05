/**
 * errors.ts — normalisation des erreurs de l'API pour l'affichage.
 *
 * À contenir :
 * - lecture du format d'erreur uniforme du backend ({ detail } + code HTTP) ;
 * - fonction toUserMessage(error) : 401 session expirée, 403 refusé, 404 introuvable,
 *   422 validation, 429 trop de requêtes, réseau/coupure -> message FR ;
 * - usage par ErrorView et les écrans (jamais d'alert() brut).
 */
