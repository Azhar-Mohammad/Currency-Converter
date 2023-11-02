import requests

convertFrom = str(input("Enter the currency you to want from : ")).upper()

convertTo = str(input("Enter the currency you to want to : ")).upper()

amount = float(input("Enter the amount you want to convert : "))

response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={convertFrom}&to={convertTo}")

print(f'The converted amount of {amount} {convertFrom} to {convertTo} is {response.json()['rates'][convertTo]} {convertTo}')