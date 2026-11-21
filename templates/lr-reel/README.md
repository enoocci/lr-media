# lr-reel — « L'ACTU EN 30 SECONDES »
`node templates/lr-reel/render-reel.js <config.json> <out.mp4>` (depuis la racine du dépôt).
1080x1920, 30 fps, ~26 s : hook 2,5 s + 4 écrans × 4,6 s + écran final A/B/C 5,5 s.
Bande CTA « 🔔 Abonnez-vous » dès 3 s, bande logo en bas, musique coupée/fade/loudnorm -14 LUFS.
Images de contrôle `*-chk-<frame>.jpg` écrites à côté de la sortie. Exemples de config dans `exemples/`.
