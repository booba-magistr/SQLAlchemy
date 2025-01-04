from .database import session_maker, engine
from .models import Worker


async def add_workers():
    async with session_maker() as session:
        worker_one = Worker(username='WorkerOne', first_name='Tom')
        worker_two = Worker(username='workerTwo', first_name='Jerry')
        session.add_all([worker_one, worker_two])
        await session.commit()