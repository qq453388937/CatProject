# -*- coding:utf-8 -*-
import redis
from rediscluster import *
import time


class RedisHelper():
    def __init__(self, host='localhost', port=6379):
        self.__redis = redis.StrictRedis(host, port)
    
    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""
    
    def set(self, key, value):
        """

        :param key:
        :param value:
        :return: 返回 True 表示成功
        """
        ret = self.__redis.set(key, value)
        return ret
    
    def delete(self, key):
        self.__redis.delete(key)


def main():
    # r = RedisHelper()
    # r.get() r.set()
    # r.pipeline()
    # 缓冲多条命令，然后一次性执行，减少服务器-客户端之间TCP数据库包，从而提高效率
    try:
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
    except Exception as e:
        print(e.message)
        raise e  # 抛出异常
    pipe = r.pipeline()
    pipe.set('name', 'world')
    pipe.set('age', 18)
    time.sleep(10)
    # pipe.get('name')
    pipe.execute()  # 一次缓冲多条命令一次执行
    # r.set("mmd","666")
    print("ok")
    
    
def cluster():
    try:
        # 构建所有的节点，Redis会使⽤CRC16算法，将键和值写到某个节点上
        startup_nodes = [
            {'host': '192.168.26.128', 'port': '7000'},
            {'host': '192.168.26.130', 'port': '7003'},
            {'host': '192.168.26.128', 'port': '7001'},
        ]
        # 构建StrictRedisCluster对象
        src = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        # 设置键为name、值为itheima的数据
        result = src.set('name', 'itheima')
        print(result)
        # 获取键为name
        name = src.get('name')
        print(name)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
    
    
