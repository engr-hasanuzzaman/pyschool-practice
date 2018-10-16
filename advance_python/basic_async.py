import asyncio

async def main():
  print('before wail')
  await asyncio.sleep(1)
  print('after wail')

asyncio.run(main())