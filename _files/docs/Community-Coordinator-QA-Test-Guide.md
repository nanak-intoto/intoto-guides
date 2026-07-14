# Intoto — Community Coordinator
## QA Test Guide

**Design reference:** [Intoto Wireframe — Community Coordinator (node 5088-26466)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5088-26466&page-id=5051%3A661)  
**Prototype:** [Community Coordinator prototype — start 5088-26466](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5088-26466&p=f&t=SHs6dnxTAjeaxqN7-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5088%3A26466)  
**Audience:** QA, UAT, release validation  
**Version:** 1.0

---

## 1. Scope

Validate **Community Coordinator** (`community_coordinator`) against Figma **5088-26466**:

- Home overview (app bar, Quick Way, Quick Actions, pending/active carousels, analytics, banners)
- Pending community approve/reject with reason validation
- Active community browse, profile, feed, posts
- Create community (staff instant publish path)
- Community tab flows
- Reports moderation (if configured for role)
- Chats, Support, notifications, role switcher
- Student cross-check: pending hidden until approved; approved visible in discover
- Boundaries: no Manage Users, no event approval, no student assignment on CC-only account

**Out of scope:** Event Coordinator event queues, TPC assignment, Ambassador profile form.

---

## 2. Test data

| Data | Purpose |
|------|---------|
| 1 Community Coordinator account | Primary |
| 1+ pending community request | Approve/reject |
| 1+ active community | Feed/profile |
| 1 Student account | Submit + discover |
| Multi-role CC + Student | Role switcher |
| 1 report case (optional) | Moderation |
| Rejected request sample | Reason display to creator |

---

## 3. Critical acceptance criteria

1. CC login → Home loads without crash; sections match API role config.
2. University header: name always visible; logo optional; tap → university details.
3. Pending list opens from Quick Way or carousel; details show full request fields.
4. **Approve** removes from pending; community appears in active/discover for students.
5. **Reject** without reason blocked; with reason succeeds; community not public.
6. **Create Community** as CC succeeds immediately (not student pending path).
7. Community Profile: members and feed load; post detail opens.
8. Quick Way counts update after pull-to-refresh post-approval.
9. CC-only account cannot open Manage Users or event pending approval as primary owner.
10. Role switcher changes dashboard when CC ↔ Student.

---

## 4. Test suites

## Suite A — Login and shell

### A-01 Login Community Coordinator
**Expected:** Home; tabs Home, Community, Chats, Profile.

### A-02 App bar
**Steps:** Bell; envelope; tap university.  
**Expected:** Notifications; invitations; university/campus details.

### A-03 Role switcher
**Steps:** CC ↔ Student.  
**Expected:** CC Home shows community stats; Student Home shows student sections — not mixed.

---

## Suite B — Quick Way and Quick Actions

### B-01 Quick Way render
**Expected:** Community-relevant cards only (per config).

### B-02 Total Communities
**Expected:** List; search; filter; row → profile.

### B-03 Pending Communities
**Expected:** Pending queue only.

### B-04 Community Members (if shown)
**Expected:** Member list or hub loads.

### B-05 Communities / Create quick actions
**Expected:** Correct destinations.

### B-06 Support
**Expected:** Support screen.

---

## Suite C — Pending approval

### C-01 Pending carousel
**Steps:** Swipe; tap; View All.  
**Expected:** Details; list consistency.

### C-02 Approve
**Expected:** Pending ↓; active ↑; student discoverability.

### C-03 Reject empty reason
**Expected:** Validation error.

### C-04 Reject with reason
**Expected:** Success; creator sees reason (notification or status).

### C-05 Duplicate / policy edge
**Expected:** Server or UI error per product rules.

---

## Suite D — Create community (staff)

### D-01 Create required fields
**Expected:** Immediate live community; success copy differs from student pending message.

### D-02 Create validation
**Expected:** Required fields enforced.

### D-03 Images optional/required
**Expected:** Per wireframe validation.

---

## Suite E — Active community management

### E-01 Active carousel / list
**Expected:** Only live communities.

### E-02 Community Profile
**Expected:** About, members, feed entry.

### E-03 Post detail
**Expected:** Opens from feed tap.

### E-04 Create post (if permitted)
**Expected:** Publishes to feed.

### E-05 Moderation actions (if in Figma)
**Expected:** Remove/hide behaves; audit trail if designed.

---

## Suite F — Community tab

### F-01 Discover
**Expected:** Lists live communities.

### F-02 My communities
**Expected:** Joined groups for coordinator account.

### F-03 Create from tab
**Expected:** Same as quick action create path.

---

## Suite G — Lists utilities

### G-01 Search
### G-02 Filter apply/clear
### G-03 Pagination
### G-04 Pull refresh Home and lists

---

## Suite H — Reports (if configured)

### H-01 Open report list
### H-02 Status workflow Assigned → Resolved
### H-03 Link from report to community/post context

---

## Suite I — Student integration

### I-01 Student submit → pending message
### I-02 CC approve → student sees community in Discover
### I-03 CC reject → student does not see live community

---

## Suite J — Chats and regression

### J-01 Chat with student creator
### J-02 Community tab smoke
### J-03 Profile logout

---

## Suite K — Boundaries

### K-01 No Manage Users on CC-only account
### K-02 No assign-student flows
### K-03 No primary event approve UI on CC-only account

---

## 5. Defect severity

| Severity | Example |
|----------|---------|
| Critical | Crash on Home; approve no-op; student sees unapproved community |
| Major | Pending stuck after approve; wrong list on Quick Way |
| Minor | Copy vs Figma |
| Trivial | Spacing |

---

## 6. Sign-off checklist

- [ ] A–B Home and navigation  
- [ ] C Pending approve/reject  
- [ ] D Staff create  
- [ ] E–F Community profile and tab  
- [ ] G List utilities  
- [ ] H Reports (if applicable)  
- [ ] I Student integration  
- [ ] J–K Smoke and boundaries  
- [ ] Full Figma walk 5088-26466  

---

*Prototype: [5088-26466](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5088-26466&p=f&t=SHs6dnxTAjeaxqN7-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5088%3A26466)*
