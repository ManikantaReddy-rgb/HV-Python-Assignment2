import pandas as pd
inputseries = pd.Series([int(input("Enter numbers:")) for i in range(5)])
z=pd.Series(inputseries**2)
print("The given inputs are:\n",inputseries)
print("The square of given inputs is: \n",z)


