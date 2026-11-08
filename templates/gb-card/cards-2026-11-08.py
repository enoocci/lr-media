# G&B cards for Sun 8 -> Sat 14 Nov 2026. Usage: python3 cards-2026-11-08.py <out_dir>
import sys, gb
FOL_NBA = '🔔 Suivez Goals &amp; Buckets pour toute la saison NBA'
FOL_FOOT = '🔔 Suivez Goals &amp; Buckets pour le foot du monde entier'
C = {}

def std(flash, title, sub, rows, q, opts, fol, extra=''):
    return (f'<div><span class="flash">{flash}</span></div><div class="dv">{title}</div><div class="sub">{sub}</div>'
            + gb.clues(rows) + extra + f'<div class="q2">{q}</div>' + (gb.ops(*opts) if opts else '') + f'<div class="fol">{fol}</div>')

# Sun 8 13:00 - DEVINE #4 (Jokic)
C['gb-devine-4'] = gb.page('Le jeu de la semaine', std('Devine le joueur #4', 'Qui <em>suis-je ?</em>', '4 indices · Basket', [
    ('1', 'Je suis né en Serbie en février 1995.'),
    ('2', "J'ai été choisi au 41<sup>e</sup> rang de la draft NBA 2014."),
    ('3', "J'ai été élu MVP de la NBA en 2021, 2022 et 2024."),
    ('4', 'Champion NBA et MVP des Finales 2023 avec Denver.')],
    'Votre réponse <em>en commentaire</em> 👇', None, '🔔 Suivez Goals &amp; Buckets · Réponse jeudi',
    '') .replace('<div class="q2">', '<div class="q2">', 1).replace('<div class="fol">', '<div class="ans">Réponse du #3 : Victor Wembanyama ✅</div><div class="fol">'),
    '<div class="qm">?</div>')

# Sun 8 20:00 - LE CHIFFRE 81 (Kobe)
C['gb-chiffre-kobe-81'] = gb.page('NBA · Record', '<div><span class="flash">LE CHIFFRE</span></div><div class="hn">81</div>'
    '<div class="sub">points en un match · Kobe Bryant</div>' + gb.clues([
    ('22 janv. 2006', 'Lakers 122–104 Toronto Raptors.'),
    ('28 / 46', 'Tirs réussis, dont 7 à 3 points, et 18 lancers francs sur 20.'),
    ('55', 'Points en 2<sup>e</sup> mi-temps. Les Lakers étaient menés de 18 points.'),
    ('3<sup>e</sup>', "Plus gros total de l'histoire, derrière Chamberlain (100) et Bam Adebayo (83, en 2026).")]) +
    '<div class="q2">Le plus fort <em>des trois ?</em> 👇</div>' + gb.ops('Wilt 100', 'Bam 83', 'Kobe 81') + f'<div class="fol">{FOL_NBA}</div>')

# Mon 9 13:00 - LE PROFIL Melchie Dumornay
C['gb-profil-dumornay'] = gb.page('Grenadières · Haïti', std('Le profil', 'Melchie <em>Dumornay</em>', 'Milieu · née à Mirebalais · OL Lyonnes', [
    ('2003', 'Née le 17 août à Mirebalais. Son surnom : « Corventina ».'),
    ('2023', 'Doublé contre le Chili (2–1) : les Grenadières vont à leur 1<sup>er</sup> Mondial.'),
    ('2 fois', 'Meilleure jeune joueuse de la Ligue des champions (2023-24, 2024-25).'),
    ('4<sup>e</sup>', "Au Ballon d'Or 2026, après une 18<sup>e</sup> place en 2025.")],
    "Le Ballon d'Or, <em>c'est pour quand ?</em> 👇", ('2027', 'Un jour', 'Elle le mérite'),
    '🔔 Suivez Goals &amp; Buckets pour toutes les Grenadières'), '<div class="yr">HT</div>')

# Mon 9 20:00 - TOP 5 buteurs Coupe du monde
C['gb-top5-buteurs-mondial'] = gb.page('Coupe du monde · Histoire', '<div><span class="flash">TOP 5</span></div>'
    '<div class="dv">Les rois <em>du Mondial</em></div><div class="sub">Buts en Coupe du monde · après 2026</div>' + gb.top5([
    ('Kylian Mbappé', 'France', 22), ('Lionel Messi', 'Argentine', 21), ('Miroslav Klose', 'Allemagne', 16),
    ('Ronaldo', 'Brésil', 15), ('G. Müller · H. Kane', 'Allemagne · Angleterre', 14)], 'buts') +
    "<div class=\"note2\">⚽ Mondial 2026 : 10 buts pour Mbappé, 1<sup>er</sup> à gagner deux fois le Soulier d'or (2022, 2026).</div>"
    '<div class="q2">Mbappé finira <em>à combien ?</em> 👇</div>' + gb.ops('Moins de 25', '25 à 29', '30 et plus') +
    f'<div class="fol">{FOL_FOOT}</div>', css='.mid{top:120px;bottom:165px}.dv{font-size:100px}.r5{min-height:72px;padding:4px 24px}.r5 .nm b{font-size:37px}.r5 .nm span{font-size:23px;line-height:1.15}.top5{gap:9px}.q2{margin-top:18px}.note2{font-size:26px;margin-top:16px}')

# Tue 10 13:00 - LE DUEL Hakeem vs Shaq
C['gb-duel-hakeem-shaq'] = gb.page('NBA · Légendes', '<div><span class="flash">LE DUEL</span></div>'
    '<div class="dv">Hakeem <em>vs</em> Shaq</div><div class="sub">Deux pivots de légende · carrière</div>' +
    gb.duel('Hakeem', 'Shaq', [('2', 'Titres NBA', '4'), ('1', 'MVP', '1'), ('2', 'MVP des Finales', '3'),
                              ('21,8', 'Points / match', '23,7'), ('11,1', 'Rebonds / match', '10,9'), ('3,1', 'Contres / match', '2,3')]) +
    "<div class=\"note2\">🏀 Finales 1995 : Houston (Hakeem) balaie Orlando (Shaq) 4–0. Hakeem, né à Lagos, reste le meilleur contreur de l'histoire : 3 830.</div>"
    '<div class="q2">Votre pivot ? <em>👇</em></div>' + gb.ops('Hakeem', 'Shaq', 'Les deux') + f'<div class="fol">{FOL_NBA}</div>', css='.mid{top:120px;bottom:175px}.du td{font-size:44px}.du td.l{font-size:22px}.note2{font-size:26px;margin-top:14px}.du{margin-top:14px}')

# Tue 10 20:00 - LE DÉBAT meilleur Africain
C['gb-debat-africain'] = gb.page('Le Débat', std('Le débat', 'Le meilleur <em>Africain</em>', "de l'histoire du foot · à vous de voter", [
    ('A · Weah', "Ballon d'Or 1995 : le seul Africain sacré. Plus tard président du Liberia."),
    ("B · Eto'o", "4 fois Joueur africain de l'année : 2003, 2004, 2005 et 2010."),
    ('C · Drogba', "2 fois Joueur africain de l'année. Héros de Chelsea, champion d'Europe 2012."),
    ('D · Salah', "2 fois Joueur africain de l'année (2017, 2018), avec Liverpool.")],
    'Votre choix : <em>A, B, C ou D ?</em> 👇', None, FOL_FOOT), '<div class="qm">?</div>', '.dv{line-height:1.14}.mid{top:120px}')

# Wed 11 13:00 - CE JOUR-LÀ Tony Parker n°9
C['gb-cejour-parker'] = gb.page('NBA · France', std('Ce jour-là', '11 novembre <em>2019</em>', 'Les Spurs retirent le n°9 de Tony Parker', [
    ('4', 'Titres NBA avec San Antonio : 2003, 2005, 2007 et 2014.'),
    ('2007', 'MVP des Finales : 24,5 points par match, 4–0 contre Cleveland.'),
    ('17', 'Saisons aux Spurs, puis une dernière à Charlotte.'),
    ('1 254', 'Matchs NBA : 15,5 points et 5,6 passes de moyenne.')],
    'Le meilleur Français <em>de la NBA ?</em> 👇', ('Parker', 'Gobert', 'Wemby'), FOL_NBA), '<div class="yr">2019</div>')

# Wed 11 20:00 - LE CHIFFRE 15 (Real Madrid)
C['gb-chiffre-real-15'] = gb.page('Foot · Ligue des champions', '<div><span class="flash">LE CHIFFRE</span></div><div class="hn">15</div>'
    '<div class="sub">Ligues des champions · Real Madrid, le record</div>' + gb.clues([
    ('1956-1960', 'Les 5 premières éditions, toutes gagnées par le Real.'),
    ('2024', '15<sup>e</sup> titre : 2–0 contre Dortmund à Wembley.'),
    ('7', 'Titres pour l\'AC Milan, 2<sup>e</sup> club le plus titré.'),
    ('2026', 'Le PSG garde sa couronne, aux tirs au but contre Arsenal.')]) +
    '<div class="q2">Le Real ira <em>jusqu\'à 16 ?</em> 👇</div>' + gb.ops('Cette saison', 'Plus tard', 'Jamais') + f'<div class="fol">{FOL_FOOT}</div>')

# Thu 12 13:00 - DEVINE #5 (Henry)
C['gb-devine-5'] = gb.page('Le jeu de la semaine', std('Devine le joueur #5', 'Qui <em>suis-je ?</em>', '4 indices · Foot', [
    ('1', 'Je suis né en région parisienne en 1977.'),
    ('2', "Champion du monde 1998 et champion d'Europe 2000."),
    ('3', 'En 2003-04, mon club finit le championnat sans perdre un match.'),
    ('4', "228 buts : je suis le meilleur buteur de l'histoire d'Arsenal.")],
    'Votre réponse <em>en commentaire</em> 👇', None, '🔔 Suivez Goals &amp; Buckets · Réponse samedi'
    ).replace('<div class="fol">', '<div class="ans">Réponse du #4 : Nikola Jokić ✅</div><div class="fol">'), '<div class="qm">?</div>')

# Thu 12 20:00 - LE PROFIL SGA
C['gb-profil-sga'] = gb.page('NBA · MVP', std('Le profil', 'Shai <em>Gilgeous-Alexander</em>', "Meneur · né à Toronto · Thunder d'OKC", [
    ('2018', '11<sup>e</sup> choix de la draft (Charlotte), échangé aux Clippers le soir même.'),
    ('2019', "Envoyé à Oklahoma City dans l'échange de Paul George."),
    ('2025', 'Champion NBA, MVP de la saison et MVP des Finales.'),
    ('2026', "2<sup>e</sup> MVP de suite (31,1 pts/match) : 14<sup>e</sup> joueur de l'histoire à le faire.")],
    'Le meilleur joueur NBA <em>actuel ?</em> 👇', ('SGA', 'Jokić', 'Wemby'), FOL_NBA), '<div class="yr">MVP</div>',
    '.dv{font-size:84px}.clues{margin-top:20px}')

# Fri 13 13:00 - CE JOUR-LÀ Haïti 1-0 Costa Rica
C['gb-cejour-haiti-costa-rica'] = gb.page('Grenadiers · Mondial', std('Ce jour-là', '13 novembre <em>2025</em>', 'Haïti 1–0 Costa Rica · qualifs Mondial 2026', [
    ('44<sup>e</sup>', 'Frantzdy Pierrot marque le seul but du match, juste avant la pause.'),
    ('0', 'But encaissé : Johny Placide garde sa cage inviolée.'),
    ('Curaçao', 'Match « à domicile » joué à Willemstad, au stade Ergilio Hato.'),
    ('18 nov.', '5 jours plus tard, 2–0 contre le Nicaragua : Haïti file au Mondial.')],
    'Votre héros <em>de la campagne ?</em> 👇', ('Pierrot', 'Placide', 'Bellegarde'),
    '🔔 Suivez Goals &amp; Buckets pour tous les Grenadiers'), '<div class="yr">2025</div>')

# Fri 13 20:00 - LE DUEL Zidane vs Ronaldo
C['gb-duel-zidane-ronaldo'] = gb.page('Foot · Légendes', '<div><span class="flash">LE DUEL</span></div>'
    '<div class="dv">Zidane <em>vs</em> Ronaldo</div><div class="sub">France – Brésil · deux génies</div>' +
    gb.duel('Zidane', 'Ronaldo', [('1', 'Coupe du monde', '2'), ('1', "Ballon d'Or", '2'), ('3', 'Joueur FIFA de l\'année', '3'),
                                  ('5', 'Buts en Coupe du monde', '15')]) +
    '<div class="note2">⚽ Finale 1998 : France 3–0 Brésil, avec 2 têtes de Zidane. Finale 2002 : Ronaldo marque 2 fois contre l\'Allemagne.</div>'
    '<div class="q2">Votre légende ? <em>👇</em></div>' + gb.ops('Zidane', 'Ronaldo', 'Les deux') + f'<div class="fol">{FOL_FOOT}</div>', css='.du th{width:26%}.du th:nth-child(2){width:48%}')

# Sat 14 13:00 - LE DÉBAT meilleur entraîneur
C['gb-debat-entraineur'] = gb.page('Le Débat', std('Le débat', 'Le meilleur <em>entraîneur</em>', "de l'histoire du foot · à vous de voter", [
    ('A · Ancelotti', '5 Ligues des champions, le record : Milan 2003, 2007 · Real 2014, 2022, 2024.'),
    ('B · Ferguson', '13 titres de Premier League et 2 C1 (1999, 2008) avec Manchester United.'),
    ('C · Guardiola', '3 C1 (Barça 2009, 2011 · City 2023) et 6 titres de Premier League.'),
    ('D · Zidane', 'Le seul à gagner 3 C1 de suite : 2016, 2017, 2018 avec le Real.')],
    'Votre choix : <em>A, B, C ou D ?</em> 👇', None, FOL_FOOT), '<div class="qm">?</div>', '.dv{line-height:1.14}.mid{top:120px}')

# Sat 14 20:00 - TOP 5 Ballon d'Or
C['gb-top5-ballon-or'] = gb.page('Foot · Histoire', '<div><span class="flash">TOP 5</span></div>'
    "<div class=\"dv\">Rois du <em>Ballon d'Or</em></div><div class=\"sub\">Ballons d'Or remportés</div>" + gb.top5([
    ('Lionel Messi', '2009 → 2023', 8), ('Cristiano Ronaldo', '2008 → 2017', 5), ('Johan Cruyff', '1971 → 1974', 3),
    ('Michel Platini', '1983 → 1985', 3), ('Marco van Basten', '1988 → 1992', 3)], '') +
    "<div class=\"note2\">🏆 2026 : Harry Kane gagne son 1<sup>er</sup> Ballon d'Or, devant Kylian Mbappé et Lamine Yamal.</div>"
    '<div class="q2">Le prochain <em>multiple vainqueur ?</em> 👇</div>' + gb.ops('Mbappé', 'Yamal', 'Kane') + f'<div class="fol">{FOL_FOOT}</div>', css='.mid{top:120px;bottom:165px}.dv{font-size:100px}.r5{min-height:72px;padding:4px 24px}.r5 .nm b{font-size:37px}.r5 .nm span{font-size:23px;line-height:1.15}.top5{gap:9px}.q2{margin-top:18px}.note2{font-size:26px;margin-top:16px}')

if __name__ == '__main__':
    only = sys.argv[2:]
    gb.build({k: v for k, v in C.items() if not only or k in only}, sys.argv[1])
