# Modèle d'affiche LR (1080x1350)
- `modele-photo-duo.html` : photo en haut (2 photos + VS), badge de série, titre, 3 boîtes chiffres, question A/B/C, ligne rouge « 🔔 Abonnez-vous », sources, bande logo. Photos : ph-flavio.jpg (Senado Federal / CC BY 2.0), ph-lula.jpg (Ricardo Stuckert / CC BY-SA 4.0).
- `modele-titre-sombre.html` : bandeau sombre en haut (drapeau emoji + grand titre), sans photo. À utiliser quand il n'y a pas de photo libre.
- Copier un modèle dans le même dossier, modifier le texte, puis : `npm i playwright` si besoin (Chromium : /opt/pw-browsers/chromium) et `node render.js $PWD/mon-affiche.html mon-affiche.jpg`.
- Polices : Oswald, IBM Plex Sans Condensed (licence OFL) dans fonts/.

## Générateur de cartes evergreen (sans photo) — `gen-series.py`
- `python3 gen-series.py cards-AAAA-MM-JJ.json /chemin/sortie --render [id ...]` → `lr-<id>.html` + `lr-<id>.jpg` (1080x1350). Les HTML pointent vers ce dossier via `<base>` (polices, logo) : les écrire hors du dépôt (scratchpad), ne pas les committer.
- 3 mises en page : `dark` (« LE SAVIEZ-VOUS ? » / cartes pratiques énergie-santé : badge, titre, lede, icône, 3–4 boîtes), `histoire` (série « ILS ONT MARQUÉ L'HISTOIRE » : pays, nom, dates, citation + attribution, 3 dates clés), `chiffre` (« LE CHIFFRE » : grand nombre auto-ajusté + 2 lignes de contexte).
- Icônes SVG maison dans `lr_icons.py` (bulb, quake, bottle, heat, fridge, drop, mosquito, smoke, compost, cholera, burn, lamp, co, rat, net, haiti).
- Automatique : options A/B/C jamais coupées, `Port‑au‑Prince` insécable, nombres + unités insécables. Mettre `&nbsp;` entre les deux derniers mots des titres.
- Exemple complet (semaine du 8 au 14 nov. 2026, avec textes Facebook dans le même JSON) : `cards-2026-11-08.json`.
- Avant : `npm i playwright@1` dans ce dossier si besoin (Chromium : /opt/pw-browsers/chromium, jamais `playwright install`).
