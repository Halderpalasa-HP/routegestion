/**
 * ControlDraftContext.tsx — brouillon de constat partagé entre écrans.
 * À contenir : véhicule courant + code QR, anomalies cochées
 * (document_type_id + libellés), lieu du contrôle, observations ;
 * actions addAnomaly/removeAnomaly/setField/reset ; réinitialisé au succès
 * ou à l'abandon. Alimente ControlSave, alimenté par DocumentDetail.
 * Aucune donnée sensible n'y est stockée (pas de jeton).
 */
