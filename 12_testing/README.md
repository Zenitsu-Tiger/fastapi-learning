# 12 - 测试（Testing）

## 本章知识点

- 使用 `TestClient` 进行接口测试
- 使用 `pytest` 编写测试用例
- 覆盖依赖项（mock 数据库等）
- 测试异步代码（`pytest-asyncio`）
- 测试文件上传

## 示例文件

| 文件 | 说明 |
|------|------|
| `main.py` | 被测试的应用 |
| `test_main.py` | 测试文件 |

## 依赖

```bash
pip install pytest httpx pytest-asyncio
```

## 运行测试

```bash
pytest test_main.py -v
```
