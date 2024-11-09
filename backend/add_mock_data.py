import pandas as pd
from schemas.database_init import create_db_and_tables, get_session


def main():
    print("HIII")
    engine = create_db_and_tables()
    with engine.connect() as connection:

        mock_user = pd.read_csv("./mock_data/user.csv", sep="\t")
        mock_user.to_sql(name="user", con=connection, if_exists='append', index=False)

        mock_api = pd.read_csv("./mock_data/api.csv", sep="\t")
        mock_api.to_sql(name="api", con=connection, if_exists='append', index=False)

        mock_ticket = pd.read_csv("./mock_data/ticket.csv", sep="\t")
        mock_ticket.to_sql(name="ticket", con=connection, if_exists='append', index=False)

        mock_comment = pd.read_csv("./mock_data/comment.csv", sep="\t")
        mock_comment.to_sql(name="comment", con=connection, if_exists='append', index=False)

        mock_sub = pd.read_csv("./mock_data/ticket_subs.csv", sep="\t")
        mock_sub.to_sql(name="ticket_subscription", con=connection, if_exists='append', index=False)

        mock_update = pd.read_csv("./mock_data/update.csv", sep="\t")
        mock_update.to_sql(name="update", con=connection, if_exists='append', index=False)


    engine.dispose()
    print("Done")

if __name__ == "__main__":
    main()