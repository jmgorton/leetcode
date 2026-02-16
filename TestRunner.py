from typing import List, Dict, Any
import threading
import time

class TestRunner:
    def __init__(
        self,
        test_cases: List[Dict[str, Any]],
        solution_cls: type,
        method_name: str,
        input_keys: List[str],
    ):
        """
        Initialize TestRunner for solution-agnostic test execution.
        
        Args:
            test_cases: List of test case dictionaries with "id", "expected", and input keys
            solution_cls: The Solution class to instantiate
            method_name: Name of the method to call on the solution instance
            input_keys: List of parameter names that map to keys in test_case dict
                       e.g., ["s"] for longestBalanced(s), ["nums"] for solve(nums)
        """
        self.test_cases = test_cases
        self.solution_cls = solution_cls
        self.solution = solution_cls()
        self.method_name = method_name
        self.input_keys = input_keys
        self.results = []
        self.results_lock = threading.Lock()
    
    def _format_input_value(self, value: Any, max_len: int = 30) -> str:
        """
        Format a single input value, truncating with ellipsis if it exceeds max_len.
        
        Args:
            value: The value to format
            max_len: Maximum length before truncation
            
        Returns:
            Formatted string representation of the value
        """
        str_value = str(value)
        
        # Check if value has a length property and exceeds max_len
        if hasattr(value, '__len__') and len(str_value) > max_len:
            return f"{str_value[:max_len]}... (len={len(value)})"
        
        return str_value
    
    def run_test(self, test_case: Dict[str, Any]):
        """Run a single test case and store the result with timing."""
        test_id = test_case["id"]
        expected = test_case["expected"]
        
        # Extract input parameters from test case
        input_kwargs = {key: test_case[key] for key in self.input_keys}
        
        start_time = time.time()
        
        try:
            # Call the solution method dynamically with provided parameters
            method = getattr(self.solution, self.method_name)
            result = method(**input_kwargs)
            passed = result == expected
            
            elapsed_time = time.time() - start_time
            
            result_entry = {
                "id": test_id,
                **input_kwargs,  # Include all input parameters in the result
                "result": result,
                "expected": expected,
                "passed": passed,
                "error": None,
                "execution_time": elapsed_time
            }
            
            # Log result
            status = "PASS" if passed else "FAIL"
            # print(f"Test {test_id}: {nums}")
            print(f"  Result: {result}, Expected: {expected}, {status}")
            
        except Exception as e:
            elapsed_time = time.time() - start_time
            
            result_entry = {
                "id": test_id,
                **input_kwargs,
                "result": None,
                "expected": expected,
                "passed": False,
                "error": str(e),
                "execution_time": elapsed_time
            }
            # print(f"Test {test_id}: {nums}")
            print(f"  ERROR: {e}")
        
        # Store result thread-safely
        with self.results_lock:
            self.results.append(result_entry)

    def run_tests(self):
        """Run all test cases concurrently and print summary."""
        # Create and start threads
        threads = []
        for test_case in self.test_cases:
            thread = threading.Thread(target=self.run_test, args=(test_case,))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Print summary
        print("\n" + "=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        
        passed_count = sum(1 for r in self.results if r["passed"])
        total_count = len(self.results)
        
        for result in sorted(self.results, key=lambda x: x["id"]):

            status = "✓ PASS" if result["passed"] else "✗ FAIL"
            
            # Build input display from input_keys using truncation formatting
            input_display = ", ".join(
                f"{key}={self._format_input_value(result[key])}"
                for key in self.input_keys
                if key in result
            )
            
            execution_time_str = f" ({result['execution_time'] * 1000:.2f}ms)"
            
            if result["error"]:
                print(f"  Test {result['id']}: {status} ({input_display}, Error: {result['error']}){execution_time_str}")
            elif result["passed"]:
                print(f"  Test {result['id']}: {status} ({input_display}){execution_time_str}")
            else:
                print(f"  Test {result['id']}: {status} ({input_display}, Result: {result['result']}, Expected: {result['expected']}){execution_time_str}")
        
        print("=" * 70)
        print(f"Total: {passed_count}/{total_count} tests passed")
        print("=" * 70 + "\n")
        
        # Assert all passed
        # assert passed_count == total_count, f"Some tests failed: {passed_count}/{total_count} passed"
        # print("✓ All tests passed!")
        if passed_count != total_count: print(f"Some tests failed: {passed_count}/{total_count} passed")
        else: print("✓ All tests passed!")