import geometry
import sets
import statistics 
import trignometry
import algebra
switcher={
    1:algebra.main,
    2:trignometry.main,
    3:geometry.main,
    4:statistics.main,
    5:sets.main,
}
def invalid():
    print("I cannot do that, Please retry")
    return main()
           

def main():
    print("Welcome to Math Genie.")
    print("Which problem do you want me to solve")
    print("Select Subject")
    print("1. Algebra")
    print("2. Trignometry")
    print("3. Geometry")
    print("4. Statistics")
    print("5. Sets & Relations")
    choice=int(input("Enter the Subject Number"))
    func=switcher.get(choice,"invalid")
    func()
    return 

if __name__=="__main__":
    main()

