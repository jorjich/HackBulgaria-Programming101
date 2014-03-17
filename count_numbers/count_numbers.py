def count_numbers(numbers):
  candidates = set([a // b for a in numbers for b in numbers
                    if a > b and a // b not in numbers])
  while candidates:
        numbers += candidates
        candidates = set([a // b for a in numbers for b in numbers
                      if a > b and a // b not in numbers])
  return len(numbers)
