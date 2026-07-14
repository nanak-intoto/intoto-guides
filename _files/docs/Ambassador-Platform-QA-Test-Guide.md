# Intoto — The Ambassador Platform
## QA Test Guide

**Design reference:** [Intoto Wireframe — The Ambassador Plateform (5051:661)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)  
**Primary frame:** [All Ambassadors — 5104:244443](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5104-244443&page-id=5051%3A661)  
**Audience:** QA, UAT, release validation  
**Version:** 1.0

---

## 1. Scope

This guide validates **The Ambassador Platform** (web) behavior across:

- signup, login, email verification, and create-profile onboarding
- **All Ambassadors** directory — search, filter chips, card grid, See More
- ambassador **public profile** (detail panel, About me, Chat CTA)
- **individual chat** — list, thread, composer, quick-reply chips, attachments
- **group chat** — list, thread, member count, detail, mute, leave
- chat moderation — report and delete conversation
- **Ambassador FAQ** accordion
- account — view profile, logout, delete account
- responsive layouts — desktop (1920), tablet (1280), mobile (412)

**Out of scope:**
- Intoto mobile app Ambassador mentor role (`docs/Ambassador-QA-Test-Guide.md`)
- University Admin, Intoto Admin, or tenant configuration UIs
- Backend ambassador profile CMS (unless exposed in this web UI)

---

## 2. Test data setup

Prepare at least:

- 1 **verified** platform user (completed Basic Information)
- 1 **unverified** signup (for email verification flow)
- 6+ ambassadors: mix of **Student**, **Alumni**, **Staff** badges
- 2+ ambassadors **Online** (green indicator)
- ambassadors across **2+ programs** and **2+ countries** (for filter tests)
- 1 individual chat with **3+ messages** and unread badge on peer thread
- 1 group chat (e.g. *International Students 2025*) with **10+ members**
- 2+ FAQ items (one long answer for scroll/expand test)
- test image file for chat attachment (jpg/png within size limits)

**Browsers:** Chrome (latest), Safari (latest), one mobile viewport (412px) or real device.

---

## 3. Critical acceptance criteria

1. Header shows **Student Ambassadors**, subtitle, chat icon, profile icon, **Powered by Intoto**.
2. Search placeholder reads **Search ambassadors, programs, countries…**; Search returns relevant cards.
3. All filter chips navigate to correct filtered views without broken empty states (unless no data).
4. **AmbassadorCard** shows Online dot, role badge, name, program, bio snippet, **Chat** CTA.
5. **Chat** from card opens correct individual thread with correct ambassador.
6. **Ambassadors Profile** shows Program, Country, Languages, About me; **Chat** CTA works.
7. Chat inbox has **Individual Chats** and **Group Chats** tabs; switching preserves state.
8. Composer placeholder **Type your message...**; send delivers message and updates list preview.
9. Quick-reply chips appear per design; tapping chip sends or prefills message.
10. **⋮** menu offers **Report a conversation** and **Delete conversation** with confirmations.
11. **Logout Confirmation?** and **Delete Account** require explicit confirm.
12. FAQ accordion expands/collapses without layout break.
13. Mobile (412px): chat list → detail navigation works; no horizontal overflow on cards.

---

## 4. Functional test suites

## Suite A — Authentication

### A-01 Signup — happy path
**Steps**
1. Open **Signup**.
2. Enter valid email and password.
3. Tap **Continue**.

**Expected**
- Navigates to **Verification Required!** or create-profile per env config.
- **Already have an account? Log in** opens Login.

### A-02 Signup — validation
**Steps**
1. Submit empty form.
2. Submit invalid email format.
3. Submit weak/missing password per rules.

**Expected**
- Inline or toast validation; no account created.

### A-03 Login — happy path
**Steps**
1. Open **Login**.
2. Enter verified user credentials.
3. Submit.

**Expected**
- **Loader** (if shown) → **All Ambassadors**.

### A-04 Email verification
**Steps**
1. Complete signup as unverified user.
2. Observe **Verification Required!** copy references submitted email.
3. Complete verification link (test inbox).
4. Return to platform.

**Expected**
- Copy: *A verification email has been sent to your university email ID* + email display.
- After verify, user can log in or auto-continue.

### A-05 Forget Password
**Steps**
1. On Signup/Login, tap **Forget Password?**

**Expected**
- Password reset flow opens (per implementation); no dead link.

---

## Suite B — Create profile

### B-01 Basic Information — required fields
**Steps**
1. After auth, open **Create profile** / **Basic Information**.
2. Leave required fields empty → tap **Submit**.
3. Fill First Name, Last Name, Email ID, Phone Number, Country → **Submit**.

**Expected**
- Validation blocks empty required fields.
- Success → **All Ambassadors**.

### B-02 Photo upload
**Steps**
1. Tap **Upload Picture** → select valid image.
2. Submit profile.

**Expected**
- Avatar preview updates; image persists on **View Profile**.

### B-03 Country code picker
**Steps**
1. Change phone country code.
2. Enter national number.

**Expected**
- Code and number stored correctly; E.164 or equivalent on API.

---

## Suite C — Directory (All Ambassadors)

### C-01 Page chrome
**Steps**
1. Load **All Ambassadors** as logged-in user.

**Expected**
- Title **Student Ambassadors**; subtitle visible.
- Chat and Profile header icons present.
- **Powered by Intoto** visible.

### C-02 Search
**Steps**
1. Search known ambassador name.
2. Search known program keyword.
3. Search known country.
4. Search nonsense string.

**Expected**
- Relevant results for 1–3; empty state for 4.

### C-03 Filter chips
**Steps**
1. Tap each chip: **All Ambassadors**, **Available Now**, **Students**, **Alumni**, **Staff**, **By Program**, **By Country**.

**Expected**
- Active chip styling (teal); list filters correctly.
- **By Program** / **By Country** open picker then list views.

### C-04 Ambassador card — Chat CTA
**Steps**
1. Tap **Chat** on a specific card.

**Expected**
- Opens **Chat** with that ambassador's individual thread (new or existing).

### C-05 Ambassador card — profile navigation
**Steps**
1. Tap card (not Chat button).

**Expected**
- Opens **Ambassadors Profile** for correct ambassador.

### C-06 See More
**Steps**
1. Tap **See More** link below card section.

**Expected**
- Expanded list / **Ambassadors List** with additional cards.

### C-07 Chat with Our Ambassadors section
**Steps**
1. Verify section heading and card grid render.

**Expected**
- Section title matches Figma; cards aligned in grid per breakpoint.

---

## Suite D — Ambassador profile

### D-01 Detail panel fields
**Steps**
1. Open **Ambassadors Profile** for known ambassador.

**Expected**
- Name, role badge, Program, Country, Languages, Favourite Programs (if data exists).
- **Chat** CTA visible and functional.

### D-02 About me
**Steps**
1. Scroll **About me** long text.

**Expected**
- Full bio readable; no truncation without expand control.

### D-03 Ask me a question
**Steps**
1. Tap **Ask me a question** (if shown).

**Expected**
- Routes to chat or prefilled composer per design.

### D-04 Like / share
**Steps**
1. Interact with **Like share** controls (if enabled).

**Expected**
- Share action completes or shows not-implemented only if out of MVP scope (document).

---

## Suite E — Individual chat

### E-01 Empty inbox
**Steps**
1. New user with no chats → open **Chat**.

**Expected**
- **If there is no chat** empty state; subtitle *Start a conversation with an ambassador*.

### E-02 Thread list
**Steps**
1. User with multiple threads → open **Individual Chats**.

**Expected**
- Rows show avatar, name, date/time, unread badge when applicable.
- Tapping row loads correct thread in right panel (desktop) or **Chat Detail** (mobile).

### E-03 Send message
**Steps**
1. Type message → send.

**Expected**
- Message appears in thread (outgoing style); list preview updates.

### E-04 Quick-reply chips
**Steps**
1. Open thread where ambassador message shows chips.
2. Tap **Campus life**, then **Accommodation**.

**Expected**
- Chip tap sends or inserts text per spec; ambassador side receives (integration test).

### E-05 Typing indicator
**Steps**
1. Trigger **msg typing** state (ambassador typing).

**Expected**
- Typing UI shown without breaking scroll position.

### E-06 Image attach
**Steps**
1. Tap attachment → select image → send.

**Expected**
- Image renders in thread; **Image attach** / **Image share** layouts match design.

### E-07 Online status in thread header
**Steps**
1. Open chat with online ambassador.

**Expected**
- **Online** green indicator and role badge in header.

---

## Suite F — Group chat

### F-01 Group list
**Steps**
1. **Chat** → **Group Chats** tab.

**Expected**
- Groups listed with name and preview; unread badges when applicable.

### F-02 Open group thread
**Steps**
1. Open **International Students 2025** (or test group).

**Expected**
- Header shows group name and member count (e.g. **24 members**).
- Messages show sender name and role badge.

### F-03 Group detail
**Steps**
1. From group header, open **Group Detail**.

**Expected**
- Member list or settings per design; back navigation works.

### F-04 Group images
**Steps**
1. Open **Group images** / shared gallery.

**Expected**
- Media grid loads; tap opens viewer.

### F-05 Mute group
**Steps**
1. **mute group** action → confirm.

**Expected**
- Mute state persists; notifications suppressed per spec.

### F-06 Leave group
**Steps**
1. **Leave group** → **Leave Group popup** → confirm.

**Expected**
- User removed from group; **after exit group** state; group absent from list.

---

## Suite G — Moderation

### G-01 Three-dot menu
**Steps**
1. Open any chat → tap **⋮**.

**Expected**
- **Report a conversation** and **Delete conversation** visible.

### G-02 Report conversation
**Steps**
1. Tap **Report a conversation** → complete **Report** modal → submit.

**Expected**
- **after report** UI; report recorded; user can still navigate away.

### G-03 Delete conversation
**Steps**
1. Tap **Delete conversation** → confirm in popup.

**Expected**
- Thread removed from list; reopening ambassador starts fresh or restores per product rules.

### G-04 Cancel destructive actions
**Steps**
1. Open Report/Delete/Leave/Logout modals → cancel.

**Expected**
- No state change; returns to previous screen.

---

## Suite H — FAQ

### H-01 Accordion expand
**Steps**
1. On **All Ambassadors**, scroll to **Ambassador FAQ**.
2. Tap collapsed question.

**Expected**
- Answer expands; chevron rotates or state changes.

### H-02 Accordion collapse
**Steps**
1. Tap expanded question again.

**Expected**
- Answer collapses.

### H-03 Multiple FAQs
**Steps**
1. Expand second question while first is open.

**Expected**
- Behavior matches spec (single vs multi expand — default: one open at a time unless design says otherwise).

---

## Suite I — Account

### I-01 View Profile
**Steps**
1. Tap header profile icon.

**Expected**
- **View Profile** shows user's Basic Information fields.

### I-02 Edit profile
**Steps**
1. Change phone or country → save.

**Expected**
- Changes persist after refresh.

### I-03 Logout
**Steps**
1. **Logout** → **Logout Confirmation?** → confirm.

**Expected**
- Session cleared; **Login** shown.

### I-04 Delete Account
**Steps**
1. **Delete Account** → confirm (use disposable test user).

**Expected**
- Account removed; cannot log in with same credentials.

---

## Suite J — Responsive / cross-browser

### J-01 Desktop 1920
**Steps**
1. Run Suites C, E, F at 1920px width.

**Expected**
- Two-column chat layout; 4-column card grid (approx).

### J-02 Tablet 1280
**Steps**
1. Repeat key flows at 1280px.

**Expected**
- Layout matches Figma tablet frames; no clipped header.

### J-03 Mobile 412
**Steps**
1. Repeat directory, profile, **Chat Detail**, auth at 412px.

**Expected**
- Single-column cards; full-screen chat detail; touch targets ≥ 44px.

### J-04 Safari + Chrome parity
**Steps**
1. Run A-03, C-03, E-03 on both browsers.

**Expected**
- No layout or auth cookie regressions.

---

## 5. Regression smoke (release gate)

Run before every release:

| # | Test | Pass |
|---|------|------|
| 1 | Login → All Ambassadors loads | ☐ |
| 2 | Search returns results | ☐ |
| 3 | Filter **Students** works | ☐ |
| 4 | Card **Chat** opens correct thread | ☐ |
| 5 | Send text message | ☐ |
| 6 | Group Chats tab loads | ☐ |
| 7 | FAQ expand works | ☐ |
| 8 | Logout works | ☐ |
| 9 | Mobile 412 — directory + chat detail | ☐ |
| 10 | Powered by Intoto visible | ☐ |

---

## 6. Figma alignment checklist

Compare implemented UI to Figma frames on page **5051:661**:

| Frame | Node ID | Verified |
|-------|---------|----------|
| All Ambassadors | 5104:244443 | ☐ |
| Signup | 5104:252820 | ☐ |
| Login | 5104:252818 | ☐ |
| Email Verification Required! | 5104:252904 | ☐ |
| Create profile | 5104:252955 | ☐ |
| chat | 5104:249815 | ☐ |
| Group chat | 5104:250460 | ☐ |
| Ambassadors Profile | 5104:250814 | ☐ |
| 3 dots menu | 5104:252806 | ☐ |
| Logout | 5104:246377 | ☐ |

---

## 7. Related documentation

| Document | Use |
|----------|-----|
| `Ambassador-Platform-Features-and-Flows.md` | Feature reference |
| `Ambassador-Platform-Client-Demo-Guide.md` | Demo script |
| `Ambassador-QA-Test-Guide.md` | In-app Ambassador role (mobile) |

---

## Document history

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | Jun 2026 | Initial QA guide from Figma 5051:661 |
