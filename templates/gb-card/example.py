# Example: rebuild of the published Dalembert profile card (Oct 21 2026) to check the template.
import gb
body = '''<div><span class="flash">LE PROFIL</span></div>
<div class="dv">Samuel <em>Dalembert</em></div>
<div class="sub">Pivot · né à Port-au-Prince · 2,11 m</div>
''' + gb.clues([('2001', 'Drafté en 26e position par les 76ers, après Seton Hall.'),
                ('886', 'Matchs NBA en 13 saisons, avec 6 équipes (dont les Knicks).'),
                ('1,7', 'Contre par match en carrière, avec 7,7 points et 7,8 rebonds.'),
                ('2010', "Après le séisme, il aide Haïti : 100&nbsp;000&nbsp;$ à l'UNICEF et le prix J. Walter Kennedy.")]) + '''
<div class="q2">Un Haïtien en NBA, <em>vous saviez ?</em> 👇</div>''' + gb.ops('Oui', 'Non', "J'en connais d'autres") + '''
<div class="fol">🔔 Suivez Goals &amp; Buckets : le sport avec l'œil haïtien</div>'''
if __name__ == '__main__':
    import sys
    gb.build({'example-profil': gb.page('NBA · Haïti', body, '<div class="yr">HT</div>')}, sys.argv[1] if len(sys.argv) > 1 else gb.BUILD)
