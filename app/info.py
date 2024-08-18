class RedisReplicationInfo:
    def __init__(self, role="master", connected_slaves=0, master_replid="8371b4fb1155b71f4a04d3e1bc3e18c4a990aeeb",
                 master_repl_offset=0, second_repl_offset=-1, repl_backlog_active=0,
                 repl_backlog_size=1048576, repl_backlog_first_byte_offset=0,
                 repl_backlog_histlen=0):
        self.role = role
        self.connected_slaves = connected_slaves
        self.master_replid = master_replid
        self.master_repl_offset = master_repl_offset
        self.second_repl_offset = second_repl_offset
        self.repl_backlog_active = repl_backlog_active
        self.repl_backlog_size = repl_backlog_size
        self.repl_backlog_first_byte_offset = repl_backlog_first_byte_offset
        self.repl_backlog_histlen = repl_backlog_histlen

    def __str__(self):
        return (f"Role: {self.role}\n"
                f"Connected Slaves: {self.connected_slaves}\n"
                f"Master Replication ID: {self.master_replid}\n"
                f"Master Replication Offset: {self.master_repl_offset}\n"
                f"Second Replication Offset: {self.second_repl_offset}\n"
                f"Replication Backlog Active: {self.repl_backlog_active}\n"
                f"Replication Backlog Size: {self.repl_backlog_size}\n"
                f"Replication Backlog First Byte Offset: {self.repl_backlog_first_byte_offset}\n"
                f"Replication Backlog History Length: {self.repl_backlog_histlen}")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @staticmethod
    def default_values_as_str():
        return (f"role: master\n"
                f"connected_slaves: 0\n"
                f"master_replid: 8371b4fb1155b71f4a04d3e1bc3e18c4a990aeeb\n"
                f"master_repl_offset: 0\n"
                f"second_repl_offset: -1\n"
                f"repl_backlog_active: 0\n"
                f"repl_backlog_size: 1048576\n"
                f"repl_backlog_first_byte_offset: 0\n"
                f"repl_backlog_histlen: 0")

# # Example usage
# if __name__ == "__main__":
#     # Create an instance with default values
#     replication_info = RedisReplicationInfo(
#         master_replid="8371b4fb1155b71f4a04d3e1bc3e18c4a990aeeb"
#     )

#     # Print the current state
#     print(replication_info)

#     # Update some attributes
#     replication_info.update(
#         connected_slaves=5,
#         master_repl_offset=123456,
#         repl_backlog_histlen=789012
#     )

#     # Print the updated state
#     print("\nUpdated State:")
#     print(replication_info)