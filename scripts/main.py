from extract import extract_data
from transform import transform_data
from load import load_data
from db_connection import get_engine
from logger_config import setup_logger


logger = setup_logger()


def main():

    logger.info("ETL pipeline started.")

    try:

        # EXTRACT
        df = extract_data("data/sales.csv")
        logger.info("Data extracted successfully.")

        # TRANSFORM
        df = transform_data(df)
        logger.info("Data transformed successfully.")

        # DATABASE CONNECTION
        engine = get_engine()
        logger.info("Database connection created.")

        # LOAD
        load_data(df, "sales", engine)
        logger.info("Data loaded successfully.")

        logger.info("ETL pipeline completed successfully.")

    except Exception as e:

        logger.error(f"ETL pipeline failed: {e}")

        raise


if __name__ == "__main__":
    main()