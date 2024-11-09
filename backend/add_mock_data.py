import pandas as pd
from schemas.database_init import create_db_and_tables, get_session


def main():
    print("HIII")
    engine = create_db_and_tables()
    with engine.connect() as connection:

        mock_tickets = pd.read_csv("./mock_data/tickets.csv", sep="\t")
        mock_tickets.to_sql(name="ticket", con=connection, if_exists='append', index=False)

    engine.dispose()
    print("Done")

if __name__ == "__main__":
    main()