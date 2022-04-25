from p2 import solution

file = open('numbers.txt','r')

answer = ''

for line in file:
  answer += str(solution(int(line)))
  answer += '\n'

print (answer)

def solution(a):
  return a / 8
