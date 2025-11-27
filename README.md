♟️ Chess Rating System API

Professional Chess Rating Platform — Backend System

Bu loyiha shaxmat reytingi va turnir tizimi uchun backend API bo'lib, Chess.com va Lichess.org kabi platformalar prinsiplariga asoslangan.

Muhim: Authentication talab qilinmaydi — barcha endpointlar ochiq (public access).

Tizim Game (Turnir), Player (Shaxmatchi), va Score (Partiya natijasi) ma’lumotlarini boshqaradi, hamda Rating System va Leaderboard funksiyalarini qo'llab-quvvatlaydi.

📂 Loyiha Strukturasi
/
├── core/                    # Project: Asosiy project
├── games/                   # App: Turnirlar moduli
├── players/                 # App: Shaxmatchilar moduli
├── scores/                  # App: Partiyalar va natijalar
├── leaderboard/             # App: Rating va statistika

🗄️ Ma'lumotlar Bazasi Modellari
1. Game Model (games/models.py)

Shaxmat turnirlari haqida ma’lumot.

Field	Type	Description	Constraints
id	AutoField	Primary key	Auto-generated
title	CharField(200)	Turnir nomi	Required, max_length=200
location	CharField(100)	O‘tkazilish joyi	Required
start_date	DateField	Boshlanish sanasi	Required
description	TextField	Tavsif	Optional, blank=True, null=True
created_at	DateTimeField	Yaratilgan vaqt	auto_now_add=True

__str__ metodi title qaytaradi

O'chirishdan oldin unga bog'liq scorelar tekshiriladi

Meta class: ordering = ['-created_at']

2. Player Model (players/models.py)

Shaxmatchilar profili va reytingi.

Field	Type	Description	Constraints
id	AutoField	Primary key	Auto-generated
nickname	CharField(50)	Shaxmatchi nomi	Required, unique
country	CharField(50)	Mamlakat	Required
rating	IntegerField	Joriy reyting	Default: 0
created_at	DateTimeField	Ro'yxatdan o'tgan vaqt	auto_now_add=True

nickname unique bo‘lishi shart

__str__ metodi nickname qaytaradi

rating har partiyadan keyin avtomatik yangilanadi

3. Score Model (scores/models.py)

Shaxmat partiyalari natijalari.

Field	Type	Description	Constraints
id	AutoField	Primary key	Auto-generated
game	ForeignKey	Turnirga bog‘lanish	Required, on_delete=PROTECT
player	ForeignKey	Shaxmatchiga bog‘lanish	Required, on_delete=PROTECT
result	CharField(10)	Partiya natijasi	Choices: 'win', 'loss', 'draw'
points	IntegerField	Partiya oldidan reyting	
opponent_name	CharField(50)	Raqib ismi	Optional
created_at	DateTimeField	Natija kiritilgan vaqt	auto_now_add=True

Bir player bir game uchun ko‘p marta score qo‘shishi mumkin (har xil raqiblar bilan)

Meta class: ordering = ['-created_at']

Result qiymatlari:

win = 10 ball

draw = 5 ball

loss = 0 ball

🚀 API Endpoints

Base URL: http://localhost:8000/api/

♟️ Game Endpoints
Method	Endpoint	Description
POST	/games/	Yangi turnir yaratish
GET	/games/{id}/	Turnir ma’lumotlarini olish
PATCH	/games/{id}/	Turnirni yangilash
DELETE	/games/{id}/	Turnirni o‘chirish (agar score mavjud bo‘lsa xato beradi)
👤 Player Endpoints
Method	Endpoint	Description
POST	/players/	Yangi shaxmatchi yaratish
GET	/players/	Shaxmatchilar ro‘yxati (filter/search)
GET	/players/{id}/	Shaxmatchi ma’lumotlarini olish
PATCH	/players/{id}/	Shaxmatchi ma’lumotlarini yangilash
DELETE	/players/{id}/	Shaxmatchi o‘chirish (agar score mavjud bo‘lsa xato beradi)
🏆 Score Endpoints
Method	Endpoint	Description
POST	/scores/	Yangi partiya natijasi yaratish
GET	/scores/	Partiyalar ro‘yxati (filter/search)
GET	/scores/{id}/	Natija ma’lumotlarini olish
DELETE	/scores/{id}/	Natijani o‘chirish (rating qayta hisoblanadi)

POST body example:

{
  "game": 1,
  "player": 3,
  "result": "win",
  "opponent_name": "GrandMaster"
}

🏆 Leaderboard Endpoints
Method	Endpoint	Description
GET	/leaderboard/?game_id={id}	Game Leaderboard
GET	/leaderboard/top/?game_id={id}&limit={n}	Top Players Leaderboard
GET	/leaderboard/global/?country={country}&limit={n}	Global Rating Leaderboard

Business Logic:

Ballar: win=10, draw=5, loss=0

Reyting o‘zgarishi va rank avtomatik hisoblanadi

🔍 Filtering & Search

Game: search (title), location

Player: search (nickname), country, min_rating

Score: game_id, player_id, result

⚙️ Admin Panel

URL: http://127.0.0.1:8000/admin/

Superuser orqali barcha modellarni boshqarish mumkin.