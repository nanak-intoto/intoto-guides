# Intoto — Intoto Admin
## QA Test Guide

**Design reference:** [Intoto Wireframe — Intoto Admin (node 5051-661)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)  
**Prototype:** [Intoto Admin prototype](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5051%3A661)  
**Audience:** QA, UAT, release validation  
**Version:** 1.0

---

## 1. Scope

This guide validates **Intoto Admin** behavior across:

- platform dashboard rendering and navigation
- university management (list, details, add, suspend/activate)
- university context picker and cross-tenant scoping
- Quick Way and Quick Actions routing
- manage users and add user validation (**University** filter dimension)
- global student, coordinator, community, event, and report lists
- chats, notifications, profile/settings
- filter apply/cancel/clear and list pagination

**Out of scope (other roles):**
- Assign students to sub-coordinator wizard (University Super Admin / Third Party Coordinator)
- Single-university-only flows without platform cross-tenant behavior

---

## 2. Test data setup

Prepare at least:

- 1 **Intoto Admin** account
- **2+ universities** (Active, and Pending or Suspended if possible)
- 1 **University Super Admin** per university
- 1 invited user and 1 accepted user **in different universities**
- Students in at least 2 universities
- 1 pending community, 1 approved community
- 1 report ticket
- 1 upcoming event per university (or shared catalog)
- Optional: multi-role account (Intoto Admin + University Super Admin) for role-switch tests

---

## 3. Critical acceptance criteria

1. Dashboard loads **platform-scoped** data — not locked to one university unless context is selected.
2. Role tag shows **Intoto Admin**.
3. **Manage Universities** and **Add University** actions route correctly.
4. University List supports search, status filters, and row → details navigation.
5. **University** appears in Manage Users filter sidebar and list columns.
6. Add User enforces **University** for university-scoped roles; **no campus** for University Super Admin.
7. Every visible Quick Way card routes to the correct destination.
8. University context picker scopes lists/counts until cleared.
9. Report status transitions persist and refresh list state.
10. Settings changes show nav bar **Save** only when dirty; POST on Save.

---

## 4. Functional test suites

## Suite A — Login and shell

### A-01 Login as Intoto Admin
**Steps**
1. Launch app.
2. Login with Intoto Admin credentials.

**Expected**
- Home dashboard opens.
- Role tag indicates **Intoto Admin**.
- Bottom tabs visible: Home, Community, Chats, Profile.

### A-02 Multi-role selection
**Steps**
1. Login with account that has Intoto Admin + another role.
2. Select **Intoto Admin**.

**Expected**
- Platform dashboard loads (not single-university-only USuper Admin dashboard).

### A-03 Header actions
**Steps**
1. Tap platform / university block in app bar.
2. Tap notification bell.
3. Tap pending invitation envelope if shown.

**Expected**
- University picker or details opens per wireframe.
- Notifications list opens.
- Pending invitation list opens.

---

## Suite B — University management

### B-01 University List from Quick Way
**Steps**
1. Tap **Total Universities** on dashboard.

**Expected**
- University List opens with search and status chips (if configured).
- Rows show logo, name, status.

### B-02 University Details
**Steps**
1. From University List, tap one university.

**Expected**
- University Details shows campuses, status, summary metrics.
- Back navigation returns to list.

### B-03 Add University — happy path
**Steps**
1. Tap **Add University** quick action.
2. Fill required fields (name, identifier, campus if required).
3. Submit.

**Expected**
- Success feedback.
- New university appears in University List with correct status.

### B-04 Add University — validation
**Steps**
1. Open Add University form.
2. Submit with empty required fields.

**Expected**
- Inline or toast validation; no partial create.

### B-05 Suspend / activate university
**Steps**
1. Open University Details for active university.
2. Tap **Suspend** → confirm.
3. Repeat with **Activate** on suspended university (if test data exists).

**Expected**
- Status badge updates.
- List reflects new status after refresh.

### B-06 Manage Universities quick action
**Steps**
1. Tap **Manage Universities** on dashboard.

**Expected**
- Same destination as Total Universities stat (University List).

---

## Suite C — University context

### C-01 Picker scopes list
**Steps**
1. Open **Manage Users**.
2. Select **University A** via header picker or filter.
3. Note list contents.
4. Select **University B** or **All Universities**.

**Expected**
- List contents change to match selected scope.
- Clearing context restores global view.

### C-02 Dashboard counts after context change
**Steps**
1. Select one university in picker.
2. Pull to refresh dashboard.

**Expected**
- Quick Way counts reflect scoped tenant (per API contract) or remain global with clear UX label — match Figma copy.

---

## Suite D — Quick Way routing

### D-01 Card render
**Expected**
- Each card shows icon, label, count without layout breakage.

### D-02 Card tap routing
**Steps**
1. Tap every visible Quick Way card.

**Expected**
- Correct list or screen opens for each card.
- No crash or dead tap.

### D-03 Pull-to-refresh
**Steps**
1. Pull down on dashboard.

**Expected**
- Loader shows and dismisses.
- Sections and counts refresh.

---

## Suite E — Quick Actions

### E-01 Manage User
**Expected**
- Opens Manage Users with cross-tenant list.

### E-02 Add User
**Expected**
- Opens invite form with Role and University fields.

### E-03 Events / Support
**Expected**
- Events → events catalog; Support → support screen.

---

## Suite F — Manage Users

### F-01 Status chips
**Steps**
1. Tap each chip: All, Invited, Accepted, Suspended, etc.

**Expected**
- List filters correctly per status.

### F-02 Search
**Steps**
1. Search by name and email (≥3 characters if enforced).

**Expected**
- Results match query across tenants (or scoped university if picker active).

### F-03 University + Role filter
**Steps**
1. Tap Filter.
2. Select **University** and **Role**.
3. Apply.

**Expected**
- List shows only matching users.
- Filter badge or indicator visible on list.

### F-04 Single-user actions
**Steps**
1. Open Invited user → Resend invite.
2. Open Accepted user → Suspend.
3. Open Suspended user → Re-initiate.

**Expected**
- Action succeeds; status updates after refresh.

### F-05 Bulk email
**Steps**
1. Multi-select users.
2. Take Action → Send email.

**Expected**
- Mail compose opens with selected recipients.

---

## Suite G — Add User

### G-01 University Super Admin invite
**Steps**
1. Role = University Super Admin.
2. Select University.
3. Leave Campus empty.
4. Submit.

**Expected**
- Invite created; appears under Invited for that university.

### G-02 Student invite
**Steps**
1. Role = Student.
2. Select University and Campus.
3. Submit.

**Expected**
- Invite created with campus association.

### G-03 Missing University validation
**Steps**
1. Select Student role.
2. Omit University.
3. Submit.

**Expected**
- Validation error; no invite sent.

---

## Suite H — Global directories

### H-01 All Students
**Steps**
1. Open via Total Students.
2. Filter by University.
3. Open one profile.

**Expected**
- Student Profile Hub loads with correct tenant context shown.

### H-02 Coordinator directories
**Steps**
1. Open Event Coordinator (or similar) stat card.
2. Filter by University.
3. Open one User Profile.

**Expected**
- Read-only profile; correct university attribution.

### H-03 Reports
**Steps**
1. Open Total Reports.
2. Change status on one ticket.
3. Return to list.

**Expected**
- Status persists; list reflects update.

---

## Suite I — Community, Events, Travel

### I-01 Community tab and lists
**Steps**
1. Open Community tab.
2. Open community from stat card with university filter.

**Expected**
- Community profile loads; filter respected.

### I-02 Events
**Steps**
1. Open Events quick action or Total Events.
2. Open Event Details.

**Expected**
- Event loads with correct university/campus metadata.

### I-03 Travel plans
**Steps**
1. Open Total Travel Plans.
2. Apply university filter.

**Expected**
- List scopes correctly.

---

## Suite J — Chat, notifications, profile

### J-01 Chats tab
**Expected**
- Thread list loads; send message succeeds.

### J-02 Notifications
**Steps**
1. Tap bell.
2. Tap one notification with deep link.

**Expected**
- Related screen opens when deep link configured.

### J-03 Settings deferred save
**Steps**
1. Profile → Settings → Notification.
2. Toggle one value.
3. Verify **Save** appears on nav bar.
4. Tap Save.

**Expected**
- POST on Save only; Save hides after success.
- Navigating back without Save reverts or prompts per design.

### J-04 Logout
**Steps**
1. Profile → Logout → confirm.

**Expected**
- Returns to login screen; session cleared.

---

## Suite K — Filters (regression)

### K-01 Apply / Cancel / Clear All
**Steps**
1. Open filter on Manage Users.
2. Select values → Cancel → reopen (unchanged).
3. Select values → Apply → reopen (persisted).
4. Clear All → Apply.

**Expected**
- Cancel discards; Apply persists; Clear All resets.

### K-02 Visit Schedule date filter (if available)
**Steps**
1. Select Visit Schedule in sidebar.
2. Set start/end dates → Apply.

**Expected**
- List filters by date range.

---

## Suite L — Role switch regression

### L-01 Switch to University Super Admin and back
**Steps**
1. From Intoto Admin, switch to University Super Admin role.
2. Verify single-university dashboard.
3. Switch back to Intoto Admin.

**Expected**
- Each role loads correct dashboard config.
- No stale university picker state breaks USuper Admin view.

---

## 5. Non-functional checks

- [ ] Dashboard loads within acceptable time on cold start
- [ ] Pagination loads more rows on scroll (lists ≥30 items)
- [ ] Empty states shown when no data (university list, invites, reports)
- [ ] Error toast on network failure for Save and Submit actions
- [ ] Logo missing — app bar layout does not break

---

## 6. Figma spot-check (node 5051-661)

- [ ] Quick Action labels match wireframe
- [ ] University List and Details fields match wireframe
- [ ] Add University form fields match wireframe
- [ ] Manage Users shows University column and filter
- [ ] Intoto Admin role tag copy matches design
- [ ] Settings Save-on-nav-bar pattern matches wireframe

---

## 7. Sign-off checklist

- [ ] All Suite A–L cases executed
- [ ] No P1/P2 open defects for Intoto Admin scope
- [ ] Cross-tenant data isolation verified (University A data not leaked when filtering B)
- [ ] Figma spot-check completed or exceptions documented

---

*Design reference: [Figma — Intoto Admin node 5051-661](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&p=f&t=Fqpnfj5F0UbdlVZB-0)*
