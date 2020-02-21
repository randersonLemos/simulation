import datetime
import dateutil.relativedelta as relativedelta
import calendar
import pandas

class Simtime:
    def __init__(self,  bgn_date, end_date, ref_time):
        self.bgn_date = datetime.date(*bgn_date)
        self.end_date = datetime.date(*end_date)
        self.ref_time = ref_time

    def simtime(self):
        return self._build()

    def _build(self):
        cur_date = self.bgn_date
        cur_time = self.ref_time
        days = 0
        lst = []
        while cur_date <= self.end_date:
            cur_time += days
            lst.append('*TIME {} ** DATE {}'.format(cur_time, cur_date))
            nxt_month = cur_date.month + 1
            nxt_year = cur_date.year
            if nxt_month == 13:
                nxt_month = 1
                nxt_year += 1
            _, days = calendar.monthrange(nxt_year, nxt_month)
            cur_date += datetime.timedelta(days=days)
        lst.insert(0, '*WSRF GRID TNEXT')
        lst.insert(int(len(lst)/2), '*WSRF GRID TNEXT')
        lst.insert(-1,  '*WSRF GRID TNEXT')
        return '\n'.join(lst)
