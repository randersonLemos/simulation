def update_legend():
    Leg = plt.legend().get_texts()
    Leg[0].set_text('Methodology')
    for leg, tex in zip(Leg[1:5], ['REF', 'WSS', 'NSS', 'BSS']):
        leg.set_text(tex)

from header import *
from simulation.table.special_graph import Special_Graph

Tables = Get_tables('list.tables')
for tables in Tables: tables.date_range(ini='2020')

sg = Special_Graph(Tables)
for i in range(0, len(prod_zone_lst), 3):
    well = prod_zone_lst[i].split('_')[0]
    ROOT = pathlib.Path('./fig/{}'.format(well))
    ROOT.mkdir(parents=True, exist_ok=True)

    sg.oil_prod(prod_zone_lst[i:i+3]); update_legend(); plt.savefig(ROOT / 'zone-oil-prod.png'); plt.close()
    sg.gas_prod(prod_zone_lst[i:i+3]); update_legend(); plt.savefig(ROOT / 'zone-gas-prod.png'); plt.close()
    sg.wat_prod(prod_zone_lst[i:i+3]); update_legend(); plt.savefig(ROOT / 'zone-wat-prod.png'); plt.close()
    sg.gor(prod_zone_lst[i:i+3]);  update_legend(); plt.savefig(ROOT / 'zone-gor.Png'); plt.close()
    sg.wcut(prod_zone_lst[i:i+3]); update_legend(); plt.savefig(ROOT / 'zone-wcut.png'); plt.close()

    sg.oil_prod_dot(prod_zone_lst[i:i+3]); update_legend(); plt.savefig(ROOT / 'zone-oil-prod-rate.png'); plt.close()
    sg.gas_prod_dot(prod_zone_lst[i:i+3]); update_legend(); plt.savefig(ROOT / 'zone-gas-prod-rate.png'); plt.close()
    sg.wat_prod_dot(prod_zone_lst[i:i+3]); update_legend(); plt.savefig(ROOT / 'zone-wat-prod-rate.png'); plt.close()
