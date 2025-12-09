class DistinctAlgorithmSuite:
    def __init__(self):
        print("Initializing Distinct Algorithm Suite (Set 3)...")

    # ---------------------------------------------------------
    # DAY 1 WORK: SORTING
    # Algorithm: Heap Sort
    # Theory: Binary Heap Data Structure
    # Complexity: O(n log n)
    # Note: Builds a max-heap, then swaps root with end.
    # ---------------------------------------------------------
    def heap_sort(self, arr):
        n = len(arr)

        # Build a maxheap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self._heapify(arr, i, 0)

        return arr

    def _heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)

    # ---------------------------------------------------------
    # DAY 2 WORK: GRAPH TRAVERSAL
    # Algorithm: Depth-First Search (DFS)
    # Theory: Stack-based traversal (Recursion)
    # Application: Solving mazes, topological sorting
    # Complexity: O(V + E)
    # ---------------------------------------------------------
    def dfs_traversal(self, graph, start_node, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_node)
        path = [start_node]

        # Explore neighbors depth-first
        if start_node in graph:
            for neighbor in graph[start_node]:
                if neighbor not in visited:
                    path.extend(self.dfs_traversal(graph, neighbor, visited))

        return path

    # ---------------------------------------------------------
    # DAY 3 WORK: NUMBER THEORY
    # Algorithm: Sieve of Eratosthenes
    # Theory: Iterative filtering
    # Application: Generating prime numbers efficiently
    # Complexity: O(n log(log n))
    # ---------------------------------------------------------
    def sieve_of_eratosthenes(self, limit):
        primes = []
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        for number in range(2, int(limit ** 0.5) + 1):
            if is_prime[number]:
                # Mark multiples of the prime as non-prime
                for multiple in range(number * number, limit + 1, number):
                    is_prime[multiple] = False

        # Collect all primes
        for number in range(limit + 1):
            if is_prime[number]:
                primes.append(number)

        return primes


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    suite = DistinctAlgorithmSuite()

    # Execution of Day 1 Work (Heap Sort) ---
    unsorted_data = [12, 11, 13, 5, 6, 7]
    print(f"Original: {unsorted_data}")
    sorted_data = suite.heap_sort(unsorted_data)
    print(f"Heap Sort: {sorted_data}\n")

    # Execution of Day 2 Work (DFS)
    graph_data = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    path = suite.dfs_traversal(graph_data, 'A')
    print(f"DFS Path: {' -> '.join(path)}\n")

    # Execution of Day 3 Work (Sieve of Eratosthenes)
    limit = 50
    primes = suite.sieve_of_eratosthenes(limit)
    print(f"Primes up to {limit}: {primes}")