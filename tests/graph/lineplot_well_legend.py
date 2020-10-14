def update_legend(is_visible=True):
    if is_visible:
        Leg = plt.legend().get_texts()
        Leg[0].set_text('METH.')
        for leg, tex in zip(Leg[1:], ['REF', 'WSS', 'NSS', 'BSS']):
            leg.set_text(tex)
    else:
        plt.legend().set_visible(is_visible)


from header import *
from simulation.table.well_graph import Well_Graph

Tables = Get_tables('list.tables')
for tables in Tables: tables.date_range(ini='2020')

wg = Well_Graph(Tables)

for well in prod_lst:
    #ROOT = pathlib.Path('./fig/{}'.format(well))
    ROOT = pathlib.Path('/home/pamonha/Shared/20200730 - Encontro EQNR/images/{}'.format(well))
    ROOT.mkdir(parents=True, exist_ok=True)

    wg.oil_prod(well); update_legend(); plt.savefig(ROOT / 'oil-prod.png'); plt.close()
    wg.gas_prod(well); update_legend(False); plt.savefig(ROOT / 'gas-prod.png'); plt.close()
    wg.wat_prod(well); update_legend(False); plt.savefig(ROOT / 'wat-prod.png'); plt.close()
    wg.wcut(well); update_legend(False); plt.savefig(ROOT / 'wcut.png'); plt.close()
    wg.gor(well); update_legend(False); plt.savefig(ROOT / 'gor.png'); plt.close()
    wg.bhp(well); update_legend(False); plt.savefig(ROOT / 'bhp.png'); plt.close()

    wg.oil_prod_dot(well); update_legend(); plt.savefig(ROOT / 'oil-prod-rate.png'); plt.close()
    wg.gas_prod_dot(well); update_legend(False); plt.savefig(ROOT / 'gas-prod-rate.png'); plt.close()
    wg.wat_prod_dot(well); update_legend(False); plt.savefig(ROOT / 'wat-prod-rate.png'); plt.close()
