/**
 * ControlDetailScreen.tsx — détail d'un contrôle enregistré.
 *
 * À contenir : en-tête (référence, date, agent, lieu), statut global, constat FIGÉ
 * pièce par pièce (control_items : type, statut à l'instant du contrôle, expiration),
 * observations de l'agent ; bouton « Consulter / Télécharger l'e-PV » ->
 * GET /controls/{id}/pv.pdf rendu via expo-print + expo-file-system.
 * Le figetage reste vrai même après renouvellement d'une pièce (règle §10 archi).
 */
