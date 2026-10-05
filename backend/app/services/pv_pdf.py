"""
pv_pdf.py — PvPdfService (génération du PDF e-PV avec reportlab).

À contenir : mise en page du constat (en-tête RDC/RouteGestion, référence,
véhicule, agent, date/lieu, tableau des pièces constatées, observations,
statut global, signature) ; accents français corrects ; rendu à la demande
depuis GET /controls/{id}/pv.pdf (pas de stockage obligatoire, décision §14).
Réf. : ARCHITECTURE.md §2 (reportlab) et §7.
"""
