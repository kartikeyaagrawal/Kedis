kedis: A Lightweight In-Memory Data Store

Introduction:

kedis is a lightweight in-memory data store inspired by Redis. It offers basic key-value storage with features like string and list data types. Built as a learning project or a simple data store for small-scale applications, kedis provides a foundation for understanding key-value data structures and in-memory storage concepts.

Features

Key-Value Storage: Stores data associated with unique keys.
String Data Type: Handles basic strings for various uses.
List Data Type: Manages ordered collections of elements.
In-Memory Persistence: Data resides in memory for fast access but is lost upon process termination. (Consider persistent storage for production use.)
Getting Started

Prerequisites

A C compiler (e.g., GCC, Clang)
Basic understanding of C programming
Building

Clone this repository:

Bash
git clone https://your-github-repository/kedis.git
Use code with caution.

Navigate to the project directory:

Bash
cd kedis
Use code with caution.

Build the kedis executable:

Bash
make
Use code with caution.

This will create the kedis executable in the current directory.

Running

Bash
./kedis
Use code with caution.

This will start the kedis server.

Usage

kedis accepts commands on its standard input (stdin). Each command consists of a keyword and optional arguments, separated by spaces.

Supported Commands

SET key value

Sets the value associated with the specified key.
Example: SET name Alice
GET key

Retrieves the value associated with the key.
Example: GET name
LPUSH key element

Inserts an element at the head of the list identified by the key.
If the key doesn't exist, it creates a new list.
Example: LPUSH colors red
RPUSH key element

Inserts an element at the tail of the list identified by the key.
If the key doesn't exist, it creates a new list.
Example: RPUSH colors blue
LRANGE key start end

Returns a range of elements from the list identified by the key.
start and end are zero-based indices.
Example: LRANGE colors 0 1 (returns the first two elements)
QUIT

Exits the kedis server.
Example Session

SET name Alice
GET name
# Output: Alice
LPUSH colors red
RPUSH colors blue
LRANGE colors 0 1
# Output: red blue
QUIT
Limitations

In-memory persistence: Data is lost when the process terminates.
Basic features: Limited to strings and lists for this learning implementation.
Future Considerations

Persistence options: Explore mechanisms for data persistence (e.g., file-based storage).
Additional data types: Consider implementing more complex data structures (e.g., sets, hashes).
Advanced features: Expand the functionality with features like TTL (Time-to-Live) for key expiration.
Contributing

Feel free to submit pull requests with enhancements or bug fixes. This project welcomes contributions for ongoing development.

License

This project is licensed under the MIT License.

Enjoy building and exploring kedis!