
class ShardEntry:
    def __init__(self, shard_id, shard_name, shard_description, login_host, login_port, lobby_host, lobby_port, mcots_host, status_id, status_reason, server_group_name, population, max_personas_per_user, diag_host, diag_port):
        self.shard_id = shard_id
        self.shard_name = shard_name
        self.shard_description = shard_description
        self.login_host = login_host
        self.login_port = login_port
        self.lobby_host = lobby_host
        self.lobby_port = lobby_port
        self.mcots_host = mcots_host
        self.status_id = status_id
        self.status_reason = status_reason
        self.server_group_name = server_group_name
        self.population = population
        self.max_personas_per_user = max_personas_per_user
        self.diag_host = diag_host
        self.diag_port = diag_port

    def to_dict(self):
        return {
            'shard_id': self.shard_id,
            'shard_name': self.shard_name,
            'shard_description': self.shard_description,
            'shard_url': self.shard_url,
            'login_host': self.login_host,
            'login_port': self.login_port,
            'lobby_host': self.lobby_host,
            'lobby_port': self.lobby_port,
            'mcots_host': self.mcots_host,
            'status_id': self.status_id,
            'status_reason': self.status_reason,
            'server_group_name': self.server_group_name,
            'population': self.population,
            'max_personas_per_user': self.max_personas_per_user,
            'diag_host': self.diag_host,
            'diag_port': self.diag_port
        }
