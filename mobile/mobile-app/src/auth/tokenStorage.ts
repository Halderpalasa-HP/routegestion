/**
 * tokenStorage.ts — stockage sécurisé du jeton opaque d'agent.
 *
 * À contenir : get/ set/ delete du jeton via expo-secure-store (Keychain/Keystore).
 * Règles : le jeton n'est JAMAIS stocké en clair ailleurs (ni AsyncStorage ni .env) ;
 * effacement obligatoire à la déconnexion et sur 401 ; expiration gérée par le serveur
 * (table api_tokens, ARCHITECTURE.md §11).
 */
