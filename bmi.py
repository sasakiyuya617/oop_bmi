class BMI:
    def __init__(self, height, weight):
        self.value = weight / (height ** 2)

        if not (10 <= self.value <= 40):
            raise ValueError("BMIが正常値の範囲を超えています")

    def __str__(self):
        return f"{self.value:.2f}"


tanaka_bmi = BMI(height=1.80, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)
bob_bmi = BMI(height=1.70, weight=75000.0)

print(tanaka_bmi)
print(sasami_bmi)
print(bob_bmi)

