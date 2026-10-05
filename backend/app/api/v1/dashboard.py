"""
dashboard.py — endpoints DASHBOARD (ADMIN).

À contenir : GET /dashboard/stats (KPIs conformes/non conformes/total, §4),
GET /dashboard/activity?from=&to=&province_id= (courbe des contrôles),
GET /dashboard/anomalies?from=&to= (répartition par type de document).
Même règle de statut que le reste, appliquée en SQL (§4).
Réf. : ARCHITECTURE.md §7 (ADMIN).
"""
