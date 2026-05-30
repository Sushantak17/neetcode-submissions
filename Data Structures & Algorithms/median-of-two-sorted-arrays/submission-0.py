class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A)

        while True:

            mid = (l + r) // 2
            other_cut = half - mid

            Aleft = A[mid - 1] if mid > 0 else float("-inf")
            Aright = A[mid] if mid < len(A) else float("inf")

            Bleft = B[other_cut - 1] if other_cut > 0 else float("-inf")
            Bright = B[other_cut] if other_cut < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2:
                    return min(Aright, Bright)

                return (
                    max(Aleft, Bleft) +
                    min(Aright, Bright)
                ) / 2

            elif Aleft > Bright:
                r = mid - 1

            else:
                l = mid + 1

