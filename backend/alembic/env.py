"""
env.py — environnement Alembic (migrations).

À contenir : lecture de alembic.ini + DATABASE_URL, fourniture du
target_metadata = Base.metadata (import app.models pour tout charger),
modes offline/online, run_migrations_online avec engine SQLAlchemy.
Réf. : ARCHITECTURE.md §13 (étape 3 : migrations + seeds).
"""
