"""http://geektimes.ru/post/111843/#comment_3575129"""
for i in xrange(1, 100): print ("" if i % 3 else "Fizz") + ("" if i % 5 else "Buzz") or i
