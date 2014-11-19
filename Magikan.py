""" http://geektimes.ru/post/111843/#comment_7880507 """
for i in ("FizzBuzz" if i % 3 + i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in xrange(100)):
    print i
