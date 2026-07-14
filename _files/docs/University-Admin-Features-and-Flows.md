# Intoto — University Admin
## Features & Flows (User Guide)

**Design reference:** [INTOTO WebApp — University Super Admin (node 81-7360)](https://www.figma.com/design/hNVFYMIiLyFZJKD8khkn4Q/INTOTO-WebApp?node-id=81-7360&p=f&m=dev)  
**Prototype (walkthrough):** [INTOTO WebApp — Dashboard (546-1397)](https://www.figma.com/design/hNVFYMIiLyFZJKD8khkn4Q/INTOTO-WebApp?node-id=546-1397&page-id=81%3A7360)  
**Role:** University Admin (INTOTO WebApp — browser)  
**Audience:** Product, Engineering, QA, Client demos  
**Version:** 1.0  
**Last updated:** Jun 2026

---

## About this document

This guide explains **what a University Admin can do in the INTOTO WebApp**, **why each feature exists**, and **exactly how to use it** — step by step. It follows the same structure as the Student, University Super Admin, Event Coordinator, Community Coordinator, and Ambassador Platform documentation.

**Note on Figma:** The [University Admin frames](https://www.figma.com/design/hNVFYMIiLyFZJKD8khkn4Q/INTOTO-WebApp?node-id=81-7360&p=f&m=dev) live on page **81:7360** (*UNIVERSITY SUPER ADMIN*) in file `INTOTO-WebApp`. Walk each connected frame and compare labels, spacing, empty states, and actions to this document. Content reflects the **web admin portal** scope and is **not** derived from application source code.

**Important:** This is the **web admin portal** (desktop browser). For the **mobile app** University Super Admin role, see `University-Super-Admin-Features-and-Flows.md`.

---

## 1. Who is the University Admin?

### What this role is

The **University Admin** is the highest operational administrator **within one university** on the **INTOTO WebApp**. They manage users, campuses, communities, events, travel, ambassadors, profile reviews, configurations, and university profile content — all scoped to their institution.

The Figma page is titled *UNIVERSITY SUPER ADMIN*; the header shows role **University Admin** (e.g. *Rakesh Kumar*).

They do **not** manage other universities (that is Intoto Admin).

### What they typically do day to day

- Monitor **Dashboard** metrics and charts
- **Manage Users** — invite, approve, suspend, filter by role/campus
- Review **Profile Review** queue (complete / incomplete / pending)
- Configure **My University** (overview, programs, admission, onboarding, roles, features)
- Manage **Campus** list and campus detail (students, programs, faculty, travel)
- Moderate **Community** (active, pending requests, reports)
- Oversee **Travel Plans** and travel detail by status
- Manage **Internal** and **External Ambassadors** and lead detail
- Create and approve **Events**; mark attendance and collect feedback
- Use **Chat**, **Invite Data**, **Manage Ads**, **Configurations**, **Support**

### How this role differs from others

| Topic | University Admin (WebApp) | University Super Admin (mobile) | Intoto Admin |
|-------|---------------------------|----------------------------------|--------------|
| Surface | Browser — 1920px desktop | iOS/Android native app | Browser — cross-tenant |
| Navigation | Left sidebar (12 modules) | Bottom tabs: Home, Community, Chats, Profile | Platform dashboard |
| Scope | One university | One university | All universities |
| Campus management | Full Campus module | Via university details | Tenant-level |
| Profile Review queue | Dedicated sidebar module | Student lists / profile flows | N/A |

---

## 2. Getting into the app

### Feature: Login

**What the user does:** Opens the WebApp and authenticates via Intoto's identity provider.

**How to do it:**
1. Open the INTOTO WebApp URL.
2. On **Login or Sign-up**, read *By continuing you agree to Intoto's Conditions of Use and Privacy Notice.*
3. Tap **Continue**.
4. Complete sign-in on the external authentication provider (*You will be redirected to our authentication provider.*).

**What happens next:** If the user has only the University Admin role, they land on **Dashboard**. If they have multiple roles, **Role** selection appears first. Unverified signups may see **Email Verification Required!** before continuing.

**Figma frames:** `Login` (1913:58209), `Signup` (1913:58211), `Email Verification Required!` (1913:58295)

---

### Feature: Role selection (multiple roles only)

**What it is:** Lets one person switch between roles assigned to their account before entering the admin portal.

**When the user needs it:** They hold more than one role (e.g. University Admin + Campus Admin).

**How to do it:**
1. On first login, choose the admin context from the **Role** picker (`Role` — 556:4088), **or**
2. Use **Dasboard role change** from the dashboard when switching context.

**What happens next:** Dashboard counts and sidebar modules reload for the selected role.

**Roles available in Manage Users / filters include:** University Super Admin, Campus Admin, Student, Ambassador, Event Coordinator, Community Coordinator, Third Party Coordinator, Social Media Coordinator.

---

### Feature: Sidebar navigation (main app areas)

**What it is:** Primary navigation — a fixed left sidebar with university logo and module links.

| Menu item | What the user does here |
|-----------|-------------------------|
| **Dashboard** | Stat cards, charts, admissions and travel widgets |
| **Admission Portal** | Admissions pipeline (sidebar variant) |
| **Manage User** | User directory, invites, approve/reject |
| **Invite Data** | Bulk invitation data import/tracking |
| **Profile Review** | Student profile completion queue |
| **Manage Ads** | Promotional banners |
| **My University** | University profile, programs, admission, onboarding |
| **Campus** | Campus list and per-campus detail |
| **Community** | Active communities, pending requests, reports |
| **Chat** | Staff messaging and group creation |
| **Configurations** | University settings and feature flags |
| **Support** | Help desk / tickets |
| **Log Out** | End session (footer) |

**How to use it:** Click any item. The active item is highlighted in blue (`#2563EB`) with white bold text.

**Figma frame:** `Sidebar/Default` — 2412:31468

---

### Feature: Top header

**What it is:** Global bar on every screen — greeting, language, notifications, and user profile.

**How to use it:**
1. Read date (e.g. **13 Aug, 2025**) and **Welcome !** on the left.
2. Change language via **Eng (US)** dropdown if needed.
3. Tap the notification bell (badge e.g. **21**) for alerts.
4. Tap the profile block — name (e.g. **Rakesh Kumar**), role **University Admin** — for **Profile popup** shortcuts (2427:160637).

---

### Feature: Date range filter

**What it is:** Shared filter on Dashboard, Manage Users, Profile Review, and list screens.

**How to do it:**
1. Open period dropdown — **All** or **Custom**.
2. Set **From Date** and **To Date** (calendar icons).
3. Tap the apply/download button to refresh data.

**Select week** popup (`614:6249`) offers quick week selection on the dashboard.

---

## 3. Dashboard — Overview

### What it is

The **Dashboard** is the University Admin control panel after login. It shows live stat cards, analytics charts, and right-column widgets — all scoped to the university.

**How to open it:** Click **Dashboard** in the sidebar (default after login).

**Figma frame:** `Dasboard` — 546:1397

---

### Feature: Dashboard Overview — stat cards

**What it is:** Two rows of count cards; each card opens the related list or module.

**Row 1:**

| Card | Example count |
|------|---------------|
| **Communities** | 1k |
| **Travel Plans** | 754 |
| **Events** | 643 |
| **Ambassadors** | 24 |
| **Students** | 24k |

**Row 2:**

| Card | Example count |
|------|---------------|
| **External Ambassadors** | 542 |
| **Event Coordinators** | 5 |
| **Third-Party Coordinators** | 10 |
| **Community Coordinators** | 2 |
| **University Super Admin** | 4 |

**How to use it:**
1. Scan **Dashboard Overview** for operational health.
2. Click any card → navigates to the filtered list behind that metric.
3. Adjust the date filter to change widget ranges.

---

### Feature: Right-column widgets

| Widget | Content |
|--------|---------|
| **Student Admission** | Bar chart by intake term; **Total Students: 64737**; Fall/Summer/Spring 2025 |
| **Student Travel Plan** | Donut chart (e.g. center **12,450**); legend |
| **Massage** *(Figma label)* | **Total Massages: 64737**; progress bars (e.g. 20%, 30%) |

Each widget has a download/expand icon.

---

### Feature: Student's Location chart

**What it is:** Donut chart of student distribution by country.

**How to use it:**
1. Read subtitle **Total Student: 64737**.
2. Hover a segment (e.g. **India** — 3200, 30%) for tooltip detail.
3. Use the legend below for country + percentage rows.

---

### Feature: Community analytics

**What it is:** Member and community-creation breakdown on the dashboard.

**How to use it:** Review **Total Members: 64737** and **Community Created** chart segments. **Total Domestic** appears in related location breakdown.

---

## 4. Manage User

### What it is

Central directory for all university users — staff, coordinators, students, ambassadors.

**How to open it:** Sidebar → **Manage User**.

**Figma frame:** `Manage Users` — 629:4355

---

### Feature: User table

**What the user sees:**

| Column | Content |
|--------|---------|
| Checkbox | Row / bulk selection |
| **Name** | Avatar, name, email |
| **Role** | University Super Admin, Student, Ambassador, Campus Admin, Event Coordinator, etc. |
| **Campus** | Main Campus, University of Texas at… |
| **Locality** | Domestic, International, — |
| **Expires Date** | e.g. Aug 10, 2028 |
| **Status** | Accepted, Invited, Withdrawn, Suspended, Reject, Submitted |
| **Action** | ⋮ menu |

**Toolbar:** **Select All**, **Total Users: N**, **Add Users**, **Search students...**, column grid, filter, refresh. Pagination: **Showing 1–10**, page numbers.

**How to use it:**
1. Search or open **Filter** (2391:24947) → apply role, campus, status.
2. Row ⋮ → **Approve**, **Reject**, or **Download**.
3. **Select All** for bulk actions when available.

---

### Feature: Add Users

**What it is:** Invite flow for any university role.

**How to do it:**
1. Tap **Add Users**.
2. Select **Role** and **Campus** (if applicable).
3. Fill invite fields → submit.
4. New row appears with status **Invited**; user moves to **Accepted** after accepting.

**Figma frames:** `Add New User` — 635:16243, 700:8433, 700:9849

**Bulk paths:** **Invite Data** (700:10908), **Bulk Data** (738:1570)

---

## 5. Profile Review

### What it is

Queue for reviewing student profile completion before full platform access.

**How to open it:** Sidebar → **Profile Review**.

**Figma frame:** `Profile Review` — 2169:16374

---

### Feature: Summary cards

| Card | Example |
|------|---------|
| **Total Students** | 10k |
| **Complete** | 8k |
| **Incomplete** | 2k |
| **Action Required** | 500 |
| **Pending Review** | 7k |
| **Reject** | (count) |

**How to use it:**
1. Scan cards for backlog size.
2. Click **Pending Review** (or similar) to filter the list.
3. Open a student row → review profile → approve or reject.
4. Counts update on **Complete** / **Reject** cards.

---

## 6. My University

### What it is

University marketing and configuration content — what students see during onboarding.

**How to open it:** Sidebar → **My University**.

**Figma frame:** `My University Overview` — 702:12369

---

### Feature: Tab navigation

| Tab | Purpose |
|-----|---------|
| **Overview** | About, contact, social, address, rankings, accreditation, brand color |
| **Programs & Services** | Academic and service catalog |
| **Admission Information** | Admissions copy and requirements |
| **Onboarding Setup** | Student onboarding steps |
| **Role Management** | Role definitions for the university |
| **Features** | Paid Intoto modules — see [§ Features (paid modules)](#features-paid-modules) below |

---

## Features (paid modules)

Intoto is sold as **standalone paid features**, not as a single all-or-nothing platform license. A university can subscribe to **one module, several, or all six**, and can **add modules at any time** as its needs grow.

**How to open it:** Sidebar → **My University** → **Features** tab.

Each module appears as its own card with a description, an **Active** badge, and subscription **Start Date** / **End Date**. The University Admin does **not** turn modules on or off from this screen — Intoto provisions subscriptions during commercial onboarding. This tab is the source of truth for what the web portal and mobile app expose.

### On every Features card

| Field | Meaning |
|-------|---------|
| **Title & description** | Commercial module name and one-line summary |
| **Active** | Module is currently entitled — related tools are available |
| **Start Date / End Date** | Subscription window (e.g. Jul 13, 2025 – Jul 13, 2026) |

---

### Feature: Ambassador Management

**Card copy:** Connect students with ambassadors.

**What it is:** Structured ambassador program — internal in-app mentors and external partner ambassadors.

**When Active — admin can:**
- Dashboard **Ambassadors** and **External Ambassadors** cards
- Sidebar ambassador directories and ambassador detail (overview, communication, documents, activity)
- Invite ambassador roles from Manage User

**When inactive:** Ambassador sidebar entries hidden; no ambassador invites; students do not see ambassador discovery.

---

### Feature: Travel Plan

**Card copy:** Manage student travel arrangements.

**What it is:** Student travel itineraries, arrival status, and coordinator visibility (arriving, in transit, on campus).

**When Active — admin can:**
- Dashboard **Travel Plans** card
- Sidebar **Travel Plan** module and travel detail by status
- Campus → **Travel Plans** tab

**When inactive:** Travel sidebar and dashboard card hidden; no travel lists or campus travel tab.

---

### Feature: Community

**Card copy:** Student connections & groups.

**What it is:** Student-led and official communities — creation requests, feeds, posts, moderation, and reports.

**When Active — admin can:**
- Sidebar **Community** (pending requests, active communities, reports)
- Approve or deny student-created communities
- Dashboard community analytics

**When inactive:** Community module hidden; students cannot create or join communities.

---

### Feature: Chat

**Card copy:** Direct messaging between users.

**What it is:** One-to-one and group messaging between students, ambassadors, coordinators, and staff.

**When Active — admin can:**
- Sidebar **Chat** and create group chat on web
- Message any user; bulk outreach where mail is enabled

**When inactive:** Chat sidebar hidden; no direct messaging in the product.

---

### Feature: Event Management

**Card copy:** Create and manage campus events.

**What it is:** Event lifecycle — draft, approval, publish, registration, attendance, feedback.

**When Active — admin can:**
- Dashboard **Events** card
- Sidebar events module — create, pending, published flows
- Mark attendance and collect feedback

**When inactive:** Events sidebar and dashboard card hidden; no event creation or registration.

---

### Feature: User Management

**Card copy:** Control user limits & invitations.

**What it is:** Licensed seat pool for the tenant — caps how many users can be invited across all roles, with optional domestic vs international split.

**Features card fields (example):**

| Field | Example |
|-------|---------|
| **Total Capacity** | 5,000 |
| **Utilization** | 20% · 1,000 Invited |
| **Domestic users** | 501 of 4,001 limit |
| **International users** | 499 of 4,001 limit |

**When Active — admin can:**
- Sidebar **Manage User**, **Invite Data**, **Profile Review**
- **Add User** / bulk invite (within remaining capacity)
- Dashboard people stat cards

**When inactive:** User invitation and directory tools unavailable.

---

**Modular subscriptions:** A university might run only **User Management** and **Chat** in year one, then add **Travel Plan** and **Ambassador Management** before the next intake. Each new module appears on the Features tab with its own dates once Intoto provisions it.

---

### Feature: Overview tab

**Banner:** Photo, logo, name (e.g. **Texas University**), **College Station, Texas**, **Established Year: 1975**, **Export** button.

**Editable sections** (pencil icon): **About**, **Contact Details** (phone, email, website), **Social Media**, **Address** + **View on Map**, **Ranking**, **Accreditation**, **Interface Design** (e.g. **#0085DB**).

**How to update:**
1. Choose the relevant tab.
2. Tap **Edit** on a section → save changes.
3. Tap **Export** on the banner for a data snapshot.

---

## 7. Campus

### Feature: Campus List

**How to open it:** Sidebar → **Campus**.

**What the user does:** Browse campuses, select rows, search, delete with confirmation (`Delete campus` → `delete succesfull`).

**Figma frame:** `Campus List` — 645:20514

---

### Feature: Add New Campus

**How to do it:**
1. Open **Add New Campus** (empty: 2401:127889; filled: 645:21695).
2. Complete required fields → submit.
3. See **Campus Created Successfully!** (2412:30718) → return to list.

---

### Feature: Campus detail tabs

| Tab | Purpose |
|-----|---------|
| **Campus Overview** | Summary metrics |
| **Campus Students** | Roster |
| **Campus Courses / Programs** | Programs |
| **Campus Faculty** | Faculty list |
| **Campus Travel Plans** | Travel per campus |

---

## 8. Community

### What it is

Moderation and management of student communities and reports.

**How to open it:** Sidebar → **Community**.

---

### Feature: Pending Requests

**How to do it:**
1. Open **Pending Requests** (2414:48295).
2. Review each request → approve or deny.
3. Approved communities move to **Active Communities** (2414:47600).

---

### Feature: Community feed and posts

**How to do it:**
1. Open an active community → **Community Feed** (1250:33698).
2. **Create post** — text, image, video, or document variants (1204:*, 1205:*).
3. Open **post detail**; use **share to** when needed.

---

### Feature: Reports

**How to do it:**
1. Open **Reports** (2414:49792).
2. Triage by status: Pending, Assigned, Under review, resolved.
3. Open **Report Detail** → assign or resolve.

**Figma frames:** 804:16962, 2418:33622, 2418:34078, 805:18504

---

## 9. Travel Plan

### What it is

Visibility into student travel itineraries by status.

**How to open it:** Dashboard **Travel Plans** card or travel module.

**Figma frame:** `Travel Plan` — 805:19572

**Detail screens:** Upcoming (2418:49008), Ongoing (2418:49704), Completed (2418:50315), Cancelled (2418:50926)

**How to use it:** Open list → filter/search → open row for status-specific detail.

---

## 10. Ambassadors

### Feature: Internal Ambassadors

**How to open it:** Dashboard **Ambassadors** card or `Internal Ambassadors` list (844:2091).

---

### Feature: External Ambassadors

**How to open it:** Dashboard **External Ambassadors** card or `External Ambassador` (918:2469).

---

### Feature: Ambassador Detail and leads

**How to do it:**
1. Open **Ambassador Detail** (846:4607).
2. For recruitment leads, use tabs: **Overview**, **Communication**, **Document**, **Activity Log** (852:11873, 936:7099, 853:14572, 852:10384).

---

## 11. Events

### What it is

Full event lifecycle — create, approve, publish, register, attend, feedback.

**Figma frames:** `Events` (1739:113157), `My Events` (1739:113619), `Create Event` (1739:106593+)

**How to create and run an event:**
1. **Create Event** → fill form → submit or save **Draft Event**.
2. **Assign Co-ordinator** if required (1739:108817).
3. Approve → **Published Event Detail**; reject → **Rejected Event Detail**.
4. Students **Register Event** → **Registration list** / **Attendees list**.
5. Event day → **Mark Present** → **Attendance Marked** → **Feedback**.

---

## 12. Chat

### Feature: Create group

**How to do it:**
1. Sidebar → **Chat**.
2. **Create Group** → select members (1183:32563) → name group (1183:33381) → confirm (`created group` — 1183:34176).

---

## 13. Invite Data, Manage Ads, Configurations, Support

| Module | Purpose | Figma |
|--------|---------|-------|
| **Invite Data** | Bulk invitation tracking | 700:10908 |
| **Manage Ads** | Promotional banners | Sidebar variant |
| **Configurations** | University settings | 1131:56999+ |
| **Support** | Help desk tickets | 964:12603 |

---

## 14. Profile and logout

| Screen | Frame |
|--------|-------|
| Profile | 728:7344 |
| Profile faq | 728:13044 |
| Profile setting | 728:13713 |
| Logout | 553:2942 |

**How to log out:** Sidebar → **Log Out** → confirm **Logout** → **Login** screen.

---

## 15. End-to-end playbooks

### Flow A — Invite an Event Coordinator

1. **Login** → **Continue** → auth provider.
2. **Manage User** → **Add Users** → role **Event Coordinator** + campus.
3. Submit → **Invited** → user accepts → **Accepted**.

### Flow B — Clear profile review backlog

1. **Profile Review** → click **Pending Review** card.
2. Open student → approve or reject.
3. Verify **Complete** / **Reject** counts update.

### Flow C — Approve a pending community

1. **Community** → **Pending Requests** → approve.
2. Verify in **Active Communities** → monitor **Community Feed**.

### Flow D — Publish an event

1. **Create Event** → submit → **Pending Event Detail**.
2. Approve → **Published Event Detail**.
3. After event → **Mark Present** → **Feedback**.

---

## 16. Figma validation checklist

- [ ] Login — Continue, Conditions of Use, Privacy Notice, auth redirect
- [ ] Sidebar — all 12 modules + Log Out; active blue state
- [ ] Header — Welcome, date, language, notifications, University Admin role
- [ ] Dashboard Overview — 10 stat cards
- [ ] Widgets — Student Admission, Student Travel Plan, Student's Location
- [ ] Manage Users — columns, statuses, Add Users, ⋮ actions
- [ ] Profile Review — 6 summary cards
- [ ] My University — 6 tabs, Overview edit, Export
- [ ] Campus — list, add, delete, detail tabs
- [ ] Community — pending, active, feed, reports
- [ ] Travel — list + four detail statuses
- [ ] Ambassadors — internal, external, lead tabs
- [ ] Events — create through feedback
- [ ] Logout confirmation

---

## 17. Related documentation

| Document | Scope |
|----------|-------|
| `University-Admin-Client-Demo-Guide.md` | Client demo script |
| `University-Admin-QA-Test-Guide.md` | QA test suites |
| `University-Super-Admin-Features-and-Flows.md` | Mobile app (same university scope) |
| `Intoto-Admin-Features-and-Flows.md` | Platform admin (cross-university) |

---

## Document history

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | Jun 2026 | Initial guide from INTOTO WebApp Figma 81:7360 |

*Design: [INTOTO WebApp — 81:7360](https://www.figma.com/design/hNVFYMIiLyFZJKD8khkn4Q/INTOTO-WebApp?node-id=81-7360&p=f&m=dev)*
