from typing import List, Dict, Any
import threading

class SegmentTree:
    def __init__(self, n):
        # 4*n because worst-case binary tree has ~4n nodes
        self.tree = [0] * (4 * n)
    
    def identity(self):
        # Identity element for the operation (e.g., 0 for sum, inf for min)
        return 0
    
    def combine(self, left_val, right_val):
        # Combine two child values (e.g., sum, min, max)
        return left_val + right_val  # Example for sum; change for other operations
    
    def build(self, arr, node, start, end):
        # Recursively build from leaves up
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node + 1, start, mid)
            self.build(arr, 2*node + 2, mid + 1, end)
            # Combine children (e.g., sum, min, max)
            self.tree[node] = self.combine(self.tree[2*node + 1], self.tree[2*node + 2])
    
    def update(self, index, value, node, start, end):
        # Navigate to the leaf for index
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update(index, value, 2*node + 1, start, mid)
        else:
            self.update(index, value, 2*node + 2, mid + 1, end)
        # Propagate change upward
        self.tree[node] = self.combine(self.tree[2*node + 1], self.tree[2*node + 2])
    
    def query(self, qleft, qright, node, start, end):
        # Three cases:
        # 1. [start, end] completely outside [qleft, qright] → skip
        # 2. [start, end] completely inside [qleft, qright] → use this node's value
        # 3. [start, end] partially overlaps → recurse to children
        
        if qright < start or qleft > end:  # Case 1: no overlap
            return self.identity()  # 0 for sum, inf for min, etc.
        
        if qleft <= start and end <= qright:  # Case 2: complete overlap
            return self.tree[node]
        
        mid = (start + end) // 2  # Case 3: partial overlap
        left_result = self.query(qleft, qright, 2*node + 1, start, mid)
        right_result = self.query(qleft, qright, 2*node + 2, mid + 1, end)
        return self.combine(left_result, right_result)
    
class LazySegmentTree:
    """
    Lazy segment tree for range updates and point queries.
    Supports:
    - Range add: add a value to all elements in a range [l, r]
    - Point query for zero: find if any position in range has value 0
    """
    
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (4 * n + 5)
        self.lazy = [0] * (4 * n + 5) # Pending updates not yet applied

    def push(self, node: int, start: int, end: int) -> None:
        """
        Apply pending lazy updates to this node and propagate to children.
        
        When lazy[node] != 0, it means we have a pending add operation.
        We apply it: tree[node] += lazy[node]
        Then propagate to children if this is not a leaf.
        """
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            
            # If not a leaf, propagate to children
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            
            self.lazy[node] = 0
    
    def range_update(self, qleft: int, qright: int, value: int, 
                     node: int = 0, start: int = None, end: int = None) -> None:
        """
        Add value to all positions in range [qleft, qright].
        Uses lazy propagation to defer work until needed.
        
        Time complexity: O(log n)
        """
        if start is None:
            start = 0
            end = self.n - 1
        
        self.push(node, start, end)
        
        # No overlap between [start, end] and [qleft, qright]
        if qright < start or qleft > end:
            return
        
        # Complete overlap: mark this node for lazy update
        if qleft <= start and end <= qright:
            self.lazy[node] += value
            self.push(node, start, end)
            return
        
        # Partial overlap: recurse to children
        mid = (start + end) // 2
        self.range_update(qleft, qright, value, 2 * node + 1, start, mid)
        self.range_update(qleft, qright, value, 2 * node + 2, mid + 1, end)
        
        # Update parent by combining children (after pushing their pending updates)
        self.push(2 * node + 1, start, mid)
        self.push(2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query_for_zero(self, qleft: int, qright: int, 
                       node: int = 0, start: int = None, end: int = None) -> int:
        """
        Find the rightmost position in [qleft, qright] where tree value = 0.
        
        Returns the index of the rightmost position with value 0,
        or -1 if no such position exists in the range.
        
        Time complexity: O(log n)
        """
        if start is None:
            start = 0
            end = self.n - 1
        
        self.push(node, start, end)
        
        # No overlap between [start, end] and [qleft, qright]
        if qright < start or qleft > end:
            return -1
        
        # Leaf node: check if it has value 0 and is in query range
        if start == end:
            if qleft <= start <= qright and self.tree[node] == 0:
                return start
            return -1
        
        mid = (start + end) // 2
        
        # Query right child first (to find rightmost zero)
        right_result = self.query_for_zero(qleft, qright, 2 * node + 2, mid + 1, end)
        if right_result != -1:
            return right_result
        
        # Query left child if right child had no zero
        left_result = self.query_for_zero(qleft, qright, 2 * node + 1, start, mid)
        return left_result

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        """
        Find the longest balanced subarray.
        
        A subarray is balanced if: count(distinct odds) == count(distinct evens)
        
        Algorithm:
        1. Define balance[i] = distinct_odd_count[0..i] - distinct_even_count[0..i]
        2. A subarray [l, r] is balanced iff balance[r] = balance[l-1]
        3. Use a lazy segment tree to efficiently maintain and query balance values
        4. For each starting position l, find the rightmost r where balance[r] = 0
        
        Key insights:
        - sign = +1 for odd values, -1 for even values (CRITICAL!)
        - Query BEFORE updating: query for balanced subarray, then update for next iteration
        - This ensures we find optimal balance before removing value's contribution
        
        Time complexity: O(n log n)
        Space complexity: O(n)
        """

        n = len(nums)
        if n == 0:
            return 0
        
        # pos[value] = list of indices where value appears (in order)
        pos = {}
        for i, v in enumerate(nums):
            if v not in pos:
                pos[v] = []
            pos[v].append(i)
        
        # Initialize lazy segment tree
        segtree = LazySegmentTree(n)
        
        # Initialize: for each distinct value, add its contribution from first occurrence onward
        # sign = +1 for odd values, -1 for even values
        # This builds balance[i] = distinct_odd[0..i] - distinct_even[0..i]
        for v in pos:
            sign = 1 if v % 2 == 1 else -1  # Odd = +1, Even = -1
            first_idx = pos[v][0]
            segtree.range_update(first_idx, n - 1, sign)
        
        ans = 0
        
        # Slide left pointer: for each starting position, find longest balanced subarray
        for l in range(n):
            v = nums[l]
            sign = 1 if v % 2 == 1 else -1  # Odd = +1, Even = -1
            
            # Query FIRST (before updating) to get the balanced subarray for this starting position
            zero_pos = segtree.query_for_zero(l, n - 1)
            if zero_pos != -1:
                ans = max(ans, zero_pos - l + 1)
            
            # Now update for next iteration
            # Remove this value's first occurrence from our tracking
            pos[v].pop(0)
            
            # Find the next occurrence of nums[l] (or n if none exists)
            next_idx = pos[v][0] if pos[v] else n
            
            # Update segment tree: subtract sign from range [0, next_idx - 1]
            # This "unrecords" the fact that this value became new at position l
            segtree.range_update(0, next_idx - 1, -sign)
        
        return ans


# ============================================================================
# Test Cases (from LeetCode problem 3721)
# ============================================================================

def test_solution():
    """Run all test cases using threading for pseudo-parallel execution."""
    sol = Solution()
    
    # Test cases definition
    test_cases = [
        {
            "id": 1,
            "nums": [2, 5, 4, 3],
            "expected": 4
        },
        {
            "id": 2,
            "nums": [3, 2, 2, 5, 4],
            "expected": 5
        },
        {
            "id": 3,
            "nums": [1, 2, 3, 2],
            "expected": 3
        }
    ]
    
    # Results storage (thread-safe with lock)
    results = []
    results_lock = threading.Lock()
    
    def run_test(test_case: Dict[str, Any]) -> None:
        """Run a single test case and store the result."""
        test_id = test_case["id"]
        nums = test_case["nums"]
        expected = test_case["expected"]
        
        try:
            result = sol.longestBalanced(nums)
            passed = result == expected
            
            result_entry = {
                "id": test_id,
                "nums": nums,
                "result": result,
                "expected": expected,
                "passed": passed,
                "error": None
            }
            
            # Log result
            status = "PASS" if passed else "FAIL"
            print(f"Test {test_id}: {nums}")
            print(f"  Result: {result}, Expected: {expected}, {status}")
            
        except Exception as e:
            result_entry = {
                "id": test_id,
                "nums": nums,
                "result": None,
                "expected": expected,
                "passed": False,
                "error": str(e)
            }
            print(f"Test {test_id}: {nums}")
            print(f"  ERROR: {e}")
        
        # Store result thread-safely
        with results_lock:
            results.append(result_entry)
    
    # Create and start threads
    threads = []
    for test_case in test_cases:
        thread = threading.Thread(target=run_test, args=(test_case,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    
    passed_count = sum(1 for r in results if r["passed"])
    total_count = len(results)
    
    for result in sorted(results, key=lambda x: x["id"]):
        status = "✓ PASS" if result["passed"] else "✗ FAIL"
        if result["error"]:
            print(f"  Test {result['id']}: {status} (Error: {result['error']})")
        else:
            print(f"  Test {result['id']}: {status} (Result: {result['result']}, Expected: {result['expected']})")
    
    print("=" * 70)
    print(f"Total: {passed_count}/{total_count} tests passed")
    print("=" * 70 + "\n")
    
    # Assert all passed
    assert passed_count == total_count, f"Some tests failed: {passed_count}/{total_count} passed"
    print("✓ All tests passed!")


if __name__ == "__main__":
    test_solution()