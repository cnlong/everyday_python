"""
协程嵌套

"""
import asyncio
import time


def now():
    return time.time()


async def do_some_work(x):
    print("Waiting:",x)
    await asyncio.sleep(x)
    # time.sleep(x)
    return "Done after {}s".format(x)


async def main():
    cor1 = do_some_work(1)
    cor2 = do_some_work(2)
    cor3 = do_some_work(4)
    tasks = [asyncio.ensure_future(cor1),
             asyncio.ensure_future(cor2),
             asyncio.ensure_future(cor3)
             ]
    await asyncio.wait(tasks)
    for task in tasks:
        print("Task ret:", task.result())
    # gather将协程执行的结果组成列表返回
    # results = await asyncio.gather(*tasks)
    # print(results)
    # 返回的是一个执行状态及结果的集合
    # result = await asyncio.wait(tasks)
    # print(result)



start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("Time:", now() - start )

