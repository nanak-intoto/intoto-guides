# Intoto — Student
## QA Test Guide

**Design reference:** [Intoto Wireframe — Prototype (node 5051-661)](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&t=Fqpnfj5F0UbdlVZB-1)  
**Audience:** QA, UAT, release validation  
**Version:** 1.0

---

## 1. Scope

This guide validates **Student** (`student`) behavior across:

- login, profile setup, and student dashboard (`DashboardViewController`)
- profile/travel completion alerts and section hubs
- quick actions routing (campus, travel, events, support, AI, social)
- discovery lists (classmates, roommates, travel buddies) with search/filter
- events (browse, register, feedback)
- community (browse, join, create with approval)
- ambassadors, chat, notifications, profile tab settings

**Out of scope for Student QA:** Quick Way admin stat cards, Manage Users, Add User, student assignment, report moderation.

---

## 2. Test data setup

Prepare at least:

- 1 Student account (incomplete profile and/or travel for alert testing)
- 1 Student account with **complete** profile and travel (for travel buddy gate)
- 1 upcoming event with open registration (+ optional registration questions)
- 1 past event eligible for feedback popup (if API supports)
- 2+ peer students for discovery lists
- 1 ambassador on dashboard
- 1 approved community; optional 1 pending student-created community
- 1 chat thread
- 1 notification with deep link (optional)
- 1 pending role invitation (optional, for envelope icon)

---

## 3. Critical acceptance criteria

1. Student lands on **DashboardViewController** (not admin overview).
2. **No Quick Way stat cards** render for student role.
3. Profile alert (`INCOMPLETE_PROFILE_DATA`) opens **My Profile** hub; travel alert (`INCOMPLETE_TRAVEL_DATA`) opens **Travel Plan** hub.
4. Quick actions route per `actionId` without crash.
5. Profile sections save, show updated status, and support Next/Previous flow.
6. Travel plan sections save; signature requires consent when configured.
7. Travel hub **Connect with Other Travellers** blocked until travel plan complete.
8. Event registration succeeds and reflects on My Events when applicable.
9. Student community create shows **approval pending** message (not instant live).
10. Discovery lists: search (3+ chars), filter apply/cancel, row → peer profile.

---

## 4. Functional test suites

## Suite A — Login and shell

### A-01 Login as Student
**Steps**
1. Launch app.
2. Login with Student credentials.

**Expected**
- Home dashboard opens (`DashboardViewController`).
- University logo/name in navigation bar.
- Bottom tabs: Home, Community, Chats, Profile.

### A-02 First-time profile setup (if applicable)
**Steps**
1. Login with new student account before tab bar access.

**Expected**
- Profile Setup screen appears.
- Continue with valid data → tab bar loads.

### A-03 Role switcher (multi-role account)
**Steps**
1. Switch to another role and back to Student.

**Expected**
- Student dashboard reloads; no admin Quick Way cards after switch back.

### A-04 Header actions
**Steps**
1. Tap notification bell.
2. Tap pending invitation envelope if shown.

**Expected**
- Notifications list opens.
- Pending Invitations list opens when applicable.

---

## Suite B — Student dashboard

### B-01 Dashboard sections render
**Expected (per API config)**
- Banner carousel (if provided).
- Quick Actions / Features grid.
- My Events, Upcoming Events, Activities, Ambassadors (when API sends them).
- **No** Quick Way stat card section.

### B-02 Pull-to-refresh
**Steps**
1. Pull down on Home.

**Expected**
- Refresh completes; events/alerts update.

### B-03 Banner and activities tap
**Steps**
1. Tap banner CTA or activity card with `action_url`.

**Expected**
- URL opens (in-app or browser) without crash.

---

## Suite C — Completion alerts

### C-01 Profile incomplete alert
**Steps**
1. Login with incomplete profile student.
2. Tap alert on Home.

**Expected**
- Navigates to `UserProfileSectionsViewController`.
- Progress percentage shown on alert when API provides it.

### C-02 Travel incomplete alert
**Steps**
1. Login with incomplete travel student.
2. Tap travel alert.

**Expected**
- Navigates to `TravelPlanSectionsViewController`.

### C-03 Alert clears after completion
**Steps**
1. Complete remaining profile or travel sections.
2. Return to Home and refresh.

**Expected**
- Corresponding alert hidden or progress updated.

---

## Suite D — Quick Actions routing

Tap each visible quick action and verify destination:

| `actionId` | Expected destination |
|------------|----------------------|
| `viewCampus` | Campus Details |
| `viewTravelPlan` | Travel Plan hub |
| `viewEvents` | Events list |
| `viewSupport` | Support screen |
| `viewAskAI` | AI Search (if configured) |
| `connectWithClassmate` | Connect with Classmates list |
| `findRoommate` | Find Roommate list |
| `travelBuddy` | Travel Buddy list |
| `myEvents` | My Events list |

**Expected**
- No crash on any tap.
- Screen title matches action label where applicable.

---

## Suite E — My Profile (studentForm)

### E-01 Section list loads
**Expected**
- Sections from API with complete/incomplete status.
- Profile header shows name, email, photo.

### E-02 Section edit and save
**Steps**
1. Open Basic Details (or any editable section).
2. Change a field → Save.

**Expected**
- Success feedback.
- Section status updates on return to hub.

### E-03 Next / Previous flow
**Steps**
1. Open a section → Save → tap **Next**.
2. Tap **Previous**.

**Expected**
- Navigates to adjacent sections in API order.
- Unsaved changes prompt when leaving with dirty form.

### E-04 Picture management
**Steps**
1. Tap Picture section or header edit.
2. Test View / Change / Remove photo.

**Expected**
- Image picker and upload work; remove clears photo.

### E-05 Personal documents
**Steps**
1. Open Personal Documents.
2. Upload or view document slot.

**Expected**
- Upload succeeds; detail view shows status (pending/approved/rejected if applicable).

### E-06 Shared by University
**Expected**
- Read-only university-shared documents visible when API provides them.

---

## Suite F — Travel Plan (travelForm)

### F-01 Hub loads travel plan
**Steps**
1. Open Travel Plan from quick action.

**Expected**
- Travel plan fetched/created; section list displays.

### F-02 Travel Details save
**Steps**
1. Open Travel Details → fill required fields → Save.

**Expected**
- Data persists; section marked complete when criteria met.

### F-03 Travel Documents upload
**Expected**
- Document upload and review status behave like personal documents.

### F-04 Signature and consent
**Steps**
1. Open Signature section.
2. Attempt submit without consent checkbox.

**Expected**
- Validation blocks submit until consent checked.
3. Draw/upload signature → Submit.

**Expected**
- Success; section complete.

### F-05 Connect with Other Travellers gate
**Steps**
1. With **incomplete** travel plan, tap Connect button.

**Expected**
- Toast/message to complete travel plan first.

**Steps**
2. With **complete** travel plan, tap Connect.

**Expected**
- Opens Travel Buddy list.

### F-06 Program Details location
**Expected**
- Program Details edited from **My Profile**, not travel hub section list.

---

## Suite G — Social discovery

### G-01 Connect with Classmates
**Expected**
- List loads; search debounces at 3+ characters.
- Filter apply/cancel works.
- Row tap → peer profile (`UserProfileViewController`).

### G-02 Find Roommate
**Expected**
- Same search/filter/pagination/profile behavior as classmates.

### G-03 Travel Buddy
**Expected**
- List loads with travel-specific filters.
- Row tap → peer profile.

### G-04 Peer profile visibility
**Expected**
- Peer viewer sees allowed sections only (basic details, preferences per config).
- No admin/coordinator assignment actions.

### G-05 Chat from profile
**Steps**
1. From peer or ambassador profile, start chat if action available.

**Expected**
- Chat thread opens or composes correctly.

---

## Suite H — Ambassadors

### H-01 Dashboard carousel
**Steps**
1. Tap ambassador card on Home.

**Expected**
- Ambassador profile opens.

### H-02 View All
**Steps**
1. Tap View All on ambassadors section.

**Expected**
- Ambassador list opens; row tap → profile.

---

## Suite I — Events

### I-01 Upcoming events carousel
**Expected**
- Card tap → Event Details.
- View All → upcoming events list.

### I-02 Event registration (no questions)
**Steps**
1. Open active event → Register Now.

**Expected**
- Success alert; registration recorded.

### I-03 Event registration (with questions)
**Steps**
1. Open event with additional questions.
2. Submit without required answers.

**Expected**
- Validation error.
3. Complete answers → Register.

**Expected**
- Success; event appears under My Events when configured.

### I-04 Event feedback popup
**Steps**
1. Login when pending feedback API returns an event.

**Expected**
- Popup on dashboard; Give Feedback → feedback screen.
- No Thanks dismisses without crash.

---

## Suite J — Community

### J-01 Browse and join
**Steps**
1. Community tab → open community → join if needed.

**Expected**
- Feed loads; membership state updates.

### J-02 Create community (Student)
**Steps**
1. Create Community → submit valid form.

**Expected**
- **Request Sent / submitted for approval** message (not instant success like super admin).
- Community not immediately public until approved.

### J-03 Create post (member)
**Expected**
- Post publishes in community feed when permitted.

---

## Suite K — Chat and notifications

### K-01 Chat inbox
**Expected**
- Threads load; send message succeeds.

### K-02 Notifications
**Expected**
- Bell opens list; tap navigates when deep link configured.

---

## Suite L — Profile tab and account

### L-01 My Profile entry
**Expected**
- Profile tab → My Profile opens section hub.

### L-02 Settings / FAQs / About
**Expected**
- Each menu item opens correct screen.

### L-03 Logout
**Steps**
1. Logout → confirm.

**Expected**
- Returns to login; session cleared.

### L-04 Delete account (staging only)
**Expected**
- Confirmation flow works per environment policy.

---

## 5. Non-functional checks

- No crash when rapidly switching tabs during dashboard load.
- Loader shows/hides on dashboard refresh and section saves.
- Empty states on discovery lists are readable (no broken layout).
- University name in nav bar wraps correctly when logo missing.
- Keyboard dismisses on discovery list tap (where implemented).

---

## 6. Regression hotspots

Re-test when touching:

1. `DashboardViewModel.prepareConfig` student Quick Way exclusion
2. `DashboardViewController.didTapQuichAction` routing
3. `DashboardAlertView` alert types and tap handlers
4. `UserProfileSectionsViewController` + `ProfileSectionFlowCoordinator`
5. `TravelPlanSectionsViewController` connect gate + section editors
6. `SignatureVC` consent and travel upload path
7. `CreateCommunityViewController` student vs super-admin success messaging
8. `EventDetailsViewController` registration and feedback entry
9. Buddies list controllers + `UserFilterNavigation` for travel mate / students

---

## 7. QA sign-off checklist

- [ ] Suites A–L pass on target build
- [ ] No P0/P1 open for student flows
- [ ] Profile + travel E2E completion verified with real API data
- [ ] Quick action routing verified for all configured tiles
- [ ] Student community create shows approval path (not instant live)
- [ ] Smoke path passes:
  - Login → Alert → My Profile section save → Travel Plan → Upcoming Event register → Community browse → Chats

---

## 8. Related documents

- Full feature guide: `docs/Student-Features-and-Flows.md`
- Client demo guide: `docs/Student-Client-Demo-Guide.md`
