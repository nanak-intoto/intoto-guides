# Intoto — Event Coordinator
## Features & Flows (User Guide)

**Design reference:** [Intoto Wireframe — Event Coordinator (node 5086-25745)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&page-id=5051%3A661)  
**Prototype (walkthrough):** [Intoto Wireframe — Event Coordinator prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&p=f&t=ttUcU9kASuy321kT-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5086%3A25745)  
**Role:** Event Coordinator (`event_coordinator`)  
**Audience:** Product, Engineering, QA, Client demos  
**Version:** 1.0  
**Last updated:** Jun 2026

---

## About this document

This guide explains **what an Event Coordinator can do in Intoto**, **why each feature exists**, and **how to use it** step by step. It follows the same structure as the Student, Ambassador, University Super Admin, and Third Party Coordinator guides.

**Note on Figma:** The [Event Coordinator prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&p=f&t=ttUcU9kASuy321kT-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5086%3A25745) requires sign-in. Walk every frame from starting node **5086-25745** on page **5051:661** and compare labels, empty states, and actions to this document. Content is written from the Event Coordinator wireframe scope (events lifecycle, approvals, analytics, overview dashboard) — not from application source code.

---

## 1. Who is the Event Coordinator?

### What this role is

The **Event Coordinator** is university staff (or delegated staff) responsible for **campus events end to end**: creating events, reviewing submissions before they go live, monitoring registrations and attendance, and using **analytics** to understand programming by category.

They operate **within one university** (and campus scope where the tenant configures it). They are **not** the full university administrator — they do not run invite/suspend for all roles, assign students to third-party coordinators, or own every community approval queue unless explicitly given extra permissions.

### What they typically do day to day

- Open **Home** and scan **Total Events**, **Events Analytics**, and event carousels (upcoming / pending / completed)
- **Approve** or **reject** events waiting in the pending queue
- **Create** or **edit** events (schedule, venue, registration window, imagery, category)
- Open **Event Details** for registrations, attendance, and feedback
- Use **Events** quick action for the full catalog
- Answer student questions in **Chats** and use **Support**
- Browse **Community** when the role includes community access

### How this role differs from others

| Topic | Event Coordinator | Student | University Super Admin |
|-------|-------------------|---------|------------------------|
| Dashboard focus | Events + analytics | Profile, travel, peers | All university operations |
| Quick Way | Events counts & analytics | Usually none | Many governance stats |
| Creates / edits events | Yes | No (registers only) | Yes (oversight) |
| Approves pending events | Yes (primary owner) | No | May also approve |
| Assigns students to coordinators | No | No | Yes (via coordinators) |
| Manage Users / invites | No (typical) | No | Yes |

---

## 2. Getting into the app

### Feature: Login

**What the user does:** Signs in with university credentials.

**How to do it:**
1. Open the Intoto app.
2. Enter email/password or use configured SSO.
3. Wait for profile and role to load.

**What happens next:**
- **Single role (Event Coordinator only):** Lands on **Home** (Event Coordinator dashboard).
- **Multiple roles:** **Role Selection** — choose **Event Coordinator**.
- **Pending invitations:** Alert at login — **Accept** or **Do it later** (envelope icon on Home later).

---

### Feature: Role selection (multiple roles only)

**What it is:** Switching context when the account also has Student, Ambassador, or admin roles.

**How to do it:**
1. On login, pick **Event Coordinator**, **or**
2. From Home, tap **role switcher** row, **or**
3. **Profile** tab → change role.

**What happens next:** Home reloads with Event Coordinator sections (event Quick Way, event carousels, analytics chart — not student travel alerts).

---

### Feature: Bottom navigation

| Tab | What the Event Coordinator does here |
|-----|----------------------------------------|
| **Home** | Dashboard — stats, shortcuts, event sections, banners, charts |
| **Community** | Communities and posts (when permitted) |
| **Chats** | Messages with students, staff, ambassadors |
| **Profile** | Own profile (read-only or limited edit), settings, logout |

**How to use it:** Tap a tab icon; selected tab is highlighted.

---

## 3. Home — Event Coordinator Dashboard

### What it is

**Home** is an **API-driven overview dashboard** for the Event Coordinator role. The backend returns an ordered list of sections: custom app bar, optional alerts, Quick Way stat cards, Quick Actions, event carousels, promotional content, and analytics visuals. Only configured sections render.

**How to open it:** Tap **Home** (default after login as Event Coordinator).

**How to refresh:** Pull down on Home. Counts, carousels, and chart data reload from the server.

---

### Feature: Custom app bar (university logo + name)

**What it is:** Top bar with university **logo** (when available) and **name** on the left; **notification bell** and **pending invitation** icon on the right when applicable.

**Why it matters:** The coordinator always knows which institution’s events program they manage.

**How to use it:**
1. Read logo + name.
2. **Tap** university block → **University / campus details** (read-only).
3. **Bell** → **Notifications**.
4. **Envelope** (when shown) → **Pending Invitations**.

**Logo missing:** Layout adjusts so name remains readable without a broken empty image area (per wireframe).

---

### Feature: Role switcher (multi-role accounts)

**What it is:** Row showing active role (e.g. “Event Coordinator”) with navigation to role picker.

**How to use it:** Tap → select role → Home reloads for that role’s dashboard config.

---

## 4. Quick Way (stat cards)

### What it is

**Quick Way** is a grid of **count cards** — icon, numeric value, label. Each card is tappable and opens a deeper screen.

**Typical Event Coordinator Quick Way cards (wireframe / API):**

| Card (typical label) | `viewKey` (typical) | What it means | What the user does |
|----------------------|---------------------|---------------|-------------------|
| **Total Events** | `quick_way_total_events` | All events in scope (draft, published, completed — per backend rules) | Opens **All Events** list |
| **Events Analytics** | `quick_way_events_analytics` | Reporting entry point | Opens **Event Analytics** screen |

**How to use Quick Way:**
1. Scroll to **Quick Way** on Home.
2. Tap a card.
3. Use search/filter on lists or filters on analytics.
4. Return to Home; pull to refresh after creating or approving events.

### Quick Way routing map

| `viewKey` | Typical destination |
|-----------|---------------------|
| `quick_way_total_events` | All Events list (paginated, searchable) |
| `quick_way_events_analytics` | Event Analytics dashboard |

**Note:** Backend may add more keys; use card label and Figma frame until product confirms mapping.

---

## 5. Quick Actions

### What it is

Shortcut tiles (`QUICK_ACTIONS`) for frequent tasks without opening a stat card first.

**Typical Event Coordinator Quick Actions:**

| Action (typical label) | `actionId` / `viewKey` (typical) | Purpose |
|------------------------|----------------------------------|---------|
| **Events** | `viewEvents` / `quick_actions_events` | Event catalog hub |
| **Support** | `viewSupport` / `quick_actions_support` | Help / FAQ / contact |

**How to use it:**
1. Find **Quick Actions** on Home.
2. Tap **Events** → all events list.
3. Tap **Support** → support screen.
4. Use **Home** tab or back to return.

---

## 6. Dashboard event sections (carousels)

Horizontal **carousels** with optional **View All** in the section header. Swipe left/right on Home.

### Upcoming Events

**What it means:** Published events scheduled in the future — visible to students for registration when registration window is open.

**What the user does:**
1. Swipe cards on Home.
2. Tap card → **Event Details**.
3. Tap **View All** → upcoming-filtered list.

**Empty state:** Section hidden or empty message when no items.

---

### Pending Events

**What it means:** Events awaiting **approval** before students see them (submitted by staff, students, or other creators per policy).

**What the user does:**
1. Review pending cards on Home.
2. Tap card → **Event Details**.
3. **Approve** or **Reject** (with reason).
4. Tap **View All** → pending queue list.

**Why it matters:** Quality and compliance gate — wrong dates, missing venue, or policy violations should not reach the student app.

---

### Completed Events

**What it means:** Events whose date has passed or status is **completed**.

**What the user does:**
1. Browse completed carousel.
2. Tap card → **Event Details** (read-only or limited edit per policy).
3. Tap **View All** → completed list.
4. Review **registrations**, **attendance**, **feedback** tabs inside details when wireframe provides them.

---

### Events by Category (graph section)

**What it means:** On-Home analytics — **pie chart** or **bar chart** showing distribution of events by category, often with a subtitle (e.g. “Events by category”).

**What the user does:**
1. Scroll to chart section after Home loads.
2. Read legend and segments.
3. Optional: tap segment or **View All** if wireframe links to filtered list or full analytics.

**Note:** Chart may load shortly after overview payload; brief placeholder is expected.

---

## 7. Banners and Activities & Ads

### Banners

**What it is:** Promotional carousel (university campaigns, featured programs).

**How to use it:**
1. Swipe banners on Home.
2. Tap card or CTA → in-app screen or external URL.

### Activities & Ads

**What it is:** Partner or sponsor tiles (similar interaction to banners).

**How to use it:** Swipe → tap → follow CTA / `action_url`.

---

## 8. Events — list and filters

### All Events

**What it is:** Searchable, paginated catalog — entry from **Total Events** Quick Way or **Events** quick action.

**How to do it:**
1. Open list.
2. **Search** — typically 3+ characters, debounced.
3. Tap **Filter** → status, category, campus, date range (API-driven categories).
4. **Apply** → list refreshes; **Clear** resets.
5. Tap row → **Event Details**.

**Common list contexts:**

| Context | Intent |
|---------|--------|
| All | Full catalog |
| Upcoming | Published future events |
| Pending | Awaiting approve/reject |
| Completed | Past events |
| My events | Created by this coordinator (if wireframe separates) |

**Pagination:** Scroll to load more; pull to refresh resets to first page.

---

## 9. Event Details

### What it is

Single-event hub: hero image, title, description, schedule, location, registration window, capacity, status badges.

**Typical areas and actions:**

| Area | Actions |
|------|---------|
| Overview | Read info; share link if enabled |
| Registrations | View registered students; export or message per policy |
| Attendance | Mark or review attended participants |
| Approval (pending) | **Approve** / **Reject** |
| Feedback | Post-event ratings or comments summary |

---

### Approve a pending event — step by step

1. Open event from **Pending Events** on Home or pending list.
2. Verify title, dates, registration start/end, location, image, category, capacity.
3. Tap **Approve**.
4. Confirm in dialog if wireframe requires.
5. Success message → event leaves pending → appears under **Upcoming** per rules.
6. Pull to refresh Home → **Total Events** count updates.

---

### Reject a pending event — step by step

1. Open pending event.
2. Tap **Reject**.
3. Enter **mandatory reason** (explain what to fix).
4. Submit → event removed from pending queue or shows rejected status.
5. Creator can fix and resubmit (workflow outside app or via new submission).

**Validation:** Reject without reason must be blocked.

---

## 10. Create and edit events

### Create event

**What it is:** Form-driven flow to add a university event.

**Typical steps (wireframe):**
1. From event list, tap **Create** / **+**.
2. Fill required fields:
   - Title, description
   - Event date and time (timezone clear in copy)
   - Registration start and end
   - Location (physical address or virtual link)
   - Category
   - Cover image
   - Capacity / visibility (if shown)
3. Tap **Save** or **Submit for approval**.
4. Event lands in **Pending** or **Upcoming** depending on auto-publish rules.

**Validation:** Required fields block save; invalid date ranges show inline errors.

---

### Edit event

**What it is:** Update an existing event.

**How to do it:**
1. Open **Event Details**.
2. Tap **Edit**.
3. Change allowed fields (some fields may lock after registration opens or event starts).
4. Save → return to details; lists and Home refresh on next pull.

---

### Cancel or unpublish (if wireframe provides)

**How to do it:**
1. Event Details → **Cancel** / **Unpublish**.
2. Confirm → students no longer register; event may move to completed/cancelled state.

---

## 11. Event Analytics (full screen)

### What it is

Dedicated analytics from **Events Analytics** Quick Way — beyond the Home category chart.

**Typical content (wireframe):**
- KPI tiles — total events, registrations, attendance rate (API-driven labels)
- **Bar chart** — registrations or attendance over time
- **Pie chart** — events by category (may mirror Home section)
- Filters — date range, campus, category

**How to use it:**
1. Tap **Events Analytics** on Home.
2. Apply filters.
3. Interpret charts for planning (which categories need more events).
4. Drill down to filtered event list if frame supports tap-through.

---

## 12. Registrations and attendance

### Registrations (coordinator view)

**What the user does:**
1. Event Details → **Registrations** tab or section.
2. Scroll student list; search if available.
3. Open student row → profile (read-only) or message per policy.
4. Export list if wireframe provides **Export**.

### Attendance

**What the user does:**
1. Event Details → **Attendance** (during or after event).
2. Mark students attended (checkbox / scan / manual list per wireframe).
3. Save → attendance reflected in analytics.

**Why it matters:** Proof of participation for reports and follow-up communications.

---

## 13. Community (tab)

### What it is

University communities — browse, read posts, optional create/post.

**How to open:** **Community** tab.

**How to use it:**
1. Browse feed or community directory.
2. Open community → read posts.
3. Create post if member and permitted.

**Boundary:** Event Coordinator typically does **not** approve **pending communities** (University Super Admin / Community Coordinator). Confirm in Figma for your tenant.

---

## 14. Chats (tab)

### What it is

Messaging with students and staff about events.

**How to use it:**
1. Tap **Chats** tab.
2. Open thread → reply.
3. Search for user if compose/search is available.

**Typical scenarios:** Registration deadline questions, venue changes, accessibility requests.

---

## 15. Profile (tab)

### What it is

Account settings; own profile for Event Coordinator is typically **read-only basic details + photo** (not full `studentForm` / `ambassadorForm`).

**How to use it:**
1. Tap **Profile**.
2. View name, email, role; open FAQs, terms, privacy.
3. **Logout** when finished.

---

## 16. Notifications and invitations

### Notifications

**How to open:** Bell on Home app bar.

**Typical types:**
- New pending event submission
- Registration threshold alerts
- Event starting soon
- Chat messages
- Role invitations

**How to use:** Tap notification → deep link to Event Details, pending list, or chat.

### Pending invitations

**How to open:** Envelope after deferring invite.

**How to use:** Accept or decline additional roles on the account.

---

## 17. Support

**How to open:** Quick Action **Support** on Home.

**When to use:** Escalate policy questions, technical issues, or content disputes outside coordinator authority.

---

## 18. End-to-end flows (playbooks)

### Flow A — Publish a new event (auto-publish tenant)

1. Home → Quick Action **Events**.
2. **Create** → complete form → **Save**.
3. Event appears in **Upcoming Events** carousel.
4. Student app shows event for registration (UAT cross-check).
5. **Total Events** count increases after refresh.

### Flow B — Approve a submitted event

1. Home → **Pending Events** → open event.
2. Review fields → **Approve** → confirm.
3. Verify carousel moves event to **Upcoming**.
4. Reject path: **Reject** + reason → pending list updates.

### Flow C — Run event day and close out

1. **Upcoming** → Event Details day-of → attendance marking.
2. After date passes → event in **Completed** carousel.
3. Review feedback tab.
4. **Events Analytics** → check category and attendance metrics.

### Flow D — Plan next semester using analytics

1. Home → note **Events by Category** chart.
2. Open **Events Analytics** → filter last 90 days.
3. Identify under-used categories → create new events in those categories.

---

## 19. Search, filter, and pagination

**Search**
- Minimum character threshold (often 3) on event and registration lists.
- Debounced input; clear restores full list.

**Filter**
- Filter icon → categories from API → **Apply** / **Clear All**.

**Pagination**
- Infinite scroll or page index on long event lists.
- Pull to refresh on Home and list screens.

---

## 20. Permissions and boundaries

**Event Coordinator can (typical):**
- Create, edit, and publish events (per workflow).
- Approve/reject pending events in scope.
- View registrations and record attendance.
- View event analytics for scoped data.
- Chat and use Support.
- Browse communities when permitted.

**Event Coordinator cannot (typical):**
- Invite or suspend arbitrary users (Manage Users).
- Assign students to sub-coordinators.
- Manage all university Quick Way stats (USA scope).
- Cross-university administration.
- Override community approval queue without community-admin role.

---

## 21. Empty states and errors

| Situation | Expected UX |
|-----------|-------------|
| No upcoming events | Hidden section or empty illustration |
| No pending events | Empty pending message |
| Network error on Home | Toast/banner; retry via pull-to-refresh |
| Reject without reason | Validation; submit blocked |
| Chart loading | Placeholder until analytics payload returns |
| Create with invalid dates | Inline error on registration end before start |

---

## 22. Student-facing impact (for demos and UAT)

| Coordinator action | Student experience |
|--------------------|-------------------|
| Approve pending event | Event appears in student **Upcoming Events** / **Events** |
| Reject pending event | Students do not see event |
| Edit registration end | Student register button enables/disables per dates |
| Cancel event | Registration closes; event removed or marked cancelled |

---

## 23. Screen list

| Screen | How the user gets there |
|--------|-------------------------|
| Event Coordinator Home | Home tab after login |
| All Events list | Total Events Quick Way or Events quick action |
| Upcoming / Pending / Completed lists | Carousel View All or filters |
| Event Details | Tap event card or list row |
| Create / Edit event | + or Edit on details |
| Event Analytics | Events Analytics Quick Way |
| Registrations / Attendance | Tabs on Event Details |
| Community feed | Community tab |
| Chats | Chats tab |
| Notifications | Bell on Home |
| Support | Support quick action |
| University details | Tap university header |
| Role Selection | Role switcher |

---

## 24. Figma validation checklist (node 5086-25745)

On the [Event Coordinator prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&p=f&t=ttUcU9kASuy321kT-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5086%3A25745), confirm:

- [ ] Home — app bar, Quick Way (Total Events, Events Analytics)
- [ ] Quick Actions — Events, Support
- [ ] Upcoming / Pending / Completed carousels + View All
- [ ] Events by Category chart
- [ ] Banners and Activities
- [ ] All Events — search, filter, pagination
- [ ] Event Details — approve, reject, registrations, attendance
- [ ] Create / Edit event forms and validation
- [ ] Event Analytics full screen
- [ ] Community, Chats, Profile tabs
- [ ] Notifications, invitations, role switcher
- [ ] Empty and error states per frame

---

## 25. Document history

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | Jun 2026 | Initial Event Coordinator guide — Figma start node 5086-25745, page 5051:661 |

---

## Related docs

- `docs/Event-Coordinator-Client-Demo-Guide.md`
- `docs/Event-Coordinator-QA-Test-Guide.md`
- `docs/Student-Features-and-Flows.md` (student event registration view)
- `docs/University-Super-Admin-Features-and-Flows.md` (Total Events oversight)

*Design: [node 5086-25745](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&page-id=5051%3A661) · Prototype: [starting point 5086-25745](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&p=f&t=ttUcU9kASuy321kT-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5086%3A25745)*
