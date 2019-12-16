import asyncio
import time


now = lambda: time.time()


# async def do_some_work(x):
#     print("waiting:", x)

# 通过aync定义协程对象函数
async def do_some_work(x):
    print("waiting:", x)
    return "Done after {}s".format(x)


"""
# part one: 定义一个协程
start = now()
# 新建一个协程对象
coroutine = do_some_work(2)
print(coroutine)
# 创建一个事件loop
loop = asyncio.get_event_loop()
# 将协程加入到事件循环loop,并启动事件循环
loop.run_until_complete(coroutine)
print("Time:", now()-start)

"""

"""
# part two:创建一个task
start = now()
# 新建一个协程对象
coroutine = do_some_work(2)
# 创建一个事件loop
loop = asyncio.get_event_loop()
# 创建loop事件循环任务对象，传入协程对象作为参数，保存协程运行后的状态,用于获取协程的结果
task = loop.create_task(coroutine)
# 在加入事件循环之前协程的状态是pending
print(task)
# 将协程加入到事件循环loop,并启动事件循环
loop.run_until_complete(task)
# 循环之后，协程状态为finished
print(task)
print("Time:", now()-start)
"""


# part three:绑定回调，task执行完成之后，获取执行的结果，定义回调函数，回调的参数是futu
# 定义回调函数
def callback(future):
    print("callback:", future.result())


start = now()
# 新建一个协程对象
coroutine = do_some_work(2)
# 创建一个事件loop
loop = asyncio.get_event_loop()
# 创建loop事件循环任务对象，传入协程对象作为参数，并保存协程运行后的状态,用于获取协程的结果
# 和create_task方法类似
task = asyncio.ensure_future(coroutine)
# 在加入事件循环之前协程的状态是pending
print(task)
# 给task任务对象添加回调函数
# 当task执行完成的时候，就会调用回调函数，通过参数future获取协程执行的结果
# 这里的future对象实际上和task是同一个对象
task.add_done_callback(callback)
print(task)
# 将协程加入到事件循环loop,并启动事件循环
loop.run_until_complete(task)
# 这里就是手动回调协程执行的结果
# print(task.result())

print("Time:", now()-start)