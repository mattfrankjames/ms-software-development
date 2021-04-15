def anagram(str1, str2):
  aList1 = list(str1)
  aList2 = list(str2)

  aList1.sort()
  aList2.sort()

  pos = 0
  matches = True

  while pos < len(str1):
    if aList1[pos] == aList2[pos]:
      pos = pos + 1
    else:
      matches = False

  return matches

print(anagram('abcde', 'ohiuh'))