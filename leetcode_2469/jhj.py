class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        
        Temperature = []
        Temperature.append(Kelvin)
        Temperature.append(Fahrenheit)
        
        return Temperature

"""
Runtime: 46 ms
Memory Usage: 16.2 MB
"""