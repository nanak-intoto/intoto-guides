# Intoto - Third Party Coordinator
## QA Test Guide

**Design reference:** [Intoto Wireframe - Prototype (node 5051-661)](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&t=Fqpnfj5F0UbdlVZB-1)  
**Audience:** QA, UAT, release validation  
**Version:** 1.0

---

## 1. Scope

This guide validates **Third Party Coordinator** (`thirdparty_coordinator`) behavior across:

- dashboard rendering and Quick Way routing
- Quick Actions (Manage User, Add User, Events, Support)
- Manage Users (coordinator-specific status chips and actions)
- student lists, assignment flow, and profile visibility configuration
- sub-coordinator list and arrival request browse-only behavior
- filters, search, pagination, chat, notifications

---

## 2. Test data setup

Prepare at least:

- 1 Third Party Coordinator account
- 1 invited sub-coordinator, 1 accepted sub-coordinator, 1 student-assigned sub-coordinator
- 1 suspended sub-coordinator (optional)
- 1 unassigned student, 1 assigned student
- 1 arrival request record
- 1 upcoming event (if dashboard section enabled)

---

## 3. Critical acceptance criteria

1. Dashboard loads with role tag **Third Party Coordinator** (or localized equivalent).
2. Quick Way cards route to correct screens per `viewKey`.
3. Manage Users shows coordinator status set including **Student Assigned**.
4. **Accepted / Student Assigned** actions include Student List, Assign Student, Suspend, Send Email.
5. Assign student flow completes and moves student off unassigned list.
6. Total Arrival Requests list is browse-only (details open; no assign on that screen).
7. Add User validates campus for roles that require it.
8. Filters apply, clear, and cancel behave correctly on list screens.

---

## 4. Functional test suites

## Suite A - Login and shell

### A-01 Login as Third Party Coordinator
**Steps**
1. Launch app.
2. Login with Third Party Coordinator credentials.

**Expected**
- Home dashboard opens.
- Role tag shows Third Party Coordinator.
- Bottom tabs: Home, Community, Chats, Profile.

### A-02 Header actions
**Steps**
1. Tap university logo/name.
2. Tap notification bell.
3. Tap pending invitation envelope if shown.

**Expected**
- University/campus details opens.
- Notifications list opens.
- Pending invitations list opens when applicable.

### A-03 Role switcher (multi-role account)
**Steps**
1. Switch to another role and back to Third Party Coordinator.

**Expected**
- Dashboard sections/cards appropriate to coordinator role after switch back.

---

## Suite B - Quick Way routing

### B-01 Quick Way render
**Expected**
- Section title and cards visible (per API config).
- Icon, label, count displayed per card.

### B-02 Coordinator viewKey routing
**Steps**
Tap each visible card and verify destination:

| `viewKey` | Expected destination |
|-----------|------------------------|
| `quick_way_total_students` | All Students |
| `quick_way_total_assigned_students` | Assigned Student List |
| `quick_way_total_sub_coordinator` | Sub Coordinator List |
| `quick_way_total_thirdparty_sub_coordinators` | Sub Coordinator List |
| `quick_way_total_arrival_requests` | Arrival requests list (browse) |
| `quick_way_total_unassigned_requests` | Unassigned Student List |
| `quick_way_total_unassigned_students` | Unassigned Student List |
| `quick_way_my_assigned_requests` | Assigned Student List |
| `quick_way_my_upcoming_arrivals` | Sub Coordinator List |
| `quick_way_my_completed_arrivals` | No navigation / stable no-op |

**Expected**
- No crash on any tap.
- Correct screen title from stat card label.

### B-03 Pull-to-refresh
**Steps**
1. Pull down on Home dashboard.

**Expected**
- Refresh completes; counts update where data changed.

---

## Suite C - Quick Actions

### C-01 Manage User
**Expected:** Manage Users opens with coordinator role context.

### C-02 Add User
**Expected:** Add User form opens.

### C-03 Events
**Expected:** Events list opens.

### C-04 Support
**Expected:** Support screen opens.

---

## Suite D - Manage Users (coordinator-specific)

### D-01 Status chips present
**Expected chips include:**
- All, Invited, Accepted, **Student Assigned**, Withdrawn, Rejected, Suspended

**Not expected (vs super admin):** super-admin-only chip differences only if API sends same set — verify **Student Assigned** exists for coordinator.

### D-02 Search and pagination
**Steps**
1. Search with 3+ characters.
2. Scroll to end for pagination.

**Expected**
- Debounced search filters list.
- Next page loads when `hasNextPage` true.

### D-03 Action matrix — Suspended
**Steps**
1. Filter Suspended, select row(s), Take Action.

**Expected actions:** Withdraw Invite, Resend Invite, Send Email.

### D-04 Action matrix — Accepted / Student Assigned
**Steps**
1. Filter Accepted or Student Assigned.
2. Select one sub-coordinator, Take Action.

**Expected actions:** **Student List**, **Assign Student**, Suspend Account, Send Email.

### D-05 Student List action
**Steps**
1. Take Action → Student List on accepted coordinator.

**Expected**
- Assigned Student List opens scoped to that coordinator/sub-coordinator info.

### D-06 Assign Student action
**Steps**
1. Take Action → Assign Student on accepted coordinator.

**Expected**
- Unassigned Student List opens with coordinator context (`subcoordinatorInfo`).

### D-07 Resend invite
**Steps**
1. Invited or Withdrawn/Rejected row → Resend → set expiry → confirm.

**Expected**
- Success toast; list refreshes.

### D-08 Bulk Send Email
**Steps**
1. Multi-select rows with valid emails.
2. Take Action → Send Email.

**Expected**
- Mail composer opens with recipients.

---

## Suite E - Add User

### E-01 Empty submit validation
**Expected:** Required fields block submit.

### E-02 Campus required for sub-coordinator / student roles
**Steps**
1. Select role requiring campus.
2. Submit without campus.

**Expected:** Campus validation error.

### E-03 Successful invite
**Steps**
1. Complete valid invite for sub-coordinator.
2. Check Manage Users → Invited.

**Expected:** New row appears under Invited.

---

## Suite F - Student lists

### F-01 All Students
**Expected:** Search, filter, pagination, profile on row tap.

### F-02 Assigned Students
**Expected:** List scoped to assigned students; profile opens on tap.

### F-03 Unassigned Students
**Expected:** List shows unassigned; selection enables assign flow entry point.

---

## Suite G - Assign student flow

### G-01 Full assignment
**Steps**
1. Unassigned list → select student(s) → Assign.
2. Choose sub-coordinator, dates, work description.
3. Configure profile section visibility.
4. Confirm.

**Expected**
- Success feedback.
- Student no longer in unassigned list (or count decreases).
- Student visible in assigned list / coordinator student list.

### G-02 Assign from Manage Users shortcut
**Steps**
1. Manage Users → Accepted coordinator → Assign Student.
2. Complete assignment for at least one student.

**Expected**
- Same assignment pipeline as unassigned list entry.

---

## Suite H - Arrival requests (browse-only)

### H-01 List and details
**Steps**
1. Open Total Arrival Requests.
2. Tap row.

**Expected**
- Arrival Request Details opens.
- No assign button on this list that bypasses unassigned flow.

### H-02 Search/filter on arrival list
**Expected:** List narrows correctly when filter/search applied.

---

## Suite I - Sub-coordinator list

### I-01 Sub-coordinator drill-down
**Steps**
1. Open Total Sub Coordinator or ThirdParty Sub Coordinators card.
2. Tap sub-coordinator row.

**Expected**
- Navigates to assigned students for that sub-coordinator (per configuration).

---

## Suite J - Events and dashboard extras

### J-01 Upcoming events carousel (if shown)
**Expected:** Card → Event Details; View All → upcoming list.

### J-02 Activities carousel (if shown)
**Expected:** Tap opens URL or in-app destination without crash.

---

## Suite K - Filters

### K-01 Manage Users filter categories
**Expected:** Campus, Role (and others per list type); Apply/Cancel/Clear All work.

### K-02 All Students filter categories
**Expected:** Extended categories (campus, country, languages, visit schedule, etc.) apply correctly.

### K-03 Visit Schedule date filter
**Expected:** Start/end dates apply to student list.

---

## Suite L - Chat and notifications

### L-01 Chat
**Expected:** Thread opens; message sends.

### L-02 Notifications
**Expected:** Bell opens list; tap navigates when deep link configured.

---

## 5. Non-functional checks

- No crash when rapidly switching status chips on Manage Users.
- Loader shows/hides on list and dashboard refresh.
- Empty states readable (no broken layout).
- University header shows full name (multi-line) without broken layout when logo missing.

---

## 6. Regression hotspots

Re-test when touching:

1. `DashboardOverviewViewController` `handleOverviewStatTap` routing
2. `ManageUserViewModel.buildActionsForCoordinator`
3. `ManageUsersViewController` Assign Student / Student List navigation
4. Unassigned → assignment → profile configuration chain
5. `CoordinatorAssignmentUserListConfiguration.totalArrivalRequests`
6. User Filter + Manage Users list type `.manageUser`

---

## 7. QA sign-off checklist

- [ ] Suites A–L pass on target build
- [ ] No P0/P1 open for coordinator flows
- [ ] Assign student E2E verified with real API data
- [ ] Coordinator action matrix verified for Accepted and Student Assigned
- [ ] Smoke path passes:
  - Home → Unassigned → Assign → Manage Users → Student List → Arrival Details

---

## 8. Related documents

- Full feature guide: `docs/Third-Party-Coordinator-Features-and-Flows.md`
- Client demo guide: `docs/Third-Party-Coordinator-Client-Demo-Guide.md`
