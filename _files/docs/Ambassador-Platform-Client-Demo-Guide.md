# Intoto — The Ambassador Platform
## Client Demo Guide

**Design reference:** [Intoto Wireframe — The Ambassador Plateform (5051:661)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)  
**Starting frame:** [All Ambassadors — 5104:244443](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5104-244443&page-id=5051%3A661)  
**Audience:** Client demos, university admissions/marketing stakeholders  
**Demo length:** 12–18 minutes  
**Version:** 1.0

---

## 1. Demo objective

Show how a **prospective or incoming student** can:

- discover **Student Ambassadors** on a branded web portal (**Powered by Intoto**)
- search and filter ambassadors by availability, role, program, and country
- read rich **ambassador profiles** and FAQs
- start **individual chats** with mentors
- join **group chats** for cohorts and programs
- sign up, verify email, and manage their own account

**Not in scope for this demo:** Intoto mobile app roles (Student, in-app Ambassador mentor, University Admin).

---

## 2. Pre-demo checklist

Before starting, confirm the environment has:

- Ambassador Platform URL (staging or demo tenant)
- at least **6 ambassador cards** visible on home (mix of Student, Alumni, Staff)
- at least **1 ambassador Online** (green badge)
- at least **1 individual chat thread** with sample messages and quick-reply chips
- at least **1 group chat** (e.g. *International Students 2025*) with member count
- **Ambassador FAQ** section with at least 2 questions (one expanded)
- test signup account **or** pre-verified login (avoid live email dependency if possible)
- desktop browser (1920px) — optionally resize to mobile for closing beat

---

## 3. Quick narrative (talk track)

Use this short opening:

> "This is the **Ambassador Platform** — a web experience where students meet real ambassadors before they ever download the app.  
> Universities embed it on their site; Intoto powers discovery, chat, and trust at scale.  
> A prospect can search by program or country, read authentic stories, and message ambassadors in seconds."

---

## 4. Step-by-step demo flow

## Step 1 — First impression: directory home (2 min)

**What to do**
1. Open **All Ambassadors** (logged-in or public view per product config).
2. Point to header: **Student Ambassadors**, subtitle, **Powered by Intoto**.
3. Scroll filter chips: **All Ambassadors**, **Available Now**, **Students**, **Alumni**, **Staff**, **By Program**, **By Country**.
4. Type in search: *Business* → tap **Search**.

**What to say**
- "This is the university's ambassador storefront — not the full Intoto app."
- "Filters help prospects find someone like them — same program, same country, or someone online right now."

---

## Step 2 — Ambassador cards (2 min)

**What to do**
1. Highlight one **Online** card with **Student** badge.
2. Read name, program line, bio snippet, **Program** row.
3. Tap **Chat** on card → show chat opens with that ambassador.
4. Go back → tap card body → **Ambassadors Profile**.

**What to say**
- "Online ambassadors get priority — green dot drives conversion."
- "One tap to chat; full profile for students who want depth before messaging."

---

## Step 3 — Ambassador profile detail (2 min)

**What to do**
1. On **Ambassadors Profile**, walk left panel: photo, name, **Chat** CTA, Program, Country, Languages, Favourite Programs, response time.
2. Scroll **About me** on the right.
3. Point to **Ask me a question** if visible.
4. Tap **Chat** → return to thread.

**What to say**
- "Profiles are ambassador-authored — authentic voice, not marketing copy."
- "Response-time hints set expectations before the first message."

---

## Step 4 — Individual chat (2–3 min)

**What to do**
1. Open **Chat** from header icon.
2. Show **Individual Chats** tab and thread list (names, dates, unread badges).
3. Open a thread — show incoming/outgoing bubbles and timestamps.
4. Point to quick-reply chips: **Campus life**, **Accommodation**, **Academic programs**, **Student life**.
5. Type in **Type your message...** → send (or show **Type** / **msg typing** state).
6. Optional: show **Image attach** flow.

**What to say**
- "Guided chips lower the barrier — students don't need to know what to ask."
- "Same chat experience ambassadors use in the ecosystem; students stay in the browser."

---

## Step 5 — Group chats (2 min)

**What to do**
1. Switch to **Group Chats** tab.
2. Open **International Students 2025** (or similar).
3. Show **24 members** in header and multi-sender thread.
4. Optional: open **Group Detail** → **Group images** → show **Leave group** popup (don't leave in live demo).

**What to say**
- "Cohort groups scale peer support — one thread for an entire intake."
- "Admins can curate groups by program or theme; students opt in by joining."

---

## Step 6 — FAQ and See More (1 min)

**What to do**
1. Return to **All Ambassadors** home.
2. Scroll to **Ambassador FAQ** — expand one question.
3. Tap **See More** under ambassador cards if present.

**What to say**
- "FAQ content is ambassador-sourced SEO-friendly material — works even before chat."
- "See More loads the full directory when the carousel isn't enough."

---

## Step 7 — Signup & onboarding (2 min) *(optional — use test account if email is slow)*

**What to do**
1. Log out → open **Signup**.
2. Show **Email address**, **Password**, **Remember Me**, **Forget Password?**, **Continue**.
3. Show **Verification Required!** screen (or skip with pre-verified account).
4. Walk **Create profile** → **Basic Information**: photo, name, email, phone, country → **Submit**.
5. Land back on **All Ambassadors**.

**What to say**
- "Lightweight onboarding — university email verification builds trust."
- "Profile is minimal; chat is the goal, not another form."

---

## Step 8 — Account safety (1 min)

**What to do**
1. Open profile icon → **View Profile** / **Profile**.
2. Show **Logout** → **Logout Confirmation?** (cancel).
3. Mention **Delete Account** exists for GDPR-style self-service.
4. In chat, tap **⋮** → show **Report a conversation** and **Delete conversation** (don't submit report in demo).

**What to say**
- "Students control their data — logout, delete, and report are one tap away."
- "Universities get moderation hooks without exposing admin tools here."

---

## Step 9 — Mobile beat (optional, 1 min)

**What to do**
1. Resize browser to ~412px or open mobile Figma frame.
2. Show stacked cards, **Chat Detail** full-screen, compact header.

**What to say**
- "Same product on phone — critical for international students on mobile data."

---

## 5. Demo personas

| Persona | Focus |
|---------|-------|
| **Admissions director** | FAQ, profile depth, Powered by Intoto branding |
| **International recruitment** | By Country filter, group chats, online ambassadors |
| **IT / procurement** | Auth, email verification, delete account, report flow |

---

## 6. Objection handling

| Objection | Response |
|-----------|----------|
| "We already have live chat on our website." | "This is peer-to-peer — students trust ambassadors more than generic support bots." |
| "How is this different from the Intoto app?" | "Platform is discovery + chat in the browser; the app is the full student journey post-enrollment." |
| "Who moderates chats?" | "Report flow is built in; university staff use Intoto admin tools separately." |
| "Can we white-label?" | "Powered by Intoto is in design; discuss branding scope with product." |

---

## 7. Closing summary

End with:

> "The Ambassador Platform turns your student mentors into a **scalable recruitment channel** — searchable, filterable, and chat-ready on day one.  
> Prospects get real answers; your team gets measurable engagement before applications complete."

---

## 8. Related documentation

| Document | Use |
|----------|-----|
| `Ambassador-Platform-Features-and-Flows.md` | Full screen inventory and flows |
| `Ambassador-Platform-QA-Test-Guide.md` | Pre-release validation |
| `Ambassador-Features-and-Flows.md` | In-app Ambassador mentor role (mobile) |

---

## Document history

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | Jun 2026 | Initial demo script from Figma 5051:661 |
