from redsift_client import *
import time

if __name__ == '__main__':
    # data = load_numbers_in_stream("seq01")
    # print(data)

    start_time = time.time()

    cursor = conn().cursor()

    # for number in load_numbers_in_stream("seq01"):
    for number in range(31, 99):
        query = read_query(number)
        print(query)
        cursor.execute(query)
        rows = cursor.fetchall()
        print("query {} is done".format(number))

    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    close_conn(cursor, conn)
