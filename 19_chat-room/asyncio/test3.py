"""
并发和并行
并行：多个任务在同一时刻进行，多个cou同时执行多个任务
并发：多个任务在同一时间循环进行，一个cpu交替执行多个任务
"""
import asyncio
import time


def now():
    return time.time()


async def do_some_work(x):
    print("Waiting:",x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)


start = now()
cor1 = do_some_work(1)
cor2 = do_some_work(2)
cor3 = do_some_work(4)
# 将多个协程创建为task对象，放置于列表中
# task对象能够记录协程的执行状态及结果
tasks = [asyncio.ensure_future(cor1),
         asyncio.ensure_future(cor2),
         asyncio.ensure_future(cor3)
         ]
loop = asyncio.get_event_loop()
# 以下两种方式一样。gather方法更为高级
# asyncio.wait并发执行多个任务
# loop.run_until_complete(asyncio.wait(tasks))
loop.run_until_complete(asyncio.gather(*tasks))
for task in tasks:
    print("Task ret:", task.result())

print("Time:", now() - start )

"""
程序运行总的时间大概在4s左右，如果是不是使用协程的方式来异步执行，按照同步顺序执行，
只有当第一个执行完成，才能执行第二个，第二个执行完成才能执行第三个，这样总时间至少需要7s
"""