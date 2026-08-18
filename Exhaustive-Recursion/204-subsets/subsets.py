def subsets(elements):

  if len(elements) == 0:
    return [ [] ]

  first = elements[0]
  subs_without_first = subsets(elements[1:])
  subs_with_first = []

  for sub in subs_without_first:
    subs_with_first.append([first , *sub])

  return subs_without_first + subs_with_first