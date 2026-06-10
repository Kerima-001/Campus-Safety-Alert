# Campus Safety Alert System

**Protecting students through real-time safety intelligence.**

A full-stack emergency response platform that connects students, faculty, and campus security through instant alerts, incident reporting, and live location awareness. Built with Flutter, FastAPI, PostgreSQL, and Firebase.

---

## Overview

Campus emergencies demand immediate communication. Traditional methods — mass emails, loudspeakers, word of mouth — are too slow. This system replaces them with a mobile-first platform where alerts are geofenced to your location, incidents can be reported with photos and GPS coordinates in seconds, and security personnel have a live operations dashboard at their fingertips.

---

## Core Features

**Real-Time Emergency Alerts**
Security dispatches alerts instantly across campus. Each notification includes the incident type, severity level, GPS location, safety instructions, and emergency contacts. Supported alert types include active threats, medical emergencies, suspicious activity, severe weather, fire alarms, missing persons, and campus closures.

**Location-Aware Notifications**
Alerts are delivered based on proximity. A user 0.2 miles from Swenson Hall gets a targeted notification with relevant instructions. Users on the other side of campus do not. This reduces noise and improves response.

**Mobile Incident Reporting**
Students submit reports directly from the app — theft, harassment, suspicious activity, vandalism, medical emergencies, facility issues, and safety hazards. Each report captures a description, GPS coordinates, photos, severity level, and timestamp.

**One-Tap SOS System**

| Action | Response |
|---|---|
| Single tap | Notify campus security |
| Double tap | Call emergency services |
| Long press | Share live location |

**Interactive Campus Map**
A live map surfaces active incidents, safe zones, emergency phones, security offices, evacuation routes, residence halls, and medical stations.

**Security Dashboard**
Operations staff see open cases, active alerts, average response times, high-risk areas, and real-time incident maps. Built for fast triage, not just reporting.

**Analytics and Reporting**
Incident frequency, monthly trends, response time tracking, and alert effectiveness metrics feed daily, monthly, and annual safety reports.

---

## Tech Stack

| Layer | Tools |
|---|---|
| Backend | Python, FastAPI, SQLAlchemy |
| Database | PostgreSQL |
| Mobile | Flutter, Dart |
| Push Notifications | Firebase Cloud Messaging |
| Maps | Google Maps API |

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/Kerima-001/campus-safety-alert-system.git
cd campus-safety-alert-system

# Set up Python environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS / Linux

# Install backend dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary

# Start the backend
python -m uvicorn backend.main:app --reload

# Run the mobile app
flutter pub get
flutter run
```

---

## Project Structure

```
campus-safety-alert-system/
    backend/
        main.py
        database.py
        models.py
        auth.py
        routes/
            alerts.py
            incidents.py
            emergency.py
            users.py
    mobile/
        lib/
            screens/
            services/
            widgets/
            models/
    assets/
```

---

