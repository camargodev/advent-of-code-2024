from src.part_1.MemoryMultiplier import Memorymultiplier as FirstMemorymultiplier
from src.part_2.MemoryMultiplier import Memorymultiplier as SecondMemorymultiplier

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_3/res/input.txt", "r")]
    print(FirstMemorymultiplier().multiply(lines))
    print(SecondMemorymultiplier().multiply(lines))
