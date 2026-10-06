import multiply

def main():
    a = int(input("a값은 무엇일까요????: "))
    b = int(input("b값은 무엇일까요????: "))
    result = multiply.Power1(a, b)
    print(f"결과: {result}")

if __name__ == "__main__":
    main()