# Intoto — Intoto Admin
## Client Demo Guide

**Design reference:** [Intoto Wireframe — Intoto Admin (node 5051-661)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)  
**Prototype:** [Intoto Admin prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5051%3A661)  
**Audience:** Client demos, stakeholders, pre-sales  
**Demo length:** 15–22 minutes  
**Version:** 1.0

---

## 1. Demo objective

Show how an **Intoto Admin** can:

- govern the **entire Intoto platform** across all universities
- onboard and manage **university tenants**
- invite and control **users at any institution**
- monitor **platform-wide metrics** from one dashboard
- scope into a single university when needed without losing global context
- triage **reports and operational data** across tenants

---

## 2. Pre-demo checklist

Before starting, confirm the environment has:

- one `intoto_admin` login
- at least **two universities** (one active, one pending or suspended if possible)
- at least one **University Super Admin** per university
- one invited user and one accepted user **across different universities**
- sample students in at least two tenants
- at least one report, one community, and one upcoming event
- notification and chat test data (optional but recommended)

---

## 3. Quick narrative (talk track)

Use this short opening:

> "Intoto Admin is the **platform operator** — above any single university.  
> From one dashboard they see every tenant, onboard new schools, and manage users everywhere on Intoto.  
> When they need to focus on one institution, they pick a university — but they never lose the global view."

---

## 4. Step-by-step demo flow

## Step 1 — Login and platform context (1–2 min)

**What to do**
1. Login with Intoto Admin credentials.
2. Show role tag **Intoto Admin** and platform app bar (Intoto branding).

**What to say**
- "This role is not tied to one university — it runs the whole platform."
- "University Super Admins manage one school; Intoto Admin manages all of them."

---

## Step 2 — Platform dashboard overview (2 min)

**What to do**
1. Scroll through Home — Quick Way, Quick Actions, banners, event carousels.
2. Pull to refresh once.

**What to say**
- "The dashboard is API-driven — only what this role needs appears."
- "Counts are live; pull to refresh after any change."

---

## Step 3 — University management (3–4 min)

**What to do**
1. Tap **Total Universities** (or **Manage Universities**).
2. Open one university → **University Details** (campuses, status, metrics).
3. Return to dashboard → tap **Add University** (show form fields; submit only if safe in demo env).

**What to say**
- "Every institution on Intoto is listed here — search, filter, open details."
- "Adding a university is the first step in onboarding a new client."
- "Suspend or activate controls tenant access at the platform level."

---

## Step 4 — University context switching (1–2 min)

**What to do**
1. Use **university picker** in header or filter on a list.
2. Select University A → show scoped counts or list.
3. Clear or select **All Universities** → return to global view.

**What to say**
- "Admins can zoom into one tenant without switching accounts."
- "Filters and lists respect the selected university until you change it."

---

## Step 5 — Cross-tenant user management (3–4 min)

**What to do**
1. Tap **Manage User**.
2. Show status chips — **Invited**, **Accepted**, **Suspended**.
3. Open **Filter** → apply **University** + **Role**.
4. Open one user → show available actions (resend, suspend, email).
5. Tap **Add User** → invite **University Super Admin** for a university (no campus).

**What to say**
- "One place to manage invitations and accounts across every school."
- "University Super Admin invite requires university — not campus."
- "Bulk email works from multi-select on the list."

---

## Step 6 — Global student directory (2 min)

**What to do**
1. Tap **Total Students**.
2. Search for a student.
3. Filter by **University**.
4. Open one **Student Profile Hub**.

**What to say**
- "Platform-wide student lookup with tenant scoping."
- "Oversight and support — day-to-day assignment stays with university ops."

---

## Step 7 — Reports and moderation (1–2 min)

**What to do**
1. Tap **Total Reports**.
2. Open one report.
3. Change status (e.g. **Under Review** → **Resolved**).

**What to say**
- "Moderation queue spans all universities."
- "Filter by university when triaging at scale."

---

## Step 8 — Communication (1 min)

**What to do**
1. Tap **Chats** tab → show one thread.
2. Return Home → tap **bell** for notifications.

**What to say**
- "Direct messaging and alerts work the same platform-wide."

---

## Step 9 — Profile and settings (1 min)

**What to do**
1. **Profile** tab → Settings.
2. Show Configuration / Notification / Language (if configured).
3. Mention **Save** on nav bar when values change.

**What to say**
- "Admin preferences are staged and saved explicitly — not on every toggle."

---

## Step 10 — Close (30 sec)

**What to say**
- "Intoto Admin is the control plane: tenants, users, and platform health in one app."
- "University teams run day-to-day operations; Intoto Admin scales the platform."

---

## 5. Optional deep dives (if time allows)

| Topic | Show |
|-------|------|
| Events | Total Events → filter by university → Event Details |
| Communities | Pending Communities → approve one request |
| Coordinators | Event Coordinator stat → filter by university |
| Travel | Total Travel Plans → tenant filter |

---

## 6. Demo pitfalls to avoid

- Do not demo **assign students to sub-coordinator** — that is University Super Admin / coordinator flow.
- Do not confuse **Intoto Admin** with **University Super Admin** — different scope and dashboard.
- If **Add University** submit is risky in prod, walk the form only and say "submits in staging."
- Confirm university picker state before student/report demos — wrong tenant confuses the narrative.

---

## 7. Figma alignment note

Walk the [Intoto Admin prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5051%3A661) before the demo and confirm:

- Quick Action labels match live app (Manage Universities, Add University, etc.)
- University picker placement matches build
- Filter sidebar includes **University** on Manage Users

---

*Design reference: [Figma — Intoto Admin node 5051-661](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)*
