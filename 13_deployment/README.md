# 13 - 部署（Deployment）

## 本章知识点

- 使用 Uvicorn / Gunicorn 部署
- Docker 容器化部署
- Docker Compose 多服务编排
- 使用 Nginx 作为反向代理
- 环境变量与配置管理（`pydantic-settings`）
- 部署到云平台（Railway / Render / AWS）

## 示例文件

| 文件 | 说明 |
|------|------|
| `main.py` | 生产就绪的应用示例 |
| `Dockerfile` | Docker 镜像构建文件 |
| `docker-compose.yml` | 多容器编排配置 |

## 依赖

```bash
pip install gunicorn pydantic-settings
```

## 生产启动命令

```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```
