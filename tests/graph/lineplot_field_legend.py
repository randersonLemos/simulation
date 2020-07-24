def update_legend():
    Leg = plt.legend().get_texts()
    Leg[0].set_text('Methodology')
    for leg, tex in zip(Leg[1:], ['REF', 'WSS', 'NSS', 'BSS']):
        leg.set_text(tex)

from header import *
from simulation.table.sector_graph import Sector_Graph

Tables = Get_tables('list.tables')
for tables in Tables: tables.date_range(ini='2020')

sg = Sector_Graph(Tables)

ROOT = pathlib.Path('./fig/field')
ROOT.mkdir(parents=True, exist_ok=True)

sg.oil_prod(); update_legend(); plt.savefig(ROOT / 'field-oil-prod.png'); plt.close()
sg.gas_prod(); update_legend(); plt.savefig(ROOT / 'field-gas-prod.png'); plt.close()
sg.wat_prod(); update_legend(); plt.savefig(ROOT / 'field-wat-prod.png'); plt.close()
sg.gas_inje(); update_legend(); plt.savefig(ROOT / 'field-gas-inje.png'); plt.close()
sg.wat_inje(); update_legend(); plt.savefig(ROOT / 'field-wat-inje.png'); plt.close()

sg.oil_prod_dot(); update_legend(); plt.savefig(ROOT / 'field-oil-prod-dot.png'); plt.close()
sg.gas_prod_dot(); update_legend(); plt.savefig(ROOT / 'field-gas-prod-dot.png'); plt.close()
sg.wat_prod_dot(); update_legend(); plt.savefig(ROOT / 'field-wat-prod-dot.png'); plt.close()
sg.gas_inje_dot(); update_legend(); plt.savefig(ROOT / 'field-gas-inje-dot.png'); plt.close()
sg.wat_inje_dot(); update_legend(); plt.savefig(ROOT / 'field-wat-inje-dot.png'); plt.close()

sg.avg_pres(); update_legend(); plt.savefig(ROOT / 'field-avg-pres.png'); plt.close()
