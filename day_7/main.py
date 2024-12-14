from src.part_1.CalculationManager import Calculationmanager as FirstCalculationmanager
from src.part_2.CalculationManager import Calculationmanager as SecondCalculationmanager

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_7/res/input.txt", "r")]
    print(FirstCalculationmanager().calculate(lines))
    print(SecondCalculationmanager().calculate(lines))
