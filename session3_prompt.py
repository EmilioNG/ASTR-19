Date: "10/09/24"

#define an equation and the value it will return
def f(x):
    return((x ** 3) + 8)

#define the main function in which x will be defined
def main():
    result = f(9)
    print(result)
    if result > 27:
        print("YAY!")
#initialize the code        
if __name__=="__main__":
    main()
