def merge_triplets_to_form_target_triplet(triplets, target):
    good = set()
        
    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue
                
        for i,v in enumerate(t):
            if v == target[i]:
                good.add(i)
                    
    return len(good) == 3

