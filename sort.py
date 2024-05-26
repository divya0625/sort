def find_highest_two_numbers(numbers):
    if len(numbers)<2:
      raise ValueError(" the list must contain at  least 2 numbers")
    
    highest=float('-inf')
    second_highest=float('-inf')

    for number in numbers:
        if number > highest:
       
         second_highest= highest
         highest= number
        elif number > second_highest:
          second_highest=number

    return highest,second_highest

number=[10,20,4,45,99,6,70]
highest,second_highest=find_highest_two_numbers(number)
print(f"the highest number is {highest}")
print(f"the second highest number is {second_highest}")