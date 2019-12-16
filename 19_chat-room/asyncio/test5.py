"""
1.主线程中创建事件循环
2.创建子线程，并在子线程中开启无限事件循环
3.主线程新注册协程对象，在子线程中进行事件循环完成并发操作
"""
import asyncio
import time
from threading import Thread


now = lambda: time.time()


# 定义函数，用于无限事件循环
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_some_work(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))


def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))


start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop, ))
t.start()
asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)
print('TIME: {}'.format(time.time() - start))

