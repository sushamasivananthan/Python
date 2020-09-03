def highlight_word(sentence, word):
  ret = ""
  l = len(word)
  words = sentence.split()
  for i,w in enumerate(words):
    if w[:l] == word:
      ret += w[:l].upper()+w[l:]
    else:
      ret += w
    if i != len(words)-1:
      ret += " "
  return ret



print(highlight_word("Good Morning Everyone", "Everyone"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
