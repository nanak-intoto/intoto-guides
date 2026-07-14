# Intoto — Intoto Admin
## Features & Flows (User Guide)

**Design reference:** [Intoto Wireframe — Intoto Admin (node 5051-661)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)  
**Prototype (walkthrough):** [Intoto Wireframe — Intoto Admin prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5051%3A661)  
**Role:** Intoto Admin (`intoto_admin`)  
**Audience:** Product, Engineering, QA, Client demos  
**Version:** 1.0  
**Last updated:** Jun 2026

---

## About this document

This guide explains **what an Intoto Admin can do in Intoto**, **why each feature exists**, and **exactly how to use it** — step by step. It follows the same structure as the University Super Admin, Event Coordinator, Community Coordinator, Student, Ambassador, and Third Party Coordinator guides.

**Note on Figma:** The [Intoto Admin prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5051%3A661) is on page **5051:661** (page title: **Intoto Admin**). Walk every connected frame from starting node **5051-661** and compare labels, empty states, and actions to this document. Content reflects the **Intoto Admin wireframe scope** (platform governance, cross-university oversight, tenant onboarding) and is **not** derived from application source code.

---

## 1. Who is the Intoto Admin?

### What this role is

The **Intoto Admin** is the **platform-level administrator** for Intoto. They operate **across all universities (tenants)** on the platform — not within a single institution like a University Super Admin.

They onboard and manage universities, invite top-level university administrators, monitor platform-wide health metrics, and govern users, communities, events, and reports at a **cross-tenant** level when the wireframe configures those capabilities.

### What they typically do day to day

- Open **Home** and review **platform Quick Way** counts (universities, campuses, students, invites, reports)
- **Add** or **manage universities** — branding, status, initial Super Admin invite
- **Switch university context** (picker in header or filters) to drill into one tenant
- **Manage users** across tenants — invite, suspend, resend, withdraw
- **Invite University Super Admins** for specific universities
- Browse **global directories** (students, coordinators, ambassadors, communities, events)
- Triage **reports** and notifications that span the platform
- Use **Chats** and **Support** for escalations

### How this role differs from others

| Topic | Intoto Admin | University Super Admin | Event / Community Coordinator |
|-------|--------------|------------------------|------------------------------|
| Scope | **All universities** on Intoto | **One university** | One university (narrow domain) |
| Manages universities / tenants | **Yes (primary)** | No | No |
| University picker / filter | **Yes** | No (fixed to own uni) | No |
| Manage Users / invites | Yes (cross-tenant) | Yes (single-tenant) | No (typical) |
| Assign students to sub-coordinators | No (university ops) | Yes | No |
| Approve pending communities / events | Oversight / global view | Yes (primary for one uni) | Domain-specific approval |
| Dashboard branding | **Intoto** and/or selected university | University logo + name | University logo + name |

---

## 2. Getting into the app

### Feature: Login

**What the user does:** Signs in with Intoto platform credentials.

**How to do it:**
1. Open the Intoto app.
2. Enter email/password or use configured SSO.
3. Wait for profile and role to load.

**What happens next:**
- **Single role (Intoto Admin only):** Lands on **Home** (Intoto Admin platform dashboard).
- **Multiple roles:** **Role Selection** — choose **Intoto Admin**.
- **Pending invitations:** Alert at login — **Accept** or **Do it later** (envelope icon on Home later).

---

### Feature: Role selection (multiple roles only)

**What it is:** One account may also hold University Super Admin, Coordinator, or other roles. Role selection switches dashboard configuration and permissions.

**How to do it:**
1. On login, pick **Intoto Admin**, **or**
2. From Home, tap the **role switcher** row (role chip with chevron), **or**
3. **Profile** tab → switch role.

**What happens next:** Home reloads with platform-admin sections — university management shortcuts, cross-tenant Quick Way cards, and global filters — not a single-university-only view.

---

### Feature: Bottom navigation

| Tab | What the Intoto Admin does here |
|-----|----------------------------------|
| **Home** | Platform dashboard — stats, shortcuts, events, banners, analytics |
| **Community** | Browse communities (global or university-scoped per wireframe) |
| **Chats** | Message users across the platform |
| **Profile** | Own profile, settings, logout |

**How to use it:** Tap any tab icon. The selected tab is highlighted.

---

## 3. Home — Intoto Admin Dashboard

### What it is

**Home** is an **API-driven overview dashboard** for the Intoto Admin role. The backend returns an ordered list of sections: custom app bar, role tag, Quick Way stat cards, Quick Actions, event carousels, promotional content, and analytics visuals. Only configured sections render.

**How to open it:** Tap **Home** (default after login as Intoto Admin).

**How to refresh:** Pull down on Home. Counts, carousels, and chart data reload from the server.

---

### Feature: Platform app bar (Intoto branding + context)

**What it is:** A custom top bar distinct from university-scoped roles. Per wireframe, the leading area shows **Intoto branding** and/or the **currently selected university** when the admin is drilling into one tenant.

**Why it matters:** The admin always knows whether they are in **platform-wide** context or focused on **one university**.

**How to use it:**
1. Read the leading block — Intoto logo/name and/or selected university.
2. **Tap** the university block (when shown) → **University picker** or **University Details**.
3. **Bell** (top-right) → **Notifications**.
4. **Envelope** (when shown) → **Pending Invitations**.

**Logo missing:** Layout adjusts so text remains readable without a broken empty image area.

---

### Feature: Role tag

**What it is:** A colored badge showing **“Intoto Admin”**.

**Why it matters:** Confirms platform-admin context, especially when the account has multiple roles.

**How to use it:** Read-only indicator. Tap role switcher (when available) to change role.

---

### Feature: University context switcher (Admin-specific)

**What it is:** A control — in the app bar, filter defaults, or a dedicated picker — that lets the admin **focus on one university** or return to **all universities**.

**When the user needs it:** Reviewing one tenant’s students, inviting a Super Admin for a specific university, or auditing a single institution.

**How to do it:**
1. Tap the **university name** or **“All Universities”** chip in the header (per wireframe).
2. Search or scroll the university list.
3. Select a university → lists and some dashboard counts **scope to that tenant**.
4. Select **All Universities** (or clear selection) → return to platform-wide view.

**What happens next:** Quick Way counts and list screens respect the selected university context until changed.

---

## 4. Quick Way — stat cards

### What it is

**Quick Way** is a grid of cards on the dashboard. Each card shows an icon, a **number** (count from the server), and a **label** (e.g. “Total Universities”).

**Why it matters:** Gives at-a-glance **platform health** — how many tenants, students, pending invites, reports, etc.

**How to use it:**
1. Scroll to **“Quick Way”** on Home.
2. **Tap any card** to open the full list or screen behind that number.
3. Pull to refresh on Home after changes elsewhere.

Below, each typical Intoto Admin card is described. Validate exact labels and presence against the [Figma Admin frames](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0).

---

### Total Universities

**What it means:** Number of universities (tenants) on the Intoto platform — active, pending, and suspended per backend rules.

**What the user does:** Reviews all tenants and opens university details.

**How to do it:**
1. Tap **Total Universities** on the dashboard.
2. Browse the **University List** — search by name, filter by status if available.
3. Tap a row → **University Details** (overview, campuses, configuration summary).

---

### Total Campuses

**What it means:** All campuses **across all universities** (or scoped to selected university if context is set).

**What the user does:** Audits campus footprint platform-wide.

**How to do it:**
1. Tap **Total Campuses**.
2. Browse campus list — each row typically shows **university name** + campus name.
3. Tap a campus → **Campus Details** (read-only overview).

---

### Total Students

**What it means:** All students registered on the platform (or within selected university context).

**What the user does:** Global student directory — search, filter, open profiles, bulk email.

**How to do it:**
1. Tap **Total Students**.
2. Type in **search** (at least 3 characters).
3. Tap **Filter** → narrow by **University**, Campus, Country, Program, etc. (see [Section 18 — Filters](#18-filters--how-to-narrow-any-list)).
4. Tap a **student row** → **Student Profile Hub**.
5. For bulk outreach: selection mode → select rows → **Take Action** → **Send email**.

---

### Total Invites

**What it means:** Pending invitations platform-wide (users not yet accepted).

**What the user does:** Monitors onboarding pipeline across tenants.

**How to do it:**
1. Tap **Total Invites** (or open **Manage Users** → **Invited**).
2. Filter by **University** and **Role** as needed.
3. Tap a row → resend, withdraw, or email.

---

### University Super Admins

**What it means:** Count of **University Super Admin** users across the platform (top admin per university).

**What the user does:** Directory of institutional leads — audit who runs each tenant.

**How to do it:**
1. Tap the **University Super Admin** stat card.
2. Search or filter by university.
3. Tap a row → **User Profile** (read-only browse).

---

### Total Communities / Community Members

**What it means:** All communities (or total membership) platform-wide.

**What the user does:** Cross-tenant community oversight.

**How to do it:**
1. Tap the community stat card.
2. Filter by university if needed.
3. Tap a community → **Community Profile** and feeds.

---

### Pending Communities

**What it means:** Communities awaiting approval across tenants.

**What the user does:** Platform-level review of pending community requests (when wireframe grants this to Admin).

**How to do it:**
1. Tap **Pending Communities**.
2. Filter by university.
3. Open request → review → **Approve** or **Reject** with reason.

---

### Total Events

**What it means:** All events on the platform.

**What the user does:** Opens global events catalog.

**How to do it:**
1. Tap **Total Events**.
2. Browse, search, filter by university/campus.
3. Tap an event → **Event Details**.

---

### Total Reports / Assigned Reports / My Assigned Reports

**What it means:** User-generated moderation reports — all platform reports, team workload, or reports assigned to this admin.

**What the user does:** Triages cross-tenant moderation cases.

**How to do it — all reports:**
1. Tap **Total Reports**.
2. Filter by university if needed.
3. Open a report → read context → update status: **Assigned → Under Review → Escalated → Resolved**.

**How to do it — personal queue:**
1. Tap **My Assigned Reports**.
2. Work cases assigned to you → set **Resolved** when done.

---

### Total Travel Plans

**What it means:** Student travel plan submissions platform-wide.

**What the user does:** Opens travel hub for volume and compliance oversight.

**How to do it:**
1. Tap **Total Travel Plans**.
2. Filter by university.
3. Browse submissions and drill into details.

---

### Coordinator directories (Event / Community / Third-Party)

**What it means:** Count of users in each coordinator role across the platform.

**What the user does:** Staffing overview — browse coordinator directories.

**How to do it:**
1. Tap the relevant coordinator stat card.
2. Filter by **University**.
3. Tap a person → **User Profile** (read-only).

---

### Total Ambassadors / External Ambassadors

**What it means:** Ambassador counts platform-wide.

**What the user does:** Opens ambassador directory for outreach oversight.

**How to do it:**
1. Tap the ambassador stat card.
2. Search, filter by university/campus.
3. Tap a row → profile or chat.

---

## 5. Quick Actions — shortcuts

### What it is

**Quick Actions** are large shortcut tiles below Quick Way — faster paths to common platform-admin tasks.

**How to use:** Tap any action tile on the dashboard.

---

### Manage Universities

**What the user does:** Opens the full **university / tenant management** list.

**How to do it:**
1. Tap **Manage Universities** on the dashboard.
2. You arrive on **University List** (see [Section 7](#7-university-management--tenants)).

---

### Add University

**What the user does:** Starts onboarding a **new university** onto Intoto.

**How to do it:**
1. Tap **Add University** on the dashboard.
2. Complete the create-university form (see [Add University — onboard a tenant](#add-university--onboard-a-tenant)).

---

### Manage User

**What the user does:** Opens cross-tenant invitation and user management.

**How to do it:**
1. Tap **Manage User**.
2. You arrive on **Manage Users** (see [Section 8](#8-manage-users--invite-and-control-accounts)).

---

### Add User

**What the user does:** Invites someone new — platform role or university-scoped role.

**How to do it:**
1. Tap **Add User**.
2. Complete the invite form (see [Add User — invite someone new](#add-user--invite-someone-new)).

---

### Events

**What the user does:** Opens the full events list directly.

**How to do it:** Tap **Events** → browse events (filter by university as needed).

---

### Support

**What the user does:** Accesses platform support resources.

**How to do it:** Tap **Support** → follow in-app support content or links.

---

## 6. Other dashboard content

### Banners

**What it is:** Promotional carousel (platform announcements, partner campaigns).

**How to use:**
1. Swipe horizontally through banners.
2. Tap **CTA** or banner → linked destination.

---

### Upcoming Events carousel

**What it is:** Preview of near-future events across tenants (or scoped university).

**How to use:**
1. Swipe through event cards.
2. Tap a card → **Event Details**.
3. Tap **View All** → full upcoming list.

---

### Pending Events (when shown)

**What it is:** Events awaiting approval.

**How to use:**
1. On each card, tap **Approve** or **Reject**.
2. For reject, enter reason.
3. Tap **View All** for full approval queue.

---

### Activities & Ads

**What it is:** Sponsored or informational cards.

**How to use:** Swipe and tap → opens URL or in-app destination.

---

### Analytics charts (when shown)

**What it is:** Platform or university analytics visuals (e.g. events by category, growth trends).

**How to use:** Scroll to chart section on Home → tap drill-down links if wireframe provides them.

---

## 7. University management — tenants

### What it is

**University management** is the **core Intoto Admin capability** — creating, viewing, editing, and controlling the lifecycle of universities on the platform. University Super Admins cannot do this; only platform admins can.

**How to open:**
- Dashboard → **Quick Action “Manage Universities”**, or
- Dashboard → **Total Universities** stat card, or
- App bar → university picker → **Manage all**.

---

### University List

**What the user sees:**
- Title and total count subtitle
- **Search bar**
- **Status filters** (if wireframe shows): All · Active · Pending · Suspended
- Scrollable list of universities (logo, name, status badge, optional counts)

**How to find a university:**
1. Type in **search** (name or identifier).
2. Tap a **status chip** to narrow the list.
3. Tap **Filter** if additional dimensions exist (region, plan tier, etc.).

**How to act on one university:**
1. Tap a row → **University Details**.

---

### University Details

**What the user sees (typical wireframe sections):**
- University **logo** and **name**
- **Status** (Active / Pending / Suspended)
- **Campus list** summary
- **Key metrics** (students, invites, communities — per wireframe)
- **Configuration summary** (domains, branding, feature flags — read-only or editable per design)
- **Actions:** Edit, Suspend, Activate, Invite Super Admin

**How to use it:**
1. Review institution overview.
2. Tap **Campuses** section → campus list for this university.
3. Tap **Edit** (if available) → update branding or metadata.
4. Tap **Invite Super Admin** → shortcut to **Add User** with university pre-selected.

---

### Add University — onboard a tenant

**What it is:** A form to register a new university on Intoto.

**How to open:** Dashboard → **Add University** quick action, or University List → **+** / **Add**.

**How to onboard step by step:**

1. **University name** — enter official institution name.
2. **Logo** — upload university logo (optional per wireframe).
3. **Identifier / domain** — enter tenant identifier used for routing and invites.
4. **Primary contact** — email or admin contact (if wireframe includes).
5. **Initial campus** — add at least one campus if required by form.
6. **Invite first University Super Admin** — optional checkbox: send invite to operational lead.
7. **Paid feature modules** — enable one or more of the six standalone modules (see **§ Paid features for universities** below and `Intoto Paid Features Guide.html`).
8. Tap **Submit** → success state → university appears in list (Pending or Active per rules).

**What happens next:**
- Success message → university appears in **University List** (status per wireframe: Pending or Active).
- If Super Admin invite was included, they appear under **Manage Users → Invited** for that university.

---

### Suspend / activate a university

**What it is:** Tenant-level control — suspending blocks new activity for that institution; activating restores access.

**When the user does this:** Contract ended, compliance hold, or re-onboarding after suspension.

**How to do it:**
1. Open **University Details**.
2. Tap **Suspend** (or **Activate** if currently suspended).
3. Confirm in the dialog.
4. Status badge updates; users at that university may see restricted access per product rules.

---

## 7A. Paid features for universities

Intoto sells **six standalone paid modules** to each tenant — not an all-or-nothing platform license. The **Intoto Admin** provisions modules during onboarding or when editing a university. The **University Super Admin** sees the result read-only on **My University → Features**.

**Full catalog:** `_files/Intoto Paid Features Guide.html` (standalone) · University view: `University-Admin-Features-and-Flows.md` → Features section.

### The six modules

| Module | Card copy | Intoto Admin provisions |
|--------|-----------|-------------------------|
| **Ambassador Management** | Connect students with ambassadors. | Ambassador rosters · discovery · Ambassador Platform |
| **Travel Plan** | Manage student travel arrangements. | Travel lists · arrival status · campus travel tab |
| **Community** | Student connections & groups. | Communities · pending · reports |
| **Chat** | Direct messaging between users. | Chat · groups · mobile Chats tab |
| **Event Management** | Create and manage campus events. | Event lifecycle · registration · attendance |
| **User Management** | Control user limits & invitations. | Manage User · Invite Data · Profile Review · seat limits |

### How to provision

1. Open **Add University** or **Edit University** / **University Details**.
2. Enable each module per the commercial agreement — set **Active**, **Start Date**, **End Date**.
3. For **User Management**, set **Total Capacity** and optional domestic/international limits.
4. Save — the tenant's portal and app expose only provisioned modules.
5. To add a module mid-contract, edit the university and enable it; it appears on the tenant's **Features** tab with its own dates.

### FAQs (Intoto Admin)

**Can a university buy only some features?**  
Yes — one, several, or all six; add more at any time.

**Who can the university admin change subscriptions?**  
They cannot. Only Intoto Admin provisions modules; the university sees read-only cards on **My University → Features**.

**What if a module is not provisioned?**  
Related admin sidebar entries and student experiences are hidden for that tenant.

---

## 8. Manage users — invite and control accounts

### What it is

**Manage Users** is where the Intoto Admin sees everyone invited to or active on the platform **across all universities** — and takes action on account status.

**How to open:**
- Dashboard → **Quick Action “Manage User”**, or
- **Total Invites** stat card, or
- Coordinator / Super Admin directory actions.

---

### Manage Users list

**What the user sees:**
- Title and **“Total Users: X”** subtitle
- **Status chips:** All · Invited · Accepted · Withdrawn · Rejected · Suspended
- **Search bar**
- **Filter button**
- Scrollable list (name, email, role, **university** column)

**How to find someone:**
1. Tap a **status chip** (e.g. **Invited**).
2. Type in **search** (name or email).
3. Tap **Filter** → choose **University**, **Campus**, and/or **Role** → **Apply**.

**How to act on one person:**
1. Tap their row → detail screen with available actions.

**How to act on many people:**
1. Enter selection mode.
2. Select multiple rows.
3. Tap **Take Action** → batch email or other bulk action.

| Their status | What you can do |
|--------------|-----------------|
| **Invited** | Withdraw invite, Resend invite, Send email |
| **Accepted** | Suspend account, Send email |
| **Suspended** | Re-initiate account, Send email |
| **Withdrawn / Rejected** | Resend invite, Send email |
| **All** filter | Send email only (when all statuses selected) |

---

### Add User — invite someone new

**What it is:** A form to send platform invitations by email — for any invitable role, scoped by university and campus where required.

**How to open:** Dashboard → **Add User** quick action.

**How to invite step by step:**

1. **Select Role** — Student, Coordinator, Ambassador, **University Super Admin**, etc.
2. **Select University** — **required** for all university-scoped roles and for **University Super Admin**.
3. **Enter email** — one email or bulk import.
4. **Select Campus** — required for Student, Coordinator, Ambassador, etc. **Not required** for **University Super Admin**.
5. **Ambassador Type** — only if role is Ambassador / External Ambassador.
6. **Profile visibility** — for non-student roles.
7. **Invite type** — for students.
8. **Expiry date** — when invitation expires.
9. Tap **Submit**.

**What happens next:** Person appears in **Manage Users → Invited**. They receive email to join.

**Examples:**

| I want to… | Role | University? | Campus? |
|------------|------|-------------|---------|
| Onboard a university’s top admin | University Super Admin | Yes | No |
| Invite a student at Tenant A | Student | Yes (Tenant A) | Yes |
| Invite event coordinator | Event Coordinator | Yes | Yes |
| Invite platform-only role (if configured) | Per wireframe | Per rules | Per rules |

---

## 9. Student lists and profiles (cross-tenant)

### All Students — global directory

**What the user does:** Finds any student on the platform, filters by university and attributes, opens profile, sends bulk messages.

**How to do it:** Same as **Total Students** Quick Way card.

**Student Profile Hub — what you see:**
- Personal and academic sections (API-driven)
- Travel and documents (if configured)
- **University** and **campus** context clearly labeled
- Actions available from profile (message, view sections — per wireframe)

**Note:** Intoto Admin typically has **read oversight** on student profiles. Day-to-day **assignment** of students to sub-coordinators is a **University Super Admin / coordinator** operation, not the primary Admin workflow.

---

### Assigned / Unassigned Students (when shown on Admin dashboard)

**What it means:** Operational assignment metrics — may appear on Admin dashboard for platform visibility.

**What the user does:** **Reviews** lists for volume and compliance. Assignment actions (if any on Admin wireframe) should be validated in Figma — default expectation is **browse and audit**, not coordinator-style assign flow.

**How to do it:**
1. Tap **Assigned Students** or **Unassigned Students** stat.
2. Filter by **University**.
3. Tap row → student profile or assignment status (read-only oversight).

---

## 10. Coordinator and staff directories

### University Super Admins

**What the user does:** Audits top administrators per university.

**How to do it:**
1. Open via **University Super Admin** Quick Way card.
2. Filter by university.
3. Tap row → **User Profile**.

### Event / Community / Third-party coordinators

**What the user does:** Platform-wide staffing directory.

**How to do it:**
1. Open matching stat card.
2. Filter by **University**.
3. Tap person → **User Profile** (read-only).

---

## 11. Community (platform view)

### Browse communities

**How to do it:**
- **Dashboard stat** → community list, **or**
- **Community tab** → Explore.

Filter by **University** when reviewing a specific tenant. Tap any community → profile, members, feed.

### Pending communities (when Admin approves)

**How to do it:**
1. Tap **Pending Communities**.
2. Filter by university.
3. Open request → **Approve** or **Reject** with reason.

### Create community (if wireframe allows Admin)

**How to do it:**
1. Community tab → **Create Community**.
2. Select **University** (required for Admin-created official communities).
3. Fill form → **Submit**.

Official admin-created communities may go live immediately (per wireframe parity with University Super Admin behavior).

---

## 12. Events (platform view)

### Browse all events

**How to do it:**
- **Events** quick action, **or**
- **Total Events** stat card.

Filter by university. Tap any event → **Event Details**.

### Upcoming events from Home

**How to do it:**
1. Scroll to **Upcoming Events** on dashboard.
2. Swipe cards; tap for details.
3. **View All** → complete list.

### Approve or reject events (when Pending Events section exists)

**How to do it:**
1. On **Pending Events** carousel → **Approve** or **Reject**.
2. Or **View All** → full approval queue.
3. Filter by university when triaging at scale.

---

## 13. Reports (moderation — cross-tenant)

### What it is

Reports are user flags about inappropriate content or behavior. Intoto Admin can triage across all universities.

### Work all reports

**How to do it:**
1. Tap **Total Reports**.
2. Filter by **University** if needed.
3. Open report → read context.
4. Update status: **Assigned → Under Review → Escalated → Resolved**.
5. Set **Resolved** when closed.

### My assigned reports

**How to do it:** Tap **My Assigned Reports** → personal queue → same status workflow.

---

## 14. Travel plans (platform view)

**What it is:** Overview of travel plan submissions across tenants.

**How to use:**
1. Tap **Total Travel Plans** or related quick action.
2. Filter by **University**.
3. Browse and drill into student travel records.

---

## 15. Chat

### What it is

Direct messaging with users across the platform.

**How to open:** Tap **Chats** in the bottom tab bar.

**How to use:**
1. See existing threads.
2. Tap thread → read → send message.
3. Start new conversation via search / user directory when available.

**Bulk email (from lists):**
1. On Manage Users or All Students → select multiple rows.
2. **Take Action** → **Send email**.

---

## 16. Profile and settings

**How to open:** Tap **Profile** in the bottom tab bar.

| Feature | What the user does | How |
|---------|-------------------|-----|
| **View / edit profile** | Update own admin profile | Tap sections on profile screen |
| **Settings** | App preferences | Profile → Settings |
| **Configuration** | Toggle app configuration options (if wireframe shows) | Settings → Configuration → edit → **Save** |
| **Notifications** | Notification preferences | Settings → Notification → edit → **Save** |
| **Language** | Change app language | Settings → Language → **Save** |
| **FAQs** | Help articles | Profile → FAQs |
| **About App** | Version info | Profile → About |
| **Logout** | Sign out | Profile → Logout → confirm |
| **Switch role** | Change to another assigned role | Profile or dashboard role switcher |

**Settings save pattern (wireframe):** Changes are staged in memory; nav bar **Save** appears when values differ from server; POST on Save tap.

---

## 17. Notifications and invitations

### Notifications

**How to do it:**
1. Tap **bell** on dashboard.
2. Scroll notification list.
3. Tap item → deep link to related screen when supported.

### Pending role invitations

**How to do it:**
1. On login alert: **Accept** or **Do it later**.
2. If deferred: **envelope** on dashboard header.
3. Tap envelope → **Pending Invitations** → accept or review.

---

## 18. Filters — how to narrow any list

### What it is

The **Filter** screen narrows long lists by **University**, Campus, Role, Country, Program, and more — depending on which list was opened.

**How to open:** On any list (Manage Users, All Students, University List, etc.) → tap **filter icon** next to search.

### How to apply filters — step by step

1. Tap **Filter** on the list screen.
2. On the **left sidebar**, tap a category (e.g. **University**, **Campus**, **Role**).
3. On the right, **Search** options (≥2 characters).
4. **Tap checkboxes** to multi-select.
5. Switch sidebar category to add more filters.
6. Tap **Apply** (bottom-right).
7. Or **Cancel** to discard, **Clear All** to reset.

### Filters on Manage Users (Intoto Admin)

**University**, **Campus**, and **Role** appear — the **University** dimension is the key difference from University Super Admin (who only sees Campus + Role within their fixed tenant).

### Special: Visit Schedule filter

When **Visit Schedule** is selected:
- Pick **Start date** and **End date**.
- Tap **Apply**.

---

## 19. Quick reference — permissions

| Can do | Cannot do (typical) |
|--------|---------------------|
| Manage all universities on the platform | Act as day-to-day sub-coordinator for arrival assignment |
| Add / suspend / activate universities | Replace University Super Admin’s campus-only ops without tenant context |
| Invite any role including University Super Admin | — |
| Manage users **across all tenants** | — |
| Browse global students, events, communities, reports | — |
| Switch university context via picker / filters | See only one university forever (that is USuper Admin) |
| Platform-wide oversight and moderation | University-scoped assign-students wizard (coordinator flow) |
| Chat, email, notify users | — |

---

## 20. Demo walkthrough (what to show a client)

| # | Show this | Say this |
|---|-----------|----------|
| 1 | Login as Intoto Admin | “This is the platform administrator — above any single university.” |
| 2 | Dashboard — Intoto branding + role tag | “Platform context, not locked to one school.” |
| 3 | **Total Universities** → one university details | “Every tenant on Intoto is managed from here.” |
| 4 | **Add University** quick action | “Onboard a new institution in minutes.” |
| 5 | University picker / filter | “Drill into one university without losing platform access.” |
| 6 | **Manage User** → filter by University + Invited | “Cross-tenant invite lifecycle in one place.” |
| 7 | **Add User** → invite University Super Admin | “University required; no campus for top admin role.” |
| 8 | **Total Students** → search + university filter → profile | “Global directory with tenant scoping.” |
| 9 | **Total Reports** → triage one case | “Moderation scales across all universities.” |
| 10 | **Chats** tab | “Direct line to users anywhere on the platform.” |
| 11 | Pull to refresh dashboard | “Counts stay current after tenant or user changes.” |

---

## 21. Screen list (where each feature lives)

| Screen | How the user gets there |
|--------|-------------------------|
| Dashboard Home | Home tab after login |
| University List | Total Universities stat or Manage Universities action |
| University Details | Tap university row or app bar picker |
| Add / Edit University | Add University action or Edit on details |
| Campus List (global) | Total Campuses stat |
| Campus Details | Tap campus row |
| Manage Users | Manage User action or invite stat |
| Add User | Add User action |
| User Filter | Filter on any user list (**University** sidebar) |
| All Students (global) | Total Students stat |
| Student Profile Hub | Student list row |
| University Super Admin directory | Matching Quick Way stat |
| Coordinator directories | Coordinator stat cards |
| Community lists | Community stats or Community tab |
| Events list & details | Events action, stat, or carousel |
| Reports | Report stats |
| Travel hub | Travel stat or action |
| Chat | Chats tab |
| Notifications | Bell on dashboard |
| Pending invitations | Envelope on dashboard |
| Support | Support quick action |
| Profile & Settings | Profile tab |

---

## 22. Figma validation checklist (node 5051-661)

When reviewing the [Intoto Admin frames](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0), confirm:

- [ ] Login and role selection frames for Intoto Admin
- [ ] Platform app bar — Intoto branding vs university picker behavior
- [ ] Role tag reads **Intoto Admin**
- [ ] Every Quick Way card label, icon, and destination hotspot
- [ ] **Manage Universities** and **Add University** quick actions present
- [ ] University List — search, status chips, empty state
- [ ] University Details — fields, Suspend/Activate, campus summary
- [ ] Add University form — required fields and success state
- [ ] Manage Users — **University** column and filter sidebar
- [ ] Add User — University required; campus rules per role
- [ ] Global student list — university filter and profile hub
- [ ] Reports, events, communities — cross-tenant filter behavior
- [ ] Settings — Configuration, Notification, Language with Save on nav bar
- [ ] Bottom tabs: Home, Community, Chats, Profile
- [ ] Notification bell and pending invitation envelope flows
- [ ] Every prototype hotspot has a documented destination in this guide

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | Jun 2026 | Initial Intoto Admin guide — Figma page 5051:661, starting node 5051-661 |

---

*Design reference: [Figma design — Intoto Admin node 5051-661](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0) · [Prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5051%3A661)*
