# Modèle d'affiche LR (1080x1350)
- `modele-photo-duo.html` : photo en haut (2 photos + VS), badge de série, titre, 3 boîtes chiffres, question A/B/C, ligne rouge « 🔔 Abonnez-vous », sources, bande logo. Photos : ph-flavio.jpg (Senado Federal / CC BY 2.0), ph-lula.jpg (Ricardo Stuckert / CC BY-SA 4.0).
- `modele-titre-sombre.html` : bandeau sombre en haut (drapeau emoji + grand titre), sans photo. À utiliser quand il n'y a pas de photo libre.
- Copier un modèle dans le même dossier, modifier le texte, puis : `npm i playwright` si besoin (Chromium : /opt/pw-browsers/chromium) et `node render.js $PWD/mon-affiche.html mon-affiche.jpg`.
- Polices : Oswald, IBM Plex Sans Condensed (licence OFL) dans fonts/.
