/**
 * App.tsx — point d'entrée de l'application mobile « Contrôle Véhicule ».
 *
 * À contenir :
 * - providers : AuthContext (session), ControlDraftContext (brouillon de constat),
 *   éventuellement QueryClientProvider (react-query) ;
 * - application du thème sombre (components/Theme.ts) ;
 * - rendu de RootNavigator + restore de session au démarrage (GET /auth/me) ;
 * - captation des erreurs JS non catchées.
 *
 * Aucune logique métier ici : uniquement le câblage des providers et de la navigation.
 */
