from sqlalchemy import quoted_name


def get_updated_at_trigger_executable(trigger_name: str, table_name: str) -> str:
    safe_table = quoted_name(table_name, True)
    safe_trigger = quoted_name(trigger_name, True)

    return f"""
                CREATE TRIGGER {safe_trigger}
                BEFORE UPDATE ON {safe_table}
                FOR EACH ROW
                EXECUTE FUNCTION trigger_set_timestamp_on_update();
            """

def get_drop_trigger_executable(trigger_name: str, table_name: str) -> str:
    safe_table = quoted_name(table_name, True)
    safe_trigger = quoted_name(trigger_name, True)

    return f"""
                DROP TRIGGER IF EXISTS {safe_trigger} ON {safe_table};
            """