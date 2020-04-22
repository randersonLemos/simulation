import time


class RunManager:
    def __init__(self, runs, max_num_alives):
        self.runs = runs
        self.max_num_alives = max_num_alives
        self._alives = []
        
    
    def start(self):
        runs = list(reversed(self.runs))
        while runs:
            if len(self._alives) < self.max_num_alives:
                self._alives.append(runs.pop().run())
                time.sleep(2)
            
            deads = []
            
            for alive in self._alives:
                if not alive.is_alive():
                    deads.append(alive)
                    
            for dead in deads:
                self._alives.remove(dead)
                
   
    def interrupt(self):
        for alive in self._alives:
            alive.kill()               