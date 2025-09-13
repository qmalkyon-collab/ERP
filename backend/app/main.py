from fastapi import FastAPI
from .db import init_db, get_session
from .routers import auth, products, customers, warehouses, inventory, sales, invoices
from .config import settings
from sqlmodel import Session, select
from .models import User
from .security import get_password_hash

app = FastAPI(title=settings.APP_NAME)

@app.on_event("startup")
def on_startup():
    init_db()
    # Bootstrap admin user
    with Session(bind=None) as _:
        pass  # silence mypy
    from .db import engine
    with Session(engine) as session:
        admin = session.exec(select(User).where(User.email == settings.ADMIN_EMAIL)).first()
        if not admin:
            admin = User(
                email=settings.ADMIN_EMAIL,
                full_name="Admin",
                hashed_password=get_password_hash(settings.ADMIN_PASSWORD),
                role="admin",
                tenant_id=settings.ADMIN_TENANT,
            )
            session.add(admin)
            session.commit()

@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi.middleware.cors import CORSMiddleware

# ... κάτω από app = FastAPI(...)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # για demo — σε production βάλε το domain σου
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(customers.router)
app.include_router(warehouses.router)
app.include_router(inventory.router)
app.include_router(sales.router)
app.include_router(invoices.router)
