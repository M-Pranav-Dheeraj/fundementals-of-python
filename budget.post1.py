It’s your job to calculate the cost of replacing damaged battle droids and to check whether it is within the budget limit of Rs. 15000. The cost of the equipment and parts is given in the table below.

Blast Rifle

Rs. 350.34

Visual Sensors

Rs. 230.90

Auditory Sensors

Rs. 190.55

Arms

Rs. 125.30

Legs

Rs. 180.90

Can you write a program to do the given task?

Input:

The input consists of 5 positive integers separated by a space (A B C D E).

A: number of blast rifles needed

B: number of visual sensors needed

C: number of auditory sensors needed

D: number of arms needed

E: number of legs needed

Output:

Output consists of a single string (“yes” or “no”). Print yes if the total cost of replacing damaged battle droids is within the sanctioned budget of Rs. 15000. Print no otherwise.

Sample Input:

20 10 14 3 9

Sample Output:

yes


solution:

a=input()
b=input()
c=input()
d=input()
e=input()
sum=((int(a)*(350.34))+(int(b)*(230.90))+(int(c)*(190.55))+(int(d)*(125.30))+(int(e)*(180.90)))
if(sum<15000):
    print("yes")
else:
    print("no")
