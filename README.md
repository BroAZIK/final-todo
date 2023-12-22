# Tasks Backend

## API Endpoints

### 1. Tasklar

#### `GET: /api/Tasks`

*Ma'lumotlarni olish uchun*:

Bu endpoint orqali barcha `Task`larni olish mumkin.

**Misol so'rov:**
```
[
  {
    "id": 1,
    "title": "Vazifa 1",
    "description": "Bu birinchi vazifa",
    "completed": False,
    "created": "2023-12-20T10:40:38.880096Z",
    "user": 1
  },
  {
    "id": 2,
    "title": "Vazifa 2",
    "description": "Bu ikkinchi vazifa",
    "completed": False,
    "created": "2023-12-20T10:40:38.880096Z",
    "user": 1
  }
  
]
```
### `POST: /api/Tasks`

*Ma'lumot qo'shish uchun:*

Bu endpoint orqali yangi `Task` qo'shish mumkin.

Misol so'rov:

``````
Content-Type: application/json

{
    "title": "1 Vazifa",
    "completed": false,
    "description": "1-vazifa",
}
``````
Javob:

```
{
    "id": 1,
    "title": "1 Vazifa",
    "completed": false,
    "description": "1-vazifa",
    "created": "2023-12-20T15:14:47.457578Z",
    "user": 1
}
```
### 2. Kirish
### `POST /api/login`

Foydalanuvchi kiritish uchun:

Bu endpoint orqali foydalanuvchi kirishi amalga oshiriladi.

Misol so'rov:

Content-Type: application/json

```
{
  "username": "foydalanuvchi",
  "password": "parol123"
} 
```
Javob:

```
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```
### 3. Admin
### ```GET /admin```

Admin paneli uchun:

Bu endpoint orqali admin paneliga kirish mumkin.


## Litsenziya
Bu proyekt MIT litsenziyasi asosida tarqatilgan.


Bu README fayli barcha endpointlarni va ularning qanday ishlaydiganligi haqida qisqacha tavsif beradi. Siz shu qismni o'zgartirishingiz, endpointlarni boshqa qismlar bilan bog'lab olishingiz mumkin.