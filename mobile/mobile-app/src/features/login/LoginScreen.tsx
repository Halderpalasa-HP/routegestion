/**
 * LoginScreen.tsx — écran de connexion de l'agent.
 *
 * À contenir : formulaire identifiant (email ou matricile AGT-…) + mot de passe,
 * appel auth.service.login -> POST /auth/login, gestion des erreurs 401/422/429
 * (rate limiting ≈5/min), bouton « Se connecter », style sombre cohérent.
 * Au succès : stockage du jeton puis navigation vers MainTabs (onglet Accueil).
 * Pas d'inscription dans l'app : les comptes sont créés par l'admin (§6 archi).
 */
