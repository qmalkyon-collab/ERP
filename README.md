# ERP MVP (FastAPI + Postgres + Docker)

Ένα ελάχιστο αλλά παραγωγικό ERP starter με:
- **FastAPI** (Python) για API
- **SQLModel**/**SQLAlchemy** για μοντέλα/ORM
- **JWT Auth** (OAuth2 Password)
- **PostgreSQL** (managed σε cloud ή local με Docker)
- **Docker Compose** για τοπική ανάπτυξη
- Multi-tenant (προαιρετικά) με `tenant_id` σε βασικούς πίνακες

## Γρήγορη Εκκίνηση (local, με Docker)
1) Εγκατάσταση Docker & Docker Compose
2) Αντιγραφή `.env.example` → `.env` και ρύθμιση μεταβλητών
3) `docker compose up --build`
4) API Docs: http://localhost:8000/docs
5) Δημιουργείται admin χρήστης στην εκκίνηση (βλ. `.env`).

## Περιβάλλον
- Πίνακες δημιουργούνται αυτόματα στην εκκίνηση.
- Το ERP είναι modular: ξεκινά με Products, Customers, Warehouses, Inventory, Sales Orders, Invoices.
- Επεκτείνετε εύκολα προσθέτοντας routers και models.

## Deploy σε Cloud (ενδεικτικά)
- **DB**: Managed Postgres (π.χ. AWS RDS, GCP Cloud SQL, Azure PG, Supabase).
- **API**: Docker image σε οποιοδήποτε PaaS/Container service (Render, Railway, Fly.io, AWS ECS/Fargate, Azure Web App, GCP Cloud Run).
- Ρυθμίστε τα **secrets** (.env) στο περιβάλλον του provider.
- Ενεργοποιήστε **automatic backups**, **encryption at rest**, και **Point-in-time recovery** στη DB.

## Ασφάλεια (σημεία προσοχής)
- Υποχρεωτικό HTTPS πίσω από reverse proxy/CDN (Cloudflare/ALB/NGINX Ingress).
- Δικαιώματα με ρόλους (RBAC): admin, manager, user (δείγμα εδώ).
- Audit logs (βασικό παράδειγμα: created_at/updated_at, TODO για πλήρη ιχνηλασιμότητα).
- **GDPR**: data minimization, DPA με provider, κρυπτογράφηση backups, role-based access.

## Δομή
```
backend/
  app/
    __init__.py
    config.py
    db.py
    security.py
    models.py
    schemas.py
    deps.py
    routers/
      __init__.py
      auth.py
      products.py
      customers.py
      warehouses.py
      inventory.py
      sales.py
      invoices.py
    main.py
  requirements.txt
Dockerfile
docker-compose.yml
.env.example
```

## Default Ρόλοι
- `admin`: πλήρη δικαιώματα
- `manager`: διαχείριση καταλόγων/πωλήσεων
- `user`: read-only στις περισσότερες οντότητες

---

> Αυτό είναι ένα λειτουργικό σημείο εκκίνησης για ERP. Μπορείτε να προσθέσετε modules (π.χ. Λογιστική, Αγορές, Παραγωγή) ακολουθώντας το ίδιο μοτίβο.