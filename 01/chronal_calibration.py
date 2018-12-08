# Day 1: Chronal Calibration

class Helpers:
    def file_to_list(test_file, datatype=int):
        with open(test_file) as f:
            return [datatype(line) for line in f]
    

class ChronalCalibrator:
    def __init__(self):
        self.frequency = 0
        self.log = {}
        self.adjustments = []
        self.first_repeated = None


    def adjust(self, *adjustments):
        for a in adjustments:
            self.frequency += a
            self.adjustments.append(a)
            self.update_log(self.frequency)


    def update_log(self, frequency):
        if self.log.get(frequency):
            self.log[frequency] += 1
            if not self.first_repeated:
                self.first_repeated = frequency
        else:
            self.log[frequency] = 1
    
    
    def get_first_repeated(self):
        # self.adjustments_writable = False
        
        i = 0
        while not self.first_repeated:
            change = self.adjustments[i]    
            self.adjust(change)
            i += 1

        return self.first_repeated
        


def main():
    print("Day 1: Chronal Calibration")
    adjustments = Helpers.file_to_list("input.txt")
    
    print("\tPart 1:")
    calibrator = ChronalCalibrator()
    calibrator.adjust(*adjustments)
    print(f"\t{calibrator.frequency}")
    
    print("\tPart 2:")
    first_repeated = calibrator.get_first_repeated()
    print(f"\t{first_repeated}")

if __name__ == "__main__":
    main()