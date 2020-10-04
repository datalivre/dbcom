#!/usr/local/bin/python3.6
# _*_ coding:utf-8 _*_
# ----------------------------------------- #
# @author Robert Carlos                     #
# email robert.carlos@linuxmail.org         #
# 2020-set (CC BY 3.0 BR)                   #

import logging
import sys

from pyspark.sql import SparkSession

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
log = logging.getLogger(__name__)
path = "lib"


def conn(sql_credenctials, red_credentials, database, tables):
    spark = (SparkSession.builder.master('local[*]')
             .appName('Py Count')
             .config("spark.driver.extraClassPath", f"{path}/mssql-jdbc-6.2.2.jre8.jar:{path}/postgresql-42.2.6.jar")
             .getOrCreate())
    resultado_tb = []
    log.info(f"Iniciando a verificação")
    for table in [t.strip() for t in tables.split(',')]:
        count = []
        count.append(table)
        for cred in [sql_credenctials, red_credentials]:
            for row in spark.read.jdbc(url=cred["url"], table=f"(SELECT count(*) {cred['name']}_{table} FROM {cred['schema']}.{table}) foo", properties=cred).collect():
                count.append(row[f"{cred['name']}_{table}"])
        resultado_tb.append(count)
    log.info(f"Retornando resultados")
    return resultado_tb


if __name__ == "__main__":
    pass
