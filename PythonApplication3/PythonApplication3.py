import math


def read_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if math.isfinite(value):
                return value
            print("Please enter a finite number.")
        except ValueError:
            print("Please enter a valid number.")


def read_positive(prompt):
    while True:
        value = read_number(prompt)
        if value > 0:
            return value
        print("Please enter a number greater than zero.")


def read_choice(prompt, choices):
    while True:
        choice = input(prompt).strip()
        if choice in choices:
            return choice
        print("Please choose one of: " + ", ".join(choices))


def arithmetic_menu():
    print("\nArithmetic functions")
    first = read_number("Enter first number: ")
    second = read_number("Enter second number: ")
    print("Addition:", first + second)
    print("Subtraction:", first - second)
    print("Multiplication:", first * second)
    if second != 0:
        print("Division:", first / second)
        print("Modulus:", first % second)
    else:
        print("Division and modulus are undefined when the second number is zero.")
    try:
        print("Exponentiation:", first ** second)
    except (OverflowError, ValueError, ZeroDivisionError):
        print("The exponentiation result is undefined or too large.")


def algebra_menu():
    print("""
Algebraic functions
1. Solve a linear equation (a*x + b = 0)
2. Solve a quadratic equation (a*x^2 + b*x + c = 0)
3. Evaluate a quadratic expression (a*x^2 + b*x + c)
0. Return to main menu""")
    choice = read_choice("Choose an option: ", {"0", "1", "2", "3"})

    if choice == "1":
        a = read_number("Enter a: ")
        b = read_number("Enter b: ")
        if a == 0:
            print("There are infinitely many solutions." if b == 0 else "There is no solution.")
        else:
            print("x =", -b / a)
    elif choice == "2":
        a = read_number("Enter a: ")
        b = read_number("Enter b: ")
        c = read_number("Enter c: ")
        if a == 0:
            if b == 0:
                print("There are infinitely many solutions." if c == 0 else "There is no solution.")
            else:
                print("This is linear; x =", -c / b)
        else:
            discriminant = b * b - 4 * a * c
            if discriminant >= 0:
                root = math.sqrt(discriminant)
                print("x1 =", (-b + root) / (2 * a))
                print("x2 =", (-b - root) / (2 * a))
            else:
                real_part = -b / (2 * a)
                imaginary_part = math.sqrt(-discriminant) / abs(2 * a)
                print("x1 =", complex(real_part, imaginary_part))
                print("x2 =", complex(real_part, -imaginary_part))
    elif choice == "3":
        a = read_number("Enter a: ")
        b = read_number("Enter b: ")
        c = read_number("Enter c: ")
        x = read_number("Enter x: ")
        print("Value:", a * x * x + b * x + c)


def read_angle(prompt):
    angle = read_number(prompt)
    unit = read_choice("Use degrees or radians? (d/r): ", {"d", "r"})
    return math.radians(angle) if unit == "d" else angle


def trigonometry_menu():
    print("""
Trigonometric functions
1. Sine, cosine, tangent and reciprocals
2. Inverse trigonometric functions
3. Hyperbolic functions
4. Inverse hyperbolic functions
5. Convert degrees and radians
0. Return to main menu""")
    choice = read_choice("Choose an option: ", {"0", "1", "2", "3", "4", "5"})

    if choice == "1":
        angle = read_angle("Enter the angle: ")
        sine = math.sin(angle)
        cosine = math.cos(angle)
        tangent = math.tan(angle)
        print("Sine:", sine)
        print("Cosine:", cosine)
        print("Tangent:", tangent)
        print("Cosecant:", "undefined" if abs(sine) < 1e-12 else 1 / sine)
        print("Secant:", "undefined" if abs(cosine) < 1e-12 else 1 / cosine)
        print("Cotangent:", "undefined" if abs(tangent) < 1e-12 else 1 / tangent)
    elif choice == "2":
        value = read_number("Enter a value for the inverse function: ")
        output_unit = read_choice("Show angles in degrees or radians? (d/r): ", {"d", "r"})
        inverse_tangent = math.atan(value)
        if output_unit == "d":
            inverse_tangent = math.degrees(inverse_tangent)
        unit_name = "degrees" if output_unit == "d" else "radians"
        print("Inverse tangent:", inverse_tangent, unit_name)
        if -1 <= value <= 1:
            inverse_sine = math.asin(value)
            inverse_cosine = math.acos(value)
            if output_unit == "d":
                inverse_sine = math.degrees(inverse_sine)
                inverse_cosine = math.degrees(inverse_cosine)
            print("Inverse sine:", inverse_sine, unit_name)
            print("Inverse cosine:", inverse_cosine, unit_name)
        else:
            print("Inverse sine and cosine require a value from -1 to 1.")
    elif choice == "3":
        value = read_number("Enter a value: ")
        try:
            print("Hyperbolic sine:", math.sinh(value))
            print("Hyperbolic cosine:", math.cosh(value))
            print("Hyperbolic tangent:", math.tanh(value))
        except OverflowError:
            print("The value is too large to calculate.")
    elif choice == "4":
        value = read_number("Enter a value: ")
        try:
            print("Inverse hyperbolic sine:", math.asinh(value))
            print("Inverse hyperbolic cosine:", math.acosh(value) if value >= 1 else "requires a value of at least 1")
            print("Inverse hyperbolic tangent:", math.atanh(value) if -1 < value < 1 else "requires a value between -1 and 1")
        except OverflowError:
            print("The value is too large to calculate.")
    elif choice == "5":
        unit = read_choice("Convert from degrees or radians? (d/r): ", {"d", "r"})
        value = read_number("Enter the angle: ")
        if unit == "d":
            print("Radians:", math.radians(value))
        else:
            print("Degrees:", math.degrees(value))


def geometry_menu():
    print("""
Geometry functions
1. Circle
2. Rectangle
3. Triangle
4. Square
5. Cuboid
6. Sphere
7. Cylinder
0. Return to main menu""")
    choice = read_choice("Choose a shape: ", {"0", "1", "2", "3", "4", "5", "6", "7"})

    if choice == "1":
        radius = read_positive("Enter radius: ")
        print("Circumference:", 2 * math.pi * radius)
        print("Area:", math.pi * radius ** 2)
    elif choice == "2":
        length = read_positive("Enter length: ")
        width = read_positive("Enter width: ")
        print("Perimeter:", 2 * (length + width))
        print("Area:", length * width)
    elif choice == "3":
        first = read_positive("Enter first side: ")
        second = read_positive("Enter second side: ")
        third = read_positive("Enter third side: ")
        if first + second <= third or first + third <= second or second + third <= first:
            print("Those side lengths cannot form a triangle.")
        else:
            semi_perimeter = (first + second + third) / 2
            area = math.sqrt(semi_perimeter * (semi_perimeter - first) * (semi_perimeter - second) * (semi_perimeter - third))
            print("Perimeter:", first + second + third)
            print("Area:", area)
    elif choice == "4":
        side = read_positive("Enter side length: ")
        print("Perimeter:", 4 * side)
        print("Area:", side ** 2)
    elif choice == "5":
        length = read_positive("Enter length: ")
        width = read_positive("Enter width: ")
        height = read_positive("Enter height: ")
        print("Surface area:", 2 * (length * width + length * height + width * height))
        print("Volume:", length * width * height)
    elif choice == "6":
        radius = read_positive("Enter radius: ")
        print("Surface area:", 4 * math.pi * radius ** 2)
        print("Volume:", 4 * math.pi * radius ** 3 / 3)
    elif choice == "7":
        radius = read_positive("Enter radius: ")
        height = read_positive("Enter height: ")
        print("Curved surface area:", 2 * math.pi * radius * height)
        print("Total surface area:", 2 * math.pi * radius * (radius + height))
        print("Volume:", math.pi * radius ** 2 * height)


def main():
    while True:
        print("""
Calculator
1. Arithmetic
2. Algebraic
3. Trigonometric
4. Geometric
0. Exit""")
        choice = read_choice("Choose a category: ", {"0", "1", "2", "3", "4"})

        if choice == "0":
            print("Goodbye!")
            break
        if choice == "1":
            arithmetic_menu()
        elif choice == "2":
            algebra_menu()
        elif choice == "3":
            trigonometry_menu()
        elif choice == "4":
            geometry_menu()


if __name__ == "__main__":
    main()
