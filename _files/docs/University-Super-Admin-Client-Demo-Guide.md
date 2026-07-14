# Intoto - University Super Admin
## Client Demo Guide

**Design reference:** [Intoto Wireframe - Prototype (node 5051-661)](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&t=Fqpnfj5F0UbdlVZB-1)  
**Audience:** Client demos, stakeholders, pre-sales  
**Demo length:** 12-20 minutes  
**Version:** 1.0

---

## 1. Demo objective

Show how a University Super Admin can:

- monitor university operations from one dashboard
- manage invitation and user lifecycle
- assign and track student support operations
- govern community and moderation workflows
- use communication and notification channels

---

## 2. Pre-demo checklist

Before starting, confirm the environment has:

- one `university_super_admin` login
- at least one invited user and one accepted user
- at least one pending community request
- at least one unassigned student
- at least one report item
- at least one upcoming event

---

## 3. Quick narrative (talk track)

Use this short opening:

> "This role is the top operational admin for a single university.  
> Everything you see is scoped to that university and configured by role."

---

## 4. Step-by-step demo flow

## Step 1 - Login and role context (1 min)

**What to do**
1. Login with University Super Admin credentials.
2. Show role tag and university header.

**What to say**
- "This confirms we are in University Super Admin context."
- "No cross-university switching is needed here."

---

## Step 2 - Dashboard header actions (1-2 min)

**What to do**
1. Tap university logo/name.
2. Return and tap notification bell.
3. If visible, tap pending invitation envelope.

**What to say**
- "Header is fully actionable: details, notifications, invitations."

---

## Step 3 - Quick Way to student operations (2-3 min)

**What to do**
1. Tap **Total Students**.
2. Search for a student.
3. Open filter, apply one campus filter.
4. Tap a student row to open profile.

**What to say**
- "Counts are not static; each card opens the operational list behind the metric."

---

## Step 4 - Manage Users lifecycle (3 min)

**What to do**
1. Open **Manage User** from Quick Actions.
2. Switch to **Invited** status chip.
3. Open one user and trigger **Resend Invite**.
4. Optionally show an **Accepted** user and **Suspend Account**.

**What to say**
- "Invitation lifecycle and account control are handled in one place."

---

## Step 5 - Add User flow (2-3 min)

**What to do**
1. Open **Add User**.
2. Select a coordinator role and show required campus field.
3. Fill sample email + expiry.
4. Switch role to University Super Admin and show campus not required.

**What to say**
- "Form validation adapts by selected role, reducing user error."

---

## Step 6 - Community governance (2 min)

**What to do**
1. Open **Pending Communities** and approve one request.
2. Open Community tab and create a community.

**What to say**
- "This role can approve pending communities and create official communities instantly."

---

## Step 7 - Reports moderation (2 min)

**What to do**
1. Open **Total Reports**.
2. Open one report and update status.

**What to say**
- "Moderation workflow is native: assigned, review, escalate, resolve."

---

## Step 8 - Communication layer (1-2 min)

**What to do**
1. Open Chats tab and enter one thread.
2. Return Home and open notifications again.

**What to say**
- "Admins can coordinate operations directly through in-app messaging."

---

## 5. Key value statements (for business audience)

- **Role-scoped governance:** University-specific visibility and control.
- **Actionable dashboard:** Every metric can drive an operation.
- **Faster staffing workflows:** Unassigned to assigned student flow is structured.
- **Moderation built in:** Communities and reports can be managed centrally.
- **Operational clarity:** Search, filters, and status chips reduce handling time.

---

## 6. Common client questions

**Q: Can this role manage multiple universities?**  
A: No, it is scoped to one university.

**Q: Can they invite senior roles?**  
A: Yes, depending on invitable role policy.

**Q: Is community approval required for this role's own communities?**  
A: No, University Super Admin community creation is immediate.

**Q: Are dashboard cards fixed?**  
A: No, cards and actions are backend-configured by role.

---

## 7. Demo backup plan (if data is sparse)

If sample data is missing:

- show navigation paths even with low counts
- show role-based field changes in Add User
- show one seeded pending community and one seeded report
- use filter/search behavior as a functional demonstration

---

## 8. Related documents

- Full guide: `docs/University-Super-Admin-Features-and-Flows.md`
- QA test guide: `docs/University-Super-Admin-QA-Test-Guide.md`

