""" http://habrahabr.ru/post/240617/#comment_8072889 """

# Do not repeat it in production
for i in range(1, 101):
    res = 'FizzBuzz'  if i % 15 == 0 \ 
          else 'Buzz' if i % 5 == 0 \ 
          else 'Fizz' if i % 3 == 0 \ 
          else i
    print(res)
    
# Do not repeat this too
for res in ('FizzBuzz'  if i % 15 == 0 \
            else 'Buzz' if i % 5 == 0 \
            else 'Fizz' if i % 3 == 0 \
            else i
            for i in range (1, 101)):
    print(res)
    
# Do not watch this at all
from collections import deque

deque((print('FizzBuzz'  if i % 15 == 0 \
             else 'Buzz' if i % 5 == 0 \
             else 'Fizz' if i % 3 == 0 \
             else i)
       for i in range (1, 101)),
      maxlen=1).pop()
      
# :-)
