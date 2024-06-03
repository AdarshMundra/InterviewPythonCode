# str1 = "adarsh mundra"
# dici={}
# for i in str1:
#     if i in dici:
#         dici[i]+=1
#     else:
#         dici[i]=1
# max_count = max(dici, key = dici.get)
# print(max_count)
# most_frequent_chars = [char for char, count in dici.items() if count == max_count]
# print(dici)
# print(most_frequent_chars)

def most_frequent_char(text):
  """
  Finds the most frequent character(s) in a string.

  Args:
      text: The string to analyze.

  Returns:
      A list containing the most frequent character(s).
  """

  char_frequency = {}
  for char in text:
    if char in char_frequency:
      char_frequency[char] += 1
    else:
      char_frequency[char] = 1

  max_count = max(char_frequency.values())
  most_frequent_chars = [char for char, count in char_frequency.items() if count == max_count]

  return most_frequent_chars

# Example usage
text = "adarsh mundr"
most_frequent = most_frequent_char(text)

if len(most_frequent) == 1:
  print(f"The most frequent character is: {most_frequent[0]}")
else:
  print(f"The most frequent characters are: {', '.join(most_frequent)}")
