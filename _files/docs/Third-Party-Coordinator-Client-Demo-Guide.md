# Intoto - Third Party Coordinator
## Client Demo Guide

**Design reference:** [Intoto Wireframe - Prototype (node 5051-661)](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&t=Fqpnfj5F0UbdlVZB-1)  
**Audience:** Client demos, stakeholders, pre-sales  
**Demo length:** 12-18 minutes  
**Version:** 1.0

---

## 1. Demo objective

Show how a **Third Party Coordinator** can:

- monitor student assignment health from the dashboard
- manage sub-coordinator invitations and account status
- assign unassigned students to sub-coordinators with profile visibility rules
- review arrival requests and coordinator workloads
- use search, filters, and in-app communication for daily operations

---

## 2. Pre-demo checklist

Before starting, confirm the environment has:

- one `thirdparty_coordinator` login
- at least one **Accepted** or **Student Assigned** sub-coordinator in Manage Users
- at least one **Invited** user (for resend demo)
- at least one **unassigned** student
- at least one **assigned** student (for contrast)
- at least one **arrival request** in the list
- optional: one upcoming event on the dashboard

---

## 3. Quick narrative (talk track)

Use this opening:

> "Third Party Coordinator is the operational lead for student support staffing.  
> They see live counts on the dashboard, drill into lists, assign students to sub-coordinators, and manage coordinator accounts — all within their university scope."

---

## 4. Step-by-step demo flow

## Step 1 - Login and role context (1 min)

**What to do**
1. Login with Third Party Coordinator credentials.
2. Point to the role tag (**Third Party Coordinator**).
3. Point to the university header (logo + name).

**What to say**
- "This role is focused on running student and sub-coordinator operations, not full university-wide governance."
- "Everything on this dashboard is configured for coordinators."

---

## Step 2 - Dashboard and Quick Way overview (2 min)

**What to do**
1. Scroll through **Quick Way** cards.
2. Call out typical cards: Assigned Students, Total Arrival Requests, Total Unassigned Requests, Total Sub Coordinator.
3. Pull to refresh once to show counts update.

**What to say**
- "Each number is actionable — tap any card to open the list behind it."
- "This is how coordinators see workload at a glance."

---

## Step 3 - Student operations (2-3 min)

**What to do**
1. Tap **Total Students** (or Assigned Students).
2. Search for a student (3+ characters).
3. Open **Filter**, apply one criterion (e.g. campus), tap **Apply**.
4. Tap one row → **Student Profile Hub**.

**What to say**
- "Coordinators can find any student quickly and open full profile context before taking action."

---

## Step 4 - Unassigned students and assignment (3-4 min)

**What to do**
1. Go back to Home → tap **Total Unassigned Requests** (or Total Unassigned Students).
2. Select one or more students.
3. Start **Assign** flow.
4. Complete setup: sub-coordinator, date range, work description.
5. Show **profile visibility** toggles (what the sub-coordinator can see).
6. Confirm assignment.

**What to say**
- "This is the core workflow: move students from unassigned to assigned with clear governance on what sub-coordinators can view."

---

## Step 5 - Manage Users and coordinator actions (3 min)

**What to do**
1. Open **Manage User** from Quick Actions.
2. Switch status chip to **Accepted** or **Student Assigned**.
3. Select one sub-coordinator row → enable selection mode if needed → **Take Action**.
4. Show **Student List** (opens assigned students for that coordinator).
5. Optionally repeat with **Assign Student** (opens unassigned list scoped to that coordinator).

**What to say**
- "From one screen they manage invitations and jump straight into assign or student-list actions per coordinator."

---

## Step 6 - Arrival requests (1-2 min)

**What to do**
1. Return to Home → tap **Total Arrival Requests**.
2. Search or scroll the list.
3. Tap one row → **Arrival Request Details**.

**What to say**
- "Arrival requests are for oversight and review here; assignment happens through the unassigned student flow."

---

## Step 7 - Add User and invite (2 min)

**What to do**
1. Open **Add User**.
2. Select role **Third Party Sub Coordinator** (or similar).
3. Show campus field required.
4. Enter email + expiry → submit.
5. Open **Manage User** → **Invited** to show the new invite.

**What to say**
- "They can grow their sub-coordinator team without leaving the app."

---

## Step 8 - Communication (1 min)

**What to do**
1. Open **Chats** tab → open one thread.
2. Return Home → tap notification bell if shown.

**What to say**
- "Day-to-day coordination stays in-platform."

---

## 5. Key value statements (for business audience)

- **Operational dashboard:** Metrics map directly to assign, review, and staff workflows.
- **Structured assignment:** Unassigned → setup → visibility → assigned, with audit-friendly steps.
- **Coordinator lifecycle in one place:** Invite, assign students, suspend, resend, email.
- **Sub-coordinator visibility:** Drill from coordinator list to their assigned students.
- **Role-appropriate scope:** Powerful operations without full super-admin complexity.

---

## 6. Common client questions

**Q: Is this the same as University Super Admin?**  
A: No. Third Party Coordinator focuses on student/sub-coordinator operations; super admin has broader governance (e.g. community approval at scale).

**Q: Can they assign from the arrival requests list?**  
A: Arrival list is browse-only; assignment uses **Unassigned Students** (or **Assign Student** from Manage Users).

**Q: What is "Student Assigned" on Manage Users?**  
A: A status filter for coordinators who already have students assigned — useful for ongoing management.

**Q: Are dashboard cards fixed?**  
A: No — backend configures which Quick Way cards appear for this role.

---

## 7. Demo backup plan (if data is sparse)

- Walk Quick Way taps even with zero counts (show empty states).
- Demo Manage Users status chips and action sheet on any seeded row.
- Demo Add User form validation (campus required for sub-coordinator role).
- Demo filter UI on Total Students with minimal results.
- Explain assignment steps verbally if no unassigned students exist in test data.

---

## 8. Related documents

- Full guide: `docs/Third-Party-Coordinator-Features-and-Flows.md`
- QA test guide: `docs/Third-Party-Coordinator-QA-Test-Guide.md`
