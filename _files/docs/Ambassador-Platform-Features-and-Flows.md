# Intoto — The Ambassador Platform
## Features & Flows (User Guide)

**Design reference:** [Intoto Wireframe — The Ambassador Plateform (page 5051:661)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)  
**Primary desktop frame:** [All Ambassadors — 5104:244443](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5104-244443&page-id=5051%3A661)  
**Product:** Ambassador Platform (web) — **not** the in-app iOS Ambassador role  
**Audience:** Product, Engineering, QA, Client demos  
**Version:** 1.0  
**Last updated:** Jun 2026

---

## About this document

This guide documents **The Ambassador Platform** — a **web experience** where prospective and current students **discover university ambassadors**, read profiles, start **individual or group chats**, and browse FAQs. Content is sourced from Figma page **5051:661** (*The Ambassador Plateform*) via the Intoto Figma wireframe file.

**Important:** This is separate from:
- **In-app Ambassador role** (`docs/Ambassador-Features-and-Flows.md`) — peer mentor inside the mobile app
- **University / Intoto Admin roles** — operational governance

**Responsive layouts in Figma:**
| Breakpoint | Typical frame width | Examples |
|------------|---------------------|----------|
| Desktop | 1920px | All Ambassadors, Chat, Signup |
| Tablet | 1280px | All Ambassadors, Login, Chat variants |
| Mobile | 412px | All Ambassadors, Chat Detail, Profile |

**Design tokens (from Figma):**
- Primary / Secondary action: `#02A3CA`
- Online indicator: `#3DC076`
- Box / message background: `#F4F6F8`
- Font: Inter

---

## 1. What is The Ambassador Platform?

### What it is

A **public-facing web portal** branded **“Student Ambassadors”** with **Powered by Intoto** in the header. Visitors and enrolled users can:

- **Sign up / log in** with email and password
- **Verify email** before full access
- **Create a basic profile** after registration
- **Browse ambassadors** with search and category filters
- Open **ambassador cards** and **full profile** detail
- **Start individual chat** with an ambassador
- Join **group chats** (program/cohort communities)
- Read **Ambassador FAQ** accordion content
- Manage **own profile**, **logout**, or **delete account**

### Who uses it

| User | Goal |
|------|------|
| **Prospective student** | Learn about campus life; chat with ambassadors before applying |
| **Incoming student** | Ask visa, housing, orientation questions |
| **Ambassador (mentor)** | Appears as a card; receives chats (profile managed elsewhere) |
| **Staff ambassador** | Shown with **Staff** badge on cards and in chat |

### How it differs from the mobile app

| Topic | Ambassador Platform (web) | Intoto mobile app |
|-------|---------------------------|-------------------|
| Surface | Browser — 1920 / 1280 / 412 layouts | iOS/Android native app |
| Primary job | Discover & chat with ambassadors | Full university lifecycle (profile, travel, communities, etc.) |
| Navigation | Header: Chat icon, Profile icon, Powered by Intoto | Bottom tabs: Home, Community, Chats, Profile |
| Auth | Email/password signup, email verification | Auth0 / university SSO |
| Ambassador directory | Full-page search + filters + FAQ | Student Home **Ambassadors** carousel |

---

## 2. Global chrome (header)

Present on **All Ambassadors**, **Chat**, **Ambassadors Profile**, **Logout**, and related logged-in screens.

| Element | Label / behavior |
|---------|------------------|
| **Page title** | **Student Ambassadors** (H1, 32px bold) |
| **Subtitle** | *Discover real insights from students, alumni ambassadors, and university representatives…* |
| **Chat icon** | Opens **Chat** (`chat` frame) — inbox for individual + group |
| **Profile icon** | Opens **View Profile** / account area |
| **Powered by** | **Powered by** + Intoto logo |

**How to use:**
1. From any main screen, read title + subtitle for context.
2. Tap **chat bubble** → **Chat** screen.
3. Tap **profile avatar** → **View Profile** / **Profile** menu flows.

---

## 3. Authentication & onboarding

### 3.1 Signup (`Signup` — e.g. 5104:252820)

**What it is:** New user registration.

**Fields & controls:**
| Field | Required | Notes |
|-------|----------|-------|
| **Email address** | Yes | Placeholder label with `*` |
| **Password** | Yes | Show/hide eye icon |
| **Remember Me** | No | Checkbox |
| **Forget Password?** | Link | `#02A3CA` |
| **Continue** | Primary CTA | Full-width teal button |
| **Already have an account? Log in** | Link | Switches to Login |

**How to sign up — step by step:**
1. Open **Signup** screen.
2. Enter **email** and **password**.
3. Optionally check **Remember Me**.
4. Tap **Continue**.
5. Proceed to **Email Verification Required!** (or **Create profile** per flow branch).

**Mobile:** Frames at 412px (`Signup` — 5104:259899, 5104:259926, etc.)

---

### 3.2 Login (`Login` — e.g. 5104:252818, 5104:252847)

**What it is:** Returning user sign-in. Primary layout is a centered auth card (image/component frame).

**How to log in:**
1. Open **Login**.
2. Enter credentials (paired with Signup field pattern in related frames).
3. Submit → **Loader** → **All Ambassadors** or **Email Verification** if unverified.

**Variants in Figma:** Multiple Login frames (post-verification, error states) at 1920px, 1280px, 412px.

---

### 3.3 Email Verification Required! (`5104:252904`)

**What it is:** Blocking modal/card after signup when email is not verified.

**Copy (Figma):**
- Title: **Verification Required!**
- Body: *A verification email has been sent to your university email ID* **xx@gmail.com**

**How to use:**
1. Read confirmation message.
2. Check email inbox ( **Mail** frame shows email client mock).
3. Complete verification link → return to **Login** or auto-continue.

**Mobile:** `in app Verify Your Email` (412px — 5104:260013)

---

### 3.4 Loader (`Loader` — 5104:252953)

**What it is:** Full-screen loading state between auth actions.

**When shown:** After Continue on signup/login while API resolves.

---

### 3.5 Create profile — Basic Information (`Create profile` — 5104:252955)

**What it is:** First-time profile setup after auth.

**Header:** Back arrow + title **Basic Information**

**Fields:**
| Field | Required |
|-------|----------|
| **Upload Picture** | Optional — circular avatar + camera button |
| **First Name** | Yes |
| **Last Name** | Yes |
| **Email ID** | Yes |
| **Phone Number** | Yes — country code picker + number |
| **Country** | Yes — dropdown |

**CTA:** **Submit** (teal, full width)

**How to complete:**
1. Tap photo area → upload picture (optional).
2. Fill all required fields.
3. Tap **Submit** → land on **All Ambassadors** home.

**Extended form:** `Create profile` variant (5104:253031) and standalone **Form** / **Information** frames for additional steps.

---

## 4. All Ambassadors — directory home

### What it is

Main landing screen after onboarding (`All Ambassadors` — **5104:244443** desktop).

### Search & filters

**Search bar**
- Placeholder: **Search ambassadors, programs, countries…**
- **Search** button (teal) adjacent on desktop

**Filter chips** (horizontal scroll):
| Chip | Figma frame |
|------|-------------|
| **All Ambassadors** | Default selected (teal fill) |
| **Available Now** | `Available Now` |
| **Students** | `Students` |
| **Alumni** | `Alumni` |
| **Staff** | `Employee` frame |
| **By Program** | `By Program` + `List By Program` + `Filter by Program` |
| **By Country** | `By Country` + `Filter by Country` + `List Filter by Country` |
| **Filter icon** | Opens advanced filter UI (square icon at end of chip row) |

**How to browse — step by step:**
1. Land on **All Ambassadors**.
2. Optionally type in search → tap **Search**.
3. Tap a **filter chip** → list refreshes to category (e.g. only Alumni).
4. For **By Program** or **By Country**, use filter picker frames then **List** views.
5. Scroll **Chat with Our Ambassadors** card grid.
6. Scroll to **Ambassador FAQ** below.

---

## 5. Ambassador card (`AmbassadorCard`)

### What each card shows

| Area | Content |
|------|---------|
| Status row | **Online** (green dot) + role badge (**Student**, **Alumni**, **Staff**) |
| Photo | Circular image + country flag overlay + online dot |
| Name | e.g. **Troy Fonz**, **Aisha Rahman** (H3, 18px bold) |
| Subtitle | Program line, e.g. **Business Administration** |
| Bio snippet | Short intro text (truncated with ellipsis on some cards) |
| **Program** label | Row: label + value |
| **Chat** button | Teal CTA with chat icon |

**How to use a card:**
1. Scan **Online** / role badge.
2. Read name, program, bio preview.
3. Tap **Chat** → opens **Chat** with that ambassador (individual thread).
4. Tap card body / photo → **Ambassadors Profile** detail (see below).

**Carousel sections on home:**
- **Chat with Our Ambassadors** — primary card grid
- **Ambassadors Card Final** — alternate card layout row
- **See More** — underlined teal link → expanded list (`see more`, `Ambassadors List`)

---

## 6. Ambassador profile

### 6.1 Full page — Ambassadors Profile (`5104:250814`)

**Layout:** Directory chrome (header) + left **AmbassadorProfileDetailV2** panel + right content columns.

**Left panel (detail card):**
| Field | Example |
|-------|---------|
| Photo | Large circular image |
| Name | **Aisha Rahman** |
| Role line | Program / title |
| Badge | **Student** |
| Short description | One-line summary |
| **Chat** CTA | Teal button |
| **Program** | Business Administration |
| **Country** | Canada |
| **Languages** | English, French |
| **Favourite Programs** | Cultural Exchange Program, etc. |
| Response time | e.g. **Usually responds within 24 hours** |

**Right content:**
- **About me** — long bio (e.g. Troy Fonz introduction paragraph)
- **Ask me a question** — CTA section (`when click on Ask me a question`)
- **Like share** — social proof / share actions (`Like share` frame)
- **Image View** — full-screen image viewer

**How to open:**
1. From card grid → tap ambassador (not Chat button) → **Ambassadors Profile**.
2. Read **About me**.
3. Tap **Chat** on left panel → individual chat thread.
4. Tap **Ask me a question** → prefilled or guided chat entry.

### 6.2 Click Profile (`Click Profile` — 5104:246034)

Variant showing profile interaction from directory — same information architecture with focus on profile panel expansion.

### 6.3 View Profile — own account (`View Profile` — 5104:253308)

Logged-in user's own profile view (distinct from public ambassador profile).

### 6.4 Mobile profile (`Ambassadors Profile` — 412px, e.g. 5104:257976)

Scrollable mobile profile with gallery sections:
- **gallery empty** / **gallery image** — photo grid
- **mute group** / **Leave group** — when accessed from group context

---

## 7. Chat

### 7.1 Chat shell (`chat` — 5104:249815)

**Header:** Back + **Chat** title + global chrome (profile, Powered by Intoto)

**Subtitle:** *Start a conversation with an ambassador*

**Layout:** Two columns on desktop
| Left (445px) | Right (1177px) |
|--------------|----------------|
| **Individual Chats** tab (default active) | Active conversation |
| Thread list with avatars, names, dates, unread badges | Message history + composer |

**Empty state:** `If there is no chat` (5104:249677) — no threads yet.

---

### 7.2 Individual chat list

Each row shows:
- Avatar
- Name (e.g. **Troy Fonz**, **Sarah Chen**)
- Last message date or time
- Unread count badge (teal circle, e.g. **3**)

**How to open a thread:**
1. Go to **Chat** via header icon or card **Chat** button.
2. Ensure **Individual Chats** tab selected.
3. Tap a row → conversation loads in right panel.

---

### 7.3 Individual conversation (right panel)

**Thread header:**
- Ambassador photo + name
- **Online** status (green)
- **Student** / **Staff** badge
- **⋮** menu (three dots) → **Report a conversation** | **Delete conversation**

**Messages:**
- Incoming: gray bubble (`#F4F6F8`), left-aligned with sender name
- Outgoing: light teal bubble (`rgba(2,163,202,0.1)`), right-aligned
- Timestamps: e.g. **05 December**

**Quick reply chips** (after ambassador message):
- *What would you like to know about?*
- Chips: **Campus life** | **Accommodation** | **Academic programs** | **Student life**

**Composer:**
- Attachment icon
- Placeholder: **Type your message...**
- Send button (teal when active)

**Variants:**
| Frame | Purpose |
|-------|---------|
| **Type** | User typing state |
| **msg typing** | Typing indicator |
| **Image attach** | Image attachment flow |
| **Image share** | Shared image in thread |
| **after report chat design** | UI after reporting |
| **after report** | Mobile post-report state |

---

### 7.4 Group chat (`Group chat` — 5104:250460)

**Tabs:** **Individual Chats** | **Group Chats** (bold when active)

**Group list rows:**
- Group icon (teal circle)
- Name: e.g. **International Students 2025**, **Business Administration Students**, **Campus Events & Activities**
- Preview: last message snippet
- Unread badge when applicable

**Group conversation header:**
- Group name
- **24 members** (member count)
- **⋮** menu → report / delete options

**Messages:** Show sender name + **Student** / **Staff** badge per message.

**Group detail flows:**
| Frame | Purpose |
|-------|---------|
| **Group Detail** / **group detail** | Member list, settings |
| **Group images** / **gallery image** | Shared media |
| **image share in group** | Posting image to group |
| **mute** / **mute group** | Mute notifications |
| **Leave Group popup** / **Leave group** | Confirm leave |
| **after exit group** | State after leaving |

---

### 7.5 Chat moderation menu (`3 dots` — 5104:252806)

| Action | Label |
|--------|-------|
| Report | **Report a conversation** |
| Delete | **Delete conversation** |

**Report flow:**
1. Tap **⋮** in chat header.
2. Tap **Report a conversation**.
3. **Report** / **click on Report** modal — enter reason, submit.
4. **after report** / **after report chat design** — confirmation UI.

**Delete flow:**
1. Tap **Delete conversation**.
2. **Delete conversation** confirmation popup (5104:268249).
3. Thread removed from list.

---

## 8. Ambassador FAQ

**Section title:** **Ambassador FAQ** (below card grids on **All Ambassadors**)

**Pattern:** Accordion cards — question header + expand chevron + answer body.

**Example question (Figma):**
- **What is campus life like for international students?**
- Answer: Long-form ambassador-written paragraph about diversity, cultural clubs, international food festival, etc.

**Additional collapsed FAQ rows** appear below first expanded item.

**How to use:**
1. Scroll to **Ambassador FAQ** on home.
2. Tap a question row → expands answer.
3. Tap again or another row to switch.

---

## 9. Account & profile management

### 9.1 Profile menu (`Profile` — 5104:260226 mobile)

Entry from header profile icon. Links to settings, logout, delete.

### 9.2 Basic Information / Information (`Basic Information` — 5104:260060)

Edit profile fields (same family as **Create profile**).

### 9.3 Logout (`Logout` — 5104:246377)

**Confirmation modal:** **Logout Confirmation?**

**Actions:**
- Cancel
- **Logout** (confirm)

**Mobile:** `Logout` 412px (5104:260556)

**Tablet/desktop:** `Logout Confirmation?` (1280px — 5104:265361)

### 9.4 Delete Account (`Delete Account` — 5104:246720)

Destructive account removal flow with confirmation (`Delete` mobile frame 5104:261209).

---

## 10. End-to-end flows (playbooks)

### Flow A — New visitor → first chat

1. Open platform URL → **Signup**.
2. Enter email/password → **Continue**.
3. **Verification Required!** → verify email.
4. **Create profile** → **Basic Information** → **Submit**.
5. **All Ambassadors** → search or filter.
6. Tap ambassador card → **Ambassadors Profile**.
7. Tap **Chat** → compose message → send.
8. Ambassador replies with quick-reply chips → student taps **Campus life** or types reply.

### Flow B — Filter by program

1. **All Ambassadors** → tap **By Program**.
2. **Filter by Program** picker → select program.
3. **List By Program** → browse filtered cards.
4. Tap **Chat** on chosen ambassador.

### Flow C — Group chat

1. Header → **Chat** → **Group Chats** tab.
2. Tap **International Students 2025**.
3. Read thread → type in **Type your message...** → send.
4. Tap group header → **Group Detail** → view members.
5. Optional: **Leave group** → confirm popup.

### Flow D — Report inappropriate chat

1. Open individual or group chat.
2. Tap **⋮** → **Report a conversation**.
3. Complete **Report** modal.
4. View **after report** state; thread may be flagged or hidden per product rules.

### Flow E — Logout

1. Tap profile icon → **Profile** / account.
2. Choose **Logout**.
3. Confirm **Logout Confirmation?** → return to **Login**.

---

## 11. Responsive behavior

| Feature | Desktop 1920 | Tablet 1280 | Mobile 412 |
|---------|----------------|-------------|------------|
| Filter chips | Full horizontal row | Wrapped / scroll | Stacked / scroll |
| Chat layout | Side-by-side list + thread | Side-by-side (narrower) | Stacked — list → full-screen **Chat Detail** |
| Ambassador cards | 4-column grid | 3-column | 1-column |
| FAQ accordion | Full width | Full width | Full width, smaller padding |
| Auth forms | Centered card ~510px | Centered ~1280 canvas | Full-width mobile sheet |

**Figma mobile chat frames:** `Individual chats`, `Chat Detail`, `Empty Chat`, `Group Chat`, `Group Chat Detail`, `type and image`

---

## 12. Permissions & boundaries (platform)

**Users can:**
- Sign up, verify email, create basic profile
- Search and filter ambassadors
- View public ambassador profiles
- Start individual and group chats
- Attach images in chat (per wireframe)
- Report or delete conversations
- Read FAQ content
- Log out and delete own account

**Users cannot (not in this Figma scope):**
- Administer university tenants
- Invite staff or approve communities (mobile admin roles)
- Edit another user's ambassador profile from this web UI (ambassador content is read-only for visitors)

---

## 13. Screen inventory (Figma frame names)

| Screen | Figma frame name | Node ID (reference) |
|--------|------------------|---------------------|
| Directory home | All Ambassadors | 5104:244443 |
| Expanded list | see more / Ambassadors List | 5104:245158 / 5104:245712 |
| Filter: Available Now | Available Now | 5104:247066 |
| Filter: Students | Students | 5104:247335 |
| Filter: Alumni | Alumni | 5104:247656 |
| Filter: Staff | Employee | 5104:247977 |
| Filter: By Program | By Program / List By Program / Filter by Program | 5104:248182+ |
| Filter: By Country | By Country / List Filter by Country | 5104:256177+ |
| Public profile | Ambassadors Profile | 5104:250814 |
| Profile detail panel | AmbassadorProfileDetailV2 | (child of 5104:250814) |
| Ask question | when click on Ask me a question | 5104:252804 |
| Signup | Signup | 5104:252820 |
| Login | Login | 5104:252818 |
| Email verify | Email Verification Required! | 5104:252904 |
| Create profile | Create profile | 5104:252955 |
| Loader | Loader | 5104:252953 |
| Chat inbox | chat | 5104:249815 |
| Empty chat | If there is no chat | 5104:249677 |
| Group chat | Group chat | 5104:250460 |
| Group detail | Group Detail / group detail | 5104:251236+ |
| Chat menu | 3 dots | 5104:252806 |
| Report modal | Report / click on Report | 5104:268271+ |
| Delete conversation | Delete conversation | 5104:268249 |
| Leave group | Leave Group popup | 5104:251932 |
| Own profile | View Profile / Profile | 5104:253308 / 5104:260226 |
| Logout | Logout / Logout Confirmation? | 5104:246377 / 5104:265361 |
| Delete account | Delete Account / Delete | 5104:246720 / 5104:261209 |
| FAQ section | (section on All Ambassadors) | 5104:244740+ |
| Shared / Community | Shared / Community | 5104:244786 / 5104:268621 |

---

## 14. Figma validation checklist (page 5051:661)

- [ ] Signup — all fields, Remember Me, Forget Password, Continue, Log in link
- [ ] Login — all variants (1920, 1280, 412)
- [ ] Email Verification Required! — copy and email display
- [ ] Create profile / Basic Information — photo upload, all required fields, Submit
- [ ] All Ambassadors — search placeholder, Search button, all filter chips
- [ ] AmbassadorCard — Online, role badge, Chat CTA, program row
- [ ] Ambassadors Profile — detail panel fields, About me, Chat CTA
- [ ] Chat — Individual vs Group tabs, thread list, composer, quick-reply chips
- [ ] Group chat — member count, group names, leave/mute flows
- [ ] 3-dot menu — Report, Delete conversation
- [ ] Report and Delete modals — all breakpoints
- [ ] Ambassador FAQ — accordion expand/collapse
- [ ] Logout / Delete Account confirmations
- [ ] Mobile 412px — Chat Detail, profile, auth flows
- [ ] Tablet 1280px — directory and chat layouts
- [ ] Powered by Intoto header on all main screens

---

## 15. Related documentation

| Document | Scope |
|----------|-------|
| `docs/Ambassador-Platform-Client-Demo-Guide.md` | Client demo script |
| `docs/Ambassador-Platform-QA-Test-Guide.md` | QA test suites |
| `docs/Ambassador-Features-and-Flows.md` | In-app Ambassador **role** (mobile) |
| `docs/Student-Features-and-Flows.md` | Student mobile app |

---

## Document history

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | Jun 2026 | Initial guide from Figma page 5051:661 via Figma MCP |

*Design: [The Ambassador Plateform — 5051:661](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)*
