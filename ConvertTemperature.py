class Solution:
    def convertTemperature( celsius):
        ans =[]
        z = ans
        if celsius >= 0:
            kelvin = celsius + 273.15
            Fahrenheit = (celsius * 1.80 )+ 32.00
            z.append(kelvin)
            z.append(Fahrenheit)
        return ans
    


print(Solution.convertTemperature(36.5))