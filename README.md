# Kedis: A Python Redis Clone

Welcome to **Kedis**, a Python-based Redis clone designed to emulate core Redis functionalities. Kedis aims to provide a simple yet powerful key-value store with a focus on ease of use and performance.

## 🚀 Features

- **Key-Value Storage**: Store and retrieve data with various data types.
- **Persistence**: Options for snapshotting and AOF (Append-Only File) persistence.
- **Pub/Sub**: Implement publish and subscribe messaging.
- **Transactions**: Support for multi-command transactions.
- **Replication**: Basic master-slave replication for high availability.
- **Lua Scripting**: Execute Lua scripts for server-side logic.
- **Atomic Operations**: Support for atomic operations on keys.

## 🔧 Installation

### Prerequisites

- **Python**: Ensure you have Python 3.6 or higher installed.
- **Dependencies**: Required Python packages will be managed with `requirements.txt`.

### Install Dependencies

```bash
git clone https://github.com/yourusername/kedis.git
cd kedis
pip install -r requirements.txt
🏃‍♂️ Usage
To start the Kedis server, run:

bash
Copy code
python kedis_server.py
To interact with the Kedis server, use the Kedis CLI:

bash
Copy code
python kedis_cli.py
📜 Commands
Kedis supports a subset of Redis commands. Here are a few examples:

SET key value: Set a key-value pair.
GET key: Retrieve the value associated with the key.
DEL key: Delete a key.
PUBLISH channel message: Publish a message to a channel.
SUBSCRIBE channel: Subscribe to a channel.
🛠 Development
To contribute to Kedis, follow these steps:

Fork the Repository: Create a personal fork of the Kedis repository on GitHub.
Clone Your Fork: git clone https://github.com/yourusername/kedis.git
Create a Branch: git checkout -b feature/your-feature
Commit Your Changes: git commit -am 'Add new feature'
Push to Your Fork: git push origin feature/your-feature
Create a Pull Request: Open a pull request on the main repository.
🤝 Contributing
We welcome contributions from the community! If you have suggestions, bug reports, or feature requests, please open an issue on GitHub.

📝 License
Kedis is licensed under the MIT License. See the LICENSE file for details.

📞 Contact
For any questions or feedback, you can reach out to the project maintainer:

Kartikeya Agrawal
Email: kartikeyaagrawal000@gmail.com
LinkedIn: Kartikeya Agrawal