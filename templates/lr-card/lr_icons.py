# Simple brand SVG illustrations for no-photo LR designs (viewBox 0 0 400 400)
G = '#0E7447'; R = '#C3232B'; W = '#F4F5F2'; GL = '#3FB27A'

def svg(inner, size=520):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'

ICONS = {
 'bulb': f'''
  <g stroke="{W}" stroke-width="10" stroke-linecap="round" fill="none">
   <line x1="200" y1="18" x2="200" y2="52"/><line x1="70" y1="70" x2="94" y2="94"/><line x1="330" y1="70" x2="306" y2="94"/>
   <line x1="24" y1="180" x2="58" y2="180"/><line x1="376" y1="180" x2="342" y2="180"/></g>
  <path d="M200 70c-62 0-110 48-110 108 0 40 20 66 40 88 14 15 22 30 22 48h96c0-18 8-33 22-48 20-22 40-48 40-88 0-60-48-108-110-108z" fill="{G}" stroke="{W}" stroke-width="10"/>
  <path d="M168 300v-60l32-40 32 40v60" fill="none" stroke="{W}" stroke-width="9" stroke-linejoin="round"/>
  <rect x="150" y="322" width="100" height="22" rx="8" fill="{W}"/><rect x="158" y="350" width="84" height="20" rx="8" fill="{W}"/>
  <rect x="176" y="374" width="48" height="16" rx="6" fill="{W}"/>
  <text x="200" y="170" text-anchor="middle" font-family="Oswald" font-weight="700" font-size="58" fill="{W}">LED</text>''',
 'quake': f'''
  <path d="M60 190 L200 80 L340 190" fill="none" stroke="{W}" stroke-width="12" stroke-linejoin="round"/>
  <rect x="92" y="180" width="216" height="130" fill="{G}" stroke="{W}" stroke-width="10"/>
  <path d="M210 182 l-24 40 l30 22 l-26 46 l14 20" fill="none" stroke="#141816" stroke-width="10" stroke-linejoin="round"/>
  <rect x="120" y="212" width="46" height="40" fill="{W}"/><rect x="236" y="212" width="46" height="40" fill="{W}"/>
  <path d="M0 360 h70 l16 -40 l20 70 l22 -90 l24 110 l22 -80 l18 50 l14 -20 h194" fill="none" stroke="{R}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>''',
 'bottle': f'''
  <rect x="168" y="22" width="64" height="34" rx="6" fill="{R}"/>
  <path d="M176 56h48v34c0 14 44 30 44 74v196c0 14-12 24-26 24h-84c-14 0-26-10-26-24V164c0-44 44-60 44-74z" fill="none" stroke="{W}" stroke-width="10" stroke-linejoin="round"/>
  <path d="M136 200h128M136 300h128" stroke="{W}" stroke-width="6" opacity=".5"/>
  <path d="M136 330h128v30c0 10-8 18-18 18h-92c-10 0-18-8-18-18z" fill="{G}"/>
  <text x="200" y="272" text-anchor="middle" font-family="Oswald" font-weight="700" font-size="76" fill="{W}">9 %</text>''',
 'heat': f'''
  <circle cx="290" cy="110" r="52" fill="{R}"/>
  <g stroke="{R}" stroke-width="10" stroke-linecap="round"><line x1="290" y1="22" x2="290" y2="40"/><line x1="290" y1="180" x2="290" y2="198"/>
  <line x1="202" y1="110" x2="220" y2="110"/><line x1="360" y1="110" x2="378" y2="110"/><line x1="228" y1="48" x2="240" y2="60"/>
  <line x1="352" y1="48" x2="340" y2="60"/><line x1="228" y1="172" x2="240" y2="160"/><line x1="352" y1="172" x2="340" y2="160"/></g>
  <path d="M110 60a40 40 0 0 1 80 0v196a64 64 0 1 1-80 0z" fill="none" stroke="{W}" stroke-width="10"/>
  <rect x="136" y="120" width="28" height="160" rx="12" fill="{R}"/><circle cx="150" cy="306" r="42" fill="{R}"/>
  <g stroke="{W}" stroke-width="6"><line x1="196" y1="100" x2="216" y2="100"/><line x1="196" y1="150" x2="216" y2="150"/><line x1="196" y1="200" x2="216" y2="200"/></g>''',
 'fridge': f'''
  <rect x="110" y="30" width="180" height="340" rx="22" fill="{G}" stroke="{W}" stroke-width="10"/>
  <line x1="110" y1="150" x2="290" y2="150" stroke="{W}" stroke-width="10"/>
  <rect x="130" y="80" width="12" height="44" rx="6" fill="{W}"/><rect x="130" y="176" width="12" height="70" rx="6" fill="{W}"/>
  <path d="M250 196 l-30 52 h26 l-22 52" fill="none" stroke="#FFD24A" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
  <line x1="60" y1="60" x2="340" y2="340" stroke="{R}" stroke-width="12" stroke-linecap="round"/>''',
 'drop': f'''
  <path d="M200 30C200 30 80 170 80 250a120 120 0 0 0 240 0C320 170 200 30 200 30z" fill="{G}" stroke="{W}" stroke-width="10"/>
  <path d="M136 250a64 64 0 0 0 52 62" fill="none" stroke="{W}" stroke-width="10" stroke-linecap="round"/>
  <g fill="{W}"><circle cx="220" cy="200" r="9"/><circle cx="252" cy="236" r="9"/><circle cx="236" cy="276" r="9"/></g>''',
 'mosquito': f'''
  <ellipse cx="200" cy="200" rx="34" ry="90" fill="{W}"/><circle cx="200" cy="96" r="30" fill="{W}"/>
  <line x1="200" y1="96" x2="200" y2="20" stroke="{W}" stroke-width="8" stroke-linecap="round"/>
  <g fill="{G}" opacity=".95"><ellipse cx="120" cy="160" rx="80" ry="30" transform="rotate(-25 120 160)"/><ellipse cx="280" cy="160" rx="80" ry="30" transform="rotate(25 280 160)"/></g>
  <g stroke="{W}" stroke-width="7" fill="none" stroke-linecap="round"><path d="M176 220 l-70 40 l-20 60"/><path d="M224 220 l70 40 l20 60"/><path d="M180 180 l-80 0 l-40 -30"/><path d="M220 180 l80 0 l40 -30"/></g>
  <g fill="#141816"><rect x="186" y="170" width="28" height="10"/><rect x="186" y="210" width="28" height="10"/><rect x="186" y="250" width="28" height="10"/></g>
  <path d="M40 360 q40 -24 80 0 t80 0 t80 0 t80 0" fill="none" stroke="{R}" stroke-width="10" stroke-linecap="round"/>''',
 'smoke': f'''
  <path d="M110 300h180l-20 70h-140z" fill="{G}" stroke="{W}" stroke-width="10" stroke-linejoin="round"/>
  <g fill="{R}"><path d="M150 300c-10-30 20-40 10-70 30 20 30 50 20 70z"/><path d="M200 300c-14-40 26-50 12-90 40 26 34 66 22 90z"/><path d="M246 300c-8-26 16-34 8-60 26 18 26 44 18 60z"/></g>
  <g fill="none" stroke="{W}" stroke-width="10" stroke-linecap="round" opacity=".8"><path d="M170 200c-30-30 30-50 0-90s30-60 0-90"/><path d="M230 190c-30-30 30-50 0-90s30-50 10-80"/></g>''',
'compost': f"""
  <path d="M90 150h220l-24 220H114z" fill="{G}" stroke="{W}" stroke-width="10" stroke-linejoin="round"/>
  <rect x="70" y="122" width="260" height="30" rx="8" fill="{W}"/>
  <g fill="none" stroke="{W}" stroke-width="9" stroke-linecap="round"><path d="M200 330c-40-40-40-100 0-140 40 40 40 100 0 140z"/><path d="M200 330v-120"/></g>
  <path d="M150 90c0-30 30-50 50-56M250 90c0-30-30-50-50-56" fill="none" stroke="{GL}" stroke-width="9" stroke-linecap="round"/>
  <circle cx="200" cy="30" r="14" fill="{R}"/>""",
 'cholera': f"""
  <path d="M200 30C200 30 90 160 90 236a110 110 0 0 0 220 0C310 160 200 30 200 30z" fill="{G}" stroke="{W}" stroke-width="10"/>
  <rect x="180" y="170" width="40" height="130" rx="8" fill="{W}"/><rect x="135" y="215" width="130" height="40" rx="8" fill="{W}"/>
  <text x="200" y="400" text-anchor="middle" font-family="Oswald" font-weight="700" font-size="44" fill="{R}">SRO</text>""",
 'burn': f"""
  <path d="M120 60h110v40h-40v30h-30v-30h-40z" fill="{W}"/><rect x="226" y="52" width="60" height="22" rx="8" fill="{W}"/>
  <g fill="#7FC8F8"><path d="M175 150c-12 20-12 30 0 34 12-4 12-14 0-34z"/><path d="M175 205c-12 20-12 30 0 34 12-4 12-14 0-34z"/><path d="M175 260c-12 20-12 30 0 34 12-4 12-14 0-34z"/></g>
  <path d="M90 330c40-30 120-40 220-20v60H90z" fill="{G}" stroke="{W}" stroke-width="10" stroke-linejoin="round"/>
  <path d="M290 250c-16-30 14-44 4-74 30 20 32 56 18 74z" fill="{R}"/>""",
 'lamp': f"""
  <circle cx="300" cy="96" r="44" fill="#FFD24A"/>
  <g stroke="#FFD24A" stroke-width="9" stroke-linecap="round"><line x1="300" y1="22" x2="300" y2="36"/><line x1="300" y1="156" x2="300" y2="170"/><line x1="226" y1="96" x2="240" y2="96"/><line x1="360" y1="96" x2="374" y2="96"/><line x1="248" y1="44" x2="258" y2="54"/><line x1="352" y1="44" x2="342" y2="54"/></g>
  <path d="M90 150a50 30 0 0 1 100 0" fill="none" stroke="{W}" stroke-width="10"/>
  <rect x="96" y="150" width="88" height="20" rx="6" fill="{W}"/>
  <path d="M104 170h72l14 120H90z" fill="none" stroke="{W}" stroke-width="10" stroke-linejoin="round"/>
  <path d="M140 270c-14-26 10-40 0-66 26 18 28 48 14 66z" fill="{R}"/>
  <rect x="80" y="290" width="120" height="70" rx="12" fill="{R}"/>
  <line x1="40" y1="370" x2="240" y2="150" stroke="{W}" stroke-width="12" stroke-linecap="round"/>
  <rect x="250" y="210" width="96" height="150" rx="16" fill="{G}" stroke="{W}" stroke-width="10"/>
  <g stroke="{W}" stroke-width="5"><line x1="266" y1="246" x2="330" y2="246"/><line x1="266" y1="276" x2="330" y2="276"/><line x1="298" y1="226" x2="298" y2="300"/></g>""",
 'co': f"""
  <path d="M60 200L200 80l140 120" fill="none" stroke="{W}" stroke-width="12" stroke-linejoin="round"/>
  <rect x="96" y="190" width="208" height="180" fill="none" stroke="{W}" stroke-width="10"/>
  <path d="M130 330h80l-10 30h-60z" fill="{G}"/>
  <g fill="{R}"><path d="M150 330c-8-20 14-28 6-50 22 14 22 36 14 50z"/><path d="M182 330c-6-16 10-22 4-40 18 12 18 28 12 40z"/></g>
  <circle cx="250" cy="250" r="48" fill="#58615C" opacity=".85"/><circle cx="210" cy="230" r="34" fill="#58615C" opacity=".85"/>
  <text x="240" y="272" text-anchor="middle" font-family="Oswald" font-weight="700" font-size="58" fill="{W}">CO</text>""",
 'rat': f"""
  <path d="M30 330q90 -30 170 0t170 0" fill="none" stroke="#7FC8F8" stroke-width="10" stroke-linecap="round"/>
  <path d="M30 370q90 -30 170 0t170 0" fill="none" stroke="#7FC8F8" stroke-width="10" stroke-linecap="round" opacity=".6"/>
  <ellipse cx="190" cy="230" rx="110" ry="62" fill="{W}"/>
  <path d="M290 210l70 30-70 26z" fill="{W}"/>
  <circle cx="276" cy="176" r="26" fill="{W}"/><circle cx="276" cy="176" r="13" fill="{R}"/>
  <circle cx="320" cy="226" r="7" fill="#141816"/><circle cx="360" cy="240" r="8" fill="{R}"/>
  <path d="M82 236c-60 0-60 70-10 80" fill="none" stroke="{W}" stroke-width="9" stroke-linecap="round"/>
  <g stroke="{W}" stroke-width="10" stroke-linecap="round"><line x1="140" y1="286" x2="134" y2="306"/><line x1="240" y1="286" x2="246" y2="306"/></g>""",
 'net': f"""
  <path d="M200 30L70 300h260z" fill="{G}" opacity=".35"/>
  <path d="M200 30L70 300M200 30L330 300M200 30L160 300M200 30L240 300" fill="none" stroke="{W}" stroke-width="5"/>
  <g stroke="{W}" stroke-width="4" opacity=".8"><line x1="133" y1="170" x2="267" y2="170"/><line x1="110" y1="220" x2="290" y2="220"/><line x1="90" y1="262" x2="310" y2="262"/></g>
  <rect x="50" y="300" width="300" height="40" rx="10" fill="{W}"/><rect x="60" y="340" width="20" height="40" fill="{W}"/><rect x="320" y="340" width="20" height="40" fill="{W}"/>
  <rect x="80" y="280" width="90" height="24" rx="10" fill="{R}"/>
  <circle cx="200" cy="26" r="12" fill="{R}"/>""",
 'haiti': f"""
  <rect x="44" y="40" width="12" height="350" rx="6" fill="{W}"/>
  <image href="ht.svg" x="56" y="50" width="300" height="225" preserveAspectRatio="none"/>
  <circle cx="300" cy="320" r="62" fill="{GL}"/>
  <text x="300" y="350" text-anchor="middle" font-family="Oswald" font-weight="700" font-size="92" fill="#141816">?</text>""",
}
