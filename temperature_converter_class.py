#practice question 12
#12. Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32

output = TemperatureConverter.celsius_to_fahrenheit(30)
print(f"The result of celsius to fahrenheit {output}°F ")
