import math


class BodyFatCalculator:
    def __init__(self):
        self.gender = None
        self.unit = None
        self.height = 0.0
        self.neck = 0.0
        self.waist = 0.0
        self.hip = 0.0
        self.weight = 0.0
        self.weight_unit = None
        self.body_fat_pct = None

    def get_length_inputs(self):
        while True:
            self.gender = input("Select Gender (m/f): ").strip().lower()
            if self.gender in ("m", "f"):
                break
            print("Error: Expected input is 'm' or 'f'")

        while True:
            self.unit = input("Enter units for measurement (cm/in): ").strip().lower()
            if self.unit in ("cm", "in"):
                break
            print("Error: Expected input is 'cm' or 'in'")

        while True:
            try:
                self.height = float(input(f"Enter your height in {self.unit}: "))
                self.neck = float(input(f"Measure your neck in {self.unit}: "))
                self.waist = float(input(f"Measure your waist in {self.unit}: "))

                if self.gender == "f":
                    self.hip = float(input(f"Measure your hip in {self.unit}: "))
                else:
                    self.hip = 0.0

                if self.height > 0 and self.neck > 0 and self.waist > 0:
                    break
                print("Measurements must be positive numbers")
            except ValueError:
                print("Enter Numerical Values")

    def get_weight_inputs(self):
        while True:
            self.weight_unit = (
                input("Enter units for weight measurement (kg/lbs): ").strip().lower()
            )
            if self.weight_unit in ("kg", "lbs"):
                break
            print("Invalid unit. Please only enter 'kg' or 'lbs'.")

        while True:
            try:
                self.weight = float(input(f"Enter your weight in {self.weight_unit}: "))
                if self.weight > 0:
                    break
                print("Weight must be a positive number.")
            except ValueError:
                print("That is not a number. Please enter a numerical value.")

    def calculate_bodyfat(self):
        if self.unit == "cm":
            conv_unit = 1 / 2.54
        else:
            conv_unit = 1
        w = self.waist * conv_unit
        n = self.neck * conv_unit
        h = self.height * conv_unit
        hi = self.hip * conv_unit

        try:
            if self.gender == "m":
                if w > n:
                    val = 86.010 * math.log10(w - n) - 70.041 * math.log10(h) + 36.76
                    self.body_fat_pct = round(val, 2)
                    return True
                print("Error: Waist must be larger than neck.")
                return False

            if (w + hi) > n:
                val = 163.205 * math.log10(w + hi - n) - 97.684 * math.log10(h) - 78.387
                self.body_fat_pct = round(val, 2)
                return True
            print("Error: Measurements invalid for calculation.")
            return False

        except ValueError:
            print("Calculation Error: Check inputs.")
            return False

    def get_mass_breakdown(self):
        fat_mass = round(self.weight * self.body_fat_pct / 100, 2)
        lean_mass = round(self.weight - fat_mass, 2)
        return f" {'Your Fat mass:':<16} {fat_mass:>15} {self.weight_unit} \n {'Your Lean Mass:':<16} {lean_mass:>15} {self.weight_unit}"

    def get_category(self):
        response = " You are in"
        bf = self.body_fat_pct

        if self.gender == "m":
            if bf < 2:
                return "Below Essential Fat (Incorrect Inputs)"
            if 2 <= bf <= 5:
                return f"{response} 'Essential Fat' Category"
            if 5 < bf <= 13:
                return f"{response} 'Athlete' Category"
            if 13 < bf <= 17:
                return f"{response} 'Fit' Category"
            if 17 < bf <= 24:
                return f"{response} 'Average' Category"
            return f"{response} 'Obese' Category"

        if self.gender == "f":
            if bf < 10:
                return "Below Essential Fat (Incorrect Inputs)"
            if 10 <= bf <= 13:
                return f"{response} 'Essential Fat' Category"
            if 13 < bf <= 20:
                return f"{response} 'Athlete' Category"
            if 20 < bf <= 24:
                return f"{response} 'Fit' Category"
            if 24 < bf <= 31:
                return f"{response} 'Average' Category"
            return f"{response} 'Obese' Category"

        return "Unknown Category"

    def run(self):
        self.get_length_inputs()

        if self.calculate_bodyfat():
            self.get_weight_inputs()

            print("\n-------------- RESULTS --------------")
            print(f" {'Your Body Fat Percentage:':<16} {self.body_fat_pct:>6} %")
            print(self.get_mass_breakdown())
            print("-" * 37)
            print(f"{self.get_category():^38}")
            print("-" * 37, "\n")
        else:
            print("\nCould not calculate results due to measurement errors.")


if __name__ == "__main__":
    app = BodyFatCalculator()
    app.run()
