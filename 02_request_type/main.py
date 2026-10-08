from fastapi import FastAPI, Form, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/book/{id}")
def get_book(id: int = Path(..., gt=0, lt=101, description="这是书的id")):
    return {"book_id": id, "title": f"Book {id}"}


@app.get("/author/{name}")
async def get_name(
    name: str = Path(..., min_length=2, max_length=50, description="这是作者的名字"),
):
    return {"message": f"这是作者的名字: {name}"}


@app.get("/news/news_list")
async def get_news_list(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(10, ge=1, le=100, description="每页条数"),
):
    return {"message": f"这是新闻列表的页码: {page}, 每页条数: {page_size}"}


# 注册:用户名和密码 => str
class User(BaseModel):
    username: str = Field(..., min_length=2, max_length=50, description="用户名")
    password: str = Field(..., min_length=8, max_length=50, description="密码")


@app.post("/register")
async def register(user: User):
    return {"message": f"用户名: {user.username}, 密码: {user.password}"}


@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"message": f"用户名: {username}, 密码: {password}"}
