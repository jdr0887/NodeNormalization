from node_normalizer.loader import NodeLoader
import asyncio


async def load_redis():
    # instantiate the class that does all the work
    loader = NodeLoader()

    # call to load redis instances with normalized node data
    success: bool = await loader.load(1_000)

    # check the return
    if not success:
        loader.print_debug_msg(f'Failed to load node normalization data.', True)
    else:
        loader.print_debug_msg(f'Success', True)


if __name__ == '__main__':
    asyncio.run(load_redis())
