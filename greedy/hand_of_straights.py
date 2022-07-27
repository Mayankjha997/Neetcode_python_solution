import heapq

def hand_of_straights(hands,groupsize):
    if len(hands) % groupsize != 0:
        return False
    
    count = {}
    for h in hands:
        count[h] =1+ count.get(h,0)
        
    minh = list(count.keys())
    heapq.heapify(minh)

    while minh:
        first = minh[0]
        for i in range(first,first+groupsize):
            if i not in count:
                return False
            count[i]-=1
            if count[i] == 0:
                if i != minh[0]:
                    return False
                heapq.heappop(minh)
                
    return True


hands = list(map(int,input("enter the hands").strip().split())) 
groupsize = int(input("enter the groupsize "))
print(hands)
print(hand_of_straights(hands,groupsize))               