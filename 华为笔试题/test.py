nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
nums1.sort()
nums2.sort()
r, l = 0, 0
res = []
while r < len(nums1) and l < len(nums2):
    # print(r, l)
    if nums1[r] > nums2[l]:
        l = l + 1
    elif nums1[r] < nums2[l]:
        r = r + 1
    else:
        res.append(nums1[r])
        l = l + 1
        r = r + 1
        # print(res)
print(res)
