from rusty_server_web.ShardEntry import ShardEntry


def getShardList():
    shard2 = ShardEntry(
        shard_id=2,
        shard_name="Shard 2",
        shard_description="The second shard",
        login_host="rusty-motors.com",
        login_port=8226,
        lobby_host="rusty-motors.com",
        lobby_port=7003,
        mcots_host="rusty-motors.com",
        status_id=0,
        status_reason="",
        server_group_name="",
        population=0,
        max_personas_per_user=0,
        diag_host="rusty-motors.com",
        diag_port=1234,
    )

    return [shard2]
