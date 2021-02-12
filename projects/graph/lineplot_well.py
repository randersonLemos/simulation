from header import *
from simulation.table.well_graph import Well_Graph

Tables = Get_tables('list.tables')
for tables in Tables: tables.date_range(ini='2020')

wg = Well_Graph(Tables)

for well in prod_lst:
    ROOT = pathlib.Path('./fig/{}'.format(well))
    ROOT.mkdir(parents=True, exist_ok=True)

    wg.oil_prod(well); plt.savefig(ROOT / 'oil-prod.png'); plt.close()
    wg.gas_prod(well); plt.savefig(ROOT / 'gas-prod.png'); plt.close()
    wg.wat_prod(well); plt.savefig(ROOT / 'wat-prod.png'); plt.close()
    wg.wcut(well); plt.savefig(ROOT / 'wcut.png'); plt.close()
    wg.gor(well); plt.savefig(ROOT / 'gor.png'); plt.close()
    wg.bhp(well); plt.savefig(ROOT / 'bhp.png'); plt.close()

    wg.oil_prod_dot(well); plt.savefig(ROOT / 'oil-prod-rate.png'); plt.close()
    wg.gas_prod_dot(well); plt.savefig(ROOT / 'gas-prod-rate.png'); plt.close()
    wg.wat_prod_dot(well); plt.savefig(ROOT / 'wat-prod-rate.png'); plt.close()
