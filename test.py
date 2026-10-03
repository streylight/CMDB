import asyncio, asyncpg
async def main():
    conn = await asyncpg.connect("postgresql://jconnix@localhost/cmdb")
    print(await conn.fetchval("select version()"))
    await conn.close()
asyncio.run(main())