# 08 - 数据库集成（Database）

## 本章知识点

- 使用 SQLAlchemy 进行 ORM 操作
- 使用 SQLModel（FastAPI 作者出品）
- 异步数据库操作（async SQLAlchemy）
- 数据库会话管理（依赖注入 Session）
- Alembic 数据库迁移
- 关系型数据库 CRUD 操作

## 示例文件

| 文件 | 说明 |
|------|------|
| `main.py` | 数据库集成示例 |
| `models.py` | 数据库模型定义 |
| `database.py` | 数据库连接配置 |

## 依赖

```bash
pip install sqlalchemy sqlmodel alembic aiosqlite
```

## 运行示例

```bash
uvicorn main:app --reload
```
