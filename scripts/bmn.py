"""
命令接口定义
"""

import click


@click.command()
def bmn():
    """
    命令接口,help文档
    """
    print("bmn")
