from lib import greet, add_numbers


def main():
    print(greet("Egor"))
    print(f"Сума: {add_numbers(5, 7)}")
from lib import say_hello

print(say_hello("Egor"))

if __name__ == "__main__":
    main()