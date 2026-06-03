# 09 - 中间件与 CORS（Middleware & CORS）

## 本章知识点

- 自定义中间件（`@app.middleware`）
- 请求处理时间中间件示例
- CORS（跨域资源共享）配置
- `TrustedHostMiddleware`
- `GZipMiddleware` 响应压缩
- 使用第三方 ASGI 中间件

## 示例文件

| 文件 | 说明 |
|------|------|
| `main.py` | 中间件示例 |

## 运行示例

```bash
uvicorn main:app --reload
```
