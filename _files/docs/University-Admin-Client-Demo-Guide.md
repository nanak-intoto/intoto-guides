# Intoto — University Admin
## Client Demo Guide

**Design reference:** [INTOTO WebApp — University Super Admin (node 81-7360)](https://www.figma.com/design/hNVFYMIiLyFZJKD8khkn4Q/INTOTO-WebApp?node-id=81-7360&p=f&m=dev)  
**Prototype:** [INTOTO WebApp — Dashboard (546-1397)](https://www.figma.com/design/hNVFYMIiLyFZJKD8khkn4Q/INTOTO-WebApp?node-id=546-1397&page-id=81%3A7360)  
**Audience:** Client demos, stakeholders, pre-sales  
**Demo length:** 18–25 minutes  
**Version:** 1.0

---

## 1. Demo objective

Show how a **University Admin** can:

- monitor university operations from one **web dashboard**
- manage invitation and user lifecycle across all roles
- clear **Profile Review** backlog for incoming students
- configure **My University** and **Campus** data
- govern **community** and **report** workflows
- oversee **travel**, **ambassadors**, and **events**

**Not in scope:** Mobile app (`University-Super-Admin-Client-Demo-Guide.md`), platform-wide Intoto Admin.

---

## 2. Pre-demo checklist

Before starting, confirm the environment has:

- one University Admin web login
- university logo visible in sidebar
- dashboard stat cards populated (communities, travel, events, students)
- at least five users in **Manage User** with mixed statuses (Accepted, Invited)
- profile review backlog (Pending Review > 0)
- one campus in **Campus** list
- one pending community request and one active community
- one upcoming travel plan and one event
- internal and external ambassador sample rows

---

## 3. Quick narrative (talk track)

Use this short opening:

> "University Admin is the **web command center** for your institution on Intoto.  
> One dashboard covers students, travel, events, communities, and ambassadors — all scoped to your university.  
> Staff run operations here; students use the mobile app."

---

## 4. Step-by-step demo flow

## Step 1 — Login and role context (1 min)

**What to do**
1. Open WebApp URL → **Login or Sign-up** → **Continue**.
2. Complete SSO (or use pre-authenticated session).
3. Show header: **University Admin**, user name, notification badge.

**What to say**
- "Authentication goes through your identity provider — not stored on this screen."
- "This role is the top operational admin for one university on the **web portal**."

---

## Step 2 — Dashboard overview (3 min)

**What to do**
1. Point to sidebar and **Welcome !** header.
2. Walk **Dashboard Overview** cards — row 1: Communities, Travel, Events, Ambassadors, Students.
3. Row 2: External Ambassadors, coordinators, University Super Admin count.
4. Glance at **Student Admission** chart and **Student Travel Plan** widget.
5. Scroll to **Student's Location** donut.

**What to say**
- "Every card drills into the live list behind that number."
- "Admissions and travel widgets help student affairs at a glance."

---

## Step 3 — Manage User (4 min)

**What to do**
1. Sidebar → **Manage User**.
2. Show **Total Users**, search, table columns (Role, Campus, Status).
3. Tap **Add Users** → show role picker (don't submit unless safe).
4. Row ⋮ → **Approve**, **Reject**, **Download**.

**What to say**
- "One table for every role on campus."
- "Invite and lifecycle status are visible in one place."

---

## Step 4 — Profile Review (2 min)

**What to do**
1. Sidebar → **Profile Review**.
2. Walk summary cards: Complete, Incomplete, Pending Review, Action Required.
3. Open one pending row if available.

**What to say**
- "Students can't fully onboard until profiles pass review."
- "Cards show today's backlog at a glance."

---

## Step 5 — My University (2 min)

**What to do**
1. Sidebar → **My University**.
2. Show banner, name, location, established year.
3. Scroll Overview sections; preview **Programs & Services** tab.

**What to say**
- "University content is editable here — no developer needed."
- "This is what students see during onboarding."

---

## Step 6 — Campus (2 min)

**What to do**
1. Sidebar → **Campus** → open one campus.
2. Mention Students, Courses/Programs, Faculty, Travel Plans tabs.

**What to say**
- "Multi-campus schools manage each location separately."

---

## Step 7 — Community and reports (2 min)

**What to do**
1. Sidebar → **Community** → **Pending Requests**.
2. Switch to **Active Communities** → feed preview.
3. Mention **Reports** moderation.

**What to say**
- "Communities need admin approval before going live."
- "Reports use the same moderation workflow."

---

## Step 8 — Events and travel (2 min)

**What to do**
1. Dashboard → **Events** card → list preview.
2. Show **Create Event** form header.
3. Brief **Travel Plan** → **Travel Detail Upcoming**.

**What to say**
- "Events move from create → pending → published."
- "Travel shows who's arriving and when."

---

## Step 9 — Ambassadors (1 min)

**What to do**
1. Dashboard → **Ambassadors** / **External Ambassadors**.
2. Open one detail or lead overview tab.

**What to say**
- "Internal mentors and external recruitment in one module."

---

## Step 10 — Close (1 min)

**What to say**

> "University Admin on the WebApp is where your team **runs** Intoto — users, campuses, content, and compliance.  
> The mobile app is where students and coordinators engage day to day."

---

## 5. Persona focus

| Stakeholder | Emphasize |
|-------------|-----------|
| VP Student Affairs | Dashboard, Profile Review, Travel |
| IT / Identity | Manage User, Configurations |
| Admissions | Student Admission chart, Invite Data |
| Student engagement | Community, Events, Ambassadors |

---

## 6. Related documentation

| Document | Use |
|----------|-----|
| `University-Admin-Features-and-Flows.md` | Full feature reference |
| `University-Admin-QA-Test-Guide.md` | Pre-release validation |
| `University-Super-Admin-Client-Demo-Guide.md` | Mobile app demo |

---

## Document history

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | Jun 2026 | Initial demo script from INTOTO WebApp Figma |
