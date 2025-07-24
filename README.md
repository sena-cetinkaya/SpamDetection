# 📬 Spam E-Posta Tespit API'si (FastAPI + ML + Docker)

Bu proje, Türkçe e-posta içeriklerini analiz ederek bunları **spam** veya **normal (ham)** olarak sınıflandıran bir **makine öğrenmesi API'sidir**.

Proje; veritabanı kayıtları, model eğitimi, tahmin ve sonuçların kalıcı olarak saklanmasını içeren tam bir uçtan uca yapıya sahiptir.  
Model eğitimi sırasında farklı algoritmalar (Random Forest, Naive Bayes) değerlendirilir ve en iyi performansı veren model seçilip `.pkl` olarak kaydedilir.

---

## 🧠 Proje Özellikleri

- ✅ Türkçe spam verisiyle eğitim (CSV tabanlı)
- ✅ RandomForest ve Naive Bayes algoritmalarıyla model karşılaştırması
- ✅ TF-IDF vektörleştirme + Pipeline kullanımı
- ✅ Model seçimi ve kaydı (`spam_model.pkl`)
- ✅ FastAPI ile REST API servisi
- ✅ Tahmin sonrası sonucu veritabanına kaydetme
- ✅ Docker ile hızlı kurulum ve taşıma

---

## ⚙️ Kurulum

### 1️⃣ Gerekli kütüphaneleri yükle

```pip install -r requirements.txt```

### 2️⃣ Veritabanı ayarı

.env dosyasındaki DATABASE_URL değişkeni şu formatta olmalıdır:

```DATABASE_URL=sqlite:///./spam.db```

veya PostgreSQL için:

DATABASE_URL=postgresql://kullanici:sifre@localhost:5432/spam_db

### 3️⃣ Veri setini yükle + Modeli eğit

```python load_csv_once.py```

Bu script:

- CSV dosyasını işler

- Verileri veritabanına yükler

- Model eğitilmemişse en iyi sonucu veren modeli kaydeder (spam_model.pkl)

-------- 

### 🚀 Uygulamayı Çalıştırma

Lokal çalıştırmak için:

```uvicorn app.main:app --reload```

Swagger UI: http://localhost:8000/docs

🔌 API Endpoint'leri

📍 POST /predict

```
{
  "content": "Kazandınız! Hemen tıklayın."
}
```
```
{
  "prediction": "spam",
  "probability": {
    "spam: %": 92.5,
    "ham: %": 7.5
  },
  "label": 1
}
```

Tahmin edilen sonuç aynı zamanda email tablosuna otomatik olarak kaydedilir.

----------

### 🐳 Docker ile Çalıştırmak

```docker-compose up --build```

📦 Kullanılan Teknolojiler

- Python 3.10+

- FastAPI

- SQLModel

- scikit-learn

- TfidfVectorizer

- RandomForestClassifier / MultinomialNB

- Docker

- .env yapılandırması

📃 Lisans: Bu proje MIT lisansı ile açık kaynak olarak sunulmuştur.

👩‍💻 Geliştirici: Sena Çetinkaya

📧 [cetinkayasena96@gmail.com](cetinkayasena96@gmail.com)

🌐 GitHub: [https://github.com/sena-cetinkaya](https://github.com/sena-cetinkaya)
