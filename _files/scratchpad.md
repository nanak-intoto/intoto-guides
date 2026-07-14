# Intoto iOS — System Design Deck

**Audience:** mixed eng + product/leadership · **Length:** ~10 min, 16 slides
**Aesthetic:** clean technical engineering doc · blue accent (#2A6FDB) · IBM Plex Sans/Mono + Space Grotesk

## Title style: short textbook noun-phrases (Topic-style), parallel.

1. Intoto iOS — System Design (cover)
2. System Overview
3. Design Goals & Constraints
4. Technology Stack
5. Architecture at a Glance (layered + MVVM diagram)
6. Feature Module Anatomy (View / ViewModel / Model / Service)
7. Multi-Tenant, Multi-Role Model
8. Backend-Driven Configuration
9. The Networking Layer
10. Offline-First Storage & Sync
11. Authentication & Document Security
12. Real-Time Chat
13. Data Flow: Profile Completion (sequence)
14. Localization & Theming
15. Observability
16. Cross-Cutting Concerns & Next Steps (close)

## Verified technical facts
- Swift + UIKit, MVVM, SPM. Patterns: Factory/Singleton/Builder, Observer.
- Storage: Realm (heavy, UserProfileRealmObject + migration manager) + UserDefaults (light).
- Networking: AsyncNetworkClient (async/await, Alamofire), Endpoint, ResponseParser; Auth0 token refresh; reachability gate.
- Auth: Auth0 (AuthManager.getCredentials), refresh-token handling.
- Realtime: Socket.IO chat (ChatList/ChatRoom/ChatGroup/UserList).
- Analytics: Firebase Analytics + Crashlytics + Mixpanel.
- Backend-driven: dashboard sections in API order; forms via formId (studentForm, travelForm) -> sections endpoint; quick actions via actionId routing.
- Offline-first: save form locally on Next, background sync; no block on no-network.
- Roles: Student, Ambassador, Community Coordinator, Event Coordinator, Third-Party Coordinator, University Super Admin.
- Scoping: one university + campus per role assignment; multi-role switch.
- Security extras: EncryptionService, PDFTamperingDetector.
- L10n: en, bn, fr, hi, pt-PT, ru, ur (7 languages). ThemeManager.
- Integrations: GooglePlaces, LocationManager, CallKit, Share, Signature, QR scanner.

## Type scale (1920x1080)
--type-title 64 / display 92 / subtitle 40 / body 30 / small 24 / mono-label 20(use 24 floor where standalone)
