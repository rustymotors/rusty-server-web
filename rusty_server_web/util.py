from .ShardEntry import ShardEntry


def formatShardEntryForWeb(entry: ShardEntry):
    return (
        f"[{entry.shard_name}]\n"
        + f"\tDescription={entry.shard_description}\n"
        + f"\tShardId={entry.shard_id}\n"
        + f"\tLoginServerIP={entry.login_host}\n"
        + f"\tLoginServerPort={entry.login_port}\n"
        + f"\tLobbyServerIP={entry.lobby_host}\n"
        + f"\tLobbyServerPort={entry.lobby_port}\n"
        + f"\tMCOTSServerIP={entry.mcots_host}\n"
        + f"\tStatusId={entry.status_id}\n"
        + f"\tStatus_Reason={entry.status_reason}\n"
        + f"\tServerGroup={entry.server_group_name}\n"
        + f"\tPopulation={entry.population}\n"
        + f"\tMaxPersonasPerUser={entry.max_personas_per_user}\n"
        + f"\tDiagnosticServerHost={entry.diag_host}\n"
        + f"\tDiagnosticServerPort={entry.diag_port}\n"
    )


def formatShardEntriesForWeb(entries: list[ShardEntry]):
    return "\n".join([formatShardEntryForWeb(entry) for entry in entries]) + "\n"
