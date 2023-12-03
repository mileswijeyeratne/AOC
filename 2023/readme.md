# 2023 Comments

## Day 1
a. This was fairly straightforward considering python has ```.isnumeric()``` which helped parse the input.

b. The second part tripped me up in a couple of way. First, I had removed non-numeric chars when parsing so I had to change my parsing function. Second, I lost quite a few mins to the overlapping possibility of the numbers. My hacky solution at 5 in the morning was to replace the numbers like so: ```"nine" -> "nine9nine``` and run the same algorithm as part a. This meant the infamous ```"twoneight``` became ```"two2twone1oneight8eight"``` which is inelegant but worked. After completing the part I changed it making use of python's ```.startswith()``` Looking back I should've made an algorithm which traverses the string from the left and right and stops when it finds a valid number. This would've stopped the overlap problem and been more efficient - same O(n) TC worst case but best case O(2) if the valid numbers are at the edges.

## Day 2
a. Hardest part was parsing the input reasonably well. I think my code turned out fairly clean but I lost a lot of time to an error where I just removed the first 7 chars i.e ```"Game n:``` which doesn't allow for games with a 2 digit id. After I fixed this my parsing made solving the part quite easy.

b. The second part was one of those where if you have done the first part well the second is just a few modifications and that was the case this time.

## Day 3
a. This day was the easiest so far in terms of parsing but the logic took quite a long time for me. I searched the data for characters and then from there had a function ```_get_neighbours()``` to find adjacent cells and one ```_find_num()``` to get the start and end of the number found. Although probably bloated, it worked however was quite hard to debug. Something worth noting is that to avoid a number getting double counted if adjacent to more that 1 special character, I would replace the number with ```'.'``` chars after counting it the first time.

b. I got quite lucky in that my method of finding the special characters first meant I could filter invalid answers much faster. It didn't take too much modification for part b to run first time.


