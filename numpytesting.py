import numpy as np

moviechance = np.array(
                        [0.6,0.1]
                        )

parkchance = np.array(
                        [0.3,0.2]
                        )

chorechance = np.array(
                        [0.1,0.7]
                        )

class Yourfuture:
    def __init__(self, movie, park, chores, hwchancetoday):
        self.movie = movie
        self.park = park
        self.chores = chores
        
        self.futuremovie = self.calcfuture(hwchancetoday)[0]
        self.futurepark = self.calcfuture(hwchancetoday)[1]
        self.futurechores = self.calcfuture(hwchancetoday)[2]
        
    def calcfuture(self, hwchance):
        todaymovie = hwchance @ moviechance
        todaypark = hwchance @ parkchance
        todaychore = hwchance @ chorechance
        
        return todaymovie,todaypark,todaychore

hw_chances = [0.8,0.2]

tomorrow = Yourfuture(moviechance, parkchance, chorechance, hw_chances)
print("Chances of going to a movie: ",tomorrow.futuremovie)
print("Chances of going to the park: ",tomorrow.futurepark)
print("Chances of doing chores: ", tomorrow.futurechores)

