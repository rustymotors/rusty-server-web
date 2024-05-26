from rusty_server_web.ShardEntry import ShardEntry


def getShardList():
    shard1 = ShardEntry(
        shard_id=1,
        shard_name="Shard 1",
        shard_description="The first shard",
        login_host="rustyshard1.com",
        login_port=1234,
        lobby_host="rustyshard1.com",
        lobby_port=1234,
        mcots_host="rustyshard1.com",
        status_id=0,
        status_reason="",
        server_group_name="",
        population=0,
        max_personas_per_user=0,
        diag_host="rustyshard1.com",
        diag_port=1234,
    )

    shard2 = ShardEntry(
        shard_id=2,
        shard_name="Shard 2",
        shard_description="The second shard",
        login_host="rustyshard2.com",
        login_port=1234,
        lobby_host="rustyshard2.com",
        lobby_port=1234,
        mcots_host="rustyshard2.com",
        status_id=0,
        status_reason="",
        server_group_name="",
        population=0,
        max_personas_per_user=0,
        diag_host="rustyshard2.com",
        diag_port=1234,
    )

    shard3 = ShardEntry(
        shard_id=3,
        shard_name="Shard 3",
        shard_description="The third shard",
        login_host="rustyshard3.com",
        login_port=1234,
        lobby_host="rustyshard3.com",
        lobby_port=1234,
        mcots_host="rustyshard3.com",
        status_id=0,
        status_reason="",
        server_group_name="",
        population=0,
        max_personas_per_user=0,
        diag_host="rustyshard3.com",
        diag_port=1234,
    )

    shard4 = ShardEntry(
        shard_id=4,
        shard_name="Shard 4",
        shard_description="The fourth shard",
        login_host="rustyshard4.com",
        login_port=1234,
        lobby_host="rustyshard4.com",
        lobby_port=1234,
        mcots_host="rustyshard4.com",
        status_id=0,
        status_reason="",
        server_group_name="",
        population=0,
        max_personas_per_user=0,
        diag_host="rustyshard4.com",
        diag_port=1234,
    )

    shard5 = ShardEntry(
        shard_id=5,
        shard_name="Shard 5",
        shard_description="The fifth shard",
        login_host="rustyshard5.com",
        login_port=1234,
        lobby_host="rustyshard5.com",
        lobby_port=1234,
        mcots_host="rustyshard5.com",
        status_id=0,
        status_reason="",
        server_group_name="",
        population=0,
        max_personas_per_user=0,
        diag_host="rustyshard5.com",
        diag_port=1234,
    )

    shard6 = ShardEntry(
        shard_id=6,
        shard_name="Shard 6",
        shard_description="The sixth shard",
        login_host="rustyshard6.com",
        login_port=1234,
        lobby_host="rustyshard6.com",
        lobby_port=1234,
        mcots_host="rustyshard6.com",
        status_id=0,
        status_reason="",
        server_group_name="",
        population=0,
        max_personas_per_user=0,
        diag_host="rustyshard6.com",
        diag_port=1234,
    )
    
    return [shard1, shard2, shard3, shard4, shard5, shard6]
