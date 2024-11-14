Condition = 'Maybe'

if Condition == 'Yes':

   print(f"These lines are executed because Condition is 'Yes'")

   print('This line is also indented, and gets included')

   print('It can keep going like this for a LONG time')

elif Condition == 'Maybe':

   print(f"This line executes if 'Condition' is 'Maybe'")

else:

   print(f"Print this when Condition is neither 'Yes' nor 'Maybe'")