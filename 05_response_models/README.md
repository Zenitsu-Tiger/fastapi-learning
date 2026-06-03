# 05 - 响应模型（Response Models）

## 本章知识点

- 使用 `response_model` 声明响应类型
- 过滤响应字段（隐藏敏感数据如密码）
- `response_model_exclude_unset` 的使用
- 多种响应状态码
- 使用 `JSONResponse`、`HTMLResponse` 等直接返回响应
- 响应头与 Cookie

## 示例文件

| 文件 | 说明 |
|------|------|
| `main.py` | 响应模型示例 |

## 运行示例

```bash
uvicorn main:app --reload
```
