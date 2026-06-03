# 07 - 安全与认证（Security & Authentication）

## 本章知识点

- OAuth2 与 Bearer Token
- 使用 `OAuth2PasswordBearer` 实现密码流
- JWT（JSON Web Token）的生成与验证
- HTTP Basic Auth
- API Key 认证
- 作用域（Scopes）与权限控制

## 示例文件

| 文件 | 说明 |
|------|------|
| `main.py` | 安全认证示例 |

## 依赖

```bash
pip install python-jose[cryptography] passlib[bcrypt]
```

## 运行示例

```bash
uvicorn main:app --reload
```
