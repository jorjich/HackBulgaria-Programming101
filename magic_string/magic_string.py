def magic_string(s):
  return len([i for i, c in enumerate(s) if i < len(s) // 2 and c == '<'
              or i >= len(s) // 2 and c == '>'])
