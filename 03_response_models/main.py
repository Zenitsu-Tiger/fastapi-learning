from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel

app = FastAPI()


class News(BaseModel):
    id: int
    title: str
    content: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 接口 => 响应HTML代码
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>Hello World</h1>"


# 接口 => 返回图片内容
@app.get("/image", response_class=FileResponse)
async def get_image():
    path = "./A.jpg"
    return FileResponse(path)


# 接口=>response_model自定义响应模型
@app.get("/news/{id}", response_model=News)
async def get_news(id: int):
    return {"id": id, "title": "Hello World", "content": "This is a news"}


# 需求： 按 id查询新闻+>1-6
@app.get(f"/news/{id}")