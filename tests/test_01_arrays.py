import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestArrays(unittest.TestCase):
    def test_0001(self):
        mod = load_solution("01_Arrays/0001_Two_Sum.py")
        sol = mod.Solution()
        self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_0026(self):
        mod = load_solution("01_Arrays/0026_Remove_Duplicates_From_Sorted_Array.py")
        sol = mod.Solution()
        a = [1, 1, 2]; k = sol.removeDuplicates(a); self.assertEqual((k, a[:k]), (2, [1, 2]))

    def test_0027(self):
        mod = load_solution("01_Arrays/0027_Remove_Element.py")
        sol = mod.Solution()
        a = [3, 2, 2, 3]; k = sol.removeElement(a, 3); self.assertEqual((k, sorted(a[:k])), (2, [2, 2]))

    def test_0031(self):
        mod = load_solution("01_Arrays/0031_Next_Permutation.py")
        sol = mod.Solution()
        a = [1, 2, 3]; sol.nextPermutation(a); self.assertEqual(a, [1, 3, 2])

    def test_0041(self):
        mod = load_solution("01_Arrays/0041_First_Missing_Positive.py")
        sol = mod.Solution()
        self.assertEqual(sol.firstMissingPositive([3, 4, -1, 1]), 2); self.assertEqual(sol.firstMissingPositive([1, 2, 0]), 3)

    def test_0048(self):
        mod = load_solution("01_Arrays/0048_Rotate_Image.py")
        sol = mod.Solution()
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; sol.rotate(m); self.assertEqual(m, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_0053(self):
        mod = load_solution("01_Arrays/0053_Maximum_Subarray.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_0054(self):
        mod = load_solution("01_Arrays/0054_Spiral_Matrix.py")
        sol = mod.Solution()
        self.assertEqual(sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_0055(self):
        mod = load_solution("01_Arrays/0055_Jump_Game.py")
        sol = mod.Solution()
        self.assertTrue(sol.canJump([2, 3, 1, 1, 4])); self.assertFalse(sol.canJump([3, 2, 1, 0, 4]))

    def test_0056(self):
        mod = load_solution("01_Arrays/0056_Merge_Intervals.py")
        sol = mod.Solution()
        self.assertEqual(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])

    def test_0057(self):
        mod = load_solution("01_Arrays/0057_Insert_Interval.py")
        sol = mod.Solution()
        self.assertEqual(sol.insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])

    def test_0059(self):
        mod = load_solution("01_Arrays/0059_Spiral_Matrix_II.py")
        sol = mod.Solution()
        self.assertEqual(sol.generateMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_0066(self):
        mod = load_solution("01_Arrays/0066_Plus_One.py")
        sol = mod.Solution()
        self.assertEqual(sol.plusOne([9, 9]), [1, 0, 0])

    def test_0073(self):
        mod = load_solution("01_Arrays/0073_Set_Matrix_Zeroes.py")
        sol = mod.Solution()
        m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]; sol.setZeroes(m); self.assertEqual(m, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_0075(self):
        mod = load_solution("01_Arrays/0075_Sort_Colors.py")
        sol = mod.Solution()
        a = [2, 0, 2, 1, 1, 0]; sol.sortColors(a); self.assertEqual(a, [0, 0, 1, 1, 2, 2])

    def test_0088(self):
        mod = load_solution("01_Arrays/0088_Merge_Sorted_Array.py")
        sol = mod.Solution()
        a = [1, 2, 3, 0, 0, 0]; sol.merge(a, 3, [2, 5, 6], 3); self.assertEqual(a, [1, 2, 2, 3, 5, 6])

    def test_0118(self):
        mod = load_solution("01_Arrays/0118_Pascals_Triangle.py")
        sol = mod.Solution()
        self.assertEqual(sol.generate(3), [[1], [1, 1], [1, 2, 1]])

    def test_0119(self):
        mod = load_solution("01_Arrays/0119_Pascals_Triangle_II.py")
        sol = mod.Solution()
        self.assertEqual(sol.getRow(3), [1, 3, 3, 1])

    def test_0121(self):
        mod = load_solution("01_Arrays/0121_Best_Time_To_Buy_And_Sell_Stock.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_0122(self):
        mod = load_solution("01_Arrays/0122_Best_Time_To_Buy_And_Sell_Stock_II.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxProfit([7, 1, 5, 3, 6, 4]), 7)

    def test_0134(self):
        mod = load_solution("01_Arrays/0134_Gas_Station.py")
        sol = mod.Solution()
        self.assertEqual(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)

    def test_0135(self):
        mod = load_solution("01_Arrays/0135_Candy.py")
        sol = mod.Solution()
        self.assertEqual(sol.candy([1, 0, 2]), 5)

    def test_0152(self):
        mod = load_solution("01_Arrays/0152_Maximum_Product_Subarray.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxProduct([2, 3, -2, 4]), 6)

    def test_0169(self):
        mod = load_solution("01_Arrays/0169_Majority_Element.py")
        sol = mod.Solution()
        self.assertEqual(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_0189(self):
        mod = load_solution("01_Arrays/0189_Rotate_Array.py")
        sol = mod.Solution()
        a = [1, 2, 3, 4, 5, 6, 7]; sol.rotate(a, 3); self.assertEqual(a, [5, 6, 7, 1, 2, 3, 4])

    def test_0217(self):
        mod = load_solution("01_Arrays/0217_Contains_Duplicate.py")
        sol = mod.Solution()
        self.assertTrue(sol.containsDuplicate([1, 2, 3, 1])); self.assertFalse(sol.containsDuplicate([1, 2, 3]))

    def test_0228(self):
        mod = load_solution("01_Arrays/0228_Summary_Ranges.py")
        sol = mod.Solution()
        self.assertEqual(sol.summaryRanges([0, 1, 2, 4, 5, 7]), ["0->2", "4->5", "7"])

    def test_0229(self):
        mod = load_solution("01_Arrays/0229_Majority_Element_II.py")
        sol = mod.Solution()
        self.assertEqual(sorted(sol.majorityElement([1, 2])), [1, 2]); self.assertEqual(sol.majorityElement([3, 2, 3]), [3])

    def test_0238(self):
        mod = load_solution("01_Arrays/0238_Product_Of_Array_Except_Self.py")
        sol = mod.Solution()
        self.assertEqual(sol.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_0240(self):
        mod = load_solution("01_Arrays/0240_Search_A_2D_Matrix_II.py")
        sol = mod.Solution()
        self.assertTrue(sol.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]], 5))

    def test_0268(self):
        mod = load_solution("01_Arrays/0268_Missing_Number.py")
        sol = mod.Solution()
        self.assertEqual(sol.missingNumber([3, 0, 1]), 2)

    def test_0274(self):
        mod = load_solution("01_Arrays/0274_H_Index.py")
        sol = mod.Solution()
        self.assertEqual(sol.hIndex([3, 0, 6, 1, 5]), 3)

    def test_0283(self):
        mod = load_solution("01_Arrays/0283_Move_Zeroes.py")
        sol = mod.Solution()
        a = [0, 1, 0, 3, 12]; sol.moveZeroes(a); self.assertEqual(a, [1, 3, 12, 0, 0])

    def test_0289(self):
        mod = load_solution("01_Arrays/0289_Game_Of_Life.py")
        sol = mod.Solution()
        b = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]; sol.gameOfLife(b); self.assertEqual(b, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])

    def test_0315(self):
        mod = load_solution("01_Arrays/0315_Count_Of_Smaller_Numbers_After_Self.py")
        sol = mod.Solution()
        self.assertEqual(sol.countSmaller([5, 2, 6, 1]), [2, 1, 1, 0])

    def test_0330(self):
        mod = load_solution("01_Arrays/0330_Patching_Array.py")
        sol = mod.Solution()
        self.assertEqual(sol.minPatches([1, 3], 6), 1)

    def test_0414(self):
        mod = load_solution("01_Arrays/0414_Third_Maximum_Number.py")
        sol = mod.Solution()
        self.assertEqual(sol.thirdMax([3, 2, 1]), 1); self.assertEqual(sol.thirdMax([1, 2]), 2)

    def test_0442(self):
        mod = load_solution("01_Arrays/0442_Find_All_Duplicates_In_An_Array.py")
        sol = mod.Solution()
        self.assertEqual(sorted(sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])), [2, 3])

    def test_0448(self):
        mod = load_solution("01_Arrays/0448_Find_All_Numbers_Disappeared_In_An_Array.py")
        sol = mod.Solution()
        self.assertEqual(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])

    def test_0485(self):
        mod = load_solution("01_Arrays/0485_Max_Consecutive_Ones.py")
        sol = mod.Solution()
        self.assertEqual(sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)

    def test_0493(self):
        mod = load_solution("01_Arrays/0493_Reverse_Pairs.py")
        sol = mod.Solution()
        self.assertEqual(sol.reversePairs([1, 3, 2, 3, 1]), 2)

    def test_0498(self):
        mod = load_solution("01_Arrays/0498_Diagonal_Traverse.py")
        sol = mod.Solution()
        self.assertEqual(sol.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 4, 7, 5, 3, 6, 8, 9])

    def test_0561(self):
        mod = load_solution("01_Arrays/0561_Array_Partition.py")
        sol = mod.Solution()
        self.assertEqual(sol.arrayPairSum([1, 4, 3, 2]), 4)

    def test_0566(self):
        mod = load_solution("01_Arrays/0566_Reshape_The_Matrix.py")
        sol = mod.Solution()
        self.assertEqual(sol.matrixReshape([[1, 2], [3, 4]], 1, 4), [[1, 2, 3, 4]])

    def test_0605(self):
        mod = load_solution("01_Arrays/0605_Can_Place_Flowers.py")
        sol = mod.Solution()
        self.assertTrue(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1)); self.assertFalse(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))

    def test_0628(self):
        mod = load_solution("01_Arrays/0628_Maximum_Product_Of_Three_Numbers.py")
        sol = mod.Solution()
        self.assertEqual(sol.maximumProduct([-10, -10, 5, 2]), 500)

    def test_0645(self):
        mod = load_solution("01_Arrays/0645_Set_Mismatch.py")
        sol = mod.Solution()
        self.assertEqual(sol.findErrorNums([1, 2, 2, 4]), [2, 3])

    def test_0724(self):
        mod = load_solution("01_Arrays/0724_Find_Pivot_Index.py")
        sol = mod.Solution()
        self.assertEqual(sol.pivotIndex([1, 7, 3, 6, 5, 6]), 3)



if __name__ == "__main__":
    unittest.main()
