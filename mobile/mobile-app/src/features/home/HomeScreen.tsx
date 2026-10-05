/**
 * HomeScreen.tsx — « Accueil de service » (maquette 1).
 *
 * À contenir (dans l'ordre de la maquette) :
 * - AppHeader « CONTRÔLE VÉHICULE / Application de contrôle · RDC » + cloche ;
 * - date du jour en FR + « Bonjour, <nom>. » + « Votre service de contrôle documentaire. » ;
 * - carte agent : initiales, nom, matricule AGT-2026-042, pastille « Service »,
 *   lieu (Gombe, Kinshasa • Poste 04) ;
 * - carte CTA cyan : « Un scan, quatre pièces. » + bouton « Scanner un code QR » ;
 * - 2 StatTile (contrôles réalisés / non conformes) ;
 * - « Dernier contrôle » (plaque, heure•lieu, badge statut) + « Tout voir » -> Historique ;
 * - mention « Parcours illustratif… » remplacée par les données réelles une fois l'API branchée.
 * Données : hooks useDashboardStats + useControls ; bouton -> onglet Scanner.
 * ⚠️ Point API à confirmer : stats agent (voir ARCHITECTURE_MOBILE.md §7).
 */
