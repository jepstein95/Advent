FILE = 'day1.txt'

inputs = []
count = 0
counts = [0]
done = False

# Store the inputs in a local array
with open(FILE, 'r') as file:
  line = file.readline()
  while line:
    inputs.append(int(line))
    line = file.readline()

# Iterate through the inputs, multiple times if necessary
while not done:
  for value in inputs:
    count = count + value
    
    # Done if the current count was already reached
    if count in counts:
      done = True
      break

    # Otherwise, record the current count
    else:
      counts.append(count)

print(count)