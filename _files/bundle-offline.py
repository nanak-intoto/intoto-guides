#!/usr/bin/env python3
"""Regenerate Intoto All-in-One embedded guides and Portable offline bundle."""

from __future__ import annotations

import base64
import json
import re
import uuid
from pathlib import Path
from urllib.request import urlopen

BASE = Path(__file__).resolve().parent
DOC_ROOT = BASE.parent
ALL_IN_ONE = DOC_ROOT / "Intoto All-in-One Guides.html"
HUB = BASE / "Intoto Feature & Flow Guides.html"
PORTABLE = BASE / "Intoto Portable Guides (offline).html"
GUIDE_CSS = BASE / "guide.css"
CSS_LINK = "_files/guide.css"

FONT_CSS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Space+Grotesk:wght@400;500;600;700&"
    "family=IBM+Plex+Sans:wght@400;500;600;700&"
    "family=IBM+Plex+Mono:wght@400;500;600&display=swap"
)

LOADER_HEAD = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Intoto · Feature &amp; Flow Guides — All in One (Offline)</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #0E1623; display: flex; align-items: center; justify-content: center; min-height: 100vh; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    #__bundler_loading { position: fixed; bottom: 20px; right: 20px; font: 13px/1.4 -apple-system, BlinkMacSystemFont, sans-serif; color: #666; background: #fff; padding: 8px 14px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.12); z-index: 10000; }
    #__bundler_thumbnail { position: fixed; inset: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; background: #0E1623; z-index: 9999; }
    #__bundler_thumbnail svg { width: 100%; height: 100%; object-fit: contain; }
  </style>
  <noscript>
    <style>#__bundler_loading { display: none; }</style>
    <div style="position:fixed;bottom:12px;left:12px;font:13px/1.4 -apple-system,BlinkMacSystemFont,sans-serif;color:#999;background:rgba(255,255,255,0.9);padding:6px 12px;border-radius:6px;box-shadow:0 1px 4px rgba(0,0,0,0.08);z-index:10000;">
      This page requires JavaScript to display.
    </div>
  </noscript>
</head>
<body>
  <div id="__bundler_thumbnail">
  <svg viewBox="0 0 1200 800" xmlns="http://www.w3.org/2000/svg">
    <rect width="1200" height="800" fill="#0E1623"/>
    <rect x="360" y="250" width="150" height="130" rx="14" fill="none" stroke="#5C95E8" stroke-width="6"/>
    <rect x="525" y="250" width="150" height="130" rx="14" fill="none" stroke="#46B07C" stroke-width="6"/>
    <rect x="690" y="250" width="150" height="130" rx="14" fill="none" stroke="#8E76E6" stroke-width="6"/>
    <rect x="360" y="420" width="150" height="130" rx="14" fill="none" stroke="#46B07C" stroke-width="6"/>
    <rect x="525" y="420" width="150" height="130" rx="14" fill="none" stroke="#8E76E6" stroke-width="6"/>
    <rect x="690" y="420" width="150" height="130" rx="14" fill="none" stroke="#5C95E8" stroke-width="6"/>
    <circle cx="600" cy="170" r="22" fill="#6FA4EE"/>
  </svg>
</div>
  <div id="__bundler_loading">Unpacking...</div>
"""

LOADER_SCRIPT = r"""
document.addEventListener('DOMContentLoaded', async function() {
  const loading = document.getElementById('__bundler_loading');
  function setStatus(msg) { if (loading) loading.textContent = msg; }

  window.addEventListener('error', function(e) {
    var p = document.body || document.documentElement;
    var d = document.getElementById('__bundler_err') || p.appendChild(document.createElement('div'));
    d.id = '__bundler_err';
    d.style.cssText = 'position:fixed;bottom:12px;left:12px;right:12px;font:12px/1.4 ui-monospace,monospace;background:#2a1215;color:#ff8a80;padding:10px 14px;border-radius:8px;border:1px solid #5c2b2e;z-index:99999;white-space:pre-wrap;max-height:40vh;overflow:auto';
    d.textContent = (d.textContent ? d.textContent + String.fromCharCode(10) : '') +
      '[bundle] ' + (e.message || e.type) +
      (e.filename ? ' (' + e.filename.slice(0, 60) + ':' + e.lineno + ')' : '');
  }, true);

  try {
    const manifestEl = document.querySelector('script[type="__bundler/manifest"]');
    const templateEl = document.querySelector('script[type="__bundler/template"]');
    if (!manifestEl || !templateEl) {
      setStatus('Error: missing bundle data');
      return;
    }

    const manifest = JSON.parse(manifestEl.textContent);
    let template = JSON.parse(templateEl.textContent);
    const uuids = Object.keys(manifest);
    setStatus('Unpacking ' + uuids.length + ' assets...');

    const blobUrls = {};
    await Promise.all(uuids.map(async (uid) => {
      const entry = manifest[uid];
      const binaryStr = atob(entry.data);
      const bytes = new Uint8Array(binaryStr.length);
      for (let i = 0; i < binaryStr.length; i++) bytes[i] = binaryStr.charCodeAt(i);
      let finalBytes = bytes;
      if (entry.compressed && typeof DecompressionStream !== 'undefined') {
        const ds = new DecompressionStream('gzip');
        const writer = ds.writable.getWriter();
        const reader = ds.readable.getReader();
        writer.write(bytes);
        writer.close();
        const chunks = [];
        let totalLen = 0;
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          chunks.push(value);
          totalLen += value.length;
        }
        finalBytes = new Uint8Array(totalLen);
        let offset = 0;
        for (const chunk of chunks) { finalBytes.set(chunk, offset); offset += chunk.length; }
      }
      blobUrls[uid] = URL.createObjectURL(new Blob([finalBytes], { type: entry.mime }));
    }));

    setStatus('Rendering...');
    for (const uid of uuids) template = template.split(uid).join(blobUrls[uid]);
    template = template.replace(/\s+integrity="[^"]*"/gi, '').replace(/\s+crossorigin="[^"]*"/gi, '');

    const doc = new DOMParser().parseFromString(template, 'text/html');
    document.documentElement.replaceWith(doc.documentElement);
    const dead = Array.from(document.scripts);
    for (const old of dead) {
      const s = document.createElement('script');
      for (const a of old.attributes) s.setAttribute(a.name, a.value);
      s.textContent = old.textContent;
      const p = s.src ? new Promise(function(r) { s.onload = s.onerror = r; }) : null;
      old.replaceWith(s);
      if (p) await p;
    }
    if (loading) loading.remove();
    const thumb = document.getElementById('__bundler_thumbnail');
    if (thumb) thumb.remove();
  } catch (err) {
    setStatus('Error unpacking: ' + err.message);
    console.error('Bundle unpack error:', err);
  }
});
"""


def extract_guide_body(html: str) -> str:
    start = html.index('<header class="hero">')
    end = html.index('<template id="__bundler_thumbnail"')
    return html[start:end].strip()


def prefix_embed(body: str, prefix: str) -> str:
    body = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{prefix}{m.group(1)}"', body)
    body = re.sub(
        r'href="#([^"]+)"',
        lambda m: f'href="#{prefix}{m.group(1)}"' if not m.group(1).startswith(prefix) else m.group(0),
        body,
    )
    return body


def _guide_view_bounds(html: str, view: str) -> tuple[int, int, int]:
    """Return (content_start, close_tag_start, next_section_start) for a guide-view."""
    open_tag = f'<section class="guide-view" data-view="{view}" hidden>'
    start = html.index(open_tag)
    back_bar = html.index(
        '<div class="back-bar"><button data-back>← All role guides</button></div>',
        start,
    )
    content_start = html.index('</div>', back_bar) + len('</div>')
    while content_start < len(html) and html[content_start] in '\n\r':
        content_start += 1

    next_marker = '\n<section class="guide-view" data-view='
    next_pos = html.find(next_marker, start + len(open_tag))
    if next_pos == -1:
        next_pos = html.find('\n<script>', start)
    if next_pos == -1:
        raise SystemExit(f"No boundary after guide-view={view}")

    close_pos = html.rfind('</section>', start, next_pos)
    if close_pos == -1:
        raise SystemExit(f"No closing </section> for guide-view={view}")
    return content_start, close_pos, next_pos


def remove_orphaned_fragments(html: str) -> str:
    """Remove guide body HTML accidentally left outside guide-view wrappers."""
    # Only top-level </section> (guide-view close) — not indented inner </section>.
    orphan_re = re.compile(
        r'^</section>\n\n\s*<(?:section class="sec"|header class="hero")',
        re.MULTILINE,
    )
    while True:
        m = orphan_re.search(html)
        if not m:
            break
        orphan_start = html.index('\n\n', m.start()) + 2
        next_gv = html.find('\n<section class="guide-view"', orphan_start)
        if next_gv == -1:
            raise SystemExit("Orphaned guide fragment with no following guide-view")
        html = html[:orphan_start] + html[next_gv + 1 :]
    return html


def replace_section(html: str, view: str, new_inner: str) -> str:
    content_start, close_pos, _ = _guide_view_bounds(html, view)
    return html[:content_start] + new_inner + '\n' + html[close_pos:]


def remove_guide_view(html: str, view: str) -> str:
    """Remove an entire embedded guide-view section."""
    open_tag = f'<section class="guide-view" data-view="{view}" hidden>'
    if open_tag not in html:
        return html
    start = html.index(open_tag)
    _, close_pos, _ = _guide_view_bounds(html, view)
    close_end = close_pos + len('</section>')
    return html[:start] + html[close_end:].lstrip('\n')


def sync_hub_patches(allinone: str, hub: str) -> str:
    """Copy hub card + FAQ deltas from standalone hub into All-in-One hub section."""
    patches = [
        (
            '<p>An off-campus partner mentor who represents the university and supports prospective and incoming students by chat.</p>',
            '<p>An off-campus partner mentor on the web portal — student leads, profile, and chat — linked to The Ambassador Platform where prospects discover them.</p>',
        ),
        (
            '<div class="ans">Entirely through the Ambassadors carousel on their Home dashboard. A student taps an ambassador\'s card, opens the public profile, and taps Chat — the conversation lands in that ambassador\'s Chats inbox.</div></details>',
            '<div class="ans">Two paths: enrolled students use the <b>Ambassadors</b> carousel on the mobile Home dashboard; prospective students use <b>The Ambassador Platform</b> web directory — search, filter, open a card, tap <b>Chat</b>. External ambassadors are especially visible on the platform under the <b>Staff</b> filter.</div></details>',
        ),
        (
            '<div class="ans">Both use the same flows and profile form. An Ambassador is usually a current student or alumnus (often also holding the Student role); an External Ambassador is an off-campus partner — a recruitment partner, agency contact, or alumnus abroad — invited with the ambassador type set to External.</div></details>',
            '<div class="ans">An <b>Ambassador</b> is usually a current student or alumnus on the mobile app (often also holding the Student role). An <b>External Ambassador</b> is an off-campus partner — recruitment agency, regional rep, or alumnus abroad — who works from the <b>web portal</b>, appears on The Ambassador Platform with a Staff badge, and manages student leads plus chat from the browser.</div></details>',
        ),
    ]
    for old, new in patches:
        if old in allinone:
            allinone = allinone.replace(old, new)
        elif old in hub:
            pass  # hub already updated; all-in-one may already be patched
    return allinone


def ensure_extamb_scoped_css(html: str) -> str:
    block = """
  /* External Ambassador (web portal) — ambassador gold */
  .guide-view[data-view="extamb"] .eyebrow{ color:#FCD34D; }
  .guide-view[data-view="extamb"] .eyebrow .sq{ background:#FCD34D; }
  .guide-view[data-view="extamb"] a,
  .guide-view[data-view="extamb"] .kicker,
  .guide-view[data-view="extamb"] .stat .n,
  .guide-view[data-view="extamb"] .feat-num,
  .guide-view[data-view="extamb"] .faq details[open] summary{ color:#A16207; }
  .guide-view[data-view="extamb"] nav.toc a:hover{ border-color:#A16207; color:var(--ink); }
  .guide-view[data-view="extamb"] .kicker .sq{ background:#A16207; }
  .guide-view[data-view="extamb"] .flow-node{ background:#FEF3C7; border-color:#A16207; color:#A16207; }
  .guide-view[data-view="extamb"] .ia-card .tag{ color:#A16207; }
  .guide-view[data-view="extamb"] .faq summary .pls::before,
  .guide-view[data-view="extamb"] .faq summary .pls::after{ background:#A16207; }
  .guide-view[data-view="extamb"] .badge.b-web{ color:#FDE68A; border-color:#78350F; }
  .guide-view[data-view="extamb"] .badge.b-web .dot{ background:#A16207; }
  .guide-view[data-view="extamb"] .badge.b-link{ color:#9CE5F0; border-color:#1F5560; }
  .guide-view[data-view="extamb"] .badge.b-link .dot{ background:#02A3CA; }
"""
    marker = '  .guide-view[data-view="usa"] .badge.b-mobile .dot{ background:var(--qa); }\n'
    if 'data-view="extamb"] .eyebrow' not in html:
        if marker not in html:
            raise SystemExit("CSS insert marker not found")
        html = html.replace(marker, marker + block)
    return html


def ensure_usa_scoped_css(html: str) -> str:
    """University Super Admin — staff green + web portal badge (merged guide)."""
    if 'data-view="usa"] .badge.b-mobile' in html:
        return html
    block = """
  /* University Super Admin — staff green + web portal */
  .guide-view[data-view="usa"] .eyebrow{ color:#86D2AC; }
  .guide-view[data-view="usa"] .eyebrow .sq{ background:#86D2AC; }
  .guide-view[data-view="usa"] a,
  .guide-view[data-view="usa"] .kicker,
  .guide-view[data-view="usa"] .stat .n,
  .guide-view[data-view="usa"] .feat-num,
  .guide-view[data-view="usa"] .faq details[open] summary{ color:var(--qa); }
  .guide-view[data-view="usa"] nav.toc a:hover{ border-color:var(--qa); color:var(--ink); }
  .guide-view[data-view="usa"] .kicker .sq{ background:var(--qa); }
  .guide-view[data-view="usa"] .flow-node{ background:var(--qa-wash); border-color:var(--qa); color:var(--qa); }
  .guide-view[data-view="usa"] .ia-card .tag{ color:var(--qa); }
  .guide-view[data-view="usa"] .faq summary .pls::before,
  .guide-view[data-view="usa"] .faq summary .pls::after{ background:var(--qa); }
  .guide-view[data-view="usa"] .badge.b-web{ color:#9CE5F0; border-color:#1F5560; }
  .guide-view[data-view="usa"] .badge.b-web .dot{ background:#0E7C86; }
  .guide-view[data-view="usa"] .badge.b-mobile{ color:#86D2AC; border-color:#27543F; }
  .guide-view[data-view="usa"] .badge.b-mobile .dot{ background:var(--qa); }
"""
    # Insert after staff role-card styles or before extamb block
    marker = '  .guide-view[data-view="extamb"] .eyebrow{ color:#FCD34D; }\n'
    if marker in html:
        html = html.replace(marker, block + marker)
    else:
        html = html.replace('</style>', block + '</style>', 1)
    # Drop legacy univadmin scoped CSS if present
    html = re.sub(
        r'\n  /\* University Admin \(web portal\).*?'
        r'\.guide-view\[data-view="univadmin"\][^\n]*\n',
        '\n',
        html,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'  \.guide-view\[data-view="univadmin"\][^\n]+\n',
        '',
        html,
    )
    return html


def extract_hub_body(html: str) -> str:
    start = html.index('<header class="hero">')
    end = html.index('</main>', start) + len('</main>')
    return html[start:end]


def replace_hub_section(html: str, new_inner: str) -> str:
    view = "hub"
    open_tag = f'<section class="guide-view" data-view="{view}">'
    start = html.index(open_tag)
    content_start = start + len(open_tag)
    while content_start < len(html) and html[content_start] in '\n\r':
        content_start += 1
    next_pos = html.find('\n<section class="guide-view"', start + 1)
    close_pos = html.rfind('</section>', start, next_pos)
    return html[:content_start] + new_inner + '\n' + html[close_pos:]


def patch_hub_for_all_in_one(html: str) -> str:
    """Hub cards and CTAs use in-page navigation in All-in-One (not separate files)."""
    replacements = [
        (
            '<a class="role-card" data-group="platform" href="Intoto%20Paid%20Features%20Guide.html">',
            '<a class="role-card" data-group="platform" href="javascript:void(0)" data-guide="features">',
        ),
        (
            '<a class="cta" href="Intoto%20Paid%20Features%20Guide.html">Open catalog →</a>',
            '<a class="cta" href="javascript:void(0)" data-guide="features">Open catalog →</a>',
        ),
        (
            '<a class="fact module-link" href="Intoto%20Paid%20Features%20Guide.html#feat-ambassador">',
            '<a class="fact module-link" href="javascript:void(0)" data-guide="features" data-anchor="pf-feat-ambassador">',
        ),
        (
            '<a class="fact module-link" href="Intoto%20Paid%20Features%20Guide.html#feat-travel">',
            '<a class="fact module-link" href="javascript:void(0)" data-guide="features" data-anchor="pf-feat-travel">',
        ),
        (
            '<a class="fact module-link" href="Intoto%20Paid%20Features%20Guide.html#feat-community">',
            '<a class="fact module-link" href="javascript:void(0)" data-guide="features" data-anchor="pf-feat-community">',
        ),
        (
            '<a class="fact module-link" href="Intoto%20Paid%20Features%20Guide.html#feat-chat">',
            '<a class="fact module-link" href="javascript:void(0)" data-guide="features" data-anchor="pf-feat-chat">',
        ),
        (
            '<a class="fact module-link" href="Intoto%20Paid%20Features%20Guide.html#feat-events">',
            '<a class="fact module-link" href="javascript:void(0)" data-guide="features" data-anchor="pf-feat-events">',
        ),
        (
            '<a class="fact module-link" href="Intoto%20Paid%20Features%20Guide.html#feat-usermgmt">',
            '<a class="fact module-link" href="javascript:void(0)" data-guide="features" data-anchor="pf-feat-usermgmt">',
        ),
        (
            '<a class="fact module-link" href="Intoto%20Paid%20Features%20Guide.html#feat-mobility">',
            '<a class="fact module-link" href="javascript:void(0)" data-guide="features" data-anchor="pf-feat-mobility">',
        ),
        (
            '<a class="role-card" data-group="platform" href="Intoto%20Intoto%20Admin%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="platform" href="javascript:void(0)" data-guide="admin">',
        ),
        (
            '<a class="role-card" data-group="students" href="Intoto%20Student%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="students" href="javascript:void(0)" data-guide="student">',
        ),
        (
            '<a class="role-card" data-group="ambassador" href="Intoto%20Ambassador%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="ambassador" href="javascript:void(0)" data-guide="ambassador">',
        ),
        (
            '<a class="role-card" data-group="ambassador" href="Intoto%20External%20Ambassador%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="ambassador" href="javascript:void(0)" data-guide="extamb">',
        ),
        (
            '<a class="role-card" data-group="staff" href="Intoto%20Community%20Coordinator%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="staff" href="javascript:void(0)" data-guide="community">',
        ),
        (
            '<a class="role-card" data-group="staff" href="Intoto%20Event%20Coordinator%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="staff" href="javascript:void(0)" data-guide="event">',
        ),
        (
            '<a class="role-card" data-group="staff" href="Intoto%20Mobility%20Program%20Admin%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="staff" href="javascript:void(0)" data-guide="mobility">',
        ),
        (
            '<a class="role-card" data-group="staff" href="Intoto%20University%20Super%20Admin%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="staff" href="javascript:void(0)" data-guide="usa">',
        ),
        (
            '<a class="role-card" data-group="partner" href="Intoto%20Third%20Party%20Coordinator%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="partner" href="javascript:void(0)" data-guide="tpc">',
        ),
        (
            '<a class="role-card" data-group="partner" href="Intoto%20Third%20Party%20Sub%20Coordinator%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="partner" href="javascript:void(0)" data-guide="tpsc">',
        ),
        (
            '<a class="role-card" data-group="webapp" href="Intoto%20Ambassador%20Platform%20Feature%20%26%20Flow%20Guide.html">',
            '<a class="role-card" data-group="webapp" href="javascript:void(0)" data-guide="ambplat">',
        ),
    ]
    for old, new in replacements:
        html = html.replace(old, new)
    return html


def patch_inline_guide_links(html: str) -> str:
    """Convert standalone file hrefs to in-page data-guide navigation (nav only)."""
    html = re.sub(
        r'href="Intoto%20Paid%20Features%20Guide\.html#([^"]+)"',
        lambda m: f'href="javascript:void(0)" data-guide="features" data-anchor="pf-{m.group(1)}"',
        html,
    )
    html = html.replace(
        'href="Intoto%20Paid%20Features%20Guide.html"',
        'href="javascript:void(0)" data-guide="features"',
    )
    return html


def ensure_anchor_navigation(html: str) -> str:
    """Allow All-in-One tabs, data-guide links, and anchored guide jumps."""
    if "function applyRoleFilter(filter)" in html:
        return html

    legacy_script = """<script>
(function(){
  function showView(name){
    document.querySelectorAll(".guide-view").forEach(function(v){ v.hidden = (v.getAttribute("data-view") !== name); });
    window.scrollTo(0,0);
    try{ history.replaceState(null,"", name==="hub" ? location.pathname : "#g="+name); }catch(e){}
  }
  document.addEventListener("click", function(e){
    var g = e.target.closest("[data-guide]");
    if(g){ e.preventDefault(); showView(g.getAttribute("data-guide")); return; }
    var b = e.target.closest("[data-back]");
    if(b){ e.preventDefault(); showView("hub"); return; }
  });
  var m = (location.hash||"").match(/g=([a-z]+)/);
  if(m){ showView(m[1]); }
})();
</script>"""

    anchored_script = """<script>
(function(){
  function findAnchor(anchor){
    if(!anchor){ return null; }
    var clean = anchor.charAt(0)==="#" ? anchor.slice(1) : anchor;
    return document.getElementById(clean);
  }
  function showView(name, anchor){
    document.querySelectorAll(".guide-view").forEach(function(v){ v.hidden = (v.getAttribute("data-view") !== name); });
    var target = findAnchor(anchor);
    if(target){ setTimeout(function(){ target.scrollIntoView({block:"start"}); }, 0); }
    else{ window.scrollTo(0,0); }
    try{
      var hash = name==="hub" ? "" : "#g="+name+(anchor ? "&a="+encodeURIComponent(anchor.replace(/^#/,"")) : "");
      history.replaceState(null,"", name==="hub" ? location.pathname : hash);
    }catch(e){}
  }
  document.addEventListener("click", function(e){
    var g = e.target.closest("[data-guide]");
    if(g){ e.preventDefault(); showView(g.getAttribute("data-guide"), g.getAttribute("data-anchor")); return; }
    var b = e.target.closest("[data-back]");
    if(b){ e.preventDefault(); showView("hub"); return; }
  });
  var m = (location.hash||"").match(/g=([a-z]+)(?:&a=([^&]+))?/);
  if(m){ showView(m[1], m[2] ? decodeURIComponent(m[2]) : null); }
})();
</script>"""

    new_script = """<script>
(function(){
  function findAnchor(anchor){
    if(!anchor){ return null; }
    var clean = anchor.charAt(0)==="#" ? anchor.slice(1) : anchor;
    return document.getElementById(clean);
  }
  function applyRoleFilter(filter){
    var hub = document.querySelector('.guide-view[data-view="hub"]') || document;
    var tabs = hub.querySelectorAll('.tabs .tab');
    var cards = hub.querySelectorAll('.roles .role-card');
    tabs.forEach(function(tab){
      tab.classList.toggle('active', tab.getAttribute('data-filter') === filter);
    });
    cards.forEach(function(card){
      var show = filter === "all" || card.getAttribute('data-group') === filter;
      card.classList.toggle('hide', !show);
    });
  }
  function showView(name, anchor){
    document.querySelectorAll(".guide-view").forEach(function(v){ v.hidden = (v.getAttribute("data-view") !== name); });
    var target = findAnchor(anchor);
    if(target){ setTimeout(function(){ target.scrollIntoView({block:"start"}); }, 0); }
    else{ window.scrollTo(0,0); }
    try{
      var hash = name==="hub" ? "" : "#g="+name+(anchor ? "&a="+encodeURIComponent(anchor.replace(/^#/,"")) : "");
      history.replaceState(null,"", name==="hub" ? location.pathname : hash);
    }catch(e){}
  }
  document.addEventListener("click", function(e){
    var tab = e.target.closest(".tabs .tab");
    if(tab){ e.preventDefault(); applyRoleFilter(tab.getAttribute("data-filter") || "all"); return; }
    var g = e.target.closest("[data-guide]");
    if(g){ e.preventDefault(); showView(g.getAttribute("data-guide"), g.getAttribute("data-anchor")); return; }
    var b = e.target.closest("[data-back]");
    if(b){ e.preventDefault(); showView("hub"); return; }
  });
  var m = (location.hash||"").match(/g=([a-z]+)(?:&a=([^&]+))?/);
  if(m){ showView(m[1], m[2] ? decodeURIComponent(m[2]) : null); }
})();
</script>"""
    if legacy_script in html:
        return html.replace(legacy_script, new_script, 1)
    if anchored_script in html:
        return html.replace(anchored_script, new_script, 1)
    if '<script>\n(function(){\n  function findAnchor(anchor){' in html:
        html = re.sub(
            r'<script>\n\(function\(\)\{\n  function findAnchor\(anchor\)\{.*?\n\}\)\(\);\n</script>',
            new_script,
            html,
            count=1,
            flags=re.DOTALL,
        )
        if "function applyRoleFilter(filter)" in html:
            return html
        raise SystemExit("All-in-One navigation script not found")
    raise SystemExit("All-in-One navigation script not found")


def ensure_features_section(html: str, features_body: str) -> str:
    if 'data-view="features"' in html:
        return replace_section(html, "features", features_body)
    block = (
        '\n<section class="guide-view" data-view="features" hidden>\n'
        '<div class="back-bar"><button data-back>← All role guides</button></div>\n'
        f'{features_body}\n</section>\n'
    )
    marker = '\n<section class="guide-view" data-view="admin" hidden>'
    if marker not in html:
        raise SystemExit("admin guide-view marker not found for features insert")
    return html.replace(marker, block + marker, 1)


def ensure_mobility_section(html: str, mobility_body: str) -> str:
    if 'data-view="mobility"' in html:
        return replace_section(html, "mobility", mobility_body)
    block = (
        '\n<section class="guide-view" data-view="mobility" hidden>\n'
        '<div class="back-bar"><button data-back>← All role guides</button></div>\n'
        f'{mobility_body}\n</section>\n'
    )
    marker = '\n<section class="guide-view" data-view="community" hidden>'
    if marker not in html:
        raise SystemExit("community guide-view marker not found for mobility insert")
    return html.replace(marker, block + marker, 1)


def ensure_pf_scoped_css(html: str) -> str:
    block = """
  /* Paid Features catalog — product purple */
  .guide-view[data-view="features"] .eyebrow{ color:#BCA9F0; }
  .guide-view[data-view="features"] .eyebrow .sq{ background:#BCA9F0; }
  .guide-view[data-view="features"] a,
  .guide-view[data-view="features"] .kicker,
  .guide-view[data-view="features"] .stat .n,
  .guide-view[data-view="features"] .feat-num,
  .guide-view[data-view="features"] .faq details[open] summary{ color:var(--mktg); }
  .guide-view[data-view="features"] nav.toc a:hover{ border-color:var(--mktg); color:var(--ink); }
  .guide-view[data-view="features"] .kicker .sq{ background:var(--mktg); }
  .guide-view[data-view="features"] .flow-node{ background:var(--mktg-wash); border-color:var(--mktg); color:var(--mktg); }
  .guide-view[data-view="features"] .ia-card .tag{ color:var(--mktg); }
  .guide-view[data-view="features"] .faq summary .pls::before,
  .guide-view[data-view="features"] .faq summary .pls::after{ background:var(--mktg); }
"""
    marker = '  .guide-view[data-view="admin"] .faq details[open] summary{ color:var(--plat); }\n'
    if 'data-view="features"] .eyebrow' not in html:
        if marker not in html:
            raise SystemExit("CSS insert marker not found for features")
        html = html.replace(marker, marker + block)
    return html


def ensure_flow_visual_css(html: str) -> str:
    """Shared visual flow diagram styles used by Mobility Program sections."""
    if ".flow-visual .diagram-title" in html:
        return html
    block = """
  /* Visual flow diagrams */
  .flow-visual{ margin-top:26px; border:1px solid var(--line); border-radius:18px; padding:24px; background:var(--surface); overflow-x:auto; }
  .flow-visual .diagram-title{ font-family:var(--font-display); font-size:20px; font-weight:600; margin:0 0 18px; color:var(--ink); }
  .flow-track{ display:flex; align-items:stretch; gap:12px; min-width:720px; }
  .flow-node-card{ flex:1; min-width:150px; border:1px solid var(--line); border-radius:14px; padding:16px; background:var(--surface-2); position:relative; }
  .flow-node-card .label{ font-family:var(--font-mono); font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }
  .flow-node-card .title{ font-family:var(--font-display); font-size:18px; font-weight:600; line-height:1.15; margin-top:8px; color:var(--ink); }
  .flow-node-card p{ font-size:14px; line-height:1.42; margin:8px 0 0; color:var(--muted); }
  .flow-node-card.student{ border-color:var(--product-line); background:var(--product-wash); }
  .flow-node-card.admin{ border-color:var(--qa-line); background:var(--qa-wash); }
  .flow-node-card.university{ border-color:var(--plat-line); background:var(--plat-wash); }
  .flow-node-card.success{ border-color:var(--qa); background:var(--qa-wash); }
  .flow-node-card.warning{ border-color:#E9B949; background:#FFF8E5; }
  .flow-node-card.danger{ border-color:#E08A8A; background:#FFF0F0; }
  .flow-arrow{ flex:0 0 auto; align-self:center; width:34px; height:34px; border-radius:50%; background:var(--bg-dark); color:#fff; display:flex; align-items:center; justify-content:center; font-family:var(--font-mono); font-size:18px; }
  .flow-branches{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-top:14px; min-width:720px; }
  .flow-branches.two{ grid-template-columns:repeat(2,1fr); }
  .flow-lanes{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; min-width:760px; }
  .flow-lane{ border:1px dashed var(--line); border-radius:16px; padding:14px; background:#fff; }
  .flow-lane h4{ font-family:var(--font-mono); font-size:12px; letter-spacing:.08em; text-transform:uppercase; margin:0 0 12px; color:var(--muted); }
  .flow-lane .flow-node-card{ margin-top:10px; min-width:0; }
  .flow-lane .flow-node-card:first-of-type{ margin-top:0; }
  .flow-mini-grid{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; min-width:760px; }
  .flow-mini-grid .flow-node-card{ min-width:0; }
  @media (max-width:980px){
    .flow-visual{ padding:18px; }
    .flow-track, .flow-branches, .flow-lanes, .flow-mini-grid{ min-width:680px; }
  }
"""
    return html.replace("</style>", block + "</style>", 1)


def sync_merged_usa_hub(html: str) -> str:
    """Hub deltas after merging University Admin into University Super Admin."""
    patches = [
        (
            '<p>Ten in-app roles, two web admin and product guides. Filter by category, then tap a card to open its full Feature &amp; Flow Guide.</p>',
            '<p>Ten in-app roles plus web product guides and the Paid Features catalog. Filter by category, then tap a card to open its full guide.</p>',
        ),
        (
            """      <a class="role-card" data-group="platform" href="javascript:void(0)" data-guide="univadmin">
        <div class="rc-top"><span class="rc-cat">Platform · University web</span><span class="rc-arrow">→</span></div>
        <h3>University Admin</h3>
        <p>The web command center for one university — dashboard metrics, user lifecycle, profile review, campuses, communities, travel, ambassadors, and events from the browser.</p>
        <span class="rc-foot">Open guide →</span>
      </a>

""",
            '',
        ),
        (
            '<p>The top administrator of one university — manages its people, and can view every other role\'s dashboard and data without performing their actions.</p>',
            '<p>The top administrator of one university — web portal and mobile app — managing users, profile review, university content, configuration, and read-only oversight of every other role.</p>',
        ),
        (
            '<div class="ans">Ten in-app roles plus two web guides: Intoto Admin, University Admin (web portal), Student, Ambassador, External Ambassador, Community Coordinator, Event Coordinator, University Super Admin, Third Party Coordinator, Third Party Sub Coordinator, and The Ambassador Platform (public web). Each has its own guide above.</div></details>',
            '<div class="ans">Ten in-app roles plus web product guides: Intoto Admin, Student, Ambassador, External Ambassador, Community Coordinator, Event Coordinator, University Super Admin, Third Party Coordinator, Third Party Sub Coordinator, and The Ambassador Platform (public web). Each has its own guide above.</div></details>',
        ),
        (
            '<div class="ans">The Intoto Admin is the platform-level administrator — they operate across every university on Intoto, onboard and manage the universities (tenants) themselves, invite top-level University Super Admins, and can switch university context to drill into one tenant. A University Super Admin runs a single university on the <b>mobile app</b>. The <b>University Admin</b> is the same university scope on the <b>web portal</b>. Only the Intoto Admin can add, suspend, or activate a university.</div></details>',
            '<div class="ans">The Intoto Admin is the platform-level administrator — they operate across every university on Intoto, onboard and manage the universities (tenants) themselves, invite top-level University Super Admins, and can switch university context to drill into one tenant. A University Super Admin runs a <b>single university</b> on the <b>web portal</b> and <b>mobile app</b> — user lifecycle, profile review, configuration, and read-only oversight of other roles. Only the Intoto Admin can add, suspend, or activate a university.</div></details>',
        ),
    ]
    for old, new in patches:
        if old in html:
            html = html.replace(old, new)
    return html


def patch_ambplat_faq(html: str) -> str:
    old = """        <details><summary><span>How is this different from the Intoto mobile app?</span><span class="pls"></span></summary>
        <div class="ans">The platform is a browser product focused on discovery and chat — meeting ambassadors before applying or enrolling. The mobile app is the full student lifecycle after enrolment: profile, travel, communities, events, and university admin. Different audience, different surface, different scope.</div></details>

        <details><summary><span>Do visitors need to be enrolled students to use it?</span>"""
    new = """        <details><summary><span>How is this different from the Intoto mobile app?</span><span class="pls"></span></summary>
        <div class="ans">The platform is a browser product focused on discovery and chat — meeting ambassadors before applying or enrolling. The mobile app is the full student lifecycle after enrolment: profile, travel, communities, events, and university admin. Different audience, different surface, different scope.</div></details>

        <details><summary><span>How do External Ambassadors appear on the platform?</span><span class="pls"></span></summary>
        <div class="ans">Off-campus partners invited as <b>External Ambassador</b> show in the directory with a <b>Staff</b> badge (Figma <span class="mono">Employee</span> filter). Prospects filter by <i>Staff</i>, open the card, and tap <b>Chat</b>; the partner replies from the <b>External Ambassador web portal</b>. See <i>Intoto External Ambassador Feature &amp; Flow Guide</i> for the fulfilment side.</div></details>

        <details><summary><span>Do visitors need to be enrolled students to use it?</span>"""
    if old in html and "How do External Ambassadors appear" not in html:
        html = html.replace(old, new)
    return html


def ensure_share_css_link(html: str) -> str:
    """All-in-One at doc root loads stylesheet from _files/ (share layout)."""
    html = re.sub(
        r'<link href="(?:\./)?(?:_files/)?guide\.css" rel="stylesheet">',
        f'<link href="{CSS_LINK}" rel="stylesheet">',
        html,
        count=1,
    )
    return html


def update_all_in_one() -> str:
    ext_guide = (BASE / "Intoto External Ambassador Feature & Flow Guide.html").read_text()
    ext_body = prefix_embed(extract_guide_body(ext_guide), "extamb-")

    usa_guide = (BASE / "Intoto University Super Admin Feature & Flow Guide.html").read_text()
    usa_body = prefix_embed(extract_guide_body(usa_guide), "usa-")

    admin_guide = (BASE / "Intoto Intoto Admin Feature & Flow Guide.html").read_text()
    admin_body = extract_guide_body(admin_guide)

    pf_guide = (BASE / "Intoto Paid Features Guide.html").read_text()
    pf_body = prefix_embed(extract_guide_body(pf_guide), "pf-")

    mobility_guide = (BASE / "Intoto Mobility Program Admin Feature & Flow Guide.html").read_text()
    mobility_body = prefix_embed(extract_guide_body(mobility_guide), "mobility-")

    community_guide = (BASE / "Intoto Community Coordinator Feature & Flow Guide.html").read_text()
    community_body = extract_guide_body(community_guide)

    hub_body = extract_hub_body(HUB.read_text())

    html = ALL_IN_ONE.read_text()
    html = remove_orphaned_fragments(html)
    html = remove_guide_view(html, "univadmin")
    html = replace_hub_section(html, hub_body)
    html = patch_hub_for_all_in_one(html)
    html = replace_section(html, "admin", admin_body)
    html = ensure_features_section(html, pf_body)
    html = ensure_mobility_section(html, mobility_body)
    html = replace_section(html, "community", community_body)
    html = replace_section(html, "extamb", ext_body)
    html = replace_section(html, "usa", usa_body)
    html = sync_hub_patches(html, HUB.read_text())
    html = sync_merged_usa_hub(html)
    html = ensure_usa_scoped_css(html)
    html = ensure_extamb_scoped_css(html)
    html = ensure_pf_scoped_css(html)
    html = ensure_flow_visual_css(html)
    html = patch_ambplat_faq(html)
    html = patch_inline_guide_links(html)
    html = ensure_anchor_navigation(html)
    html = ensure_share_css_link(html)
    ALL_IN_ONE.write_text(html)
    print(f"Updated {ALL_IN_ONE.name}")
    return html


def inline_for_portable(html: str) -> str:
    css = GUIDE_CSS.read_text()
    html = re.sub(
        r'<link href="(?:\./)?(?:_files/)?guide\.css" rel="stylesheet">\s*',
        f"<style>\n{css}\n</style>\n",
        html,
    )
    html = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', html)
    html = re.sub(r'<link href="https://fonts\.googleapis\.com[^>]*>\s*', '', html)
    return html


def fetch_font_faces(css_text: str) -> tuple[str, dict]:
    """Download woff2 fonts referenced in Google Fonts CSS; return patched CSS + manifest."""
    urls = list(dict.fromkeys(re.findall(r"url\((https://[^)]+)\)", css_text)))
    manifest: dict[str, dict] = {}
    for url in urls:
        uid = str(uuid.uuid4())
        data = urlopen(url, timeout=60).read()
        manifest[uid] = {
            "mime": "font/woff2",
            "compressed": False,
            "data": base64.b64encode(data).decode("ascii"),
        }
        css_text = css_text.replace(url, uid)
    return css_text, manifest


def build_portable(allinone_html: str) -> None:
    html = inline_for_portable(allinone_html)

    # Fetch and inline Google Fonts @font-face rules
    font_css = urlopen(FONT_CSS_URL, timeout=60).read().decode("utf-8")
    font_css, manifest = fetch_font_faces(font_css)

    # Inject font faces into <head>
    html = html.replace("</head>", f"<style>\n{font_css}\n</style>\n</head>", 1)

    # Remove bundler thumbnail from embedded template (loader has its own)
    html = re.sub(r'<template id="__bundler_thumbnail"[^>]*>.*?</template>\s*', '', html, flags=re.DOTALL)

    # json.dumps does not escape "/" — literal </script> inside the JSON string
    # terminates the host <script> tag in HTML and breaks JSON.parse.
    template_json = json.dumps(html, ensure_ascii=False)
    template_json = re.sub(
        r"</(?=[Ss][Cc][Rr][Ii][Pp][Tt])",
        r"<\\/",
        template_json,
    )
    manifest_json = json.dumps(manifest, separators=(",", ":"))

    out = (
        LOADER_HEAD
        + "  <script>\n"
        + LOADER_SCRIPT.strip()
        + "\n  </script>\n\n"
        + f'  <script type="__bundler/manifest">\n{manifest_json}\n  </script>\n\n'
        + '  <script type="__bundler/ext_resources">\n[]\n  </script>\n\n'
        + f'  <script type="__bundler/template">\n{template_json}\n  </script>\n'
        + "</body>\n</html>\n"
    )
    PORTABLE.write_text(out)
    size_mb = PORTABLE.stat().st_size / (1024 * 1024)
    print(f"Wrote {PORTABLE.name} ({size_mb:.1f} MB, {len(manifest)} fonts)")


def main() -> None:
    html = update_all_in_one()
    build_portable(html)
    # sanity checks
    portable = PORTABLE.read_text()
    assert "The External Ambassador web portal" in portable
    assert "Students &amp; leads" in portable or "Students & leads" in portable
    assert "New Leads" in portable
    # Verify template JSON parses when extracted like the browser loader does
    m = re.search(
        r'<script type="__bundler/template">\s*(\{.*\}|".*")\s*</script>',
        portable,
        re.DOTALL,
    )
    if not m:
        raise SystemExit("Template script tag not found in portable output")
    json.loads(m.group(1))
    assert "</script>" not in m.group(1), "raw </script> leaked into template JSON"
    assert html.count('id="extamb-legend"') == 1, "duplicate extamb-legend sections"
    assert 'data-view="univadmin"' not in html, "univadmin section should be removed"
    assert html.count('id="usa-legend"') == 1, "duplicate usa-legend sections"
    assert 'data-view="features"' in html, "features guide-view missing"
    assert 'data-view="mobility"' in html, "mobility guide-view missing"
    assert 'id="admin-features"' in html, "admin features section missing"
    assert 'data-anchor="pf-feat-community"' in html, "hub feature-card anchors missing"
    assert 'data-anchor="pf-feat-mobility"' in html, "mobility feature-card anchor missing"
    assert 'id="mobility-overview"' in html, "mobility guide content missing"
    assert ".flow-visual .diagram-title" in html, "flow visual styles missing"
    assert "Application submission &amp; approval" in html, "mobility flow diagram missing"
    assert "function applyRoleFilter(filter)" in html, "hub role filters missing"
    assert "Paid Features" in html
    assert "Profile review" in html or "Profile Review" in html
    assert "topic-based discussions" in html or "Community feature" in html
    print("Sanity checks passed.")


if __name__ == "__main__":
    main()
