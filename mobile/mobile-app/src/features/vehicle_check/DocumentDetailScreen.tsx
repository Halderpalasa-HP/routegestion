/**
 * DocumentDetailScreen.tsx — détail d'une pièce (maquette 3 « Assurance expirée »).
 *
 * À contenir :
 * - AppHeader : nom du type + « {plaque} • pièce obligatoire » ;
 * - bandeau d'alerte selon statut : « Expirée depuis 8 jours » + phrase
 *   « La couverture … s'est terminée le 24 septembre 2026. » (utils/dates) ;
 * - carte attestation CLAIRE (Card variante light) : n° plaque, véhicule • titulaire,
 *   période 25/09/2025 → 24/09/2026, référence ASS-2025-01842, tag « DÉMO » ;
 * - section « Informations du document » : paires label/valeur (référence, assureur,
 *   début/fin en rouge si expiré, titulaire) ;
 * - section « À vérifier sur place » + mention « l'aperçu n'est pas une certification » ;
 * - bouton « Ajouter au constat » -> ajoute l'anomalie au ControlDraftContext,
 *   puis navigation vers ControlSave.
 * Données : GET /documents/{id} (document.service).
 */
