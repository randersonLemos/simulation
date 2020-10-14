def update_legend(is_visible=True):
    if is_visible:
        Leg = plt.legend().get_texts()
        Leg[0].set_text('METH.')
        for leg, tex in zip(Leg[1:], ['REF', 'WSS', 'NSS', 'BSS']):
            leg.set_text(tex)
    else:
        plt.legend().set_visible(is_visible)


from header import *
from simulation.table.sector_graph import Sector_Graph

Tables = Get_tables('list.tables')
for tables in Tables: tables.date_range(ini='2020')

sg = Sector_Graph(Tables)

#ROOT = pathlib.Path('./fig/field')
ROOT = pathlib.Path('/home/pamonha/Shared/20200730 - Encontro EQNR/images/field')
ROOT.mkdir(parents=True, exist_ok=True)

sg.oil_prod(); update_legend(); plt.savefig(ROOT / 'field-oil-prod.png', bbox_inches='tight', pad_inches=0.040); plt.close()
sg.gas_prod(); update_legend(False); plt.savefig(ROOT / 'field-gas-prod.png', bbox_inches='tight', pad_inches=0.040); plt.close()
sg.wat_prod(); update_legend(); plt.savefig(ROOT / 'field-wat-prod.png', bbox_inches='tight', pad_inches=0.040); plt.close()
sg.gas_inje(); update_legend(False); plt.savefig(ROOT / 'field-gas-inje.png', bbox_inches='tight', pad_inches=0.040); plt.close()
sg.wat_inje(); update_legend(False); plt.savefig(ROOT / 'field-wat-inje.png', bbox_inches='tight', pad_inches=0.040); plt.close()

sg.oil_prod_dot(); update_legend(); plt.savefig(ROOT / 'field-oil-prod-dot.png', bbox_inches='tight', pad_inches=0.010); plt.close()
sg.gas_prod_dot(); update_legend(False); plt.savefig(ROOT / 'field-gas-prod-dot.png', bbox_inches='tight', pad_inches=0.010); plt.close()
sg.wat_prod_dot(); update_legend(); plt.savefig(ROOT / 'field-wat-prod-dot.png', bbox_inches='tight', pad_inches=0.010); plt.close()
sg.gas_inje_dot(); update_legend(False); plt.savefig(ROOT / 'field-gas-inje-dot.png', bbox_inches='tight', pad_inches=0.010); plt.close()
sg.wat_inje_dot(); update_legend(False); plt.savefig(ROOT / 'field-wat-inje-dot.png', bbox_inches='tight', pad_inches=0.010); plt.close()

sg.avg_pres(); update_legend(False); plt.savefig(ROOT / 'field-avg-pres.png', bbox_inches='tight', pad_inches=0.010); plt.close()
