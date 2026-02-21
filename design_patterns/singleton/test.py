from singleton_logger import SingletonLogger
from os.path import join




def connect_to_db():
    logger = SingletonLogger("db.log")
    
    logger.log("Connecting to database")


def send_data_to_service():
    logger = SingletonLogger("service.log")
    
    logger.log("Sending data to data service")
    
def close_db_connection():
    logger = SingletonLogger("++ignore++")
    
    logger.log("Closing database connection")

def main():
    logger = SingletonLogger("app.log")
    
    connect_to_db()
    send_data_to_service()
    close_db_connection()

main()


if __name__ == "__main__":
    print(join(*list(__file__.split("\\")[:-1])))
    




    