#!/usr/local/bin/python3.6
# _*_ coding:utf-8 _*_
# ----------------------------------------- #
# @author Robert Carlos                     #
# email robert.carlos@linuxmail.org         #
# 2020-set (CC BY 3.0 BR)                   #

from simplecrypt import decrypt, encrypt


def get_string(conn_string, args):
    return {
        'sqlserver': {
            'ab_dev': {
                'name': 'sqlserver',
                'user': b'nome de usuário criptografado',
		'password': b'password criptografado'
                'driver': 'com.microsoft.sqlserver.jdbc.SQLServerDriver',
                'url': f'jdbc:sqlserver://IP\DESENV:PORT;databaseName={args.database}',
                'schema': 'dbo'
            }
            'ab_hml': {
                'name': 'sqlserver',
                'user': b'nome de usuário criptografado',
		'password': b'password criptografado'
                'driver': 'com.microsoft.sqlserver.jdbc.SQLServerDriver',
                'url': f'jdbc:sqlserver://IP\QUALID:PORT;databaseName={args.database}',
                'schema': 'dbo'
            },
            'ab_prd': {
                'name': 'sqlserver',
                'user': b'nome de usuário criptografado',
                'password':  b'password criptografado',
                'driver': 'com.microsoft.sqlserver.jdbc.SQLServerDriver',
                'url': f'jdbc:sqlserver://IP\EXTRATOR:PORT;databaseName={args.database}',
                'schema': 'dbo'
            }
        },
        'redshift': {
            'dev': {
                'name': 'redshift',
                'tempdir': 's3://dev-redshift-tempdir',
                'password':  b'password criptografado',
                'user': b'nome de usuário criptografado',
                'url': 'jdbc:postgresql://string_de_conexão:porta/database',
                "schema": f"spectrum_{args.database}_{args.category}_mobile"
            },
            'hml': {
                'name': 'redshift',
                'tempdir': 's3://hml-redshift-tempdir',
                'password':  b'password criptografado',
                'user': b'nome de usuário criptografado',
                'url': 'jdbc:postgresql://string_de_conexão:porta/database',
                "schema": f"spectrum_{args.database}_{args.category}_mobile"
            },
            'prd': {
                'name': 'redshift',
                'tempdir': 's3://prd-redshift-tempdir',
                'password':  b'password criptografado',
                'user': b'nome de usuário criptografado',
                'url': 'jdbc:postgresql://string_de_conexão:porta/database',
                "schema": f"spectrum_{args.database}_{args.category}_mobile"
            },
        }
    }.get(conn_string)[f'{args.category}_{args.ambiente}' if conn_string == 'sqlserver' else f'{args.ambiente}']


if __name__ == '__main__':
    pass
