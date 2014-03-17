def final_position(commands, A, B):
  position = 0
  for cmd in commands:
    if cmd == 'R' and position < B:
      position += 1
    elif cmd == 'L' and position > -A:
      position -= 1
  return position
