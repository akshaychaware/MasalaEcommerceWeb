# BirthdayWishes

A premium Django 5 birthday experience for **Vishuukhaa (Vishuu)**, designed as a cinematic, scroll-led surprise for her **11 August** birthday.

## Highlights

- Modular Django apps: `birthday`, `core`, `gallery`, `timeline`, `surprise`, `letters`, and `music`.
- Admin-editable hero copy, handwritten letter, photos, timeline events, flip-card reasons, secret message, tracks, theme colors, and ending message.
- Dark luxury interface with aurora gradients, glassmorphism, particles, GSAP motion, AOS scroll reveals, Alpine.js interactions, HTMX-ready templates, and accessible keyboard/focus behavior.
- Production foundations: environment variables, WhiteNoise static files, custom error pages, logging, Docker, and GitHub Actions CI.

## Local development

```bash
cd BirthdayWishes
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and use `/admin/` to replace placeholders with the birthday letter, music, and image assets.

## Content setup checklist

1. Create one active `HomeExperience`.
2. Add a `BirthdayLetter` with the final letter body and signature.
3. Upload a hero `Photo` with descriptive alt text and mark it as hero.
4. Add timeline memories and reason cards.
5. Upload one or more `Track` records.
6. Add the secret message and tune theme settings.

## Deployment checklist

- Set `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`, and HTTPS proxy settings.
- Keep `DJANGO_DEBUG=False`.
- Run `python manage.py collectstatic --noinput`.
- Use PostgreSQL by setting `DB_ENGINE=django.db.backends.postgresql` and database credentials.
- Serve media files from object storage or a protected media volume.
