# Intoto — Community Coordinator
## Features & Flows (User Guide)

**Design reference:** [Intoto Wireframe — Community Coordinator (node 5088-26466)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5088-26466&page-id=5051%3A661)  
**Prototype (walkthrough):** [Community Coordinator prototype — start 5088-26466](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5088-26466&p=f&t=SHs6dnxTAjeaxqN7-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5088%3A26466)  
**Role:** Community Coordinator (`community_coordinator`)  
**Audience:** Product, Engineering, QA, Client demos  
**Version:** 1.0  
**Last updated:** Jun 2026

---

## About this document

This guide explains **what a Community Coordinator can do in Intoto**, **why each capability exists**, and **how to complete every step** in the product. It uses the same structure as the Student, Ambassador, Event Coordinator, University Super Admin, and Third Party Coordinator documentation.

**Note on Figma:** The [Community Coordinator prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5088-26466&p=f&t=SHs6dnxTAjeaxqN7-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5088%3A26466) requires sign-in. Start at node **5088-26466** on page **5051:661** and walk each connected frame. Compare copy, spacing, empty states, and actions to this document. Content reflects the Community Coordinator wireframe scope (community lifecycle, approvals, membership, moderation, overview dashboard) and is **not** derived from application source code.

---

## 1. Who is the Community Coordinator?

### What this role is

The **Community Coordinator** is university staff responsible for **groups and social spaces** on Intoto: reviewing community creation requests, publishing official communities, monitoring active groups, and keeping conversations appropriate. They are the operational owner of **community quality and safety** within one university.

Students create communities that often need **approval** before going live. The Community Coordinator is the role that reviews those requests, approves legitimate groups, and rejects ones that violate policy. They may also **create communities directly** that go live immediately (unlike the student submission flow).

### What they typically do day to day

- Open **Home** and review **Quick Way** counts (total communities, members, pending queue)
- Process **pending community** requests — approve or reject with a clear reason
- Browse **active communities**, open profiles, and scan feeds for issues
- **Create** official communities (program houses, international student association, etc.)
- Handle **reports** or moderation tasks linked to community content (when configured)
- Use **Chats** and **Support** for escalations
- Optionally browse **events** as a participant (not as primary job)

### How this role differs from others

| Topic | Community Coordinator | Event Coordinator | University Super Admin |
|-------|----------------------|-------------------|------------------------|
| Primary focus | Communities & membership | Events & registrations | Full university operations |
| Approves pending communities | Yes (primary) | No (typical) | Yes |
| Approves pending events | No (typical) | Yes (primary) | Yes |
| Manage Users / invites | No (typical) | No | Yes |
| Assign students to coordinators | No | No | Yes |
| Student creates community | Submitted for approval | N/A | N/A |

---

## 2. Getting into the app

### Feature: Login

**What the user does:** Authenticates with university credentials so the app can load their role and dashboard configuration.

**How to do it:**
1. Open Intoto.
2. Sign in with email/password or SSO.
3. Wait for the profile and role payload to finish loading.

**What happens next:**
- **Only Community Coordinator role:** Lands on **Home** (Community Coordinator dashboard).
- **Multiple roles:** **Role Selection** appears — choose **Community Coordinator**.
- **New role invite:** May show an invitation alert — **Accept** now or **Do it later** (later: envelope icon on Home).

---

### Feature: Role selection (multiple roles only)

**What it is:** One person may also be Student, Ambassador, Event Coordinator, or admin. Role selection switches which dashboard and permissions apply.

**How to do it:**
1. At login, select **Community Coordinator**, **or**
2. On Home, tap the **role switcher** row, **or**
3. Open **Profile** tab → switch role.

**What happens next:** Home reloads with community-centric Quick Way cards and sections — not student travel alerts or event approval queues unless that role is selected.

---

### Feature: Bottom navigation

| Tab | Purpose for Community Coordinator |
|-----|-------------------------------------|
| **Home** | Operational dashboard — stats, shortcuts, pending/active community previews |
| **Community** | Primary workspace — discover, create, feeds, membership |
| **Chats** | Direct messages with students and staff |
| **Profile** | Account settings, own profile, logout |

**How to use it:** Tap an icon; the active tab is highlighted.

---

## 3. Home — Community Coordinator Dashboard

### What it is

**Home** is an **API-driven overview dashboard**. The server sends an ordered list of sections (custom app bar, Quick Way, Quick Actions, community carousels, banners, analytics). The app renders only what this role is allowed to see.

**How to open it:** Tap **Home** after login as Community Coordinator.

**How to refresh:** Pull down on the dashboard. Counts and carousels reload from the server.

---

### Feature: Custom app bar (university logo + name)

**What it is:** A branded top bar: university **logo** (when the API provides one) and **full name** on the left; **notification bell** and **pending invitation** icon on the right when applicable.

**Why it matters:** The coordinator always works in the correct institutional context — especially important when moderating user-generated group names and descriptions.

**How to use it:**
1. Confirm logo and name match the university you support.
2. **Tap** the university block → **University / campus details** (read-only reference).
3. **Bell** → **Notifications** (new community requests, reports, chats).
4. **Envelope** → **Pending Invitations** (deferred role invites).

**When logo is missing:** The layout should still show the university name without awkward empty space (wireframe: adaptive header).

---

### Feature: Role switcher (multi-role accounts)

**What it is:** A row under the header showing the active role (e.g. “Community Coordinator”) with a chevron to change role.

**How to use it:** Tap → **Role Selection** → pick another role → Home content updates.

---

## 4. Quick Way (stat cards)

### What it is

**Quick Way** displays **numeric summary cards** — each with icon, count, and label. Tapping a card opens the full list or screen behind that metric. For Community Coordinator, these metrics center on **groups and members**, not events or student assignment.

**Typical Community Coordinator Quick Way cards (confirm labels in Figma):**

| Card (typical label) | `viewKey` (typical) | What the number represents | What happens when you tap |
|----------------------|---------------------|------------------------------|---------------------------|
| **Total Communities** | `quick_way_total_community` | All communities in scope (pending, active, and archived per backend rules) | Opens the **full community catalog** with search and filter |
| **Total Community Members** | `quick_way_total_community_members` | Aggregate membership count across communities (or member records — per tenant definition) | Opens **members** or **community–member** exploration list |
| **Pending Communities** | `quick_way_pending_communities` (or pending section) | Communities awaiting approval | Opens **pending approval queue** |
| **Active / Approved Communities** | `quick_way_approved_communities` or active stat | Communities live for students | Opens **active communities** list |

**Cards usually NOT shown for Community Coordinator:** Total Students (full roster admin), Unassigned Students, Total Invites, University Super Admin, Third Party Coordinator counts, Total Events (unless dual-purpose tenant).

**How to use Quick Way well:**
1. Start the day with **Pending Communities** — clear the queue so student requests are not delayed.
2. Use **Total Communities** for spot checks on growth and naming consistency.
3. Use **Total Community Members** to understand engagement scale before planning official groups.
4. Pull to refresh after bulk approvals so counts stay accurate.

### Quick Way routing reference

| `viewKey` | Typical destination |
|-----------|---------------------|
| `quick_way_total_community` | All communities list |
| `quick_way_total_community_members` | Community members list or hub |
| `quick_way_pending_communities` | Pending communities list |
| `quick_way_approved_communities` | Active communities list |

Additional keys may appear in API config — use the card title until product publishes a full map.

---

## 5. Quick Actions

### What it is

**Quick Actions** are large shortcut tiles for tasks you run many times per week — faster than drilling through stat cards.

**Typical Community Coordinator Quick Actions:**

| Action (typical label) | `actionId` / `viewKey` (typical) | What it is for |
|------------------------|----------------------------------|----------------|
| **Communities** | `viewCommunities` / community route | Jump straight to community discovery or management hub |
| **Create Community** | `createCommunity` | Start official community creation (often **instant publish**) |
| **Support** | `viewSupport` | Policy questions, technical help, escalation paths |
| **Events** (optional) | `viewEvents` | Browse campus events as participant — secondary to community work |

**How to use it:**
1. Locate the Quick Actions block on Home.
2. Tap the tile that matches your task.
3. Complete the flow on the destination screen.
4. Return via **Home** tab or back navigation.

---

## 6. Dashboard community sections (carousels)

Many Community Coordinator Home layouts show **horizontal carousels** — swipeable previews with **View All** in the section header.

### Pending Communities (carousel)

**What it means:** Student- or staff-submitted community requests that are **not yet public**. Each card summarizes the proposed name, description snippet, and submitter context (per wireframe).

**What the user does:**
1. Swipe through pending cards on Home.
2. Tap a card → **Community request details** (full description, images, settings).
3. **Approve** to make the community live, or **Reject** with a mandatory reason.
4. Tap **View All** → full pending list for batch processing.

**Why it matters:** This is the main safety gate before a group appears in student discovery.

---

### Active / Approved Communities (carousel)

**What it means:** Communities already **live** on the platform — students can find, join, and post (subject to community rules).

**What the user does:**
1. Swipe active community cards.
2. Tap → **Community Profile** (about, members, feed entry).
3. Tap **View All** → searchable active list.
4. Monitor high-risk groups or unusually fast growth from here.

---

### Community analytics (graph section — when shown)

**What it means:** A chart on Home — for example **communities by category**, **members over time**, or **posts activity** (exact chart type per Figma).

**What the user does:**
1. Scroll to the analytics section after Home loads.
2. Read the chart title and subtitle (API may send `viewSubtitle`).
3. Use insights to plan official communities or staffing (e.g. more moderators for large groups).
4. Open full analytics from a linked Quick Way card if the wireframe provides one.

---

## 7. Banners and Activities & Ads

### Banners

**What it is:** University promotional carousel on Home (welcome campaigns, mental health week, etc.).

**How to use it:** Swipe horizontally → tap CTA or card → in-app destination or browser link.

### Activities & Ads

**What it is:** Partner or sponsor tiles with the same interaction pattern as banners.

**How to use it:** Swipe → tap → follow the advertised destination.

These sections do not replace community operations; they keep coordinators aware of campus campaigns that may drive new group creation requests.

---

## 8. Community list — search, filter, pagination

### All Communities

**What it is:** The full catalog behind **Total Communities** Quick Way or **Communities** quick action.

**How to do it:**
1. Open the list.
2. **Search** by community name (typically 3+ characters, debounced).
3. Open **Filter** → status (pending / active / rejected), category, campus, date submitted, etc. (API-driven).
4. **Apply** → list updates; **Clear** resets filters.
5. Tap a row → **Community Profile**.

**Pagination:** Scroll to load more rows; pull down to refresh from page one.

---

## 9. Community request details — approve and reject

### What it is

The detail screen for a **pending** community request — everything needed to make a governance decision.

**What the user typically reviews:**
- Proposed **name** and **description**
- **Profile and cover** images
- **Category** or tags
- **Visibility** settings (public / campus-scoped — per wireframe)
- **Submitter** identity (student or staff)
- Submission **date**

---

### Approve a pending community — step by step

1. Open the request from **Pending Communities** on Home or from the pending list.
2. Read the name and description for policy compliance (hate speech, impersonation, duplicate official groups, etc.).
3. Confirm images and settings are appropriate.
4. Tap **Approve**.
5. Confirm in the dialog if the wireframe requires it.
6. Success feedback appears; the card leaves the pending queue.
7. The community becomes discoverable to students in **Community** tab / discovery lists.
8. Pull to refresh Home — pending count decreases, active count increases.

**Outcome for students:** The creator receives a notification that the community is **live** (wording per product copy). They can invite members and post.

---

### Reject a pending community — step by step

1. Open the pending request.
2. Tap **Reject**.
3. Enter a **clear, actionable reason** (e.g. “Name too similar to official International Students society — please rename and resubmit”).
4. Submit — validation must block empty reasons.
5. The request leaves the public queue; submitter can fix and resubmit per policy.

**Outcome for students:** They see rejection reason and can edit and submit again — they do **not** get a live community until approved.

---

## 10. Create a community (Community Coordinator)

### What it is

Official communities created by staff — often **published immediately** without the student 24-hour approval wait.

**How to do it:**
1. **Community** tab → **Create Community**, **or** Home → **Create Community** quick action.
2. Enter **name** and **description** (required).
3. Upload **profile** and **cover** images if required.
4. Complete additional fields (category, campus, rules, visibility).
5. Tap **Submit**.

**What happens next:** Success message such as **“Community created successfully!”** — community is **active** immediately. Students see it in discovery without waiting for coordinator self-approval.

**Why it differs from student create:** The university vouches for official groups; the coordinator is already a trusted publisher.

---

## 11. Community Profile — day-to-day management

### What it is

The hub for one community: branding, about text, member list, and feed.

**How to open:** Tap any community from a list, carousel, or **Community** tab.

**What the Community Coordinator typically does here:**

| Area | Actions |
|------|---------|
| About | Read description and settings; edit if wireframe allows staff edit |
| Members | View member list; search members; remove member if moderation tools exist |
| Feed | Scroll posts; open post detail; hide/delete post if moderation exists |
| Join state | Join as member to monitor student experience (optional) |
| Settings | Edit visibility, posting rules, or images (if permitted) |

---

## 12. Posts and feed moderation

### Browse posts

**How to do it:**
1. **Community** tab → open a community.
2. Scroll the **feed**.
3. Tap a post → **Post detail** (full text, media, comments).

### Create a post (as coordinator)

**When useful:** Pin welcome messages, policy reminders, or official announcements in university-run groups.

**How to do it:**
1. Inside a community you belong to → **Create post**.
2. Compose text and attach media per wireframe.
3. Publish → post appears in feed.

### Moderate content (when tools exist)

**What the user does:**
1. Open violating post or comment.
2. Choose **Remove**, **Hide**, or **Report upstream** per policy.
3. Optionally message the member via **Chat** or escalate via **Support**.

**Coordination with reports:** Serious cases may also appear in a **Reports** queue (see Section 14).

---

## 13. Community tab (primary workspace)

### What it is

The **Community** tab is where coordinators spend most of their time outside Home — discovery, creation, and feeds mirror the student experience but with **staff powers**.

**Typical sub-areas (per wireframe):**
- **Discover** — find all live communities
- **My communities** — groups you joined or manage
- **Create** — new official community
- **Feed** — aggregated or per-community timelines

**How to use it daily:**
1. Open **Community** tab each morning.
2. Check **Discover** for unexpected new live groups after overnight approvals.
3. Open high-activity communities and scan feeds.
4. Create or update official groups as the academic calendar changes.

---

## 14. Reports (community moderation — when configured)

### What it is

User-generated **reports** flag inappropriate posts, comments, or behavior. Community Coordinator may receive community-related cases (exact queue per tenant).

**How to open:** Quick Way **Total Reports** / **My Assigned Reports** if shown on Community Coordinator Home — otherwise from a moderation entry in Community or Profile tools.

**How to work a report:**
1. Open the report from the list.
2. Read reporter, reported content, timestamp, and community context.
3. Move status through the workflow:

| Status | Meaning |
|--------|---------|
| **Assigned** | In someone’s queue |
| **Under Review** | Being investigated |
| **Escalated** | Needs senior / USA attention |
| **Resolved** | Closed with outcome documented |

4. Take action on content (remove post, warn user) per policy.
5. Set **Resolved** when complete.

---

## 15. Events (secondary)

### What it is

Community Coordinators may **browse and register** for events like other staff — this is not their primary dashboard focus.

**How to open:** Quick Action **Events** or an **Upcoming Events** carousel if present on Home.

**Typical use:** Promote an official community event in a post, or register to attend a fair — not to approve pending events (Event Coordinator role).

---

## 16. Chats (tab)

### What it is

Direct messaging with students, creators, and staff about community decisions.

**How to use it:**
1. Tap **Chats** tab.
2. Open threads — especially creators whose communities were rejected (explain reason kindly).
3. Reply with policy-aligned guidance.

**Typical scenarios:**
- Student asks why a group was rejected
- Clarify naming rules before resubmission
- Coordinate with USA on escalated cases

---

## 17. Profile (tab)

### What it is

Account-level settings. Community Coordinator **own profile** is typically **read-only basic details + photo** (admin-style), not the full student or ambassador section hub.

**How to use it:**
1. Tap **Profile**.
2. View account info; open FAQs, terms, privacy.
3. **Logout** when finished.

---

## 18. Notifications and invitations

### Notifications

**How to open:** Bell on Home app bar.

**Typical notification types:**
- New community submission pending approval
- Report assigned to you
- Community membership milestones
- Chat messages
- Role invitations

**How to use:** Tap a row → navigates to pending request, community profile, report, or chat.

### Pending invitations

**How to open:** Envelope icon after deferring a role invite.

**How to use:** Accept or decline additional roles on the account.

---

## 19. Support

**How to open:** **Support** quick action on Home.

**When to use:** Legal/policy questions, technical failures on approve/reject, disputes that exceed coordinator authority — document the case and escalate.

---

## 20. Student-facing impact (for demos and UAT)

| Coordinator action | Student experience |
|--------------------|-------------------|
| Approve pending community | Group appears in discovery; creator can post and invite |
| Reject pending community | Group stays hidden; creator sees reason and may resubmit |
| Create official community | Immediately visible — no approval wait |
| Remove post / member (if tool exists) | Content disappears or member loses access per rules |

---

## 20A. Community feature — overview, roles & workflows

The **Community** feature allows users to create and participate in topic-based discussions. Community Coordinators (and University Super Admins on web) create or approve communities; students propose communities for approval; Third-Party Coordinators can request communities, join approved ones, and receive join suggestions. Feeds show the **latest post**. Members can like, comment, share, initiate chat, and view profiles (Chat module permitting).

### Roles & permissions

#### Community Coordinator

- Create communities on various topics (instant publish).
- Review and approve/reject community creation requests from students or other roles.
- Moderate discussions and remove inappropriate content.
- Delete or archive communities if necessary.
- See community feeds with the latest post; like, comment, and share.
- Initiate chat with users and view profiles.
- Handle requests and reports.
- Operate as a **team** — any number of Community Coordinators can share the work.

#### Student

- Create community requests that go for approval (not live until approved).
- Join approved communities and participate in discussions.
- Post content and view posts in joined communities.
- Feeds show the latest post; like, comment, and share.
- Initiate chat with users and view profiles.

#### Third-Party Coordinator

- Create community requests that go for approval.
- Join approved communities and participate; receive **suggestions** for joining relevant communities.
- Post content in joined communities.
- Feeds show the latest post; like, comment, and share.
- Initiate chat with users and view profiles.

#### University Super Admin (web)

- Create communities instantly and clear the pending approval queue.
- Moderate from the web Community module (university-wide oversight).

### Community creation workflow

**Coordinator / Super Admin creation:** Create → community publishes instantly → visible to relevant roles (Students, Third-Party Coordinators).

**Student or Third-Party Coordinator request:** Submit request → pending queue → **Approve** (community live + notify) or **Reject** (notify with reason; community not live).

### Participation & engagement

| Area | Behaviour |
|------|-----------|
| Joining | Students and Third-Party Coordinators browse and join approved communities; TPC may get join suggestions |
| Posting | Members post, comment, like, and share; coordinators moderate inappropriate content |
| Feed | Communities feeds show the latest post |

### Visibility & notifications

Once created or approved, a community is visible to relevant users. Users receive notifications when:

- A new community is available.
- A post is made in a joined community.
- Their community creation request is approved or rejected.

---

## 21. End-to-end flows (playbooks)

### Flow A — Morning pending queue

1. Login as Community Coordinator → Home.
2. Note **Pending Communities** count on Quick Way.
3. Open pending list → review each request.
4. Approve compliant groups; reject others with specific reasons.
5. Pull to refresh → counts update.

### Flow B — Launch an official community

1. Quick Action **Create Community**.
2. Complete form with official branding.
3. Submit → success → community live.
4. **Community** tab → open group → publish welcome post.
5. Optional: link event in post if Events carousel relevant.

### Flow C — Handle a policy violation

1. Notification or Reports → open case.
2. Open reported post in community context.
3. Remove content and set report **Resolved**.
4. Chat creator if education is required; escalate to USA if severe.

### Flow D — Student submission happy path

1. (Student) Submits community → pending message.
2. (Coordinator) Approves from pending queue.
3. (Student) Receives approval notification → community live.
4. UAT: Student finds group in **Community** discover.

---

## 22. Search, filter, and pagination

**Search:** Type community name (threshold often 3 characters); debounced API; clear field restores list.

**Filter:** Sidebar categories + checkboxes; **Apply** commits; **Clear All** resets.

**Pagination:** Infinite scroll on long lists; pull-to-refresh reloads page one.

---

## 23. Permissions and boundaries

**Community Coordinator can (typical):**
- Approve/reject pending communities in scope.
- Create official communities with immediate publish.
- Browse all communities and members (scoped).
- Moderate posts/members when tools are enabled; delete or archive communities.
- Like, comment, share posts; chat with users; view profiles.
- Work community-related reports assigned to them.
- Share the queue with any number of other Community Coordinators.
- Chat and use Support.

**Community Coordinator cannot (typical):**
- Approve/reject **events** (Event Coordinator).
- **Manage Users** — invite, suspend, bulk email (USA).
- Assign students to sub-coordinators (Third Party Coordinator).
- Cross-university administration.

---

## 24. Empty states and errors

| Situation | Expected UX |
|-----------|-------------|
| No pending communities | Empty queue message; celebrate or show illustration |
| No active communities yet | Empty discover state with guidance |
| Reject without reason | Validation error; cannot submit |
| Network error on Home | Toast/banner; retry via pull-to-refresh |
| Duplicate community name | Server or inline error on create/approve |

---

## 25. Screen list

| Screen | How the user gets there |
|--------|-------------------------|
| Community Coordinator Home | Home tab after login |
| All communities list | Total Communities Quick Way or Communities action |
| Pending communities list | Pending Quick Way or carousel View All |
| Active communities list | Approved stat or carousel View All |
| Community request details | Tap pending card/row |
| Create community form | Create quick action or Community tab |
| Community Profile | Tap community row/card |
| Post detail | Tap post in feed |
| Reports list / detail | Reports Quick Way (if configured) |
| Chats | Chats tab |
| Notifications | Bell on Home |
| Support | Support quick action |
| University details | Tap university header |

---

## 26. Figma validation checklist (node 5088-26466)

On the [Community Coordinator prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5088-26466&p=f&t=SHs6dnxTAjeaxqN7-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5088%3A26466), confirm:

- [ ] Home — app bar, Quick Way, Quick Actions
- [ ] Pending Communities carousel + list + approve/reject
- [ ] Active Communities carousel + list
- [ ] Community analytics section (if present)
- [ ] Create Community — instant success path
- [ ] Community Profile — members, feed, settings
- [ ] Post create and moderation actions
- [ ] Reports workflow (if in role)
- [ ] Community tab discover / my communities
- [ ] Chats, Profile, Support, notifications
- [ ] Role switcher and empty states

---

## 27. Document history

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | Jun 2026 | Initial Community Coordinator guide — Figma 5088-26466 |

---

## Related docs

- `docs/Community-Coordinator-Client-Demo-Guide.md`
- `docs/Community-Coordinator-QA-Test-Guide.md`
- `docs/Student-Features-and-Flows.md` (student create community → pending)
- `docs/University-Super-Admin-Features-and-Flows.md` (oversight of all communities)
- `docs/Event-Coordinator-Features-and-Flows.md` (events — separate role)

*Design: [5088-26466](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5088-26466&page-id=5051%3A661) · Prototype: [5088-26466](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5088-26466&p=f&t=SHs6dnxTAjeaxqN7-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5088%3A26466)*
