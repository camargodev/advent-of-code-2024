from src.part_1.GuardRouteMapper import Guardroutemapper as FirstGuardroutemapper
from src.part_2.GuardRouteMapper import Guardroutemapper as SecondGuardroutemapper

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_6/res/input.txt", "r")]
    print(FirstGuardroutemapper().map(lines))
    print(SecondGuardroutemapper().map(lines))
