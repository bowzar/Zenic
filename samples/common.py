import core.test
import thread
import threading

print "Hello world!"
for index in range(10):
    print "Current index is %d" % index

print range(5) * 2
print range(5) == range(6)

l1 = [(1, 2, 3), ("fd", "gfd")]
l2 = [(1, 2, 3), ("fd", "gfd")]
print l1 == l2

core.test.writeLine("Hello package!")

print range(2, 10, 2)
print range(2)
print [x * 5 for x in range(2, 10, 2)]

print __name__ == "__main__"
print __file__
print __package__

print(range(2, 5))
print(range(2, 5, 2))
