def load_data(df, table_name, engine):

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully!")