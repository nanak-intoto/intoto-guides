# Intoto — Ambassador Platform
## QA Test Guide

**Design reference:** [Intoto Wireframe — Ambassador (page 5051:661)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)  
**Prototype:** [Ambassador prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661)  
**Audience:** QA, UAT, release validation  
**Version:** 2.0

---

## 1. Scope

Validate **Ambassador Platform** (`ambassador`, `external_ambassador`) against Figma Ambassador frames on page **5051:661**:

- Login, role selection, invitation accept/defer
- Home overview (app bar, alerts, Quick Way, Quick Actions, banners, events, activities)
- **My Profile** hub and **Ambassador Info** (`ambassadorForm`)
- All profile section editors, photo upload, Section Next / unsaved prompt
- Student list (scoped), student profile, Chat CTA
- Chats send/receive (ambassador ↔ student)
- Events browse/register (participant only)
- Community tab (discover, join, post smoke)
- Notifications, Support, university header
- **Student-facing:** Ambassadors carousel → public profile → chat
- Dual-role Student + Ambassador switcher
- Permissions boundaries (no admin flows)

**Out of scope:** University Super Admin governance, Third Party Coordinator assignment, Event/Community Coordinator approve/reject.

---

## 2. Test data

| Data | Purpose |
|------|---------|
| Ambassador account | Primary |
| External Ambassador account | Type field + invite path |
| Student account | Carousel + chat cross-role |
| Multi-role Student+Ambassador | Role switcher |
| Incomplete ambassador profile | Alert behavior |
| Complete ambassador profile | Student carousel visibility |
| 1+ chat thread | Messaging |
| Upcoming event | Carousel / register |
| Joined community | Post smoke |

---

## 3. Critical acceptance criteria

1. Login as Ambassador lands on Ambassador Home without crash.
2. University header shows name; logo optional without layout break; tap opens details.
3. My Profile uses **ambassadorForm** — **Ambassador Info** section present.
4. Ambassador Info save persists; completion alert updates on refresh.
5. Quick Way cards match ambassador API config (no USA-only cards unless misconfigured).
6. Total Students (if shown) opens scoped list; profile opens; **Chat** works.
7. Chats: bidirectional message with student account.
8. Student Home: Ambassadors carousel shows complete ambassador; chat opens same user.
9. Role switcher: Student ↔ Ambassador changes dashboard correctly.
10. Ambassador cannot access Manage Users, assign students, or approve pending events.

---

## 4. Test suites

## Suite A — Login and shell

### A-01 Login Ambassador
**Steps:** Launch → login as Ambassador.  
**Expected:** Home; tabs Home, Community, Chats, Profile; role tag Ambassador.

### A-02 Login External Ambassador
**Steps:** Login as External Ambassador.  
**Expected:** Same shell; ambassador type visible in profile/invite per Figma.

### A-03 Invitation accept
**Steps:** New invite → Accept at login.  
**Expected:** Role active; completion alert likely shown.

### A-04 Invitation defer
**Steps:** Do it later → envelope on Home → accept from list.  
**Expected:** Role activates; dashboard correct.

### A-05 App bar
**Steps:** With/without logo; tap university; tap bell.  
**Expected:** Layout OK; university details; notifications.

### A-06 Role switcher
**Steps:** Multi-role: Student → Ambassador → Student.  
**Expected:** Distinct dashboards — no mixed alerts.

---

## Suite B — Home sections

### B-01 Completion alert
**Steps:** Incomplete profile → read alert → tap.  
**Expected:** Routes to My Profile or Ambassador Info.

### B-02 Quick Way render
**Expected:** Icons, counts, labels per API/Figma.

### B-03 `quick_way_total_messages`
**Steps:** Tap card.  
**Expected:** Chats/messages destination; no dead tap.

### B-04 `quick_way_total_students`
**Steps:** Tap → search → open student.  
**Expected:** Scoped list; profile; no admin actions.

### B-05 Quick Actions
**Steps:** Tap Events, Support, My Profile, Chats (if present).  
**Expected:** Correct destinations per Figma hotspots.

### B-06 Upcoming Events / My Events
**Steps:** Carousel swipe; card tap; View All.  
**Expected:** Event Details; list loads.

### B-07 Banners / Activities
**Steps:** Tap items.  
**Expected:** CTA behavior per link type.

### B-08 Pull to refresh
**Steps:** Pull Home.  
**Expected:** Reload; spinner dismisses.

---

## Suite C — My Profile hub

### C-01 Section list load
**Expected:** API sections + **Ambassador Info**; order matches backend.

### C-02 Ambassador Info — happy path
**Steps:** Edit required fields → Save.  
**Expected:** Success; section complete; student-visible fields update.

### C-03 Ambassador Info — validation
**Steps:** Clear required field → Save.  
**Expected:** Inline errors; Save blocked.

### C-04 Lookup fields
**Steps:** Open ambassador type / program pickers → search → select.  
**Expected:** Value binds; Save persists.

### C-05 Profile photo
**Steps:** Change photo via header (pick → crop → upload).  
**Expected:** Header and student carousel image update after refresh.

### C-06 Other sections smoke
**Steps:** Open Basic Details, Preferences, Contact — Save one field each.  
**Expected:** No crash; completion state updates.

### C-07 Section Next / unsaved
**Steps:** Edit → Next/back without save.  
**Expected:** Unsaved prompt per Figma.

### C-08 Wrong form guard
**Expected:** Ambassador My Profile must not show student-only admin form conflation.

---

## Suite D — Students and chat

### D-01 Student list search/filter
**Steps:** Search ≥3 chars; apply filter; Clear All.  
**Expected:** List updates; pagination if long.

### D-02 Student profile Chat
**Steps:** Open student → Chat.  
**Expected:** Thread opens or creates.

### D-03 Chats tab bidirectional
**Steps:** Ambassador sends; student reads and replies.  
**Expected:** Delivery both directions; unread badges.

### D-04 No admin actions
**Expected:** No Assign, Suspend, Manage Users on ambassador paths.

---

## Suite E — Student-facing integration

### E-01 Ambassadors carousel
**Steps:** Student Home → Ambassadors → tap ambassador.  
**Expected:** Public profile; Chat CTA.

### E-02 View All ambassador list
**Steps:** Student Home → View All → search → profile → chat.  
**Expected:** Same ambassador user as carousel.

### E-03 Incomplete profile visibility
**Steps:** Ambassador with empty Ambassador Info.  
**Expected:** Hidden or deprioritized on carousel — document actual behavior.

### E-04 Public profile read-only
**Expected:** No edit controls on student-facing ambassador profile.

---

## Suite F — Events

### F-01 Event browse
**Steps:** Events quick action → open event.  
**Expected:** Details load.

### F-02 Event register
**Steps:** Register when window open.  
**Expected:** Success; optional My Events section.

### F-03 No approve/reject
**Expected:** No pending event approval UI on ambassador role.

---

## Suite G — Community

### G-01 Discover and join
**Steps:** Community tab → open community → Join.  
**Expected:** Member state updates.

### G-02 Post smoke
**Steps:** Create post in joined community.  
**Expected:** Appears in feed; no approve-community UI.

---

## Suite H — Notifications, Support, Profile tab

### H-01 Notification deep link
**Steps:** Tap chat or profile notification.  
**Expected:** Correct destination.

### H-02 Support
**Steps:** Quick Action Support.  
**Expected:** Support screen loads.

### H-03 Profile tab logout
**Steps:** Profile → Logout → confirm.  
**Expected:** Login screen.

---

## Suite I — Negative / security

### I-01 Admin flow access
**Expected:** Ambassador cannot reach USA/TPC-only screens without role.

### I-02 Cross-university data
**Expected:** Lists scoped to ambassador university/campus.

---

## 5. Defect severity

| Severity | Example |
|----------|---------|
| Critical | Crash on Ambassador Home; chat broken; Ambassador Info save fails |
| Major | Student cannot find/chat ambassador; wrong dashboard on role switch |
| Minor | Copy vs Figma; stale count until refresh |
| Trivial | Spacing |

---

## 6. Figma sign-off checklist (page 5051:661)

- [ ] Suite A–I executed  
- [ ] Full Ambassador prototype walk on page 5051:661  
- [ ] Every Quick Way / Quick Action hotspot matches doc  
- [ ] Ambassador Info fields match wireframe  
- [ ] Student carousel + public profile + chat loop verified  
- [ ] External Ambassador labels confirmed  
- [ ] Empty states match Figma  

---

*Design: [Figma — page 5051:661](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)*
