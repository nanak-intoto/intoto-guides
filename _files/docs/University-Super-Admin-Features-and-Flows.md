# Intoto — University Super Admin  
## Features & Flows (User Guide)

**Design reference:** [Intoto Wireframe — Prototype (node 5051-661)](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&t=Fqpnfj5F0UbdlVZB-1)  
**Role:** University Super Admin  
**Audience:** Product, Engineering, QA, Client demos  
**Version:** 1.1  
**Last updated:** May 2026

---

## About this document

This guide explains **what a University Super Admin can do in Intoto**, **why each feature exists**, and **exactly how to use it** — step by step. It is written so product and client teams can run demos without opening the app, and so engineering and QA know the expected user journey for each screen.

---

## 1. Who is the University Super Admin?

### What this role is

The **University Super Admin** is the highest operational administrator **within one university**. They manage people (staff, coordinators, students, ambassadors), communities, events, reports, and travel data — all scoped to their own institution.

They do **not** manage other universities (that is Intoto Admin). They do **not** pick a campus at login — the app already knows their university.

### What they typically do day to day

- Check dashboard counts (students, communities, events, reports)
- Invite new staff or coordinators
- Monitor or suspend user accounts
- Review and approve pending communities
- Browse student lists and open profiles
- Assign unassigned students to sub-coordinators
- Respond to reports and messages
- Create official communities without waiting for approval

---

## 2. Getting into the app

### Feature: Login

**What the user does:** Signs in with their university credentials (Auth0).

**How to do it:**
1. Open the Intoto app.
2. Enter email/password or use the configured SSO method.
3. Wait for the app to load the user profile and role.

**What happens next:** If the user has only the University Super Admin role, they land on the **Home dashboard**. If they have multiple roles (e.g. Super Admin + Coordinator), they may see **Role Selection** first.

---

### Feature: Role selection (multiple roles only)

**What it is:** Lets one person switch between roles assigned to their account (e.g. University Super Admin vs Student).

**When the user needs it:** They hold more than one role and want to work in a different context.

**How to do it:**
1. On first login, choose **University Super Admin** from the role list, **or**
2. From the dashboard, tap the **role switcher** row at the top (if shown), **or**
3. Go to **Profile** tab → switch role.

**What happens next:** The dashboard and available features reload for the selected role.

---

### Feature: Bottom navigation (main app areas)

**What it is:** Four primary areas of the app, always visible from the bottom bar.

| Tab | What the user does here |
|-----|-------------------------|
| **Home** | See dashboard stats, shortcuts, events, and announcements |
| **Community** | Browse, create, and manage communities and posts |
| **Chats** | Message students, staff, and ambassadors |
| **Profile** | View own profile, change settings, log out |

**How to use it:** Tap any tab icon. The selected tab is highlighted (usually in teal/blue).

---

## 3. Home — Dashboard Overview

### What it is

The **Home dashboard** is the University Super Admin’s control panel. It shows live counts, shortcuts, events, and promotions — all configured by the backend for this role.

**How to open it:** Tap **Home** in the bottom tab bar (default after login).

**How to refresh counts:** Pull down on the dashboard screen. Stat numbers and lists update from the server.

---

### Feature: University header (logo + name)

**What it is:** A custom top bar showing the university’s logo and full name — not a truncated system title.

**Why it matters:** The admin always sees which institution they are managing.

**How to use it:**
1. Look at the top-left of the dashboard — logo (if available) and university name.
2. **Tap the logo or name** to open **University Details** (overview of the institution, campuses, etc.).
3. Tap the **bell icon** (top-right) for notifications, if shown.
4. Tap the **envelope icon** (top-right) for pending role invitations, if shown after deferring an invite.

**Note:** If the logo fails to load, only the name is shown — the layout adjusts automatically.

---

### Feature: Role tag

**What it is:** A colored badge under the header showing **“University Super Admin”**.

**Why it matters:** Confirms the active role, especially when the user has multiple roles.

**How to use it:** Read-only indicator. If the user has multiple roles, tapping the role switcher (when available) changes role.

---

## 4. Quick Way — stat cards

### What it is

**Quick Way** is a grid of cards on the dashboard. Each card shows:
- An icon  
- A **number** (count from the server)  
- A **label** (e.g. “Total Students”)

**Why it matters:** Gives at-a-glance health of the university — how many students, communities, pending items, etc.

**How to use it:**
1. Scroll to the **“Quick Way”** section on Home.
2. **Tap any card** to open the full list or screen behind that number.
3. Pull to refresh on Home to update counts after making changes elsewhere.

Below, each card type is described: **what it means**, **what the user does**, and **how to do it**.

---

### Total Campus

**What it means:** Number of campuses under this university.

**What the user does:** Reviews all campuses and opens campus details.

**How to do it:**
1. Tap **Total Campus** on the dashboard.
2. Browse the campus list.
3. Tap a campus row to open **Campus Details** (info, logo, location, etc.).

---

### Total Students

**What it means:** All students registered under this university.

**What the user does:** Searches students, applies filters, opens profiles, sends bulk email or notifications.

**How to do it:**
1. Tap **Total Students**.
2. Type in the **search bar** (at least 3 characters) to find a student by name or email.
3. Tap the **filter icon** to narrow by campus, country, program, languages, etc. (see [Section 19 — Filters](#19-filters-how-to-narrow-any-list)).
4. Tap a **student row** to open their **Student Profile Hub**.
5. To message many students: long-press or enter selection mode → select rows → tap **Take Action** → choose email or notification.

---

### Assigned Students

**What it means:** Students already assigned to a sub-coordinator for arrival support.

**What the user does:** Monitors which students are under coordinator care.

**How to do it:**
1. Tap **Assigned Students**.
2. Search or filter as needed.
3. Tap a row to view the student’s full profile and assignment status.

---

### Total Sub Coordinator / Third-Party Sub Coordinators

**What it means:** Count of sub-coordinators working under third-party coordinators.

**What the user does:** Views the coordinator directory and sees which students each sub-coordinator handles.

**How to do it:**
1. Tap the stat card.
2. Search or filter the list.
3. Tap a sub-coordinator → opens **Assigned Students** for that person.

---

### Total Arrival Requests

**What it means:** Students who submitted arrival/travel-related requests.

**What the user does:** **Reviews** requests (oversight). This list is browse-only for University Super Admin — no assign action here.

**How to do it:**
1. Tap **Total Arrival Requests**.
2. Search or filter the list.
3. Tap a row → **Arrival Request Details** (dates, travel info, status).

---

### Total Unassigned Students / Unassigned Requests

**What it means:** Students who still need a sub-coordinator assignment.

**What the user does:** Finds students without support and **assigns them** to a sub-coordinator (see [Section 11 — Assign students](#11-assign-students-to-a-sub-coordinator)).

**How to do it:**
1. Tap the unassigned stat card.
2. Review the list.
3. Select one or more students → start the **Assign Students** flow.

---

### Total Ambassadors / External Ambassadors

**What it means:** Student ambassadors (internal or external) who help onboard peers.

**What the user does:** Opens the ambassador directory to chat or review profiles.

**How to do it:**
1. Tap the ambassador stat card.
2. Search or filter ambassadors.
3. Tap a row to open profile or start a chat.

---

### Total Communities / Community Members

**What it means:** All communities (or total membership) at the university.

**What the user does:** Browses every community — official and user-created.

**How to do it:**
1. Tap the community stat card.
2. Scroll the combined list.
3. Tap a community → **Community Profile** and feeds.

---

### Pending Communities

**What it means:** Communities waiting for admin approval (usually created by students or staff).

**What the user does:** **Approves or rejects** community creation requests.

**How to do it:**
1. Tap **Pending Communities**.
2. Open a requested community from the list.
3. Review name, description, and settings.
4. Tap **Approve** to make it live, or **Reject** with a reason if inappropriate.

---

### Approved / Active Communities

**What it means:** Communities already live on the platform.

**What the user does:** Monitors active communities.

**How to do it:**
1. Tap the approved/active stat card.
2. Browse and open any community to view posts and members.

---

### Total Events

**What it means:** All events associated with the university.

**What the user does:** Opens the full events catalog.

**How to do it:**
1. Tap **Total Events**.
2. Browse, search, or filter events.
3. Tap an event → **Event Details** (date, location, registration).

---

### Total Reports / Assigned Reports / My Assigned Reports

**What it means:** User-generated reports ( inappropriate content, abuse, etc.) — all reports, workload summary, or reports assigned to this admin.

**What the user does:** Triages and resolves moderation cases.

**How to do it — all reports:**
1. Tap **Total Reports**.
2. Open a report from the list.
3. Read details, change status: **Assigned → Under Review → Escalated → Resolved**.

**How to do it — assigned workload:**
1. Tap **Assigned Reports** for a stats overview, or **My Assigned Reports** for your queue.
2. Work through each case and update status when done.

---

### Total Travel Plans

**What it means:** Student travel plan submissions at the university.

**What the user does:** Opens the travel hub to review travel-related data.

**How to do it:**
1. Tap **Total Travel Plans**.
2. Browse travel plan sections and student submissions.

---

### Event / Community / Third-Party Coordinators

**What it means:** Count of users in each coordinator role.

**What the user does:** Browses staff directories (read-only profile view).

**How to do it:**
1. Tap the relevant coordinator stat card.
2. Search or filter the list.
3. Tap a person → view their **User Profile**.

---

## 5. Quick Actions — shortcuts

### What it is

**Quick Actions** are large shortcut buttons below Quick Way — faster paths to common tasks without tapping a stat card first.

**How to use:** Tap any action tile on the dashboard.

---

### Manage User

**What the user does:** Opens the full invitation and user management list.

**How to do it:**
1. Tap **Manage User** on the dashboard.
2. You arrive on **Manage Users** (see [Section 8](#8-manage-users-invite-and-control-accounts)).

---

### Add User

**What the user does:** Starts inviting someone new to the platform.

**How to do it:**
1. Tap **Add User** on the dashboard.
2. Complete the invite form (see [Section 8 — Add User](#add-user-invite-someone-new)).

---

### Events

**What the user does:** Opens the full events list directly.

**How to do it:** Tap **Events** → browse all university events.

---

### Support

**What the user does:** Gets help or contacts support resources.

**How to do it:** Tap **Support** → follow in-app support content or links.

---

### My Campus / Travel Plan

**What the user does:** Jumps to campus details or the travel plan hub without going through a stat card.

**How to do it:** Tap **My Campus** or **Travel Plan** on the dashboard.

---

## 6. Other dashboard content

### Banners

**What it is:** Promotional carousel at the top of the dashboard (job fairs, hackathons, etc.).

**How to use:**
1. Swipe horizontally through banners.
2. Tap **CTA button** or the banner itself → opens linked page (in-app or browser).

---

### Upcoming Events carousel

**What it is:** Preview of near-future events without leaving Home.

**How to use:**
1. Swipe through event cards.
2. Tap a card → **Event Details**.
3. Tap **View All** in the section header → full upcoming events list.

---

### Pending Events (when shown)

**What it is:** Events submitted by others that need admin approval.

**How to use:**
1. On each card, tap **Approve** or **Reject**.
2. If rejecting, enter a reason in the popup.
3. Tap **View All** for the full approval queue.

---

### Activities & Ads

**What it is:** Sponsored or informational cards (campus store, housing, career fair).

**How to use:** Swipe and tap a card → opens the advertised URL or in-app destination.

---

## 7. Manage users — invite and control accounts

### What it is

**Manage Users** is where the University Super Admin sees everyone invited to or active on the platform within their university — and takes action on their account status.

**How to open:**
- Dashboard → **Quick Action “Manage User”**, or  
- Any stat card that routes to user management.

---

### Manage Users list

**What the user sees:**
- Title and **“Total Users: X”** subtitle  
- **Status chips:** All · Invited · Accepted · Withdrawn · Rejected · Suspended  
- **Search bar** at the top  
- **Filter button** next to search  
- Scrollable list of people  

**How to find someone:**
1. Tap a **status chip** (e.g. **Invited** to see pending invites only).
2. Type in **search** (name or email).
3. Tap **Filter** → choose Campus and/or Role → **Apply**.

**How to act on one person:**
1. Tap their row → detail screen with available actions.
2. Choose an action based on status (table below).

**How to act on many people:**
1. Enter selection mode (long-press or select checkbox).
2. Select multiple rows.
3. Tap **Take Action** at the bottom.
4. Choose batch email or other bulk action.

| Their status | What you can do |
|--------------|-----------------|
| **Invited** (not yet accepted) | Withdraw invite, Resend invite, Send email |
| **Accepted** (active user) | Suspend account, Send email |
| **Suspended** | Re-initiate account, Send email |
| **Withdrawn / Rejected** | Resend invite, Send email |
| **All** filter selected | Send email only (when filtering all statuses) |

**Typical tasks:**

| Task | Steps |
|------|--------|
| Resend a lost invite | Manage Users → **Invited** → find person → **Resend invite** |
| Suspend a problematic user | **Accepted** → find person → **Suspend account** |
| Email many coordinators | Select rows → **Take Action** → **Send email** |

---

### Add User — invite someone new

**What it is:** A form to send platform invitations by email.

**How to open:** Dashboard → **Add User** quick action.

**How to invite step by step:**

1. **Select Role** — tap the role field and pick from the list (Student, Sub-Coordinator, Ambassador, University Super Admin, etc.).
2. **Enter email** — type one email, or import a file for bulk invites.
3. **Select Campus** — *required for most roles* (Student, Coordinator, Ambassador…). Skip this when inviting another **University Super Admin**.
4. **Ambassador Type** — *only if role is Ambassador or External Ambassador* — pick type from lookup list.
5. **Profile visibility** — *for non-student roles* — set whether their profile is public or restricted.
6. **Invite type** — *for students* — choose invite options shown on the form.
7. **Expiry date** — pick when the invitation expires.
8. Tap **Submit**.

**What happens next:** The person appears in **Manage Users** under **Invited**. They receive an email to join. When they accept, status changes to **Accepted**.

**Examples:**

| I want to… | Role | Campus? |
|------------|------|---------|
| Invite a new sub-coordinator | Third-Party Sub Coordinator | Yes |
| Invite another super admin | University Super Admin | No |
| Invite a student | Student | Yes |
| Invite an ambassador | Ambassador | Yes + Ambassador Type |

---

## 8. Student lists and profiles

### All Students — full student directory

**What the user does:** Finds any student, filters by attributes, opens deep profile, sends bulk messages.

**How to do it:** (Same as **Total Students** stat card above.)

**Student Profile Hub — what you see after tapping a student:**
- Personal and academic sections (API-driven)
- Travel and documents (if configured)
- **Assignment status** — which coordinator supports them, if any
- Actions available from profile (message, view sections)

**How to open a profile:** From any student list → tap the student’s row.

---

### Assigned Students

**What the user does:** Focuses only on students already linked to a sub-coordinator.

**How to do it:**
1. Open via **Assigned Students** stat card (or **My Assigned Requests** if personal).
2. Search, filter, tap row for profile.

**When to use:** Checking coordinator workload or verifying assignment details.

---

### Unassigned Students

**What the user does:** Finds students who still need coordinator support before arrival.

**How to do it:**
1. Open via **Unassigned** stat card.
2. Review list — these students have no sub-coordinator yet.
3. Proceed to assignment flow (next section).

---

## 9. Assign students to a sub-coordinator

### What it is

Links one or more unassigned students to a sub-coordinator for arrival support, with a date range, work description, and control over which profile sections the coordinator can see.

**When the user does this:** After seeing unassigned students on the dashboard or receiving operational need to distribute workload.

**How to do it — full flow:**

**Step 1 — Select students**
1. Open **Unassigned Students** list.
2. Select one or more students (checkbox / selection mode).
3. Tap **Assign** (or equivalent action button).

**Step 2 — Assignment setup**
1. **Choose sub-coordinator** from the picker list.
2. Set **Start date** and **End date** for the assignment period.
3. Enter **Work description** (what the sub-coordinator should do).
4. Tap **Continue** or **Next**.

**Step 3 — Profile configuration**
1. You see a list of student profile sections (personal info, travel, documents, etc.).
2. **Toggle each section** on or off — this controls what the sub-coordinator can view.
3. Tap **Confirm** or **Submit**.

**What happens next:**
- Success message appears.
- Students move from **Unassigned** to **Assigned Students**.
- Sub-coordinator can see allowed profile sections for those students.

---

## 10. Coordinator directories

### Sub-coordinators

**What the user does:** Audits who is handling students.

**How to do it:**
1. Open **Total Sub Coordinator** or **Third-Party Sub Coordinators** stat.
2. Tap a name → see **their assigned students**.

### Event / Community / Third-party coordinators

**What the user does:** Views coordinator profiles for staffing overview (not student assignment).

**How to do it:**
1. Open the matching stat card on the dashboard.
2. Tap a person → **User Profile** (read-only browse).

---

## 11. Arrival requests (read-only review)

### What it is

A list of student arrival requests for **oversight** — University Super Admin can view but does not assign from this screen.

**How to use:**
1. Tap **Total Arrival Requests** on the dashboard.
2. Search or filter if needed.
3. Tap a row → read **Arrival Request Details** (travel dates, status, student info).

**When to use:** Checking volume of arrival activity or investigating a specific case before talking to a coordinator.

---

## 12. Community

### Browse communities

**How to do it:**
- **Dashboard stat** → community list, **or**
- **Community tab** → Explore / My Communities.

Tap any community → view profile, members, and feed.

---

### Create a community (University Super Admin)

**What is special:** Communities you create are **live immediately** — no 24-hour approval wait.

**How to do it:**
1. Go to **Community tab** → **Create Community** (or create from admin community tools).
2. Fill in **name**, **description**, upload **profile/cover images** if required.
3. Complete any additional fields on the form.
4. Tap **Submit**.

**What happens next:** You see **“Community created successfully!”** and the community is active. (Students see a “submitted for approval” message instead.)

---

### Approve pending communities

**What the user does:** Reviews communities created by others before they go public.

**How to do it:**
1. Tap **Pending Communities** on the dashboard.
2. Open a requested community.
3. Read details → **Approve** or **Reject**.
4. If rejecting, provide a reason when prompted.

---

### Community tab day-to-day

| Task | How |
|------|-----|
| Read posts | Community tab → open community → scroll feed |
| View post detail | Tap any post in the feed |
| Join / manage membership | From community profile (as designed in wireframe) |
| Moderate content | Open post or report linked from community (where applicable) |

---

## 13. Events

### Browse all events

**How to do it:**
- Dashboard → **Events** quick action, **or**
- Dashboard → **Total Events** stat card.

Tap any event → **Event Details**.

---

### Upcoming events from Home

**How to do it:**
1. Scroll to **Upcoming Events** on the dashboard.
2. Swipe through cards; tap one for details.
3. Or tap **View All** for the complete upcoming list.

---

### Approve or reject events (when Pending Events section exists)

**How to do it:**
1. On the dashboard **Pending Events** carousel, tap **Approve** or **Reject** on a card.
2. For reject, enter reason in the popup.
3. Or tap **View All** → full **Event Approval** list.

---

### Event Details — what the user does there

- Read full description, schedule, and location  
- See registration status and capacity  
- Register or manage event (depending on wireframe / role rules)  
- Share event or view attendees if available  

---

## 14. Reports (moderation)

### What it is

Reports are flags from users about inappropriate posts, messages, or behavior. University Super Admin helps resolve them.

### Work all reports

**How to do it:**
1. Tap **Total Reports** on the dashboard.
2. Open a report from the list.
3. Read context (who reported, what content, when).
4. Change status as you work the case:

| Status | Meaning |
|--------|---------|
| **Assigned** | Case is in someone’s queue |
| **Under Review** | Being investigated |
| **Escalated** | Needs senior attention |
| **Resolved** | Closed |

5. When finished, set to **Resolved**.

### My assigned reports

**How to do it:** Tap **My Assigned Reports** → only cases assigned to you → same status workflow.

### Assigned reports stats

**How to do it:** Tap **Assigned Reports** for a summary view of team workload (counts/overview).

---

## 15. Travel plans

### What it is

Overview of student travel plan submissions for the university.

**How to use:**
1. Tap **Total Travel Plans** stat or **Travel Plan** quick action.
2. Browse sections and student travel records in the hub.
3. Tap items to drill into details as shown in the travel UI.

**When to use:** Monitoring travel season volume or reviewing submissions at university level.

---

## 16. Chat

### What it is

Direct messaging with students, ambassadors, coordinators, and staff.

**How to open:** Tap **Chats** in the bottom tab bar.

**How to start or continue a conversation:**
1. See existing threads in the chat list.
2. Tap a thread → read history → type message → send.
3. To find someone new: use **search** on the chat user list (if available from ambassador directory or chat compose).

**How to open ambassador directory from dashboard:**
1. Tap **Total Ambassadors** stat.
2. Search or filter → tap person → start chat or view profile.

**Bulk email (from lists, not chat tab):**
1. On Manage Users or All Students, select multiple people.
2. **Take Action** → **Send email** → compose in mail sheet.

---

## 17. Profile and settings

**How to open:** Tap **Profile** in the bottom tab bar.

| Feature | What the user does | How |
|---------|-------------------|-----|
| **View / edit profile** | Update own admin profile sections | Tap sections on profile screen |
| **Settings** | App preferences | Profile → Settings |
| **Language** | Change app language | Settings → Language → confirm restart if prompted |
| **FAQs** | Read help articles | Profile → FAQs |
| **About App** | See version info | Profile → About |
| **Logout** | Sign out securely | Profile → Logout → confirm |
| **Delete account** | Remove own account | Profile → Delete account → confirm |
| **Switch role** | Change to another assigned role | Profile or dashboard role switcher |

---

## 18. Notifications and invitations

### Notifications

**What the user does:** Reads announcements, assignment updates, community activity, system alerts.

**How to do it:**
1. On the dashboard, tap the **bell icon** (top-right).
2. Scroll the notification list.
3. Tap a notification to open the related screen (when deep link is supported).

---

### Pending role invitations

**What it is:** If someone invited this user to a **new role**, an alert appears on login.

**How to do it:**
1. On alert: tap **Accept** to switch to that role, or **Do it later** to dismiss.
2. If deferred: an **envelope icon** appears in the dashboard header.
3. Tap envelope → **Pending Invitations** list → accept or review invites.

---

## 19. Filters — how to narrow any list

### What it is

The **Filter** screen lets the user narrow a long list (students, users, chat contacts) by campus, role, country, program, languages, dates, and more — depending on which list they opened filter from.

**How to open:** On any list screen (Manage Users, All Students, etc.) → tap the **filter icon** next to search.

### How to apply filters — step by step

1. Tap **Filter** on the list screen.
2. On the **left sidebar**, tap a category (e.g. **Campus**, **Role**, **Country**).
3. On the right, use **Search** to find options quickly (type at least 2 characters).
4. **Tap checkboxes** to select one or more values (multi-select allowed).
5. Switch sidebar category to add more filters from other groups.
6. Tap **Apply** (bottom-right) to filter the list and return.
7. Or tap **Cancel** to discard changes and go back.
8. Or tap **Clear All** (top-right) to remove every filter and apply empty selection.

### Special: Visit Schedule filter

When **Visit Schedule** is selected in the sidebar:
- No checkbox list appears.
- Instead, pick **Start date** and **End date** using the date fields.
- Apply when done.

### Filters on Manage Users (University Super Admin)

Only **Campus** and **Role** appear — there is no University filter because you are already scoped to your institution.

---

## 20. Quick reference — permissions

| Can do | Cannot do |
|--------|-----------|
| Manage all users within own university | Switch to another university’s data |
| Invite any invitable role including Super Admin | See Intoto-wide cross-university admin view |
| Approve communities and events | — |
| Create communities instantly | — |
| Assign students to sub-coordinators | — |
| Suspend, resend, withdraw invitations | — |
| View arrival requests (read-only) | Assign from arrival requests list |
| Chat, email, notify users | — |

---

## 21. Demo walkthrough (what to show a client)

| # | Show this | Say this |
|---|-----------|----------|
| 1 | Login as University Super Admin | “This is the top admin for one university.” |
| 2 | Dashboard header — logo + name | “Full university name, always visible. Tap for details.” |
| 3 | Quick Way counts | “Live metrics — tap any card to drill in.” |
| 4 | Total Students → search + filter → one profile | “Find any student in seconds.” |
| 5 | Manage User → Invited → Resend | “Full control of the invitation lifecycle.” |
| 6 | Add User → invite coordinator | “Campus required for operational roles.” |
| 7 | Add User → invite Super Admin | “No campus — peer admin invite.” |
| 8 | Pending Communities → Approve | “Gatekeeping for student-created groups.” |
| 9 | Create Community as Super Admin | “Official communities go live instantly.” |
| 10 | Total Reports → change status | “Moderation workflow built in.” |
| 11 | Chats tab | “Direct line to students and ambassadors.” |
| 12 | Pull to refresh dashboard | “Counts stay current after actions.” |

---

## 22. Screen list (where each feature lives)

| Screen | How the user gets there |
|--------|-------------------------|
| Dashboard Home | Home tab after login |
| Manage Users | Quick Action or stat |
| Add User | Quick Action |
| User Filter | Filter button on any list |
| All Students | Total Students stat |
| Assigned / Unassigned Students | Matching stat cards |
| Assign Students wizard | Unassigned list → select → Assign |
| Sub-Coordinator list | Sub-coordinator stats |
| Coordinator directories | Event / Community / Third-party stats |
| Arrival Requests | Total Arrival Requests stat |
| Ambassador list | Ambassador stats |
| Community lists | Community stats or Community tab |
| Create Community | Community tab |
| Events list & details | Events action, stat, or carousel |
| Reports | Report stats |
| Travel hub | Travel stat or action |
| Chat | Chats tab |
| Notifications | Bell on dashboard |
| Pending invitations | Envelope on dashboard |
| Support | Support quick action |
| Profile & Settings | Profile tab |

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | May 2026 | Initial feature inventory |
| 1.1 | May 2026 | Added user-facing descriptions and step-by-step flows for every feature |

---

*Design reference: [Figma prototype — node 5051-661](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&t=Fqpnfj5F0UbdlVZB-1)*
