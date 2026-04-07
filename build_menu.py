import json
from pathlib import Path


def esc(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_section(sec):
    time_html = f'<span class="sec-time">{esc(sec.get("time", ""))}</span>' if sec.get("time") else ""
    cards = []
    for c in sec.get("cards", []):
        badge = f'<div class="badge">{esc(c.get("badge", ""))}</div>' if c.get("badge") else ""
        cards.append(
            f'''<div class="card">
      {badge}
      <img src="{esc(c.get("image", ""))}" alt="{esc(c.get("alt", c.get("name", "")))}" loading="lazy">
      <div class="card-body"><div class="card-name">{esc(c.get("name", ""))}</div><div class="card-price">₹{int(c.get("price", 0))}</div></div>
    </div>'''
        )
    cards_html = f'<div class="grid">\n{"".join(cards)}\n  </div>' if cards else ""

    notice_html = ""
    if sec.get("notice"):
        notice = sec["notice"]
        notice_html = f'''<div class="notice">
    <div class="notice-main">{esc(notice.get("main", ""))}</div>
    <div class="notice-sub">{esc(notice.get("sub", ""))}</div>
  </div>'''

    list_parts = []
    for group in sec.get("listGroups", []):
        if group.get("title"):
            list_parts.append(f'<div class="lst-grp">{esc(group["title"])}</div>')
        for item in group.get("items", []):
            tag = f'<span class="must">{esc(item.get("tag", ""))}</span>' if item.get("tag") else ""
            list_parts.append(
                f'<div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">{esc(item.get("name", ""))}</span>{tag}</div><div class="price">₹{int(item.get("price", 0))}</div></div>'
            )
    list_html = f'<div class="lst">\n    {"".join(list_parts)}\n  </div>' if list_parts else ""

    return f'''<div id="{esc(sec.get("id", ""))}" class="sec">
  <div class="sec-title"><span class="sec-icon">{esc(sec.get("icon", ""))}</span><span class="sec-name">{esc(sec.get("name", ""))}</span>{time_html}</div>
  {cards_html}
  {notice_html}
  {list_html}
</div>'''


data = json.loads(Path("menu.json").read_text(encoding="utf-8"))
restaurant = data["restaurant"]
sections = data["sections"]
tab_buttons = []
for i, sec in enumerate(sections):
    active = " active" if i == 0 else ""
    tab_buttons.append(
        f'<button class="ntab{active}" data-target="{esc(sec["id"])}">{esc(sec.get("tab", sec["name"]))}</button>'
    )

section_ids_js = json.dumps([s["id"] for s in sections], ensure_ascii=False)
sections_html = "\n".join(render_section(s) for s in sections)
phones_html = " / ".join([f'<a href="tel:{esc(p)}">{esc(p)}</a>' for p in restaurant.get("phones", [])])

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Sri Devi Bhavan Hotel - Authentic Pure Vegetarian Food Since 1953, Devanahalli">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#8B1A1A">
<title>Sri Devi Bhavan - Digital Menu</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--red:#8B1A1A;--red2:#A52020;--gold:#C9932A;--gold2:#E5B040;--bg:#FDF8F2;--card:#FFFFFF;--text:#2D2020;--muted:#7A6060;--border:#F0DED0;--shadow:0 2px 14px rgba(139,26,26,0.10);}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Poppins',sans-serif;background:var(--bg);color:var(--text);max-width:480px;margin:0 auto;min-height:100vh;}}
.ctx{{display:none;background:#FFF5E8;border:1px solid var(--border);border-radius:10px;margin:10px 12px;padding:8px 10px;font-size:.72rem;color:var(--red);font-weight:600;}}
.ctx.show{{display:block;}}
.hdr{{background:linear-gradient(160deg,#5c0000 0%,#8B1A1A 55%,#a52525 100%);padding:22px 16px 18px;text-align:center;position:relative;}}
.hdr-logo{{width:96px;height:96px;border-radius:50%;border:3px solid var(--gold);object-fit:cover;margin:0 auto 10px;display:block;box-shadow:0 4px 20px rgba(0,0,0,0.4);}}
.hdr-name{{font-size:1.35rem;font-weight:800;color:#fff;letter-spacing:1px;text-shadow:1px 2px 6px rgba(0,0,0,0.5);}}
.hdr-tag{{font-size:0.7rem;color:var(--gold2);letter-spacing:2.5px;text-transform:uppercase;margin:3px 0 6px;}}
.hdr-addr{{font-size:0.72rem;color:rgba(255,255,255,0.78);margin-top:4px;}}
.veg-pill{{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,0.12);border:1px solid var(--gold);color:var(--gold2);font-size:0.68rem;font-weight:600;padding:4px 12px;border-radius:30px;margin-top:10px;}}
.vdot{{width:8px;height:8px;background:#4CAF50;border-radius:50%;display:inline-block;}}
.nav-wrap{{position:sticky;top:0;z-index:200;background:var(--red);box-shadow:0 3px 10px rgba(0,0,0,0.3);}}
.nav-tabs{{display:flex;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;padding:0 6px;}}
.nav-tabs::-webkit-scrollbar{{display:none;}}
.ntab{{flex:0 0 auto;padding:11px 11px;font-size:0.7rem;font-weight:600;color:rgba(255,255,255,0.65);cursor:pointer;white-space:nowrap;border:none;border-bottom:3px solid transparent;background:none;font-family:'Poppins',sans-serif;transition:all 0.2s;}}
.ntab.active,.ntab:hover{{color:var(--gold2);border-bottom-color:var(--gold2);}}
.sec{{padding:0 12px;}}
.sec-title{{display:flex;align-items:center;gap:9px;padding:16px 0 10px;border-bottom:2px solid var(--gold);}}
.sec-icon{{font-size:1.25rem;}}
.sec-name{{font-size:1rem;font-weight:700;color:var(--red);letter-spacing:0.3px;}}
.sec-time{{font-size:0.65rem;color:var(--muted);background:#FFF0DC;padding:2px 9px;border-radius:20px;margin-left:auto;font-weight:500;}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0 6px;}}
.card{{background:var(--card);border-radius:14px;overflow:hidden;box-shadow:var(--shadow);position:relative;}}
.card img{{width:100%;height:115px;object-fit:cover;display:block;}}
.card-body{{padding:9px 11px 11px;}}
.card-name{{font-size:0.77rem;font-weight:600;color:var(--text);line-height:1.35;margin-bottom:5px;}}
.card-price{{font-size:0.92rem;font-weight:700;color:var(--red);}}
.badge{{position:absolute;top:8px;left:8px;background:#E53935;color:#fff;font-size:0.58rem;font-weight:700;padding:3px 8px;border-radius:12px;letter-spacing:0.3px;}}
.lst{{background:var(--card);border-radius:14px;overflow:hidden;box-shadow:var(--shadow);margin:6px 0 10px;}}
.lst-grp{{font-size:0.68rem;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:0.8px;padding:8px 14px 5px;background:#FFF5E8;border-bottom:1px solid var(--border);}}
.row{{display:flex;align-items:center;justify-content:space-between;padding:11px 14px;border-bottom:1px solid var(--border);}}
.row:last-child{{border-bottom:none;}}
.row-left{{display:flex;align-items:center;gap:8px;flex:1;}}
.vi{{width:13px;height:13px;border:1.5px solid #4CAF50;border-radius:3px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}}
.vi::after{{content:'';width:7px;height:7px;background:#4CAF50;border-radius:50%;display:block;}}
.row-name{{font-size:0.82rem;font-weight:500;color:var(--text);line-height:1.3;}}
.must{{font-size:0.58rem;color:#E53935;font-weight:700;background:#FFEBEB;padding:1px 6px;border-radius:8px;white-space:nowrap;margin-left:4px;}}
.price{{font-size:0.9rem;font-weight:700;color:var(--red);white-space:nowrap;padding-left:10px;}}
.notice{{background:linear-gradient(135deg,#1B5E20,#388E3C);color:#fff;padding:13px 16px;border-radius:14px;margin:6px 0 12px;text-align:center;}}
.notice-main{{font-size:0.88rem;font-weight:700;}}
.notice-sub{{font-size:0.72rem;opacity:0.85;margin-top:3px;}}
.ftr{{margin:20px 12px 0;background:linear-gradient(160deg,#5c0000,#8B1A1A);border-radius:16px 16px 0 0;padding:22px 16px 30px;color:#fff;text-align:center;}}
.ftr-phone{{font-size:1.2rem;font-weight:800;color:var(--gold2);margin:8px 0;}}
.ftr-phone a{{color:inherit;text-decoration:none;}}
.ftr-info{{font-size:0.75rem;opacity:0.8;line-height:1.9;margin:10px 0;}}
.ftr-note{{font-size:0.72rem;color:var(--gold2);font-style:italic;margin-top:10px;}}
.ftr-copy{{margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.15);font-size:0.68rem;opacity:0.5;}}
</style>
</head>
<body>
<div class="hdr">
  <img src="{esc(restaurant.get("logo", ""))}" alt="SDB Logo" class="hdr-logo" onerror="this.style.display='none'">
  <div class="hdr-name">{esc(restaurant.get("name", ""))}</div>
  <div class="hdr-tag">{esc(restaurant.get("tagline", ""))}</div>
  <div class="hdr-addr">{esc(restaurant.get("address", ""))}</div>
  <div class="veg-pill"><span class="vdot"></span> 100% Pure Vegetarian</div>
</div>
<div id="ctx" class="ctx"></div>
<div class="nav-wrap">
  <div class="nav-tabs" id="navTabs">
    {"".join(tab_buttons)}
  </div>
</div>
{sections_html}
<div class="ftr">
  <div class="ftr-title">Reach Us</div>
  <div class="ftr-phone">{phones_html}</div>
  <div class="ftr-info">Party Orders Undertaken<br>Order once placed will not be cancelled<br>GST / Taxes are applicable</div>
  <div class="ftr-note">Hot Water / Filter Water Available - Please ask<br>No Artificial Colour or Tasting Powder used</div>
  <div class="ftr-note" style="margin-top:8px;">After order, please wait 10-15 minutes</div>
  <div class="ftr-copy">Sri Devi Bhavan Hotel - Since 1953 - Devanahalli</div>
</div>
<script>
const sections = {section_ids_js};
const tabs = document.querySelectorAll('.ntab');
const NAV_H = document.querySelector('.nav-wrap').offsetHeight + 4;
const qs = new URLSearchParams(window.location.search);
const table = qs.get('table');
const lang = qs.get('lang');
const branch = qs.get('branch');
const ctx = document.getElementById('ctx');
const ctxParts = [];
if (table) ctxParts.push(`Table: ${{table}}`);
if (branch) ctxParts.push(`Branch: ${{branch}}`);
if (lang) ctxParts.push(`Language: ${{lang}}`);
if (ctxParts.length) {{
  ctx.textContent = ctxParts.join(' | ');
  ctx.classList.add('show');
}}
tabs.forEach(tab => {{
  tab.addEventListener('click', () => {{
    const id = tab.dataset.target;
    const el = document.getElementById(id);
    if (el) {{
      const top = el.getBoundingClientRect().top + window.scrollY - NAV_H - 4;
      window.scrollTo({{top, behavior:'smooth'}});
    }}
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    tab.scrollIntoView({{inline:'center', behavior:'smooth', block:'nearest'}});
  }});
}});
const obs = new IntersectionObserver((entries) => {{
  entries.forEach(entry => {{
    if (entry.isIntersecting) {{
      const id = entry.target.id;
      tabs.forEach(t => {{
        if (t.dataset.target === id) {{
          t.classList.add('active');
          t.scrollIntoView({{inline:'center', behavior:'smooth', block:'nearest'}});
        }} else {{
          t.classList.remove('active');
        }}
      }});
    }}
  }});
}}, {{rootMargin: `-${{NAV_H + 10}}px 0px -60% 0px`, threshold: 0}});
sections.forEach(id => {{
  const el = document.getElementById(id);
  if (el) obs.observe(el);
}});
if ('serviceWorker' in navigator) {{
  window.addEventListener('load', () => navigator.serviceWorker.register('service-worker.js').catch(() => null));
}}
</script>
</body>
</html>"""

Path("index.html").write_text(html, encoding="utf-8")
print("Done! index.html generated from menu.json.")
