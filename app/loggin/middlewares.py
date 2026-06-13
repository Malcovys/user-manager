from fastapi import Request
import time

from .models import Log


async def log_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start

    user = getattr(request.state, "user", None)

    safe_headers = {
        k: v for k, v in request.headers.items()
        if k.lower() not in ["authorization", "cookie"]
    }

    log = Log(
        user_id=user.id if user else None,
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent"),
        metadata={
            "headers": safe_headers,
            "duration_ms": round(duration * 1000, 2)
        }
    )

    session.add(log)
    session.commit()

    return response


async def auth_middleware(request: Request, call_next):


    return await call_next(request)