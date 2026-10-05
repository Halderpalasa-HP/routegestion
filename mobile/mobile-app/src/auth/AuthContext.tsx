/**
 * AuthContext.tsx — état de session de l'agent (contexte React).
 *
 * À contenir :
 * - user courant (nom, matricule AGT-…, rôle ADMIN/AGENT) et isAuthenticated ;
 * - login(payload) -> POST /auth/login puis stockage du jeton (tokenStorage) ;
 * - logout() -> POST /auth/logout + effacement du jeton ;
 * - restore au démarrage : GET /auth/me avec le jeton stocké (session persistée) ;
 * - état loading pendant la restauration (splash).
 *
 * Le rôle pilote l'accès aux écrans, mais les permissions sont vérées SERVEUR (§6 archi).
 */
