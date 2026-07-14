# Intoto - University Super Admin
## QA Test Guide

**Design reference:** [Intoto Wireframe - Prototype (node 5051-661)](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&t=Fqpnfj5F0UbdlVZB-1)  
**Audience:** QA, UAT, release validation  
**Version:** 1.0

---

## 1. Scope

This guide validates University Super Admin behavior across:

- dashboard rendering and navigation
- quick way and quick actions routing
- manage users and add user validation
- student assignment and arrival flows
- community, events, and report moderation
- chats, notifications, profile/settings
- filter behavior and list pagination

---

## 2. Test data setup

Prepare at least:

- 1 University Super Admin account
- 1 invited user, 1 accepted user, 1 suspended user
- 1 assigned student, 1 unassigned student
- 1 pending community and 1 approved community
- 1 report ticket
- 1 upcoming event

---

## 3. Critical acceptance criteria

1. Role-scoped dashboard loads without cross-university data.
2. University header is visible and tappable.
3. Every visible quick way card routes correctly.
4. Manage Users supports status chips, search, filter, pagination, and actions.
5. Add User enforces role-based field requirements.
6. Community create/approve behaviors match role rules.
7. Report status transitions persist and refresh list state.
8. Filter apply/cancel/clear works consistently.

---

## 4. Functional test suites

## Suite A - Login and shell

### A-01 Login as University Super Admin
**Steps**
1. Launch app.
2. Login with University Super Admin credentials.

**Expected**
- Home dashboard opens.
- Role tag indicates University Super Admin.
- Bottom tabs visible: Home, Community, Chats, Profile.

### A-02 Header action checks
**Steps**
1. Tap university name/logo.
2. Tap notification bell.
3. Tap pending invitation envelope if shown.

**Expected**
- University details opens.
- Notifications list opens.
- Pending invitation list opens.

---

## Suite B - Quick Way routing

### B-01 Quick Way render check
**Expected**
- Card icon, label, and count are visible.
- No overlapping/truncation issues in card grid.

### B-02 Card tap routing
**Steps**
1. Tap every visible quick way card.

**Expected**
- Correct destination opens for each configured `viewKey`.
- No crash or dead tap.

### B-03 Pull-to-refresh
**Steps**
1. Pull down on dashboard.

**Expected**
- Loader appears/hides properly.
- Counts/sections refresh.

---

## Suite C - Quick Actions

### C-01 Manage User action
**Expected:** Opens Manage Users screen.

### C-02 Add User action
**Expected:** Opens Add User form.

### C-03 Events action
**Expected:** Opens event list.

### C-04 Support action
**Expected:** Opens support screen.

---

## Suite D - Manage Users

### D-01 Status chips
**Steps**
1. Tap each chip: All, Invited, Accepted, Withdrawn, Rejected, Suspended.

**Expected**
- List updates according to selected status.

### D-02 Search behavior
**Steps**
1. Enter 1-2 chars.
2. Enter 3+ chars.
3. Clear search.

**Expected**
- Debounce behavior respected.
- Valid query returns filtered list.
- Clearing resets list.

### D-03 Pagination
**Steps**
1. Scroll to bottom repeatedly.

**Expected**
- Next page loads where available.
- Stops when no more pages.
- No duplicate rows.

### D-04 Action matrix by status
Validate actions:

| Status | Expected actions |
|--------|------------------|
| Invited | Withdraw, Resend, Send Email |
| Accepted | Suspend, Send Email |
| Suspended | Re-initiate, Send Email |
| Withdrawn/Rejected | Resend, Send Email |

### D-05 Bulk action
**Steps**
1. Select multiple users.
2. Tap Take Action.
3. Choose Send Email.

**Expected**
- Take Action button appears only in selection mode.
- Mail composer opens with selected recipients.

---

## Suite E - Add User

### E-01 Required field validation
**Steps**
1. Attempt submit empty form.

**Expected**
- Required validation messages shown.
- Submission blocked.

### E-02 Campus requirement by role
**Steps**
1. Select coordinator/student role and submit without campus.

**Expected**
- Campus validation error appears.

**Steps**
1. Select University Super Admin role.

**Expected**
- Campus field hidden/not required.

### E-03 Ambassador type validation
**Steps**
1. Select Ambassador or External Ambassador.
2. Submit without ambassador type.

**Expected**
- Validation requires ambassador type.

### E-04 Successful invite
**Steps**
1. Submit valid form.
2. Open Manage Users > Invited.

**Expected**
- New invite appears in Invited list.

---

## Suite F - Student flows

### F-01 Total Students
Validate:
- search
- filter
- pagination
- row tap to profile

### F-02 Assigned Students
Validate:
- list opens and loads
- row opens profile

### F-03 Unassigned assignment flow
**Steps**
1. Open unassigned list.
2. Select student(s) and start assignment.
3. Fill coordinator + dates + work description.
4. Configure profile visibility.
5. Confirm.

**Expected**
- Success shown.
- Student removed from unassigned list.
- Student appears in assigned list.

---

## Suite G - Arrival requests

### G-01 Browse-only behavior
**Steps**
1. Open total arrival requests list.
2. Tap row.

**Expected**
- Arrival request details opens.
- No assignment action on this screen.

---

## Suite H - Community

### H-01 Create community (USuper Admin)
**Steps**
1. Create community and submit.

**Expected**
- Immediate success message.
- Community is active (not pending request state).

### H-02 Pending community approval
**Steps**
1. Open pending communities.
2. Approve one item.
3. Reject one item.

**Expected**
- Approved item exits pending queue.
- Rejected item reflects rejected state.

---

## Suite I - Events

### I-01 Upcoming event card and View All
**Expected**
- Card tap opens event details.
- View All opens upcoming event list.

### I-02 Pending event decisions (if enabled)
**Expected**
- Approve/reject actions update state.

---

## Suite J - Reports

### J-01 Report workflow
**Steps**
1. Open report.
2. Move through statuses.

**Expected**
- Status updates persist.
- Lists refresh accordingly.

### J-02 My assigned reports
**Expected**
- Only assigned-to-me items shown.

---

## Suite K - Chats and notifications

### K-01 Chat thread flow
**Expected**
- Thread opens and messages send successfully.

### K-02 Notification flow
**Expected**
- Notification list opens from bell icon.
- Tapping a notification navigates correctly when link exists.

---

## Suite L - Filters

### L-01 Apply / Cancel / Clear
**Steps**
1. Open filter.
2. Select values and Apply.
3. Reopen and Clear All.
4. Reopen and Cancel unsaved changes.

**Expected**
- Apply narrows list.
- Clear All resets list.
- Cancel does not apply unsaved state.

### L-02 Visit Schedule dates
**Expected**
- Start/end dates are set and applied correctly.

---

## 5. Non-functional checks

- No major lag on dashboard load.
- No crash while rapidly switching tabs and filters.
- Proper loader and error messaging on API failures.
- Role and strings render correctly in target languages.

---

## 6. Regression hotspots

Always re-test when dashboard/admin code changes:

1. Quick Way `viewKey` routing
2. Manage Users action matrix
3. Add User role-based validation
4. Community create/approve behaviors
5. Filter application and clear all

---

## 7. QA sign-off checklist

- [ ] All critical suites A-L pass
- [ ] No P0/P1 defects open
- [ ] No data mismatch in assignment or report workflow
- [ ] End-to-end smoke path passes:
  - Home -> Total Students -> Manage Users -> Add User -> Pending Communities -> Total Reports

---

## 8. Related documents

- Full feature guide: `docs/University-Super-Admin-Features-and-Flows.md`
- Client demo guide: `docs/University-Super-Admin-Client-Demo-Guide.md`

