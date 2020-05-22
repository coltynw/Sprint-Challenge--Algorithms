#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  
<!-- a = 0
while (a < n * n * n):
    a = a + n * n -->

    n reffered to the size of the input, but here n is an input. 
    it's only a single input, it's just the one n. 
    but if that n increases it will multiplicatively affect the runtime because we're multiplying it by itself like 5 times.
    They picked a variable named n to make it more confusing.

    it's O(n)


b)
<!-- sum = 0
for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1 -->

    ok this is 2 loops, a for loop and a while loop. 4 total variables but it looks like only 2 of them are inputs. 
    The first loops runs n number of times, so the length of n is how long we are iterating through n. the while loop inside we run that many times at least as long as j is less than n. Since we're multiplying inputs by each other It'd say this is slightly less effiecent than the a) question. So I'm just going to guess because none of the other runtime expressions fit this discription.

    it's O(n log n)?

c)
 <!-- def bunnyEars(bunnies):
     if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) -->

      recursive function. Looks like only 1 input tho, == bunnies. This function runs (bunnies) number of times. That means it's Linear

      it's O(n)

## Exercise II
 <!-- Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

 Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution. -->


Since we can sort large sums of the data (the floors) at once by checking if the egg breaks, recursive sorting and iterative sorting doesn't really seem correct so I'm going to review my notes.

This is a sorted data set, the floors never change in order, so I'm going to think Binary Search. I'm going to look up more on Binary Search since that was like Monday and I don't really remember it.

Binary Search looks similar to a quick sort setting pivots, but the pivots are always the middle of the current unsorted data.

It's assumed you start at the bottom floor?
I'm just gunna say we start in the middle.
    
    So go to the middle floor.
        drop the egg.
            if the egg breaks
                go to middle floor between you and the ground or the lowest floor that an egg has previously broken on.
            if the egg does not break
                go to the middle floor between you and the roof or the highest floor that an egg has not previously broken on.

    keep repeating these methods in the middle of the middles until you get to the highest floor the egg doesn't break on.
        
    set that floor to f

    print(f)
        
google says Binary Search is O(log n)