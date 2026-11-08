# Modèle Goals & Buckets (carte 1080x1350)

Reconstruit en novembre 2026 à partir des cartes publiées (media/2026-10-05 … 2026-10-24), après la perte des fichiers locaux.

- `gb-base.css` : tout le style (marine #0B1F3A, orange #FF7A1A, bleu #7DB4FF, badge rouge #C4232B, rayures, bande Le Rapporteur). Polices : `../lr-card/fonts/` (Oswald, IBM Plex Sans Condensed).
- `gb-logo.png` (logo G&B), `lr-mark-blanc.png` (logo LR blanc).
- `gb.py` : `page(tag, body, deco, css)`, `clues()`, `ops()`, `top5()`, `duel()`, `build(cards, out_dir)`. Le HTML est écrit dans `build/` puis rendu en JPG avec `../lr-card/render.js`.
- `check.js` : `node check.js build/*.html` → hauteur du contenu, marge sous l'en-tête (gapTop doit rester > 10) et au-dessus de la bande LR, nombre de lignes du titre.
- `example.py` : la carte « Le profil · Samuel Dalembert » refaite avec ce modèle.
- `cards-2026-11-08.py` : les 14 cartes du 8 au 14 novembre 2026.

Formats : LE PROFIL, TOP 5, LE DUEL, CE JOUR-LÀ, LE DÉBAT (déco `<div class="qm">?</div>`), LE CHIFFRE (`<div class="hn">81</div>`), DEVINE LE JOUEUR (déco `?`, ligne `<div class="ans">Réponse du #N : …</div>`). Déco année : `<div class="yr">2019</div>`.

Utilisation :
```
cd templates/lr-card && npm i playwright@1   # une seule fois (Chromium : /opt/pw-browsers/chromium, jamais `playwright install`)
cd ../gb-card && python3 cards-2026-11-08.py /chemin/sortie   # option : noms de cartes à rendre
node check.js build/gb-*.html
```
Toujours vérifier chaque JPG à l'œil (débordement, mot orphelin dans le titre, logos visibles). Si le contenu déborde : réduire `.dv` ou passer `css='.mid{top:120px;bottom:165px}'`.
