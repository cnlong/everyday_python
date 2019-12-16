"""
阻塞和await
1.使用async可以定义协程对象，使用await可以针对耗时的操作进行挂起，就像生成器里的yield一样，函数让出控制权。协程遇到await，事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行
2.耗时的操作一般是一些IO操作，例如网络请求，文件读取等。我们使用asyncio.sleep函数来模拟IO操作。协程的目的也是让这些IO操作异步化。
3.遇到sleep,模拟阻塞或者耗时动作，让出控制权。即当遇到阻塞调用的函数时候，使用await方法将协程的控制权让出，以便loop调用其他的协程
"""
import time
import asyncio


# 定义用于计算时间戳的函数
def now():
    return time.time()

# 定义一个函数，并且是协程对象，内部增加耗时动作
async def do_some_work(x):
    print("waiting:", x)
    # 通过asyncio.sleep函数模拟io操作，增加耗时动作
    # 使用await对耗时动作进行挂起，类似于yield，函数让出主动权。
    # 协程遇到await，事件循环挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程
    await asyncio.sleep(x)
    return "Done after {}s".format(x)

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)

print("task ret:", task.result())
print("time:", now() - start)