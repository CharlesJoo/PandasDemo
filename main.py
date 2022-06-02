import pandas as pd
import pymysql.cursors


def get_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           database='collection',
                           cursorclass=pymysql.cursors.DictCursor)


def bulk_insert(values):
    insert_sql = '''INSERT INTO `collection`.`data_t` (
                                                        `year`, 
                                                        `imp_exp_flag`, 
                                                        `trade_type_code`, 
                                                        `trade_type_name`, 
                                                        `prosumer_country_code`, 
                                                        `prosumer_country_name`, 
                                                        `product_code`, 
                                                        `product_name`, 
                                                        `biz_unit_code`, 
                                                        `biz_unit_name`, 
                                                        `amount`
                                                        ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    connection = get_connection()
    with connection:
        cursor = connection.cursor()
        cursor.executemany(insert_sql, values)
        connection.commit()


def main():
    # max rows can be read from files every time
    chunk_size = 10000
    reader = pd.read_csv('data.txt', encoding='gbk', delimiter='\t', header=0, chunksize=chunk_size)
    for df in reader:
        values = df.itertuples(index=False, name=None)
        bulk_insert(tuple(values))


if __name__ == '__main__':
    main()
