html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Sri Devi Bhavan Hotel - Authentic Pure Vegetarian Food Since 1953, Devanahalli">
<title>Sri Devi Bhavan - Digital Menu</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--red:#8B1A1A;--red2:#A52020;--gold:#C9932A;--gold2:#E5B040;--bg:#FDF8F2;--card:#FFFFFF;--text:#2D2020;--muted:#7A6060;--border:#F0DED0;--shadow:0 2px 14px rgba(139,26,26,0.10);}
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:'Poppins',sans-serif;background:var(--bg);color:var(--text);max-width:480px;margin:0 auto;min-height:100vh;}
/* HEADER */
.hdr{background:linear-gradient(160deg,#5c0000 0%,#8B1A1A 55%,#a52525 100%);padding:22px 16px 18px;text-align:center;position:relative;}
.hdr-logo{width:96px;height:96px;border-radius:50%;border:3px solid var(--gold);object-fit:cover;margin:0 auto 10px;display:block;box-shadow:0 4px 20px rgba(0,0,0,0.4);}
.hdr-name{font-size:1.35rem;font-weight:800;color:#fff;letter-spacing:1px;text-shadow:1px 2px 6px rgba(0,0,0,0.5);}
.hdr-tag{font-size:0.7rem;color:var(--gold2);letter-spacing:2.5px;text-transform:uppercase;margin:3px 0 6px;}
.hdr-addr{font-size:0.72rem;color:rgba(255,255,255,0.78);margin-top:4px;}
.veg-pill{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,0.12);border:1px solid var(--gold);color:var(--gold2);font-size:0.68rem;font-weight:600;padding:4px 12px;border-radius:30px;margin-top:10px;}
.vdot{width:8px;height:8px;background:#4CAF50;border-radius:50%;display:inline-block;}
/* STICKY NAV */
.nav-wrap{position:sticky;top:0;z-index:200;background:var(--red);box-shadow:0 3px 10px rgba(0,0,0,0.3);}
.nav-tabs{display:flex;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;padding:0 6px;}
.nav-tabs::-webkit-scrollbar{display:none;}
.ntab{flex:0 0 auto;padding:11px 11px;font-size:0.7rem;font-weight:600;color:rgba(255,255,255,0.65);cursor:pointer;white-space:nowrap;border:none;border-bottom:3px solid transparent;background:none;font-family:'Poppins',sans-serif;transition:all 0.2s;}
.ntab.active,.ntab:hover{color:var(--gold2);border-bottom-color:var(--gold2);}
/* SECTION */
.sec{padding:0 12px;}
.sec-title{display:flex;align-items:center;gap:9px;padding:16px 0 10px;border-bottom:2px solid var(--gold);}
.sec-icon{font-size:1.25rem;}
.sec-name{font-size:1rem;font-weight:700;color:var(--red);letter-spacing:0.3px;}
.sec-time{font-size:0.65rem;color:var(--muted);background:#FFF0DC;padding:2px 9px;border-radius:20px;margin-left:auto;font-weight:500;}
/* CARD GRID */
.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0 6px;}
.card{background:var(--card);border-radius:14px;overflow:hidden;box-shadow:var(--shadow);position:relative;}
.card img{width:100%;height:115px;object-fit:cover;display:block;}
.card-body{padding:9px 11px 11px;}
.card-name{font-size:0.77rem;font-weight:600;color:var(--text);line-height:1.35;margin-bottom:5px;}
.card-price{font-size:0.92rem;font-weight:700;color:var(--red);}
.badge{position:absolute;top:8px;left:8px;background:#E53935;color:#fff;font-size:0.58rem;font-weight:700;padding:3px 8px;border-radius:12px;letter-spacing:0.3px;}
.badge-new{background:var(--gold);color:#fff;}
/* LIST */
.lst{background:var(--card);border-radius:14px;overflow:hidden;box-shadow:var(--shadow);margin:6px 0 10px;}
.lst-grp{font-size:0.68rem;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:0.8px;padding:8px 14px 5px;background:#FFF5E8;border-bottom:1px solid var(--border);}
.row{display:flex;align-items:center;justify-content:space-between;padding:11px 14px;border-bottom:1px solid var(--border);}
.row:last-child{border-bottom:none;}
.row-left{display:flex;align-items:center;gap:8px;flex:1;}
.vi{width:13px;height:13px;border:1.5px solid #4CAF50;border-radius:3px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.vi::after{content:'';width:7px;height:7px;background:#4CAF50;border-radius:50%;display:block;}
.row-name{font-size:0.82rem;font-weight:500;color:var(--text);line-height:1.3;}
.must{font-size:0.58rem;color:#E53935;font-weight:700;background:#FFEBEB;padding:1px 6px;border-radius:8px;white-space:nowrap;margin-left:4px;}
.price{font-size:0.9rem;font-weight:700;color:var(--red);white-space:nowrap;padding-left:10px;}
/* NOTICE */
.notice{background:linear-gradient(135deg,#1B5E20,#388E3C);color:#fff;padding:13px 16px;border-radius:14px;margin:6px 0 12px;text-align:center;}
.notice-main{font-size:0.88rem;font-weight:700;}
.notice-sub{font-size:0.72rem;opacity:0.85;margin-top:3px;}
/* FOOTER */
.ftr{margin:20px 12px 0;background:linear-gradient(160deg,#5c0000,#8B1A1A);border-radius:16px 16px 0 0;padding:22px 16px 30px;color:#fff;text-align:center;}
.ftr h3{font-size:0.95rem;font-weight:700;opacity:0.85;margin-bottom:6px;}
.ftr-phone{font-size:1.2rem;font-weight:800;color:var(--gold2);margin:8px 0;}
.ftr-phone a{color:inherit;text-decoration:none;}
.ftr-info{font-size:0.75rem;opacity:0.8;line-height:1.9;margin:10px 0;}
.ftr-note{font-size:0.72rem;color:var(--gold2);font-style:italic;margin-top:10px;}
.ftr-copy{margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.15);font-size:0.68rem;opacity:0.5;}
.spacer{height:16px;}
</style>
</head>
<body>

<!-- HEADER -->
<div class="hdr">
  <img src="Food images/logo1.jpg" alt="SDB Logo" class="hdr-logo" onerror="this.style.display='none'">
  <div class="hdr-name">SRI DEVI BHAVAN HOTEL</div>
  <div class="hdr-tag">Restaurants &amp; Catering · Since 1953</div>
  <div class="hdr-addr">7 B.B Road, Near Old Bus Stand, Devanahalli 562110</div>
  <div class="veg-pill"><span class="vdot"></span> 100% Pure Vegetarian</div>
</div>

<!-- STICKY NAV -->
<div class="nav-wrap">
  <div class="nav-tabs" id="navTabs">
    <button class="ntab active" data-target="beverages">☕ Beverages</button>
    <button class="ntab" data-target="breakfast">🍳 Breakfast</button>
    <button class="ntab" data-target="sweets">🍮 Sweets</button>
    <button class="ntab" data-target="evening">🌙 Evening</button>
    <button class="ntab" data-target="meals">🍛 Meals</button>
    <button class="ntab" data-target="dosa">🫓 Dosa</button>
    <button class="ntab" data-target="sdbspecial">⭐ SDB Special</button>
    <button class="ntab" data-target="chinese">🍜 Chinese</button>
    <button class="ntab" data-target="snacks">🥨 Snacks</button>
    <button class="ntab" data-target="tandoor">🫙 Tandoor</button>
  </div>
</div>

<!-- ═══════════ HOT BEVERAGES ═══════════ -->
<div id="beverages" class="sec">
  <div class="sec-title"><span class="sec-icon">☕</span><span class="sec-name">HOT BEVERAGES</span></div>
  <div class="grid">
    <div class="card">
      <img src="Food images/coffee.jpg" alt="Coffee" loading="lazy">
      <div class="card-body"><div class="card-name">Tea / Coffee</div><div class="card-price">₹25</div></div>
    </div>
    <div class="card">
      <img src="Food images/coffee1.jpg" alt="Less Tea" loading="lazy">
      <div class="card-body"><div class="card-name">Less Tea</div><div class="card-price">₹25</div></div>
    </div>
  </div>
  <div class="lst">
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Badam Milk</span></div><div class="price">₹35</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Horlicks / Bournvita / Boost</span></div><div class="price">₹35</div></div>
  </div>
</div>

<!-- ═══════════ BREAKFAST ═══════════ -->
<div id="breakfast" class="sec">
  <div class="sec-title"><span class="sec-icon">🍳</span><span class="sec-name">BREAKFAST</span></div>
  <div class="grid">
    <div class="card">
      <div class="badge">🔥 Must Try</div>
      <img src="Food images/3idli.jpg" alt="Idli" loading="lazy">
      <div class="card-body"><div class="card-name">Idli 3</div><div class="card-price">₹65</div></div>
    </div>
    <div class="card">
      <div class="badge">🔥 Must Try</div>
      <img src="Food images/1vada.jpg" alt="Vada" loading="lazy">
      <div class="card-body"><div class="card-name">Vada</div><div class="card-price">₹45</div></div>
    </div>
    <div class="card">
      <img src="Food images/poori.jpg" alt="Poori" loading="lazy">
      <div class="card-body"><div class="card-name">Poori 3</div><div class="card-price">₹80</div></div>
    </div>
    <div class="card">
      <img src="Food images/chow chow bath.jpg" alt="Chow Chow Bath" loading="lazy">
      <div class="card-body"><div class="card-name">Chow Chow Bath</div><div class="card-price">₹80</div></div>
    </div>
    <div class="card">
      <img src="Food images/khara bath.jpg" alt="Khara Bath" loading="lazy">
      <div class="card-body"><div class="card-name">Khara Bath</div><div class="card-price">₹50</div></div>
    </div>
    <div class="card">
      <img src="Food images/pongal.jpg" alt="Pongal" loading="lazy">
      <div class="card-body"><div class="card-name">Pongal</div><div class="card-price">₹50</div></div>
    </div>
  </div>
  <div class="lst">
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Idli 2</span></div><div class="price">₹50</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Idli (Single)</span></div><div class="price">₹35</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Idli Vada</span><span class="must">🔥 Must Try</span></div><div class="price">₹80</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Idli Vada (Single)</span></div><div class="price">₹70</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Poori 2</span></div><div class="price">₹60</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Rice Bath</span></div><div class="price">₹75</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Half Rice Bath</span></div><div class="price">₹45</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Kesari Bath</span></div><div class="price">₹50</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Rava Idli 1</span></div><div class="price">₹45</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Rava Idli 2</span></div><div class="price">₹80</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Shavige Bath</span></div><div class="price">₹80</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Half Shavige Bath</span></div><div class="price">₹50</div></div>
  </div>
</div>

<!-- ═══════════ SWEETS ═══════════ -->
<div id="sweets" class="sec">
  <div class="sec-title"><span class="sec-icon">🍮</span><span class="sec-name">SWEETS</span></div>
  <div class="grid">
    <div class="card">
      <img src="Food images/Gulab jamoon.jpg" alt="Gulab Jamoon" loading="lazy">
      <div class="card-body"><div class="card-name">Gulab Jamoon</div><div class="card-price">₹40</div></div>
    </div>
    <div class="card">
      <img src="Food images/Carrot halwa.jpg" alt="Carrot Halwa" loading="lazy">
      <div class="card-body"><div class="card-name">Carrot Halwa</div><div class="card-price">₹60</div></div>
    </div>
    <div class="card">
      <img src="Food images/Kashi halwa.jpg" alt="Kashi Halwa" loading="lazy">
      <div class="card-body"><div class="card-name">Kashi Halwa</div><div class="card-price">₹60</div></div>
    </div>
    <div class="card">
      <img src="Food images/Holige.jpg" alt="Holige" loading="lazy">
      <div class="card-body"><div class="card-name">Holige</div><div class="card-price">₹40</div></div>
    </div>
    <div class="card">
      <img src="Food images/Mysore pak.jpg" alt="Mysore Pak" loading="lazy">
      <div class="card-body"><div class="card-name">Mysore Pak (100g)</div><div class="card-price">₹70</div></div>
    </div>
  </div>
  <div class="lst">
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Payasa</span></div><div class="price">₹40</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Badusha (2 pc)</span></div><div class="price">₹70</div></div>
  </div>
</div>

<!-- ═══════════ EVENING SPECIAL ═══════════ -->
<div id="evening" class="sec">
  <div class="sec-title"><span class="sec-icon">🌙</span><span class="sec-name">EVENING SPECIAL</span></div>
  <div class="grid">
    <div class="card">
      <img src="Food images/ghee thate idli.jpg" alt="Ghee Thatte Idli" loading="lazy">
      <div class="card-body"><div class="card-name">Ghee Thatte Idli (1 pc)</div><div class="card-price">₹45</div></div>
    </div>
    <div class="card">
      <img src="Food images/ghee pudi thatte .jpg" alt="Ghee Pudi Thatte Idli" loading="lazy">
      <div class="card-body"><div class="card-name">Ghee Pudi Thatte Idli</div><div class="card-price">₹65</div></div>
    </div>
    <div class="card">
      <img src="Food images/button idli .jpg" alt="Button Idli" loading="lazy">
      <div class="card-body"><div class="card-name">Button Idli</div><div class="card-price">₹70</div></div>
    </div>
  </div>
  <div class="lst">
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Plain Thatte Idli (1 pc)</span></div><div class="price">₹35</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Plain Thatte Idli (2 pc)</span></div><div class="price">₹60</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Butter Thatte Idli (1 pc)</span></div><div class="price">₹45</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Masala Vade (1 pc)</span></div><div class="price">₹20</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Small Uddina Vade (1 pc)</span></div><div class="price">₹25</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Ghee Button Idli</span></div><div class="price">₹80</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Ghee Pudi Button Idli</span></div><div class="price">₹85</div></div>
  </div>
</div>

<!-- ═══════════ MEALS ═══════════ -->
<div id="meals" class="sec">
  <div class="sec-title"><span class="sec-icon">🍛</span><span class="sec-name">SOUTH BANANA LEAF MEALS</span></div>
  <div class="grid">
    <div class="card">
      <img src="Food images/poori meals.png" alt="Poori Meals" loading="lazy">
      <div class="card-body"><div class="card-name">Poori Meals</div><div class="card-price">₹120</div></div>
    </div>
    <div class="card">
      <img src="Food images/Chapathi meals.jpg" alt="Chapathi Meals" loading="lazy">
      <div class="card-body"><div class="card-name">Chapathi Meals</div><div class="card-price">₹120</div></div>
    </div>
  </div>
  <div class="notice">
    <div class="notice-main">🍃 Special Holige Meals — ₹205</div>
    <div class="notice-sub">Every Thursday to Monday only</div>
  </div>
  <div class="lst">
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Chapathi 1</span></div><div class="price">₹35</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Chapathi Plate</span></div><div class="price">₹60</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Extra Rice</span></div><div class="price">₹50</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Rice Sambar</span></div><div class="price">₹70</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Curd Rice</span></div><div class="price">₹75</div></div>
  </div>
</div>

<!-- ═══════════ DOSA ITEMS ═══════════ -->
<div id="dosa" class="sec">
  <div class="sec-title"><span class="sec-icon">🫓</span><span class="sec-name">DOSA ITEMS</span></div>
  <div class="grid">
    <div class="card">
      <div class="badge">🔥 Must Try</div>
      <img src="Food images/masala dosa.jpg" alt="Masala Dosa" loading="lazy">
      <div class="card-body"><div class="card-name">Masala Dosa</div><div class="card-price">₹80</div></div>
    </div>
    <div class="card">
      <div class="badge">🔥 Must Try</div>
      <img src="Food images/plain dosa.jpg" alt="Plain Dosa" loading="lazy">
      <div class="card-body"><div class="card-name">Plain Dosa</div><div class="card-price">₹65</div></div>
    </div>
    <div class="card">
      <div class="badge">🔥 Must Try</div>
      <img src="Food images/butter masala dosa.jpg" alt="Butter Masala Dosa" loading="lazy">
      <div class="card-body"><div class="card-name">Butter Masala</div><div class="card-price">₹90</div></div>
    </div>
    <div class="card">
      <div class="badge">🔥 Must Try</div>
      <img src="Food images/ghe onion dossa.jpg" alt="Ghee Onion Dosa" loading="lazy">
      <div class="card-body"><div class="card-name">Ghee Onion Dosa</div><div class="card-price">₹105</div></div>
    </div>
    <div class="card">
      <div class="badge">🔥 Must Try</div>
      <img src="Food images/khali dosa .jpg" alt="Khali Dosa" loading="lazy">
      <div class="card-body"><div class="card-name">Khali Dosa</div><div class="card-price">₹80</div></div>
    </div>
    <div class="card">
      <div class="badge">🔥 Must Try</div>
      <img src="Food images/neer dosa.jpg" alt="Neer Dosa" loading="lazy">
      <div class="card-body"><div class="card-name">Neer Dosa</div><div class="card-price">₹95</div></div>
    </div>
  </div>
  <div class="lst">
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Set Dosa</span><span class="must">🔥 Must Try</span></div><div class="price">₹80</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Onion Dosa</span><span class="must">🔥 Must Try</span></div><div class="price">₹90</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Ghee Set Dosa</span><span class="must">🔥 Must Try</span></div><div class="price">₹90</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Ghee Plain Dosa</span></div><div class="price">₹70</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Ghee Khali Dosa</span></div><div class="price">₹90</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Rava Plain Dosa</span></div><div class="price">₹80</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Rava Masala Dosa</span><span class="must">🔥 Must Try</span></div><div class="price">₹90</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Rava Onion Masala</span></div><div class="price">₹100</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Ragi Plain Dosa</span></div><div class="price">₹80</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Ragi Masala Dosa</span></div><div class="price">₹90</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Ragi Onion Dosa</span></div><div class="price">₹100</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Paper Plain Dosa</span><span class="must">🔥 Must Try</span></div><div class="price">₹110</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Rice Masala</span></div><div class="price">₹110</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Baby Masala</span></div><div class="price">₹75</div></div>
  </div>
</div>

<!-- ═══════════ SDB SPECIAL DOSA ═══════════ -->
<div id="sdbspecial" class="sec">
  <div class="sec-title"><span class="sec-icon">⭐</span><span class="sec-name">SDB SPECIAL DOSA</span></div>
  <div class="grid">
    <div class="card">
      <div class="badge">⭐ Special</div>
      <img src="Food images/Paneer masala dosa.jpg" alt="Paneer Masala Dosa" loading="lazy">
      <div class="card-body"><div class="card-name">Paneer Masala Dosa</div><div class="card-price">₹125</div></div>
    </div>
    <div class="card">
      <div class="badge">⭐ Special</div>
      <img src="Food images/cheese masala dosa .jpg" alt="Cheese Masala Dosa" loading="lazy">
      <div class="card-body"><div class="card-name">Cheese Masala Dosa</div><div class="card-price">₹115</div></div>
    </div>
    <div class="card">
      <div class="badge">⭐ Special</div>
      <img src="Food images/paneer masala dosa .jpg" alt="Paneer Masala Dosa 2" loading="lazy">
      <div class="card-body"><div class="card-name">Paneer Cheese Masala</div><div class="card-price">₹135</div></div>
    </div>
  </div>
  <div class="lst">
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Ghee Masala Dosa</span></div><div class="price">₹90</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Rava Onion Ghee Masala Dosa</span></div><div class="price">₹110</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Paper Masala Dosa</span></div><div class="price">₹145</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Family Masala Dosa</span><span class="must">👨‍👩‍👧‍👦 Family</span></div><div class="price">₹305</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Palak Masala Dosa</span></div><div class="price">₹105</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Palak Cheese Masala Dosa</span></div><div class="price">₹135</div></div>
  </div>
</div>

<!-- ═══════════ CHINESE ═══════════ -->
<div id="chinese" class="sec">
  <div class="sec-title"><span class="sec-icon">🍜</span><span class="sec-name">CHINESE</span><span class="sec-time">2:00 PM – 11:00 PM</span></div>
  <div class="grid">
    <div class="card">
      <img src="Food images/Veg friedrice.jpg" alt="Veg Fried Rice" loading="lazy">
      <div class="card-body"><div class="card-name">Veg Fried Rice</div><div class="card-price">₹115</div></div>
    </div>
    <div class="card">
      <img src="Food images/Mushroom friedrice.jpg" alt="Mushroom Fried Rice" loading="lazy">
      <div class="card-body"><div class="card-name">Mushroom Fried Rice</div><div class="card-price">₹135</div></div>
    </div>
    <div class="card">
      <img src="Food images/Paneer fried rice.jpg" alt="Paneer Fried Rice" loading="lazy">
      <div class="card-body"><div class="card-name">Paneer Fried Rice</div><div class="card-price">₹145</div></div>
    </div>
    <div class="card">
      <img src="Food images/Baby corn rice.jpg" alt="Baby Corn Rice" loading="lazy">
      <div class="card-body"><div class="card-name">Baby Corn Rice</div><div class="card-price">₹135</div></div>
    </div>
    <div class="card">
      <img src="Food images/Ghee rice.jpg" alt="Ghee Rice" loading="lazy">
      <div class="card-body"><div class="card-name">Ghee Rice</div><div class="card-price">₹115</div></div>
    </div>
    <div class="card">
      <img src="Food images/Jeera rice.jpg" alt="Jeera Rice" loading="lazy">
      <div class="card-body"><div class="card-name">Jeera Rice</div><div class="card-price">₹115</div></div>
    </div>
    <div class="card">
      <img src="Food images/Veg noodles.jpg" alt="Veg Noodles" loading="lazy">
      <div class="card-body"><div class="card-name">Veg Noodles</div><div class="card-price">₹115</div></div>
    </div>
    <div class="card">
      <img src="Food images/Mushroom pepper dry.jpg" alt="Mushroom Pepper Dry" loading="lazy">
      <div class="card-body"><div class="card-name">Mushroom Pepper Dry</div><div class="card-price">₹145</div></div>
    </div>
    <div class="card">
      <img src="Food images/Paneer chilly.jpg" alt="Paneer Chilly" loading="lazy">
      <div class="card-body"><div class="card-name">Paneer Chilly</div><div class="card-price">₹155</div></div>
    </div>
  </div>
  <div class="lst">
    <div class="lst-grp">MANCHURI & STARTERS</div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Gobi Manchuri</span></div><div class="price">₹115</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Mushroom Manchuri</span></div><div class="price">₹125</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Baby Corn Manchuri</span></div><div class="price">₹115</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Paneer Manchuri</span></div><div class="price">₹145</div></div>
    <div class="lst-grp">RICE</div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Gobi Rice</span></div><div class="price">₹125</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Mushroom Rice</span></div><div class="price">₹135</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Garlic Fried Rice</span></div><div class="price">₹125</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Capsicum Fried Rice</span></div><div class="price">₹115</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Schezwan Rice</span></div><div class="price">₹135</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Masala Rice</span></div><div class="price">₹125</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Tamato Rice</span></div><div class="price">₹115</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Singapore Rice</span></div><div class="price">₹125</div></div>
    <div class="lst-grp">NOODLES</div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Gobi Noodles</span></div><div class="price">₹135</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Baby Corn Noodles</span></div><div class="price">₹135</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Mushroom Noodles</span></div><div class="price">₹145</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Paneer Noodles</span></div><div class="price">₹155</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Schezwan Noodles</span></div><div class="price">₹145</div></div>
    <div class="lst-grp">CHILLY & DRY</div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Baby Corn Pepper Dry</span></div><div class="price">₹135</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Paneer Pepper Dry</span></div><div class="price">₹155</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Baby Corn Chilly</span></div><div class="price">₹135</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Mushroom Chilly</span></div><div class="price">₹145</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Gobi Chilly</span></div><div class="price">₹125</div></div>
    <div class="lst-grp">65 ITEMS</div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Baby Corn 65</span></div><div class="price">₹125</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Paneer 65</span></div><div class="price">₹165</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Gobi 65</span></div><div class="price">₹125</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Mushroom 65</span></div><div class="price">₹145</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Aloo 65</span></div><div class="price">₹115</div></div>
  </div>
</div>

<!-- ═══════════ SNACKS ═══════════ -->
<div id="snacks" class="sec">
  <div class="sec-title"><span class="sec-icon">🥨</span><span class="sec-name">SNACKS</span></div>
  <div class="grid">
    <div class="card">
      <img src="Food images/curd vada.jpg" alt="Curd Vada" loading="lazy">
      <div class="card-body"><div class="card-name">Curd Vada</div><div class="card-price">₹65</div></div>
    </div>
    <div class="card">
      <img src="Food images/Mangalore bun.jpg" alt="Mangalore Buns" loading="lazy">
      <div class="card-body"><div class="card-name">Mangalore Buns</div><div class="card-price">₹55</div></div>
    </div>
    <div class="card">
      <img src="Food images/Samosa.jpg" alt="Samosa" loading="lazy">
      <div class="card-body"><div class="card-name">Samosa (2 pcs)</div><div class="card-price">₹45</div></div>
    </div>
    <div class="card">
      <img src="Food images/mangalore bajji.jpg" alt="Bhajji / Pakoda" loading="lazy">
      <div class="card-body"><div class="card-name">Bhajji / Pakoda</div><div class="card-price">₹75</div></div>
    </div>
  </div>
  <div class="lst">
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Maddurvada 1</span></div><div class="price">₹30</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Maddurvada Plate</span></div><div class="price">₹75</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Butter Muruku</span></div><div class="price">₹65</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Bonda Soup</span></div><div class="price">₹65</div></div>
  </div>
</div>

<!-- ═══════════ TANDOOR ═══════════ -->
<div id="tandoor" class="sec">
  <div class="sec-title"><span class="sec-icon">🫙</span><span class="sec-name">TANDOOR ITEMS</span><span class="sec-time">3:00 PM – 12:00 AM</span></div>
  <div class="grid">
    <div class="card">
      <img src="Food images/aloo paratha.jpg" alt="Aloo Parota" loading="lazy">
      <div class="card-body"><div class="card-name">Aloo Parota (1)</div><div class="card-price">₹115</div></div>
    </div>
    <div class="card">
      <img src="Food images/paneer butter masala.jpg" alt="Paneer Butter Masala" loading="lazy">
      <div class="card-body"><div class="card-name">Paneer Butter Masala</div><div class="card-price">₹175</div></div>
    </div>
  </div>
  <div class="lst">
    <div class="lst-grp">ROTI & NAAN</div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Roti Curry Single</span></div><div class="price">₹70</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Roti</span></div><div class="price">₹105</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Butter Roti</span></div><div class="price">₹115</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Naan</span></div><div class="price">₹105</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Butter Naan</span></div><div class="price">₹115</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Kulcha</span></div><div class="price">₹115</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Butter Kulcha</span></div><div class="price">₹125</div></div>
    <div class="lst-grp">PAROTA</div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Paneer Parota (1)</span></div><div class="price">₹155</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Vegetable Parota (1)</span></div><div class="price">₹135</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Gobi Parota (1)</span></div><div class="price">₹125</div></div>
    <div class="lst-grp">EXTRA BREADS</div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Extra Roti (1)</span></div><div class="price">₹45</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Extra Butter Roti (1)</span></div><div class="price">₹50</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Extra Naan (1)</span></div><div class="price">₹75</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Extra Butter Naan (1)</span></div><div class="price">₹85</div></div>
    <div class="lst-grp">SIDES & CURRIES</div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Papad</span></div><div class="price">₹65</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Masala Papad</span></div><div class="price">₹75</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Dal Fry</span></div><div class="price">₹165</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Mushroom Curry</span></div><div class="price">₹175</div></div>
    <div class="row"><div class="row-left"><div class="vi"></div><span class="row-name">Tamato Curry</span></div><div class="price">₹165</div></div>
  </div>
</div>

<!-- FOOTER -->
<div class="ftr">
  <div class="ftr-title">📞 Reach Us</div>
  <div class="ftr-phone">
    <a href="tel:9972463835">9972463835</a> / <a href="tel:9972731953">9972731953</a>
  </div>
  <div class="ftr-info">
    ✓ Party Orders Undertaken<br>
    ✓ Order once placed will not be cancelled<br>
    ✓ GST / Taxes are applicable
  </div>
  <div class="ftr-note">
    Hot Water / Filter Water Available — Please ask<br>
    No Artificial Colour or Tasting Powder used
  </div>
  <div class="ftr-note" style="margin-top:8px;">⏱ After order, please wait 10–15 minutes</div>
  <div class="ftr-copy">© Sri Devi Bhavan Hotel · Since 1953 · Devanahalli</div>
</div>

<script>
const tabs = document.querySelectorAll('.ntab');
const sections = ['beverages','breakfast','sweets','evening','meals','dosa','sdbspecial','chinese','snacks','tandoor'];
const NAV_H = document.querySelector('.nav-wrap').offsetHeight + 4;

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const id = tab.dataset.target;
    const el = document.getElementById(id);
    if(el) {
      const top = el.getBoundingClientRect().top + window.scrollY - NAV_H - 4;
      window.scrollTo({top, behavior:'smooth'});
    }
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    // scroll tab into view
    tab.scrollIntoView({inline:'center', behavior:'smooth', block:'nearest'});
  });
});

// Highlight active tab on scroll
const obs = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if(entry.isIntersecting) {
      const id = entry.target.id;
      tabs.forEach(t => {
        if(t.dataset.target === id) {
          t.classList.add('active');
          t.scrollIntoView({inline:'center', behavior:'smooth', block:'nearest'});
        } else {
          t.classList.remove('active');
        }
      });
    }
  });
}, {rootMargin: `-${NAV_H + 10}px 0px -60% 0px`, threshold: 0});

sections.forEach(id => {
  const el = document.getElementById(id);
  if(el) obs.observe(el);
});
</script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done! index.html written successfully.")
