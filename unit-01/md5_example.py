import hashlib


def demonstrate_md5_hashing():
    # Example 1: Basic string hashing
    # Create a sample input string
    input_string = "Hello, World!"

    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Convert the string to bytes (required for hashing)
    # In Python, we must encode strings to bytes before hashing
    input_bytes = input_string.encode("utf-8")

    # Update the hash object with our input
    md5_hash.update(input_bytes)

    # Get the hexadecimal representation of the hash
    hash_result = md5_hash.hexdigest()

    print(f"Input string: {input_string}")
    print(f"MD5 hash: {hash_result}")
    print(f"Hash length: {len(hash_result)} characters")

    # Example 2: Demonstrating how the same input always produces the same hash
    print("\nDemonstrating hash consistency:")
    print(
        f"Hash of 'Hello, World!': {hashlib.md5('Hello, World!'.encode('utf-8')).hexdigest()}"
    )
    print(
        f"Hash of 'Hello, World!': {hashlib.md5('Hello, World!'.encode('utf-8')).hexdigest()}"
    )

    # Example 3: Demonstrating how small changes produce completely different hashes
    print("\nDemonstrating avalanche effect:")
    print(
        f"Hash of 'Hello, World!': {hashlib.md5('Hello, World!'.encode('utf-8')).hexdigest()}"
    )
    print(
        f"Hash of 'Hello, World.': {hashlib.md5('Hello, World.'.encode('utf-8')).hexdigest()}"
    )


if __name__ == "__main__":
    demonstrate_md5_hashing()
