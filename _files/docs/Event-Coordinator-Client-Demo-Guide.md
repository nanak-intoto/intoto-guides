# Intoto — Event Coordinator
## Client Demo Guide

**Design reference:** [Intoto Wireframe — Event Coordinator (node 5086-25745)](https://www.figma.com/design/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&page-id=5051%3A661)  
**Prototype:** [Event Coordinator prototype — start 5086-25745](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&p=f&t=ttUcU9kASuy321kT-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5086%3A25745)  
**Audience:** Client demos, stakeholders, pre-sales  
**Demo length:** 12–18 minutes  
**Version:** 1.0

---

## 1. Demo objective

Show how an **Event Coordinator** runs the campus **events program** from one mobile dashboard:

- operational visibility (**Total Events**, **Events Analytics**, category chart)
- **approval workflow** for pending events
- **create → publish → complete** lifecycle
- student-visible outcomes (optional second device)

---

## 2. Pre-demo checklist

| Item | Why |
|------|-----|
| Event Coordinator login | Primary role |
| ≥ 1 upcoming event on Home | Carousel proof |
| ≥ 1 pending event (or ability to create one) | Approve/reject demo |
| ≥ 1 completed event (optional) | Closed-loop story |
| Total Events count > 0 | Quick Way credibility |
| Student test account (optional) | Registration visibility |
| Figma prototype link ready | Stakeholder alignment |

---

## 3. Talk track (30 seconds)

> "Event Coordinators are the university’s events command center — not the whole admin suite.  
> They see upcoming, pending, and completed work on one Home screen, approve what’s ready for students, and use analytics to balance programming across categories."

---

## 4. Step-by-step demo flow

### Step 1 — Login and context (1 min)

**Do**
1. Log in as **Event Coordinator**.
2. Point to university **logo + name** (tap → university details optional).
3. Note role label / switcher if multi-role.

**Say**
- "Scoped to one university’s events — dashboard sections come from the server for this role only."

---

### Step 2 — Home tour (3 min)

**Do**
1. Scroll Home top to bottom.
2. **Quick Way:** **Total Events**, **Events Analytics**.
3. **Quick Actions:** **Events**, **Support**.
4. Swipe **Upcoming**, **Pending**, **Completed** carousels.
5. Point to **Events by Category** chart.

**Say**
- "Pending is the quality inbox before students see anything."
- "The chart answers where programming effort is going — not just a list of flyers."

**Optional:** Pull to refresh.

---

### Step 3 — Approve pending event (3 min)

**Do**
1. Tap **Pending Events** card or **View All**.
2. Walk title, dates, registration window, image, location.
3. **Approve** (or **Reject** + reason if you need governance story).

**Say**
- "Wrong venue or dates never reach the student app."

**Fallback:** Create event that enters pending in Step 4, then return here.

---

### Step 4 — Create or edit event (2–3 min)

**Do**
1. **Events** quick action → list → **Create**.
2. Show key fields: title, date, registration window, location, category, image.
3. Save → show in correct carousel/list.

**Say**
- "Same information architecture students see on the public event page."

---

### Step 5 — Events Analytics (2 min)

**Do**
1. Tap **Events Analytics** Quick Way.
2. Show KPIs + at least one chart.
3. Apply a filter if the frame supports it.

**Say**
- "Basic reporting without exporting to a separate BI tool for category mix."

---

### Step 6 — Student proof (optional, 2 min)

**Do**
1. Second device: **Student** login.
2. **Upcoming Events** or **Events** → show approved event + **Register**.

**Say**
- "Coordinator approval directly controls student discovery."

---

### Step 7 — Chats & close (1 min)

**Do**
1. Mention **Chats** for "where is the event?" questions.
2. **Support** quick action for escalations.

---

## 5. Short demo (5 min)

| # | Show |
|---|------|
| 1 | Home + Pending approve |
| 2 | Upcoming carousel |
| 3 | Total Events → list |
| 4 | Events Analytics chart |

---

## 6. Client FAQ

| Question | Answer |
|----------|--------|
| Multiple coordinators? | Tenant policy; wireframe supports approve/reject per event. |
| Students see pending? | No — published/upcoming only. |
| Customize dashboard? | Yes — overview API per role. |
| vs University Super Admin? | EC is events-focused; USA has full user/community governance. |

---

## 7. Do not demo on Event Coordinator role

- Manage Users / Add User / Assign Students (USA / Third Party Coordinator)
- Full USA Quick Way grid (all campuses, invites, reports queue)
- Ambassador profile or student travel onboarding

Use **role switcher** only if the account is multi-role — call out the switch explicitly.

---

*Prototype: [5086-25745](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5086-25745&p=f&t=ttUcU9kASuy321kT-1&scaling=min-zoom&content-scaling=fixed&page-id=5051%3A661&starting-point-node-id=5086%3A25745)*
