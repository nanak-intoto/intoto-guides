# Intoto — Ambassador (in-app role)
## Features & Flows (User Guide)

**Product:** Intoto **mobile app** — Ambassador / External Ambassador role  
**Roles:** Ambassador (`ambassador`), External Ambassador (`external_ambassador`)  
**Audience:** Product, Engineering, QA, Client demos  
**Version:** 2.0  
**Last updated:** Jun 2026

> **Not the web Ambassador Platform.** For the browser product (*Student Ambassadors*, signup, directory, web chat) see **`Ambassador-Platform-Features-and-Flows.md`** — sourced from Figma page **5051:661** (*The Ambassador Plateform*). This document covers the **in-app mentor role** (Home, Quick Way, Chats tab, communities, events).

---

## About this document

This guide explains **what an Ambassador can do in the Intoto mobile app**, **why each feature exists**, and **how to complete every screen and flow** step by step. It follows the same structure as the Student, University Super Admin, Event Coordinator, Community Coordinator, and Third Party Coordinator guides.

---

## 1. Who is the Ambassador?

### What this role is

An **Ambassador** on the Intoto platform is a **peer mentor** who helps incoming and current students navigate university life. Ambassadors maintain a **public-facing mentor profile** that appears on the **Student Home dashboard**, answer questions in **Chats**, and participate in **events** and **communities** as an engaged campus guide.

They operate **within one university** (and assigned campus where applicable). They are **not** operational administrators — they do not invite staff, suspend users, assign students to coordinators, approve communities, or approve events.

### Ambassador vs External Ambassador

| Type | Typical user | Wireframe differences |
|------|----------------|----------------------|
| **Ambassador** | Current student or recent graduate at the university | Often also holds **Student** role on the same account |
| **External Ambassador** | Partner, agency, or off-campus mentor | **Ambassador Type** field required at invite; same app shell and profile hub |

Both use the **ambassador profile form** and the **Ambassador Info** section so students see complete, trustworthy mentor cards.

### What they typically do day to day

- Open **Home** and check outreach stats, completion alerts, and event previews
- Complete or update **Ambassador Info** and profile photo
- Reply to **Chats** from students who found them on the dashboard
- Browse **students** in scope (when Quick Way lists are configured)
- **Register** for campus events and post in **communities**
- Switch to **Student** role on dual-role accounts for personal onboarding tasks

### How this role differs from others

| Topic | Ambassador Platform | Student | University Super Admin |
|-------|---------------------|---------|------------------------|
| Primary purpose | Mentor other students | Own onboarding & campus life | Run the university on Intoto |
| Public mentor profile | Yes — **Ambassador Info** | No (peer profile only) | Admin read-only profile |
| Shown on student Home | Yes — **Ambassadors** carousel | No (self) | No |
| Quick Way | Outreach (messages, students) | Usually none | Full governance stats |
| Manage users / invites | No | No | Yes |
| Approve events / communities | No | No | Yes |

---

## 2. Getting into the app

### Feature: Login

**What the user does:** Signs in with university credentials.

**How to do it:**
1. Open the Intoto app.
2. Enter email/password or use configured SSO.
3. Wait for profile and role payload to load.

**What happens next:**
- **Ambassador only:** Lands on **Ambassador Home** dashboard.
- **Student + Ambassador:** **Role Selection** — pick **Ambassador** for mentor work or **Student** for personal tasks.
- **New invite pending:** Invitation alert — **Accept** or **Do it later**.

---

### Feature: Role selection (multiple roles only)

**What it is:** One account commonly holds both **Student** and **Ambassador**. Role selection switches dashboard configuration and available actions.

**How to do it:**
1. At login, select **Ambassador**, **or**
2. On Home, tap **role switcher** row (role chip + chevron), **or**
3. **Profile** tab → switch role.

**What happens next:**
- **Ambassador:** Home shows mentor Quick Way, completion alerts, outreach shortcuts.
- **Student:** Home shows profile/travel alerts, classmates, **Ambassadors** carousel (other mentors — not self-admin view).

---

### Feature: Accept ambassador invitation

**What it is:** University staff invite users to **Ambassador** or **External Ambassador** via email.

**How to do it — step by step:**
1. Receive invitation email or in-app alert after login.
2. On alert, tap **Accept** (or **Do it later** → envelope icon on Home later).
3. If prompted, confirm **campus** assignment.
4. For **External Ambassador**, select **Ambassador Type** from lookup list.
5. Land on Home — likely with **profile completion alert**.
6. Tap alert → **My Profile** → complete **Ambassador Info**.

**What happens next:** Role becomes active; ambassador may appear in admin **Total Ambassadors** lists and on student **Ambassadors** carousel after profile completeness rules are met.

---

### Feature: Bottom navigation

| Tab | What the Ambassador does here |
|-----|--------------------------------|
| **Home** | Dashboard — alerts, Quick Way, shortcuts, events, banners |
| **Community** | Browse, join, and post in communities |
| **Chats** | Primary workspace — student conversations |
| **Profile** | Settings, FAQs, **My Profile** entry, logout |

**How to use it:** Tap tab icon; active tab highlighted.

---

## 3. Home — Ambassador Dashboard

### What it is

**Home** for Ambassador is an **API-driven overview dashboard** (same section pattern as coordinator roles: custom app bar, ordered sections). The server returns **mentor-focused** content — outreach stats and engagement shortcuts — not university governance panels.

**How to open it:** Tap **Home** (default after login as Ambassador).

**How to refresh:** Pull down on Home. Counts, carousels, and alerts reload.

---

### Feature: Custom app bar (university logo + name)

**What it is:** Leading block shows university **logo** (when available) and **full name**; trailing icons: **notification bell**, **pending invitation envelope** (when applicable).

**Why it matters:** Ambassadors always know which institution they represent when mentoring students.

**How to use it:**
1. Read logo + name at top of Home.
2. **Tap** university block → **University / Campus Details** (read-only).
3. **Bell** → **Notifications**.
4. **Envelope** (when shown) → **Pending Invitations**.

**Logo missing (wireframe):** Layout adjusts — name remains visible without broken empty image gap.

---

### Feature: Role tag and role switcher

**What it is:** Colored badge showing **“Ambassador”** or **“External Ambassador”**; switcher row when account has multiple roles.

**How to use it:** Tap switcher → **Role Selection** → confirm role → Home reloads for that role’s dashboard.

---

### Feature: Profile / Ambassador completion alert

**What it is:** Prominent banner when required profile sections — especially **Ambassador Info** — are incomplete.

**Why it matters:** Incomplete profiles are hidden or ranked lower on the student **Ambassadors** carousel.

**Typical alert types (wireframe / API):**

| Alert | Meaning | Tap action |
|-------|---------|------------|
| **Incomplete profile** | One or more profile sections unfilled | **My Profile** hub |
| **Incomplete Ambassador Info** | Public mentor section empty | **Ambassador Info** editor |
| **Low completion %** | Progress ring below threshold | **My Profile** |

**How to use it:**
1. Read title, description, and completion percentage.
2. Tap alert → **My Profile** or direct **Ambassador Info**.
3. Save required fields → return Home → pull to refresh → alert clears when backend marks complete.

---

## 4. Quick Way — stat cards

### What it is

**Quick Way** is a two-column grid of **count cards** (icon, number, label). Each card opens a related list or screen. Ambassador configs emphasize **messages and students**, not campus governance.

**Typical Ambassador Quick Way cards (validate labels in Figma):**

| Card label | Typical `viewKey` | What it means | Destination |
|------------|-------------------|---------------|-------------|
| **Total Messages** | `quick_way_total_messages` | Message / chat volume indicator | **Chats** inbox or messages hub |
| **Total Students** | `quick_way_total_students` | Students in ambassador browse scope | **Student list** |
| **Total Events** | `quick_way_total_events` | Campus events available | **All Events** list |
| **Total Communities** | `quick_way_total_community` | Communities at university | **Community browse** list |

**Cards NOT shown for Ambassador (wireframe):** Total Campus, Total Invites, University Super Admin, Third-Party Coordinators, Unassigned Students, Pending Events approval, Total Reports, etc.

**How to use Quick Way:**
1. Scroll to **Quick Way** on Home.
2. Tap a card.
3. Use **search** and **filter** on destination list.
4. Return via **Home** tab or back navigation.
5. Pull to refresh Home after significant chat activity.

---

### Total Messages

**What the user does:** Opens messaging to respond to student outreach.

**How to do it:**
1. Tap **Total Messages**.
2. Land on **Chats inbox** (or messages list per prototype hotspot).
3. Tap thread → reply.

---

### Total Students

**What the user does:** Browses students they may support (not admin user management).

**How to do it:**
1. Tap **Total Students**.
2. **Search** (typically ≥3 characters).
3. **Filter** by campus, program, intake, country, etc.
4. Tap row → **Student profile** (visibility-controlled) → **Chat**.

---

### Total Events / Total Communities

**What the user does:** Jumps to participation surfaces — browse events or communities.

**How to do it:** Tap card → respective list → tap item for details.

---

## 5. Quick Actions

### What it is

Shortcut tiles below Quick Way for one-tap navigation to frequent ambassador tasks.

**Typical Ambassador Quick Actions (wireframe):**

| Action label | Typical `actionId` | Purpose |
|--------------|-------------------|---------|
| **Events** | `viewEvents` | Campus events catalog |
| **Support** | `viewSupport` | Help / FAQ / contact |
| **My Profile** | `viewMyProfile` | Ambassador profile hub |
| **Chats** | `viewChats` (if configured) | Messaging inbox |

**How to use it:**
1. Locate **Quick Actions** section on Home.
2. Tap tile → complete task on destination.
3. Return via **Home** tab.

---

## 6. Dashboard content sections

Sections render **in API order**. Typical Ambassador Home includes:

### Banners

**What it is:** Horizontal promotional carousel (welcome campaigns, orientation week).

**How to use it:**
1. Swipe left/right through banners.
2. Tap banner or **CTA button** → linked screen or external URL.

---

### Upcoming Events carousel

**What it is:** Preview cards for near-future events.

**How to use it:**
1. Swipe through event cards on Home.
2. Tap card → **Event Details**.
3. Tap **View All** in section header → full upcoming events list.

**Empty state:** Section hidden or empty illustration when no events.

---

### My Events (optional section)

**What it is:** Events the ambassador already registered for.

**How to use it:** Swipe cards → tap → **Event Details** (registration status visible).

---

### Activities & Ads

**What it is:** Partner or sponsor tiles (housing, stores, career fairs).

**How to use it:** Swipe → tap tile → follow CTA / `action_url`.

---

**Sections usually NOT on Ambassador Home:** Pending Events approval queue, Events by Category admin chart, Manage Users, Unassigned Students, governance Quick Way grid.

---

## 7. My Profile — Ambassador profile hub

### What it is

The **My Profile hub** is a section list screen — the ambassador’s primary configuration surface. Sections load from the **ambassador profile form** (wireframe: `ambassadorForm`). This is **not** the admin read-only “basic details only” profile used by coordinator/admin roles.

**How to open:**
1. **Profile** tab → **My Profile**, **or**
2. Home **completion alert**, **or**
3. Quick Action **My Profile**.

**What the user sees:**
- **Profile header** — photo, name; tap photo to change image.
- **Section rows** — icon, title, completion indicator (filled / incomplete chevron).
- Optional **completion progress** summary.

---

### Section list — typical rows (API-driven per university)

| Section id (typical) | Display name | Purpose |
|----------------------|--------------|---------|
| `basicDetails` | Basic Details | Name, contact basics |
| `ambassadorInfo` | **Ambassador Info** | **Public mentor card** — mandatory for student visibility |
| `userPreferences` | Preferences | Food, hobbies, roommate prefs (if configured) |
| `contactInfo` | Contact Info | Address, emergency contact |
| `educationInfo` | Education | Program, year, qualifications |
| `documents` | Personal Documents | Upload slots (if configured for ambassadors) |
| `sharedByUniversity` | Shared by University | Read-only university-provided fields |

**Wireframe rule:** Exact section list and order come from the server — do not assume a fixed count.

---

### How to complete any profile section — step by step

1. Open **My Profile** hub.
2. Tap a section row (e.g. **Ambassador Info**).
3. Fill fields — text inputs, date pickers, lookup pickers, multi-select chips.
4. Tap **Save** on bottom bar (or **Next** when multi-section flow enabled).
5. If **Next** shown and edits unsaved: confirm **Save changes?** dialog.
6. Return to hub — row shows **completed** state.
7. Repeat until **Ambassador Info** and all required sections complete.

---

## 8. Ambassador Info — public mentor profile

### What it is

**Ambassador Info** is the **most important section** on the Ambassador Platform. Fields here drive what students see on the **Ambassadors carousel** and **public ambassador profile** screen.

**How to open:** My Profile → tap **Ambassador Info** row.

---

### Field-level behavior (typical wireframe fields)

| Field area | What the ambassador enters | Control type |
|------------|---------------------------|--------------|
| **About me / Bio** | Short introduction — how they help newcomers | Multi-line text |
| **Ambassador type** | Category (especially External Ambassador) | Lookup picker |
| **Academic year** | Current or graduated year | Lookup / picker |
| **Previous qualifications** | Background credentials | Lookup / text |
| **Favourite programs / faculties** | Programs they can advise on | Multi-select lookup |
| **Languages spoken** | Languages for international students | Multi-select |
| **Hobbies / interests** | Relatable personal tags | Multi-select chips |
| **Availability** | When they typically respond | Text or structured slots |
| **Contact preference** | In-app chat emphasis | Toggle or text |

**Lookup fields:** Tap row → search list (≥2 characters) → select value → returns to form.

**Multi-select:** Tap chips or checklist → **Apply** selection.

**How to save:**
1. Complete required fields (marked on wireframe).
2. Tap **Save**.
3. Success toast → section marked complete in hub.
4. Student-facing profile updates on next load.

**Validation:** Empty required fields block Save with inline errors.

---

## 9. Other profile sections (detail)

### Basic Details

**Purpose:** Core identity fields (name, email display, gender, DOB per tenant config).

**How to use:** My Profile → Basic Details → edit → **Save**.

---

### User Preferences

**Purpose:** Personal preferences (food, hobbies) — may appear on peer views where configured.

**How to use:** Tap section → fill pickers → **Save**.

---

### Contact Info

**Purpose:** Addresses, phone, emergency contact.

**How to use:** Tap section → complete sub-sections (permanent address, etc.) → **Save** per screen.

---

### Education Info

**Purpose:** Program, faculty, student number (for student ambassadors).

**How to use:** Tap section → lookup fields → **Save**.

---

### Personal Documents

**Purpose:** Document upload grid (if wireframe includes for ambassadors).

**How to use:**
1. Tap **Personal Documents**.
2. Tap empty **dashed slot** → camera or gallery.
3. Upload → slot shows thumbnail / reviewed state.
4. Tap existing doc → view or replace per wireframe.

---

### Shared by University

**Purpose:** Read-only fields populated by institution (scholarship flags, cohort tags).

**How to use:** View only — no Save bar.

---

### Profile photo (header)

**How to update — step by step:**
1. My Profile → tap **profile image** in header.
2. Choose **Camera** or **Gallery**.
3. **Crop** to circle/square per wireframe.
4. Confirm upload.
5. Header refreshes; student **Ambassadors** carousel image updates after refresh.

**Why it matters:** Photo is the first trust signal on student Home.

---

### Section Next flow (when enabled)

**What it is:** Nav bar **Next** moves through sections in backend order without returning to hub each time.

**How to use:**
1. Complete section → tap **Next**.
2. If unsaved edits → **Save changes?** → Save or Discard.
3. Land on next section until list complete.

---

## 10. Students — browse and support

### Student list screen

**What it is:** Directory of students the ambassador may view — entry from **Total Students** Quick Way.

**Screen elements (wireframe):**
- Navigation title (e.g. “Students”)
- **Search bar**
- **Filter** icon
- Paginated row list (photo, name, program/campus subtitle)

**How to find a student:**
1. Type in search (≥3 characters typical).
2. Tap **Filter** → select campus, program, country, languages, intake → **Apply**.
3. Scroll for pagination (load more on scroll).

**How to open profile:** Tap student row.

---

### Student profile (ambassador view)

**What the ambassador sees:**
- Header — photo, name, email
- **Section list** — only sections allowed by visibility rules (not full admin hub)
- **Chat** button — primary action
- **No** assign-student, suspend, or coordinator tools

**How to support a student:**
1. Open profile from list.
2. Read available sections for context.
3. Tap **Chat** → conversation screen.
4. Answer question; direct to **Support** or official channels when out of scope.

---

## 11. Chats

### Chats inbox screen

**What it is:** List of message threads with students and other users.

**How to open:** **Chats** tab, or **Total Messages** Quick Way.

**Screen elements:**
- Thread rows — avatar, name, last message preview, timestamp, unread badge
- Search (if wireframe provides)
- Empty state — “No messages yet” with nudge to complete profile

**How to use inbox:**
1. Open **Chats** tab.
2. Tap thread with unread badge.
3. Read history at top; newest at bottom.
4. Type in composer → **Send**.
5. Attach image/file if wireframe shows attachment icon.

---

### Conversation screen

**How to use:**
1. Scroll message history.
2. Type reply → Send.
3. Use back → return to inbox; thread moves to top with new preview.

**Typical ambassador scenarios:**
- Student tapped ambassador on Home carousel → **Chat**
- Housing, registration timeline, or orientation questions
- Follow-up after event or community interaction

**Boundaries:** No bulk messaging entire student body from ambassador role.

---

### Start chat from student profile

**How to do it:**
1. Student list → tap row → profile.
2. Tap **Chat**.
3. New or existing thread opens.

---

## 12. Events

### All Events list

**How to open:** Quick Action **Events**, **Total Events** Quick Way, or **Upcoming Events → View All**.

**How to use:**
1. Browse paginated list.
2. Search and filter (status, category, campus, date).
3. Tap row → **Event Details**.

---

### Event Details screen

**Typical content:**
- Hero image, title, date/time, location, description
- Registration window (open / closed)
- Capacity and spots remaining
- **Register** button when window open

**How to register — step by step:**
1. Open event from carousel or list.
2. Read details and registration dates.
3. Tap **Register**.
4. Confirm if dialog shown.
5. Success state — button changes to **Registered** or similar.
6. Event may appear under **My Events** on Home.

**Ambassador cannot:** Approve or reject pending events (staff roles).

---

## 13. Community

### Community tab — discover

**How to open:** **Community** tab in bottom bar.

**Typical sub-areas (wireframe):**
- **Explore / Discover** — browse all communities
- **My Communities** — joined groups
- **Feed** — aggregated posts (if configured)

---

### Community Profile screen

**How to use:**
1. Tap community from list or feed.
2. Read description, member count, cover image.
3. Tap **Join** if not a member.
4. After join: view **feed**, **members**, **about**.

---

### Posts and comments

**How to create a post:**
1. Open joined community.
2. Tap **Create post** or compose FAB.
3. Enter text; attach image if enabled.
4. Tap **Post** → appears in feed.

**How to engage:**
1. Tap post → **Post Detail**.
2. Read comments; add comment.
3. Report inappropriate content via report action if wireframe provides.

**Ambassador use case:** Welcome messages, answer FAQs in comments, point to official resources.

**Cannot do:** Approve pending community creation (University Super Admin / Community Coordinator).

---

## 14. Notifications

### Notifications list screen

**How to open:** **Bell** icon on Home app bar.

**Typical notification types:**
- New chat message
- Profile / Ambassador Info reminder
- Event reminder (starting soon)
- Community mention or reply
- Role invitation

**How to use:**
1. Scroll notification list.
2. Tap row → deep link to **Chat**, **My Profile**, **Event Details**, or **Invitation** screen.
3. Mark read implicitly on open (per wireframe).

---

## 15. Pending invitations

**How to open:** **Envelope** icon on Home (after deferring invite at login).

**How to use:**
1. View pending role invitations list.
2. Tap invite → **Accept** or **Decline**.
3. On accept: role added; switch via role switcher if needed.

---

## 16. Support

### Support screen

**How to open:** Quick Action **Support** on Home.

**What it is:** FAQs, policy links, or contact paths for questions outside ambassador scope (visa, conduct, official holds).

**When ambassadors use it:** Direct students to Support rather than giving unofficial legal or policy advice.

---

## 17. University and campus details

**How to open:** Tap **university logo + name** on Home app bar.

**What the user sees:** University name, logo, campus list or assigned campus detail, descriptive copy from wireframe.

**Purpose:** Context only — read-only for ambassadors.

---

## 18. Profile tab — settings and account

**How to open:** **Profile** tab (not the same as **My Profile** hub — Profile tab is account menu).

| Menu item | What the user does |
|-----------|-------------------|
| **My Profile** | Opens ambassador profile hub (Section 7) |
| **Settings** | App preferences |
| **Language** | Change app language → confirm → **Save** if wireframe stages changes |
| **FAQs** | Read help articles |
| **About App** | Version and legal info |
| **Logout** | Sign out → confirm dialog |
| **Delete account** | Remove own account → confirm (if wireframe shows) |
| **Switch role** | Change to Student or other assigned role |

---

## 19. How students discover ambassadors (platform loop)

Understanding the **student-facing** path explains why **Ambassador Info** matters.

**Student path — step by step:**
1. Student logs in → **Student Home** dashboard.
2. Student scrolls to **Ambassadors** section (horizontal carousel).
3. Student sees cards — **photo, name, short descriptor** (from Ambassador Info).
4. Student taps card → **Public Ambassador Profile** (read-only mentor view).
5. Student taps **Chat** → thread with this ambassador.
6. Ambassador receives notification → replies in **Chats** tab.

**Optional:** Student taps **View All** on Ambassadors section → **Ambassador List** → search/filter → profile → chat.

**Implication:** Empty **Ambassador Info**, missing photo, or incomplete profile reduces carousel visibility per product rules.

---

## 20. Public ambassador profile (student view)

**What it is:** Read-only screen students see — not the editable My Profile hub.

**Typical content shown:**
- Profile photo and name
- Bio / about me
- Programs, languages, interests
- **Chat** CTA (primary)
- No edit controls

**Ambassador action:** Keep Ambassador Info accurate so this screen builds trust.

---

## 21. End-to-end flows (playbooks)

### Flow A — New ambassador: first day

1. Accept invitation → login as **Ambassador**.
2. Home shows **completion alert** → tap.
3. **My Profile** → upload **photo**.
4. Open **Ambassador Info** → fill bio, languages, programs → **Save**.
5. Complete any other required sections.
6. Pull to refresh Home → alert cleared.
7. Open **Chats** → respond to waiting students.
8. Optional: register for **Upcoming Event**.

---

### Flow B — Answer a student question

1. Notification or **Chats** tab → open thread.
2. Read question fully.
3. Reply with clear next steps and links in prose.
4. If out of scope: mention **Support** or official coordinator channels.
5. Leave thread open for follow-up.

---

### Flow C — Student + Ambassador dual role

1. Morning: role switcher → **Student** → update travel plan.
2. Afternoon: switcher → **Ambassador** → answer chats.
3. Verify Home content matches role (no student travel alerts on ambassador Home).

---

### Flow D — Update mentor info after program change

1. My Profile → **Ambassador Info**.
2. Edit program and language fields.
3. **Save** → public student profile updates.

---

### Flow E — Event engagement

1. Home → **Upcoming Events** → tap event.
2. **Register**.
3. Post in related **Community** welcoming attendees.
4. Answer registration questions in **Chats**.

---

## 22. Search, filter, and pagination

### Search
- Minimum character threshold (often 3) before API call.
- Debounced input on lists.
- Clear search restores full list.

### Filter
1. Tap **filter icon** on list.
2. Sidebar categories (Campus, Program, Country, Role, etc.).
3. Checkbox multi-select + **Apply**.
4. **Clear All** resets filters.

### Pagination
- Infinite scroll on long student/event lists.
- Pull to refresh on Home and list screens.

---

## 23. Permissions and boundaries

**Ambassador Platform — can (typical):**
- Complete own ambassador profile (`ambassadorForm`).
- Publish **Ambassador Info** for student discovery.
- Chat with students in scope.
- Browse students, events, communities (tenant permissions).
- Register for events; post in joined communities.
- Switch to Student role on same account.

**Ambassador Platform — cannot (typical):**
- Invite or suspend users.
- Assign students to sub-coordinators.
- Approve/reject events or communities.
- Access Manage Users, Add User, or governance Quick Way.
- Edit other users’ profiles (guidance via chat only).
- Cross-university administration.

---

## 24. Empty states and errors

| Situation | Expected UX |
|-----------|-------------|
| No upcoming events | Section hidden or empty illustration |
| No chats yet | Empty inbox + encourage profile completion |
| Incomplete Ambassador Info | Persistent Home alert |
| Network error on Save | Toast; remain on editor; retry Save |
| Validation on required field | Inline error; Save blocked |
| Logo URL missing | App bar shows name only — no layout break |

---

## 25. Screen list (complete inventory)

| Screen | How the user gets there |
|--------|-------------------------|
| Login | App launch |
| Role Selection | Multi-role login or role switcher |
| Invitation alert | First login after invite |
| Ambassador Home | Home tab after login as Ambassador |
| University / Campus Details | Tap university header on Home |
| Notifications list | Bell on Home |
| Pending Invitations list | Envelope on Home |
| My Profile hub | Profile tab, alert, or My Profile quick action |
| Ambassador Info editor | Tap Ambassador Info row |
| Basic Details editor | Tap section row |
| Preferences editor | Tap section row |
| Contact Info editor | Tap section row |
| Education editor | Tap section row |
| Personal Documents | Tap section row |
| Shared by University | Tap section row (read-only) |
| Photo picker / crop | Tap header photo |
| Student list | Total Students Quick Way |
| Student profile (ambassador view) | Tap student row |
| Chats inbox | Chats tab or Total Messages |
| Conversation thread | Tap inbox row |
| All Events list | Events action, Total Events, View All |
| Event Details | Tap event card or row |
| Community Discover | Community tab |
| Community Profile | Tap community |
| Post Detail | Tap post in feed |
| Create Post | Compose action in community |
| Support | Support quick action |
| Profile tab menu | Profile tab |
| Settings / Language / FAQs / About | Profile tab sub-items |
| Public Ambassador Profile | Student taps carousel card (cross-role) |
| Ambassador List (student View All) | Student Home → View All |

---

## 26. Figma validation checklist (Ambassador frames, page 5051:661)

On the [Ambassador prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661), confirm every frame:

- [ ] Login and Role Selection (Ambassador / External Ambassador)
- [ ] Invitation accept and defer (envelope) flows
- [ ] Ambassador Home — app bar, role tag, role switcher
- [ ] Profile completion alert — copy, progress ring, tap destination
- [ ] Quick Way — each card label, icon, count, hotspot
- [ ] Quick Actions — Events, Support, My Profile, Chats
- [ ] Banners, Upcoming Events, My Events, Activities & Ads
- [ ] My Profile hub — section list and completion states
- [ ] Ambassador Info — every field, lookup, validation, Save
- [ ] Other profile sections — Basic Details, Preferences, Contact, Education, Documents
- [ ] Profile photo — pick, crop, upload, error states
- [ ] Section Next flow and unsaved-changes dialog
- [ ] Student list — search, filter, pagination, empty state
- [ ] Student profile — sections shown, Chat CTA, no admin actions
- [ ] Chats inbox and conversation — send, attachment, empty state
- [ ] Events list, Event Details, Register, registered state
- [ ] Community tab — discover, join, feed, create post, post detail
- [ ] Notifications list and deep links
- [ ] Support screen
- [ ] Profile tab — settings, language, logout
- [ ] Student-facing: Ambassadors carousel, View All list, public profile, Chat
- [ ] External Ambassador — ambassador type field and labels
- [ ] Dual role: Student Home vs Ambassador Home side-by-side

---

## 27. Document history

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | Jun 2026 | Initial Ambassador guide |
| 2.0 | Jun 2026 | Expanded **Ambassador Platform** guide — every screen and flow on page 5051:661 |

---

## Related docs

- `docs/Ambassador-Client-Demo-Guide.md`
- `docs/Ambassador-QA-Test-Guide.md`
- `docs/Student-Features-and-Flows.md` (student Ambassadors carousel)
- `docs/University-Super-Admin-Features-and-Flows.md` (inviting ambassadors)

*Design: [Figma — page 5051:661](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0) · [Prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661)*
