import uvicorn
from dependencies import close_mongo_connection, connect_to_mongo
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import crawler, datasatas, text_classification, tweet_trend, tweets

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tweets.router)
app.include_router(datasatas.router)
app.include_router(crawler.router)
app.include_router(tweet_trend.router)
app.include_router(text_classification.router)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug"
    )
