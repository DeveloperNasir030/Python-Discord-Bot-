Discord Bot - Python (VSCode)

📌 Projektbeschreibung

Dies ist ein Discord-Bot, geschrieben in Python, der mit discord.py arbeitet. Das Skript kann in Visual Studio Code (VSCode) ausgeführt werden und bietet verschiedene Moderationsfunktionen, wie Kick, Ban, Timeout sowie ein Ticket-System.

🚀 Features

✅ Moderation: Kick, Ban, Timeout

🎫 Ticket-System mit individuellen Transcripts

🚨 AutoMod mit Blacklist für unerwünschte Wörter

🛠️ Einfache Konfiguration & Erweiterbarkeit

🔧 Installation & Einrichtung

1️⃣ Voraussetzungen

Python 3.8+ installiert (Download hier)

Ein Discord-Bot-Token (Anleitung)

discord.py und weitere Abhängigkeiten installieren:

pip install discord.py python-dotenv

2️⃣ Projektdateien

bot.py – Der Hauptcode für den Discord-Bot

.env – (Optional) Token-Speicherung für Sicherheit

blacklist.json – (Optional) Liste unerlaubter Wörter für AutoMod

README.md – Diese Datei

3️⃣ Bot starten

Öffne das Terminal in VSCode und starte den Bot mit:

python bot.py

⚙️ Konfiguration

.env Datei für Token-Sicherheit (Empfohlen)

Erstelle eine Datei .env im Projektordner und füge Folgendes hinzu:

DISCORD_TOKEN=DEIN_BOT_TOKEN

Im Code kannst du darauf zugreifen mit:

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

🛠 Befehle (Commands)

Befehl

Beschreibung

Berechtigungen

!kick @user

Benutzer kicken

Kick Members

!ban @user

Benutzer bannen

Ban Members

!timeout @user X

Benutzer timeouten für X Minuten

Moderate Members

!ticket

Erstellt ein Support-Ticket

Jeder

!close

Schließt ein Ticket

Ticket-Ersteller/Admin


💡 Autor

Autor: DeveloperNasir030

