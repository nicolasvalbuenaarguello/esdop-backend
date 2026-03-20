from aiohttp import web, ClientSession

replicas = [f"http://172.22.2.36:{8010 + i}" for i in range(20)]
indice = 0

async def handle(request):
    global indice
    destino = replicas[indice]
    indice = (indice + 1) % len(replicas)

    if request.method == "OPTIONS":
        return web.Response(status=200, headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        })

    async with ClientSession() as session:
        try:
            async with session.request(
                method=request.method,
                url=f"{destino}{request.rel_url}",
                headers={k: v for k, v in request.headers.items() if k.lower() != "host"},
                data=await request.read()
            ) as resp:
                body = await resp.read()
                return web.Response(
                    status=resp.status,
                    body=body,
                    headers={
                        "Access-Control-Allow-Origin": "*",
                        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                        "Access-Control-Allow-Headers": "*",
                        "Content-Type": resp.headers.get("Content-Type", "application/json")
                    }
                )
        except Exception:
            return web.Response(status=503, text="Error al contactar réplica")

app = web.Application()
app.router.add_route("*", "/{tail:.*}", handle)

if __name__ == "__main__":
    web.run_app(app, port=5152)

