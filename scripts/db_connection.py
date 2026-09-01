from sqlalchemy import create_engine


def get_engine():

    username = "postgres"
    password = "0852"
    host = "localhost"
    port = "5432"
    database = "ecommerce_db"

    connection_string = (
        f"postgresql+psycopg2://{username}:{password}"
        f"@{host}:{port}/{database}"
    )

    engine = create_engine(connection_string)

    return engine