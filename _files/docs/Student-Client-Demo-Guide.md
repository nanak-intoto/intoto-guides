# Intoto — Student
## Client Demo Guide

**Design reference:** [Intoto Wireframe — Prototype (node 5051-661)](https://www.figma.com/proto/BSt8IrK987At3ZBXfyUbyY/Intoto-wireframe?node-id=5051-661&t=Fqpnfj5F0UbdlVZB-1)  
**Audience:** Client demos, stakeholders, pre-sales  
**Demo length:** 12–18 minutes  
**Version:** 1.0

---

## 1. Demo objective

Show how a **Student** can:

- onboard through profile and travel plan completion
- discover campus, events, and ambassadors from Home
- connect with classmates, roommates, and travel buddies
- participate in communities and in-app chat
- register for events and use support resources

---

## 2. Pre-demo checklist

Before starting, confirm the environment has:

- one `student` login (ideally with **incomplete profile or travel** so the dashboard alert shows)
- at least one **upcoming event** with open registration
- at least one **ambassador** on the dashboard carousel
- at least one **classmate/roommate/travel buddy** in discovery lists (or seeded peers)
- at least one **community** to browse
- optional: one **chat thread** and one **notification**
- quick actions enabled: My Campus, Travel Plan, Events (minimum); Classmates / Roommate / Travel Buddy if social demo is planned

---

## 3. Quick narrative (talk track)

Use this opening:

> "The Student experience is Intoto's core journey — from arrival preparation to campus life.  
> Students complete their profile and travel plan, discover peers and events, and stay connected through chat and communities — all scoped to their university."

---

## 4. Step-by-step demo flow

## Step 1 — Login and role context (1 min)

**What to do**
1. Login with Student credentials.
2. Point to university name/logo in the nav bar.
3. If shown, point to the **role switcher** row (Student).

**What to say**
- "Students land on a content-focused home — not admin stat cards."
- "Everything is scoped to their university and campus."

---

## Step 2 — Dashboard alert and completion nudge (1–2 min)

**What to do**
1. Scroll to the top alert (profile or travel incomplete).
2. Show progress ring on profile alert if present.
3. Tap the alert → **My Profile** or **Travel Plan** hub.
4. Navigate back to Home.

**What to say**
- "We guide students to finish onboarding — visibility and coordinator support depend on it."
- "One tap takes them exactly where they left off."

---

## Step 3 — My Profile guided flow (2–3 min)

**What to do**
1. Open **Profile tab → My Profile** (or use alert).
2. Tap one incomplete section (e.g. **Contact Info** or **Basic Details**).
3. Edit a field → tap **Save**.
4. Tap **Next** to show sequential section navigation.
5. Optionally show **Picture** change (view/change photo).

**What to say**
- "Sections and order come from the university config — not hardcoded."
- "Save, Next, and unsaved-change prompts keep the flow smooth."

---

## Step 4 — Travel Plan (2–3 min)

**What to do**
1. Return Home → tap **Travel Plan** quick action (or travel alert).
2. Open **Travel Details** — show arrival/transport fields.
3. Briefly show **Travel Documents** and **Signature** (consent + signature capture).
4. If travel plan is complete, tap **Connect with Other Travellers**.

**What to say**
- "Travel data powers arrival coordination on the admin side."
- "Social travel matching unlocks only after the plan is complete."

---

## Step 5 — Social discovery (2 min)

**What to do**
1. Home → **Find Roommate** or **Connect with Classmates** (whichever is configured).
2. Search (3+ characters) or open **Filter** → apply one criterion → **Apply**.
3. Tap a peer row → **Profile**.
4. Show **Chat** or contact action if available.

**What to say**
- "Students find roommates and classmates before they arrive."
- "Profiles respect visibility — peers see what the student chooses to share."

---

## Step 6 — Events (1–2 min)

**What to do**
1. Scroll to **Upcoming Events** on Home → tap one event.
2. On **Event Details**, tap **Register Now**.
3. Complete registration questions if shown.
4. Confirm success message.

**What to say**
- "Campus engagement is built into the same app as onboarding."
- "Registered events appear under My Events on the dashboard."

---

## Step 7 — Ambassadors (1 min)

**What to do**
1. Scroll to **Ambassadors** section on Home.
2. Tap one ambassador card → profile.
3. Optional: **View All** → ambassador list.

**What to say**
- "Human support — students can reach ambassadors directly from day one."

---

## Step 8 — Community (1–2 min)

**What to do**
1. Open **Community** tab.
2. Browse a community feed or open **Create Community**.
3. If creating: fill name/description → submit → show **approval pending** message.

**What to say**
- "Students build community, but creation goes through moderation for safety."
- "Unlike admin roles, student communities are not instant-live."

---

## Step 9 — Communication and campus (1 min)

**What to do**
1. Open **Chats** tab → one thread.
2. Return Home → tap **My Campus** quick action.
3. Tap notification **bell** if time allows.

**What to say**
- "Messaging, campus info, and notifications stay in one platform."

---

## 5. Key value statements (for business audience)

- **Guided onboarding:** Profile and travel completion with progress feedback on Home.
- **Pre-arrival social graph:** Classmates, roommates, and travel buddies before campus.
- **Campus engagement:** Events, communities, and ambassadors in one student home.
- **Safe community creation:** Student-created groups go through approval.
- **Configurable experience:** Dashboard shortcuts and sections are backend-driven per university.

---

## 6. Common client questions

**Q: Do students see admin dashboard counts (Total Students, etc.)?**  
A: No. Students use a content dashboard — alerts, banners, quick actions, events, ambassadors — not Quick Way stat cards.

**Q: Can students assign coordinators or manage users?**  
A: No. Those are admin/coordinator capabilities.

**Q: Is travel buddy available before travel plan is done?**  
A: From the travel hub, **Connect with Other Travellers** requires a complete travel plan. The dashboard **Travel Buddy** quick action may still open the list depending on config.

**Q: Are student-created communities live immediately?**  
A: No. They are submitted for approval (typically within 24 hours).

**Q: Are quick action tiles fixed?**  
A: No — backend configures which features appear (Campus, Travel, Events, Support, AI, social tiles, etc.).

---

## 7. Demo backup plan (if data is sparse)

- Walk profile/travel section list even if mostly complete (show status cells).
- Demo filter UI on Classmates/Roommate with zero or few results.
- Demo event details screen even if registration is closed (read-only).
- Show community browse with empty create flow validation.
- Explain travel signature/consent verbally if test account cannot submit.
- Use **Support** and **My Campus** quick actions — usually always available.

---

## 8. Related documents

- Full guide: `docs/Student-Features-and-Flows.md`
- QA test guide: `docs/Student-QA-Test-Guide.md`
