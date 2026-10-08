from fastapi import FastAPI, HTTPException

app = FastAPI()


# 需求： 按 id查询新闻+>1-6
@app.get("/news/{id}")
async def get_news(id: int):
    id_list = [1, 2, 3, 4, 5, 6]
    if id not in id_list:
        raise HTTPException(status_code=404, detail="新闻不存在")
    return {"id": id, "title": "Hello World", "content": "This is a news"}
