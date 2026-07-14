# Intoto — Event Coordinator
## QA Test Guide

**Design reference:** [Intoto Wireframe — Event Coordinator (node 5086-25745)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&page-id=5051%3A661)  
**Prototype:** [Event Coordinator prototype — start 5086-25745](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&p=f&t=ttUcU9kASuy321kT-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5086%3A25745)  
**Audience:** QA, UAT, release validation  
**Version:** 1.0

---

## 1. Scope

Validate **Event Coordinator** (`event_coordinator`) against Figma node **5086-25745**:

- Home overview (app bar, Quick Way, Quick Actions, event carousels, category graph, banners, activities)
- Event lists — search, filter, pagination, View All
- Event Details — approve, reject, registrations, attendance, feedback
- Create / edit / cancel event flows
- Event Analytics (Home chart + full screen)
- Tabs: Community, Chats, Profile (smoke)
- Notifications, invitations, role switcher
- Student cross-check: approved events visible; pending/rejected hidden

**Out of scope:** USA Manage Users, TPC student assignment, Ambassador `ambassadorForm`.

---

## 2. Test data

| Data | Purpose |
|------|---------|
| 1 Event Coordinator account | Primary |
| 1+ upcoming published event | Upcoming carousel |
| 1+ pending event | Approve/reject |
| 1+ completed event | Completed carousel |
| 1 Student account | Visibility / register |
| Multi-role EC + Student | Role switcher |
| Banner/activity payloads | Optional sections |

---

## 3. Critical acceptance criteria

1. Login as Event Coordinator → Home loads; no crash.
2. University header: logo optional; name visible; tap → university details.
3. `quick_way_total_events` → All Events list with search/filter/pagination.
4. `quick_way_events_analytics` → analytics screen with charts or graceful empty.
5. Upcoming / Pending / Completed carousels show **correct status** (not duplicate wrong-status lists).
6. Approve pending → event leaves pending; appears upcoming per rules.
7. Reject without reason → blocked; with reason → success; students do not see event.
8. Create event → correct list/carousel; edit persists.
9. View All on each carousel → correctly filtered list.
10. Pull-to-refresh updates Home counts and carousels.
11. Support quick action opens Support.
12. EC cannot access Manage Users / assign students without other roles.

---

## 4. Test suites

## Suite A — Login and shell

### A-01 Login Event Coordinator
**Expected:** Home; tabs Home, Community, Chats, Profile.

### A-02 App bar
**Steps:** Bell; envelope if present; tap university block.  
**Expected:** Notifications; invitations; university/campus details.

### A-03 Role switcher
**Steps:** EC ↔ Student on multi-role account.  
**Expected:** Dashboard sections match role (events vs student alerts).

---

## Suite B — Quick Way and Quick Actions

### B-01 Quick Way render
**Expected:** Total Events, Events Analytics (if configured).

### B-02 Total Events
**Expected:** Event list; search; filter; row → details.

### B-03 Events Analytics
**Expected:** Analytics UI; filters; no crash on empty data.

### B-04 Events quick action
**Expected:** Same catalog entry as appropriate.

### B-05 Support quick action
**Expected:** Support screen.

---

## Suite C — Home event sections

### C-01 Upcoming carousel
**Steps:** Swipe; tap card; View All.  
**Expected:** Details; upcoming list.

### C-02 Pending carousel
**Steps:** Swipe; tap; View All.  
**Expected:** Approve/reject on details; pending list.

### C-03 Completed carousel
**Steps:** Swipe; tap; View All.  
**Expected:** Details; completed list.

### C-04 Status isolation
**Steps:** Compare event IDs across three carousels on one Home load.  
**Expected:** IDs match status semantics — defect if all three identical incorrectly.

### C-05 Events by Category graph
**Expected:** Chart or empty state; subtitle if API sends `viewSubtitle`.

### C-06 Banners / Activities
**Expected:** Tap navigates per CTA.

### C-07 Pull to refresh Home
**Expected:** Reload success.

---

## Suite D — Approve / reject

### D-01 Approve
**Expected:** Pending updated; upcoming/student visibility per rules.

### D-02 Reject empty reason
**Expected:** Validation error.

### D-03 Reject with reason
**Expected:** Success; not student-visible.

---

## Suite E — Create / edit / cancel

### E-01 Create minimal required fields
**Expected:** Event created in correct status bucket.

### E-02 Create validation
**Expected:** Required field errors; no silent fail.

### E-03 Edit upcoming
**Expected:** Saved fields on details and list.

### E-04 Cancel/unpublish (if in Figma)
**Expected:** Registration closed; correct status.

---

## Suite F — Event Details deep

### F-01 Registrations list
**Expected:** Registered students; search if designed.

### F-02 Attendance
**Expected:** Mark/save attendance; reflected in analytics where applicable.

### F-03 Feedback tab
**Expected:** Loads or empty per data.

---

## Suite G — Lists

### G-01 Search debounce
### G-02 Filter apply/clear
### G-03 Pagination scroll
### G-04 Pull refresh on list

---

## Suite H — Analytics

### H-01 Full screen from Quick Way
### H-02 Home graph vs analytics consistency (rough order of magnitude)

---

## Suite I — Student cross-role

### I-01 Approved event on Student Home/Events + register
### I-02 Pending/rejected not visible to student

---

## Suite J — Regression smoke

### J-01 Community tab
### J-02 Chats send/receive with student
### J-03 Profile logout

---

## Suite K — Boundaries

### K-01 No Manage Users on EC-only account
### K-02 No assign-student flows on EC-only account

---

## 5. API expectations (UAT with backend)

When validating integrated builds, typical Home slices:

| Purpose | Method | Path (typical) |
|---------|--------|----------------|
| Overview layout | POST | `home/overview` |
| Upcoming events | GET | `home/events/upcoming` |
| Pending events | GET | `home/events/pending` |
| Completed events | GET | `home/events/completed` |
| Banners | GET | `home/banners` |
| Activities | GET | `home/activities-ads` |

Confirm with backend spec for your environment; Figma is source for UX copy and flow order.

---

## 6. Defect severity

| Severity | Example |
|----------|---------|
| Critical | Home crash; approve no-op; students see pending |
| Major | Wrong events in all carousels; analytics blank with data |
| Minor | Figma copy mismatch |
| Trivial | Spacing |

---

## 7. Sign-off checklist

- [ ] A–C Home and carousels  
- [ ] D Approve/reject  
- [ ] E Create/edit  
- [ ] F Registrations/attendance  
- [ ] G Lists  
- [ ] H Analytics  
- [ ] I Student visibility  
- [ ] J–K Smoke and boundaries  
- [ ] Figma walkthrough node 5086-25745 complete  

---

*Prototype: [5086-25745](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&p=f&t=ttUcU9kASuy321kT-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5086%3A25745)*
