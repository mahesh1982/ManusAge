from backend.common.config.db_connection import get_db_connection

async def load_active_prompt(prompt_name: str):
    conn = await get_db_connection()

    row = await conn.fetchrow(
        """
        SELECT content 
        FROM prompt_versions
        WHERE prompt_name = $1 AND is_active = TRUE
        ORDER BY version DESC
        LIMIT 1;
        """,
        prompt_name
    )

    await conn.close()

    if row:
        return row["content"]

    return None
