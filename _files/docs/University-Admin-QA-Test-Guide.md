# Intoto — University Admin
## QA Test Guide

**Design reference:** [INTOTO WebApp — University Super Admin (node 81-7360)](https://www.figma.com/design/hNVFYMIiLyFZJKD8khkn4Q/INTOTO-WebApp?node-id=81-7360&p=f&m=dev)  
**Prototype:** [INTOTO WebApp — Dashboard (546-1397)](https://www.figma.com/design/hNVFYMIiLyFZJKD8khkn4Q/INTOTO-WebApp?node-id=546-1397&page-id=81%3A7360)  
**Audience:** QA, UAT, release validation  
**Version:** 1.0

---

## 1. Scope

This guide validates **University Admin** behavior on the **INTOTO WebApp** (browser):

- authentication and role selection
- sidebar navigation and header chrome
- dashboard stat cards, charts, date filters
- Manage User (list, filter, add, row actions, pagination)
- Profile Review summary and queue
- My University tabs and edit flows
- Campus CRUD and campus detail tabs
- Community (active, pending, feed, reports)
- Travel Plan list and detail statuses
- Ambassadors (internal, external, detail, leads)
- Events lifecycle (create, approve, register, attendance, feedback)
- Chat group creation
- Invite Data, Configurations, Support, Profile, Logout

**Out of scope (other roles):**
- Mobile University Super Admin (`University-Super-Admin-QA-Test-Guide.md`)
- Intoto Admin cross-tenant platform
- Ambassador Platform public web portal

---

## 2. Test data setup

Prepare at least:

- 1 **University Admin** web account
- 1 university with branding (logo, name)
- 10+ users: mix of Student, Ambassador, Event Coordinator, Campus Admin, University Super Admin
- User statuses: Accepted, Invited, Suspended, Pending Review
- 2+ campuses
- 1 pending community request, 1 active community
- 1 open report (Pending or Under review)
- 1 upcoming travel plan
- 1 internal + 1 external ambassador
- 1 draft event, 1 pending event, 1 published event
- Notification count > 0 on header bell

**Browser:** Chrome (latest), Safari (latest), 1920×1080 viewport.

---

## 3. Critical acceptance criteria

1. Dashboard loads university-scoped data for University Admin.
2. Role label in header shows **University Admin**.
3. Sidebar lists all modules; active item highlighted blue.
4. **Dashboard Overview** shows 10 stat cards with counts.
5. Stat card click routes to correct list.
6. **Manage Users** table columns and statuses match Figma.
7. **Add Users** creates Invited row; Approve/Reject updates status.
8. **Profile Review** cards filter list correctly.
9. **My University** tabs load; Overview edits persist.
10. Campus add → list → detail tabs work.
11. Community pending approve moves to active list.
12. Event create → pending → published path works.
13. Logout clears session → Login screen.

---

## 4. Functional test suites

## Suite A — Login and shell

### A-01 Login as University Admin
**Steps**
1. Open WebApp URL.
2. Tap **Continue** on **Login or Sign-up**.
3. Complete SSO.

**Expected**
- Dashboard opens.
- Header shows **University Admin**.
- Sidebar visible with all menu items.

### A-02 Email verification
**Steps**
1. Signup as unverified user.
2. Observe **Email Verification Required!**

**Expected**
- Verification copy references submitted email.
- After verify, user can reach Dashboard.

### A-03 Multi-role selection
**Steps**
1. Login with multi-role account.
2. Select University Admin on **Role** picker.

**Expected**
- Dashboard loads with university scope.

### A-04 Sidebar navigation
**Steps**
1. Click each sidebar item.

**Expected**
- Each module loads; active highlight follows.

### A-05 Notifications
**Steps**
1. Click header bell.

**Expected**
- Panel opens; badge matches unread count.

---

## Suite B — Dashboard

### B-01 Stat cards
**Steps**
1. Load Dashboard.

**Expected**
- All 10 **Dashboard Overview** cards present with numeric counts.

### B-02 Card routing
**Steps**
1. Click **Students** card.

**Expected**
- Students list or filtered Manage Users.

### B-03 Date filter
**Steps**
1. Set Custom + From/To Date → apply.

**Expected**
- Widgets refresh; invalid range validated.

### B-04 Charts
**Steps**
1. Verify Student Admission, Student Travel Plan, Student's Location widgets.

**Expected**
- Labels and totals match API data.

---

## Suite C — Manage User

### C-01 List and search
**Steps**
1. Open **Manage User**.
2. Search known email.

**Expected**
- **Total Users** shown; search filters rows.

### C-02 Filter
**Steps**
1. Open Filter → Role + Campus + Status → apply.

**Expected**
- Table matches; clear resets.

### C-03 Add Users
**Steps**
1. **Add Users** → Event Coordinator → submit.

**Expected**
- Row **Invited**.

### C-04 Approve / Reject
**Steps**
1. ⋮ → Approve or Reject.

**Expected**
- Status updates; access reflects change.

### C-05 Pagination
**Steps**
1. Go to page 2.

**Expected**
- **Showing** range updates.

---

## Suite D — Profile Review

### D-01 Summary cards
**Steps**
1. Open **Profile Review**.

**Expected**
- Six summary cards visible.

### D-02 Approve profile
**Steps**
1. Open pending row → approve.

**Expected**
- **Complete** count increases.

---

## Suite E — My University

### E-01 Tabs
**Steps**
1. Visit all six tabs.

**Expected**
- Each loads unique content.

### E-02 Edit and export
**Steps**
1. Edit About → save.
2. Tap **Export**.

**Expected**
- Edit persists; export downloads.

---

## Suite F — Campus

### F-01 CRUD
**Steps**
1. Add campus → verify list.
2. Delete campus → confirm.

**Expected**
- Success messages; list updates.

### F-02 Detail tabs
**Steps**
1. Open campus → all detail tabs.

**Expected**
- Scoped data per tab.

---

## Suite G — Community

### G-01 Pending → active
**Steps**
1. Approve pending community.

**Expected**
- Appears in Active Communities.

### G-02 Reports
**Steps**
1. Triage report Pending → resolved.

**Expected**
- Status transitions persist.

---

## Suite H — Travel

### H-01 List and detail
**Steps**
1. Open Travel Plan → Upcoming detail.

**Expected**
- Detail matches list row.

---

## Suite I — Ambassadors

### I-01 Lists and detail
**Steps**
1. Open internal and external lists.
2. Open Ambassador Detail and lead tabs.

**Expected**
- Correct data per tab.

---

## Suite J — Events

### J-01 Lifecycle
**Steps**
1. Create event → approve → publish.
2. Register student → Mark Present → Feedback.

**Expected**
- Each stage persists correctly.

---

## Suite K — Chat, Config, Support, Logout

### K-01 Chat group
**Steps**
1. Create group chat.

**Expected**
- Group appears in chat list.

### K-02 Logout
**Steps**
1. **Log Out** → confirm.

**Expected**
- Login screen; session cleared.

---

## 5. Regression smoke (release gate)

| # | Test | Pass |
|---|------|------|
| 1 | Login → Dashboard | ☐ |
| 2 | All sidebar links load | ☐ |
| 3 | Manage User search | ☐ |
| 4 | Add Users → Invited | ☐ |
| 5 | Profile Review cards | ☐ |
| 6 | My University edit save | ☐ |
| 7 | Campus list | ☐ |
| 8 | Community approve | ☐ |
| 9 | Events list | ☐ |
| 10 | Logout | ☐ |

---

## 6. Figma alignment checklist

| Frame | Node ID | Verified |
|-------|---------|----------|
| Dashboard | 546:1397 | ☐ |
| Sidebar | 2412:31468 | ☐ |
| Manage Users | 629:4355 | ☐ |
| Profile Review | 2169:16374 | ☐ |
| My University Overview | 702:12369 | ☐ |
| Login | 1913:58209 | ☐ |
| Logout | 553:2942 | ☐ |

---

## 7. Related documentation

| Document | Use |
|----------|-----|
| `University-Admin-Features-and-Flows.md` | Feature reference |
| `University-Admin-Client-Demo-Guide.md` | Demo script |
| `University-Super-Admin-QA-Test-Guide.md` | Mobile app QA |

---

## Document history

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | Jun 2026 | Initial QA guide from INTOTO WebApp Figma |
