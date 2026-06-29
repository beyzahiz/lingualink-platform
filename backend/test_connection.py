from app.database import engine

try:
    with engine.connect() as conn:
        print("✅ Veritabanına bağlantı başarılı!")
except Exception as e:
    print("❌ Bağlantı hatası:", e)
