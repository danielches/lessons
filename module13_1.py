import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Добрыня", 10))
    task2 = asyncio.create_task(start_strongman("Илья", 8))
    task3 = asyncio.create_task(start_strongman("Алеша", 5))
    await task1
    await task2
    await task3


st = time.time()
asyncio.run(start_tournament())
end = time.time()
print(f'Время работы: {end - st}')