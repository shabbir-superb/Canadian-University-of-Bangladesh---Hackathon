"""
Distributed Key-Value Store Solution
A simplified implementation of a distributed key-value store with versioning.
"""
from typing import Any, Dict, List, Optional
import time

class DistributedKVStore:
    """
    A simple distributed key-value store with versioning.
    
    This is a simplified implementation that simulates a distributed environment.
    In a real-world scenario, this would involve network calls and consensus protocols.
    """
    
    def __init__(self, nodes: List[str]):
        """
        Initialize the distributed KV store with a list of node addresses.
        
        Args:
            nodes (List[str]): List of node addresses (e.g., ["node1:8080", "node2:8080"])
        """
        self.nodes = nodes
        # Simulate storage for each node
        self.data = {node: {} for node in nodes}
        self.version = 0  # Global version counter
    
    def put(self, key: str, value: Any) -> int:
        """
        Store a key-value pair in the distributed store.
        
        Args:
            key (str): The key to store
            value (Any): The value to store
            
        Returns:
            int: The version number of this write
        """
        self.version += 1
        timestamp = time.time()
        
        # In a real implementation, this would involve network calls to each node
        # Here we're simulating a synchronous write to all nodes for simplicity
        for node in self.nodes:
            if key not in self.data[node]:
                self.data[node][key] = {}
            self.data[node][key]['value'] = value
            self.data[node][key]['version'] = self.version
            self.data[node][key]['timestamp'] = timestamp
            
        return self.version
    
    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a value from the distributed store.
        
        In a real implementation, this might use read repair or other consistency mechanisms.
        
        Args:
            key (str): The key to retrieve
            
        Returns:
            Optional[Any]: The value if found, None otherwise
        """
        # Simulate reading from all nodes and returning the latest version
        latest = None
        
        for node in self.nodes:
            if key in self.data[node]:
                node_data = self.data[node][key]
                if latest is None or node_data['version'] > latest['version']:
                    latest = node_data
        
        return latest['value'] if latest else None
    
    def get_with_metadata(self, key: str) -> Optional[Dict]:
        """
        Retrieve a value along with its metadata from the distributed store.
        
        Args:
            key (str): The key to retrieve
            
        Returns:
            Optional[Dict]: A dictionary containing 'value', 'version', and 'timestamp' if found, None otherwise
        """
        latest = None
        
        for node in self.nodes:
            if key in self.data[node]:
                node_data = self.data[node][key]
                if latest is None or node_data['version'] > latest['version']:
                    latest = node_data
        
        return latest


if __name__ == "__main__":
    # Example usage
    nodes = ["node1:8080", "node2:8080", "node3:8080"]
    kv_store = DistributedKVStore(nodes)
    
    # Test basic operations
    version = kv_store.put("user:1", {"name": "Alice", "email": "alice@example.com"})
    print(f"Stored value at version {version}")
    
    value = kv_store.get("user:1")
    print(f"Retrieved value: {value}")
    
    # Test versioning
    kv_store.put("user:1", {"name": "Alice Smith", "email": "alice@example.com"})
    
    value_with_meta = kv_store.get_with_metadata("user:1")
    print(f"Retrieved value with metadata: {value_with_meta}")
