class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            left = arr[L:M + 1]
            right = arr[M + 1:R + 1]

            i = L
            j = 0
            k = 0

            # Merge the two sorted halves
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            # Copy remaining elements from left
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            # Copy remaining elements from right
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, L, R):
            # Base case
            if L >= R:
                return

            M = (L + R) // 2

            # Sort left half
            mergeSort(arr, L, M)

            # Sort right half
            mergeSort(arr, M + 1, R)

            # Merge sorted halves
            merge(arr, L, M, R)

        mergeSort(nums, 0, len(nums) - 1)

        return nums