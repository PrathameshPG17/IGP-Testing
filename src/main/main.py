from pyspark.sql import SparkSession
import os
import sys


# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from databases.connect_mysql import *


def main():
    
    spark = get_spark_session()

    query = """
        (
            SELECT orders_id,
                DATE(date_purchased) as Dt,
                customers_id,
                customers_email_address,
                SUM(orders_product_total_inr + shipping_cost_in_inr) AS Revenue 
            FROM igpnew.orders 
            WHERE date_purchased >= '2025-02-01 00:00:00'
                AND date_purchased <= '2025-02-01 23:59:59'
                AND fk_associate_id = 5 
                AND microsite_fk_associate_id = 0 
                AND orders_product_total_inr > 0 
                AND orders_status != 'Cancelled' 
            GROUP BY orders_id
        ) AS subquery
        """
    df_spark = fetch_data_from_mysql(spark,query)
    df_spark.show()


if __name__ == "__main__":
    main()


    