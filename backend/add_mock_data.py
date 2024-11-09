import pandas as pd
from schemas.database_init import create_db_and_tables, get_session





def main():
    print("HIII")
    engine = create_db_and_tables()
    with engine.connect() as connection:
        mock_up = pd.read_csv("./mock_data/tickets.csv", sep="\t")
        print(len(mock_up["id"].unique()), len(mock_up))
        mock_up.to_sql(name="ticket", con=connection, if_exists='append', index=False)
    engine.dispose()
    print("Done")

if __name__ == "__main__":
    main()