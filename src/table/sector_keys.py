class Sector_Keys:
    @staticmethod
    def time(): return 'TIME'

    @staticmethod
    def date(): return 'DATE'

    @staticmethod
    #def sector(): return 'SECTOR'
    def sector(): return 'FIELD'

    @staticmethod
    def recovery_factor(): return 'FIELD RECOVERY FACTOR'

    @staticmethod
    def avg_pressure(): return 'FIELD AVG PRESSURE'

    @staticmethod
    def oil_prod_sc(): return 'FIELD OIL PROD CUMU SC'

    @staticmethod
    def oil_prod_dot_sc(): return 'FIELD OIL PROD RATE SC'

    @staticmethod
    def gas_prod_sc(): return 'FIELD GAS PROD CUMU SC'

    @staticmethod
    def gas_prod_dot_sc(): return 'FIELD GAS PROD RATE SC'

    @staticmethod
    def wat_prod_sc(): return 'FIELD WATER PROD CUMU SC'

    @staticmethod
    def wat_prod_dot_sc(): return 'FIELD WATER PROD RATE SC'

    @staticmethod
    def liq_prod_sc(): return 'FIELD LIQ PROD CUMU SC'

    @staticmethod
    def liq_prod_dot_sc(): return 'FIELD LIQ PROD RATE SC'

    @staticmethod
    def oil_inje_sc(): return 'FIELD OIL INJE CUMU SC'

    @staticmethod
    def oil_inje_dot_sc(): return 'FIELD OIL INJE RATE SC'

    @staticmethod
    def gas_inje_sc(): return 'FIELD GAS INJE CUMU SC'

    @staticmethod
    def gas_inje_dot_sc(): return 'FIELD GAS INJE RATE SC'

    @staticmethod
    def wat_inje_sc(): return 'FIELD WATER INJE CUMU SC'

    @staticmethod
    def wat_inje_dot_sc(): return 'FIELD WATER INJE RATE SC'

    @staticmethod
    def liq_inje_sc(): return 'FIELD LIQ INJE CUMU SC'

    @staticmethod
    def liq_inje_dot_sc(): return 'FIELD LIQ INJE RATE SC'

    @staticmethod
    def gor_sc(): return 'FIELD GOR SC'

    @staticmethod
    def wat_cut_sc(): return 'FIELD WCUT SC'