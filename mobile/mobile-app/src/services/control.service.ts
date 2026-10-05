/**
 * control.service.ts — contrôles (e-PV).
 * À contenir : create(payload) -> POST /controls avec STRICTEMENT
 * { code, notes, location } ; list(params) -> GET /controls ; getById(id) ;
 * pvUrl(id) -> GET /controls/{id}/pv.pdf. Jamais de statut ni de référence
 * dans la requête : tout est recalcule/genere serveur (§7 archi).
 */
