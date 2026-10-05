/**
 * qr.service.ts — vérification du QR par l'agent.
 * À contenir : lookup(code) -> GET /qr-codes/{code} => vue réduite agent
 * (véhicule + documents). QR révoqué/inconnu -> erreur 404 à afficher via ErrorView.
 * Le code seul ne donne rien sans jeton valide (§8 archi).
 */
