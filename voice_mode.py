def get_tts_config(session_id: str, openai_key: str) -> TTSConfig:
    """Get or create a TTSConfig instance for the given session_id."""
    if session_id is None:
        raise ValueError("session_id cannot be None")

    try:
        return tts_config_cache[session_id]
    except KeyError:
        tts_config = TTSConfig(session_id, openai_key)
        tts_config_cache[session_id] = tts_config
        return tts_config
