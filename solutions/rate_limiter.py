"""
Rate Limiter Solution
Implements a token bucket rate limiter that allows a certain number of requests
per time window per user.
"""
import time
from collections import defaultdict

class RateLimiter:
    """
    A rate limiter that uses the token bucket algorithm to limit the number of
    requests a user can make within a given time window.
    
    The token bucket algorithm works by adding tokens to a bucket at a fixed rate.
    Each request consumes a token from the bucket. If the bucket is empty,
    the request is rate-limited.
    """
    
    def __init__(self, capacity: int, refill_rate: float):
        """
        Initialize the rate limiter.
        
        Args:
            capacity (int): Maximum number of tokens the bucket can hold
            refill_rate (float): Number of tokens added to the bucket per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = defaultdict(lambda: capacity)  # User ID -> current tokens
        self.last_refill = defaultdict(time.time)    # User ID -> last refill time
    
    def is_allowed(self, user_id: str) -> bool:
        """
        Check if a request from the given user is allowed.
        
        Args:
            user_id (str): Unique identifier for the user
            
        Returns:
            bool: True if the request is allowed, False if rate-limited
        """
        current_time = time.time()
        time_passed = current_time - self.last_refill[user_id]
        
        # Calculate how many tokens to add based on time passed
        tokens_to_add = time_passed * self.refill_rate
        
        # Refill the bucket, but don't exceed capacity
        self.tokens[user_id] = min(
            self.capacity,
            self.tokens[user_id] + tokens_to_add
        )
        
        # Update the last refill time
        self.last_refill[user_id] = current_time
        
        # Check if there are enough tokens for this request
        if self.tokens[user_id] >= 1:
            self.tokens[user_id] -= 1
            return True
        return False
    
    def get_remaining_tokens(self, user_id: str) -> float:
        """
        Get the number of remaining tokens for a user.
        
        Args:
            user_id (str): The user ID to check
            
        Returns:
            float: Number of tokens remaining
        """
        # Calculate tokens that would be added since last refill
        if user_id not in self.tokens:
            return self.capacity
            
        current_time = time.time()
        time_passed = current_time - self.last_refill[user_id]
        tokens_to_add = time_passed * self.refill_rate
        
        # Calculate current tokens without modifying state
        current_tokens = min(
            self.capacity,
            self.tokens[user_id] + tokens_to_add
        )
        
        return current_tokens


if __name__ == "__main__":
    # Example usage
    # Allow 10 requests per minute per user (1 request every 6 seconds on average)
    rate_limiter = RateLimiter(capacity=10, refill_rate=10/60)  # 10 tokens, refill 10 per minute
    
    # Simulate a user making requests
    user_id = "user123"
    
    print("Testing rate limiter with 15 requests...")
    for i in range(1, 16):
        allowed = rate_limiter.is_allowed(user_id)
        remaining = rate_limiter.get_remaining_tokens(user_id)
        print(f"Request {i}: {'Allowed' if allowed else 'Rate limited'}, Remaining tokens: {remaining:.2f}")
        
        # Sleep for a short time between requests
        time.sleep(0.5)
    
    print("\nWaiting for tokens to refill...")
    time.sleep(30)  # Wait 30 seconds for tokens to refill
    
    print("\nTesting again after waiting:")
    for i in range(1, 4):
        allowed = rate_limiter.is_allowed(user_id)
        remaining = rate_limiter.get_remaining_tokens(user_id)
        print(f"Request {i}: {'Allowed' if allowed else 'Rate limited'}, Remaining tokens: {remaining:.2f}")
