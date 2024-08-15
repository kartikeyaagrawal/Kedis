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
```


### 🏃‍♂️ Usage

To start the Kedis server, run:

```bash
python kedis_server.py
```

To interact with the Kedis server, use the Kedis CLI:
```bash
python kedis_cli.py
```

## 📜 Commands

Kedis supports a subset of Redis commands. Here are a few examples:

- **`SET key value`**: Set a key-value pair.
- **`GET key`**: Retrieve the value associated with the key.
- **`DEL key`**: Delete a key.
- **`PUBLISH channel message`**: Publish a message to a channel.
- **`SUBSCRIBE channel`**: Subscribe to a channel.


## 🛠 Development

To contribute to Kedis, follow these steps:

1. **Fork the Repository**: Create a personal fork of the Kedis repository on GitHub.
2. **Clone Your Fork**:
    ```bash
    git clone https://github.com/yourusername/kedis.git
    ```
3. **Create a Branch**:
    ```bash
    git checkout -b feature/your-feature
    ```
4. **Commit Your Changes**:
    ```bash
    git commit -am 'Add new feature'
    ```
5. **Push to Your Fork**:
    ```bash
    git push origin feature/your-feature
    ```
6. **Create a Pull Request**: Open a pull request on the main repository.

## 🤝 Contributing

We welcome contributions from the community! If you have suggestions, bug reports, or feature requests, please open an issue on GitHub.

## 📝 License

Kedis is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

## 📞 Contact

For any questions or feedback, you can reach out to the project maintainer:

- **Kartikeya Agrawal**
- Email: [kartikeyaagrawal000@gmail.com](mailto:kartikeyaagrawal000@gmail.com)
- LinkedIn: [Kartikeya Agrawal](https://linkedin.com/in/kartikeya-agrawal/)
