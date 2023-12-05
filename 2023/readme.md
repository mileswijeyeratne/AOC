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

## Day 4
a. This part was fairly easy for the logic the hardest bit was parsing the input as I didn't want to remove too much information about the game no etc. After finally parsing the input my program worked second try after I fixed a bug with ```res += 2**(count-1)``` as this will give you ```0.5``` if count is 0.

b. Part 2 was considerably harder for me. My original approach - a massive list acting as a queue to store all games - was just too slow. I then spend half an hour battling with caching and dicts until finally arriving at an approach where you store the number of each card you have in a dict and if you work through it in order you will get all the cards. Quite a nice solution in the end but definitely took longer than I would've liked.


## Day 5
a. As usual, this part's parsing took longer than the actual logic. Maybe I should get better at regex? After that, all it took was 2 loops and a range check to get the correct answer first time.

b. Compared to part a, part b was a pain. The obvious approach, run part a but with all the numbers in the ranges, would just take far to long. My initial idea was to use range bounds and do all my logic by manipulating them. This is what the function ```_apply_rule_fast_all``` does. It compares the bounds of the rule and range of numbers being checked, splits the ranges and applies the mapping accordingly. This solution caused me a lot of headache and took a lot of trial and error to implement. I ended up manually looking through all comparison cases with a pen and paper. Even after all this, my code didn't work (it gave around double the correct answer). Even though it was quick (around 5ms) it was just too hard to debug and I decided to attack the problem a different way.

b (try 2). My second idea was to count up from 0 until reaching a number that would start in the range after being reverse engineered from the end. The hardest bit of this was reversing the rules due to my slightly badly written data structures. In the end it worked but I subsequently realised it would've been easier to modify my part a parsing code. After a loop and reusing the function from part a, the code worked first try but at the cost of a 5-6 min runtime. Overall, a much harder part then expected.
