# CONNECT – AI-Powered Laptop Discovery Platform

##  Overview
**CONNECT** is a web-based platform designed to help users research and discover the best laptops for their needs.  
It features **AI-generated specifications summaries**, **natural language search**, and **personalized recommendations**, making laptop research faster and more beginner-friendly.  

Unlike traditional e-commerce websites, CONNECT focuses solely on **research and discovery** — users cannot purchase directly through the platform.  
Initially, laptops are posted by the platform owner, with future plans to allow verified sellers.

---

##  Features
- **Laptop Listings** – Detailed specs, images, and prices.
- **Advanced Filtering** – Search by price, RAM, processor, storage, and more.
- **AI-Powered Recommendations** – Suggests laptops based on user preferences.
- **Natural Language Search** – Conversational queries like  
  `"Show me gaming laptops under $1000 with 16GB RAM"`.
- **Favorites, Reviews, and Comments** – Engage and save favorite products.
- **Subscription System** – Get notified about laptops matching your preferences.
- **Push & Email Notifications** – Alerts for new relevant listings.

---

##  Tech Stack
**Backend:** Django, Django REST Framework  
**Frontend:** HTML, CSS 
**Database:** MySQL
**AI & NLP:** Gemini AI (Free Tier) or Hugging Face Models  
**Search:** Meilisearch (Open-Source)  
**Notifications:** Firebase Cloud Messaging  
**Email Alerts:** Django-mail

---

## 📡 API Integrations
- **Gemini AI API** – Generates simplified laptop specs and recommendations.
- **Meilisearch** – Enables fast, natural language search.
- **Firebase Cloud Messaging** – Sends browser push notifications.
- **Django-mail** – Sends subscription-based email alerts.

---

##  Project Structure (Apps)
- `laptops` – Manages listings, filtering, and search.
- `users` – Handles authentication, favorites, and subscriptions.
- `reviews` – Stores and displays reviews/comments.
- `notifications` – Push and email notifications.
- `ai_features` – AI summaries, recommendations, and search integration.

---

## 📦 Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/AbdulazizAyalew/connect.git
   cd connect
