def median_of_two_sorted_array(nums1,nums2):
    A, B = nums1, nums2
    total = len(nums1)+len(nums2)
    half = total // 2
    if len(B) < len(A):
        A,B = B,A 
    
    l, r = 0 , len(A) - 1
    while True:
        i = (l+r) // 2
        j = half - i - 2
        
        aleft = A[i] if i >= 0 else float("-infinity")
        aright = A[i+1] if (i+1) < len(A) else float("infinity")
        bleft = B[j] if j >= 0 else float("-infinity")
        bright = B[j+1] if (j+1) < len(B) else float("infinity")
        
        if aleft <= bright and bleft <= aright:
            if total % 2 == 0:
                return min(bright,aright)
            return (min(bright,aright) + max(aleft,bleft)) / 2
        
        elif aleft > bright:
            r = i - 1
        else:
            l = i + 1
            
nums1 = list(map(int,input("enter the number of first array ").strip().split()))
nums2 = list(map(int,input("enter the number of first array ").strip().split()))
print(nums1) 
print(nums2)
print(median_of_two_sorted_array(nums1,nums2))   
    