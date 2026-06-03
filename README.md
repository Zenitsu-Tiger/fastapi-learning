# FastAPI 学习笔记

系统学习 FastAPI 框架，代码按知识点分章节组织。

## 目录结构

| 章节 | 主题 |
|------|------|
| [01_basics](./01_basics/) | FastAPI 入门基础 |
| [02_path_params](./02_path_params/) | 路径参数 |
| [03_query_params](./03_query_params/) | 查询参数 |
| [04_request_body](./04_request_body/) | 请求体与 Pydantic |
| [05_response_models](./05_response_models/) | 响应模型 |
| [06_dependencies](./06_dependencies/) | 依赖注入 |
| [07_security](./07_security/) | 安全与认证 |
| [08_database](./08_database/) | 数据库集成 |
| [09_middleware](./09_middleware/) | 中间件与 CORS |
| [10_background_tasks](./10_background_tasks/) | 后台任务 |
| [11_websockets](./11_websockets/) | WebSocket |
| [12_testing](./12_testing/) | 测试 |
| [13_deployment](./13_deployment/) | 部署 |

## 环境搭建

```bash
# 克隆仓库
git clone https://github.com/Zenitsu-Tiger/fastapi-learning.git
cd fastapi-learning

# 创建并激活虚拟环境
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 安装全部依赖
pip install -r requirements.txt
```

## 运行某章节示例

```bash
cd 01_basics
uvicorn main:app --reload
```

打开 http://127.0.0.1:8000/docs 查看 Swagger 文档。

## 新增章节规范

详见下方 [新增章节注意事项](#新增章节注意事项)。

---

## 新增章节注意事项

1. **命名规则**：使用 `数字_主题名` 格式，数字两位补零，例如 `14_file_upload`。
2. **必须包含 `README.md`**：描述本章知识点、示例文件说明和运行方式。
3. **独立可运行**：每个章节的 `main.py` 应可单独 `uvicorn main:app --reload` 运行。
4. **不要在章节内创建虚拟环境**：统一使用项目根目录的 `.venv`。
5. **新增依赖需更新根目录 `requirements.txt`**：不要在章节内单独创建 `requirements.txt`。
6. **测试文件命名**：测试文件统一命名为 `test_*.py`，方便 pytest 自动发现。
7. **`.env` 文件**：如需环境变量，提供 `.env.example` 示例文件，`.env` 已被 `.gitignore` 忽略。
