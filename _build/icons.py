# -*- coding: utf-8 -*-
"""Inline SVG icons (animated where noted). Stroke-based, consistent 1.6 width."""

WHATSAPP = '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 .5C7.4.5.5 7.4.5 16c0 2.8.7 5.4 2 7.7L.4 31.6l8.1-2.1c2.2 1.2 4.8 1.9 7.5 1.9 8.6 0 15.5-6.9 15.5-15.5S24.6.5 16 .5zm0 28.2c-2.4 0-4.7-.7-6.7-1.9l-.5-.3-4.8 1.3 1.3-4.7-.3-.5a12.6 12.6 0 01-1.9-6.6C3.4 9 9 3.4 16 3.4S28.6 9 28.6 16 23 28.7 16 28.7zm7-9.4c-.4-.2-2.3-1.1-2.6-1.2-.3-.1-.6-.2-.9.2-.3.4-1 1.2-1.2 1.4-.2.2-.4.3-.8.1-.4-.2-1.6-.6-3.1-1.9-1.2-1-1.9-2.3-2.1-2.7-.2-.4 0-.6.2-.8l.6-.7c.2-.2.3-.4.4-.6.1-.2 0-.5-.1-.7l-1.2-2.8c-.3-.7-.6-.6-.9-.6h-.7c-.2 0-.6.1-.9.4-.3.4-1.2 1.2-1.2 2.9s1.2 3.4 1.4 3.6c.2.2 2.4 3.7 5.9 5.2.8.4 1.5.6 2 .7.8.3 1.6.2 2.2.1.7-.1 2.3-.9 2.6-1.8.3-.9.3-1.6.2-1.8-.1-.2-.3-.3-.7-.5z"/></svg>'

PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'

MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>'

PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'

ARROW = '<svg class="btn-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

# Animated "why" feature icons — each has a subtle continuous motion via CSS class
ICONS = {
"privacy": '<svg class="ico ico-privacy" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M32 6 10 16v14c0 13 9 22 22 28 13-6 22-15 22-28V16L32 6Z"/><path class="check" d="M22 32l7 7 14-15"/></svg>',
"clock": '<svg class="ico ico-clock" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="32" cy="32" r="24"/><path class="hand-h" d="M32 32V18"/><path class="hand-m" d="M32 32l12 7"/></svg>',
"leaf": '<svg class="ico ico-leaf" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M50 12C24 12 12 26 12 48c0 0 0 4 0 4s22-2 34-14C58 26 50 12 50 12Z"/><path class="vein" d="M16 48C28 36 40 24 50 12"/></svg>',
"plate": '<svg class="ico ico-plate" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="32" cy="34" r="20"/><circle cx="32" cy="34" r="11"/><path class="steam" d="M26 10c0-3 4-3 4-6M34 10c0-3 4-3 4-6"/></svg>',
}

LEAF_DIVIDER = '''<div class="leaf-divider" aria-hidden="true"><span class="rule"></span>
<svg viewBox="0 0 120 48" fill="none"><g stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><path d="M8 24 H112"/></g><g fill="currentColor"><path class="leaf-l" d="M46 24c-4-7-12-9-18-7 1 6 7 11 14 11 2 0 3-1 4-4z"/><path class="leaf-r" d="M60 24c4-7 12-9 18-7-1 6-7 11-14 11-2 0-3-1-4-4z"/><path class="leaf-t" d="M53 20c-3-6-2-13 2-18 4 5 5 12 2 18-1 1-3 1-4 0z"/></g></svg>
<span class="rule r"></span></div>'''

# social
IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>'
FB = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 9h3V6h-3c-2.2 0-4 1.8-4 4v2H7v3h3v6h3v-6h3l1-3h-4v-2c0-.6.4-1 1-1Z"/></svg>'
