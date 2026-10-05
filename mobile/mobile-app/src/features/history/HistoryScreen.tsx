/**
 * HistoryScreen.tsx — onglet « Historique ».
 *
 * À contenir : liste paginée des contrôles de l'agent connecté
 * (GET /controls?agent_id=…&page= — l'agent ne voit QUE les siens, §6 archi) ;
 * carte par contrôle : plaque, heure • lieu, badge statut, référence e-PV éventuelle ;
 * pull-to-refresh, chargement infini, recherche simple, EmptyState ;
 * tap -> ControlDetailScreen. Filtres avancés réservés à l'admin web.
 */
