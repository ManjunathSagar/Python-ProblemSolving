"""
The program illustrates how to find frequency of each word in a string in Python
Here we have levereged the concept of dictionary in python to get work count in string
"""


# Function to get word count in a string
def get_word_count(sentence):
  sentence = sentence.lower()
  wordlist = sentence.split()
  wordcount = {}

  for word in wordlist:
    if word in wordcount:
      wordcount[word] += 1
    else:
      wordcount[word] = 1
  return wordcount


# Driver Code to main function
if __name__ == "__main__":
  input_sentence = "Apple banana Cherry cherry apple banana apple"
  wordcount = get_word_count(input_sentence)
  print(wordcount)
"""
Output: {'apple': 3, 'banana': 2, 'cherry': 2}

Total Time Complexity:
O(n+k) = O(n)
(Since k <= n)

Space Complexity:
wordlist = O(k)
wordcount dictionary = O(u)
Total Space Complexity: O(k+u)
"""
