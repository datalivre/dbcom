#!/usr/local/bin/python3.6
# _*_ coding:utf-8 _*_
# ----------------------------------------- #
# @author Robert Carlos                     #
# email robert.carlos@linuxmail.org         #
# 2020-set (CC BY 3.0 BR)                   #

from simplecrypt import decrypt, encrypt


def decodex(pwd, string):
    dicio = dict()
    for k, v in string.items():
        dicio[k] = decrypt(pwd, v).decode('utf8') if any(
            map(lambda x: x in k, ['user', 'password'])) else v
    return dicio


def codex(pwd, string):
    return encrypt(pwd, string.encode('utf8'))


if __name__ == '__main__':
    pass
