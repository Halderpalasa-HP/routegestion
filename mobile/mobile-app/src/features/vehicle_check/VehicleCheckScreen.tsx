/**
 * VehicleCheckScreen.tsx — dossier du véhicule : les 4 pièces (flux après scan).
 *
 * À contenir :
 * - en-tête véhicule : plaque, marque/modèle (année), couleur, badge statut global
 *   (Conforme / À surveiller / Non conforme) et compteur « 3 / 4 » ;
 * - liste des types de documents avec statut calculé SERVEUR :
 *   Carte grise, Assurance, Contrôle technique, Taxe de circulation
 *   (MISSING affiché « Impayée » pour la taxe, EXPIRED, EXPIRING_SOON « à J-12 », VALID) ;
 * - tap sur une pièce -> DocumentDetailScreen ;
 * - bouton « Enregistrer le contrôle » -> ControlSave (dossier non conforme).
 * Données : GET /vehicles/{id} + GET /vehicles/{id}/documents (vehicle/document.service).
 * RÈGLE : aucun calcul de statut local — affichage strict de la réponse API (§4 archi).
 */
