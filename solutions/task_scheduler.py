"""
Task Scheduler Solution
Calculates the minimum time required to complete all tasks with a cooldown period
between identical tasks.
"""
from collections import Counter
from typing import List

def least_interval(tasks: List[str], cooldown: int) -> int:
    """
    Calculate the minimum time required to complete all tasks.
    
    Args:
        tasks (List[str]): List of tasks where each task is represented by a character
        cooldown (int): Cooldown period between identical tasks
        
    Returns:
        int: Minimum number of time units needed to complete all tasks
    """
    if not tasks:
        return 0
    
    # Count frequency of each task
    task_counts = Counter(tasks).values()
    
    # Find the maximum frequency
    max_count = max(task_counts)
    
    # Count how many tasks have the maximum frequency
    max_tasks = sum(1 for count in task_counts if count == max_count)
    
    # Calculate the minimum time required
    # Formula: (max_count - 1) * (cooldown + 1) + max_tasks
    # But we also need to handle the case where the number of tasks is greater than this value
    return max(len(tasks), (max_count - 1) * (cooldown + 1) + max_tasks)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (["A","A","A","B","B","B"], 2),  # Should return 8
        (["A","A","A","B","B","B"], 0),  # Should return 6 (no cooldown needed)
        (["A","A","A","A","A","A","B","C","D","E","F","G"], 2),  # Should return 16
    ]
    
    for tasks, n in test_cases:
        result = least_interval(tasks, n)
        print(f"Tasks: {tasks}")
        print(f"Cooldown: {n}")
        print(f"Minimum intervals needed: {result}\n")
