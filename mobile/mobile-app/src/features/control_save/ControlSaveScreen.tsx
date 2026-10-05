/**
 * ControlSaveScreen.tsx — « Enregistrer le contrôle » (maquette 4).
 *
 * À contenir :
 * - AppHeader « Enregistrer le contrôle / Constat documentaire / e-PV » ;
 * - stepper « • 1 · Vérification > • 2 · Consttat » ;
 * - carte véhicule (plaque, modèle) + badge statut global reçu du serveur ;
 * - « Anomalies retenues » : CheckboxRow pré-cochées issues du draft
 *   (ex. « Assurance expirée — 24/09/2026 • depuis 8 jours ») ;
 * - « Lieu du contrôle » : FormField (saisie manuelle, défaut) ou GPS si décidé ;
 * - « Observations de l'agent » : textarea multiligne ;
 * - bloc Agent / Matricule + case « Je confirme la vérification des pièces »
 *   (obligatoire avant activation du bouton) ;
 * - bouton « Enregistrer le contrôle et l'e-PV » -> control.service.create =
 *   POST /controls { code, notes, location } UNIQUEMENT (aucun statut envoyé,
 *   le serveur recalcule tout et génère la référence) -> ControlSuccess.
 */
