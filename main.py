import functions.transform_ana_to_csv as trs
from functions.tema1 import tema1
from functions.comp import compare
from functions.tema2 import tema2, objective
from functions.tema3 import tema3

def main():
    
    trs.transform('./databases/95/AUDI95.ANA','95')
    trs.transform('./databases/2021/AUDI2021.ANA','2021')

    tema1(95)
    tema1(2021)
    

    tema2(95, 10)
    tema2(2021, 11)

    tema3(95)
    tema3(2021)


if __name__ == "__main__":
    main()