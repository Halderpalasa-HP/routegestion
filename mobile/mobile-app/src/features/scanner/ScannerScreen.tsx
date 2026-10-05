/**
 * ScannerScreen.tsx — écran de scan QR (maquette 2).
 *
 * À contenir :
 * - AppHeader « Scanner un code QR / Nouveau contrôle documentaire » ;
 * - viseur caméra (expo-camera) : cadre cyan, torche (lampe), bandeau
 *   « Viseur illustratif - mode démo » -> remplacé par la vraie lecture ;
 * - détection du contenu QR (code type VEH-8F29A73) -> qr.service.lookup(code)
 *   = GET /qr-codes/{code} avec jeton -> navigation VehicleCheck ;
 * - relais « ou saisir la plaque » (PlateEntrySheet) si QR illisible ;
 * - bandeau bas : « Vérifiez que la plaque correspond au véhicule présenté. » ;
 * - erreurs : QR inconnu/révoqué, véhicule INACTIF, réseau -> ErrorView (explicite).
 * Dépend de useCameraPermission (permission refusée -> explication + saisie plaque).
 */
