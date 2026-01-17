class Cat:
    def __init__(self, spit, nespit):
        self.is_spit = False
    def start_engine(self):
        if self.is_nespit:
            print("Не спит!")
            return
        self.is_spit = True
        print("Не спит")
    def stop_engine(self):
        if not self.is_running:
            print("Спит!")
            return
        self.is_spit = False
        print("Спит")