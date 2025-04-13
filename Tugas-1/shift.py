matrix = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

for i in range(3):
  values = input().split()
  for j in range(3):
    matrix[i][j] = int(values.pop(0))
shift = int(input())
for i in range(shift):
  temp_matrix = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
  ]
  temp_matrix[0][0] = matrix[1][0]
  temp_matrix[1][0] = matrix[2][0]
  temp_matrix[2][0] = matrix[2][1]
  temp_matrix[2][1] = matrix[2][2]
  temp_matrix[2][2] = matrix[1][2] 
  temp_matrix[1][2] = matrix[0][2]
  temp_matrix[0][2] = matrix[0][1]
  temp_matrix[0][1] = matrix[0][0]
  temp_matrix[1][1] = matrix[1][1]
  matrix = temp_matrix
for i in range(3):
    print(matrix[i][0], matrix[i][1], matrix[i][2])
