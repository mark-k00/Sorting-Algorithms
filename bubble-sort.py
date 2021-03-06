#Bubble Sort
#!/usr/bin/env python
n = raw_input()
a = []
while n != "end":
   n = int(n)
   a.append (n)
   n = raw_input()

print a #original list made from user input


i = 0

while i < len(a): #while 0 is less than the length of the list a
   j = 1 #the position just above position a[0]
   while j < len(a): #1<length of list so that the while loop is not infinite
      if a[j] < a[j - 1]: #a[1]<a[0] for example position a[1]= 6 and a[0]=8 therefore a[1] is less than a[0] and while loop will run
         tmp = a[j] #temporary variable set as integer from position a[1]
         a[j] = a[j - 1] #integer from position a[1] is replaced with integer from position a[0] (which must be a higher number in an earlier place) so that it can be sorted in order of rising numbers
         a[j - 1] = tmp #now a[0] is given the temporary variable so that there positions are officially swapped and the smaller number should be at an earlier position
      j = j + 1 #j turns into 2 so that we can go through the full list
   i = i + 1 #i turns into 1 for same reason as above

print a #sorted list, sorted using Bubble Sort Algorithm