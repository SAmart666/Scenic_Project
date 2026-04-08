# Table of Contents
- E:\scenic-digital-human\.gitignore
- E:\scenic-digital-human\介绍.md
- E:\scenic-digital-human\backend\database.py
- E:\scenic-digital-human\backend\main.py
- E:\scenic-digital-human\backend\models.py
- E:\scenic-digital-human\backend\requirements.txt
- E:\scenic-digital-human\backend\schemas.py
- E:\scenic-digital-human\backend\test.py
- E:\scenic-digital-human\frontend\index.html
- E:\scenic-digital-human\frontend\vite.config.ts
- E:\scenic-digital-human\frontend\src\App.vue
- E:\scenic-digital-human\frontend\src\env.d.ts
- E:\scenic-digital-human\frontend\src\main.ts
- E:\scenic-digital-human\frontend\src\router\index.ts
- E:\scenic-digital-human\frontend\src\views\Dashboard.vue
- E:\scenic-digital-human\frontend\src\views\DigitalHumanConfig.vue
- E:\scenic-digital-human\frontend\src\views\KnowledgeBase.vue
- E:\scenic-digital-human\sql\init.sql

## File: E:\scenic-digital-human\.gitignore

- Extension: 
- Language: unknown
- Size: 57 bytes
- Created: 2026-04-08 16:45:56
- Modified: 2026-04-08 16:45:59

### Code

```unknown
1 | __pycache__/
2 | .env
3 | node_modules/
4 | dist/
5 | *.pyc
6 | .vscode/
```

## File: E:\scenic-digital-human\介绍.md

- Extension: .md
- Language: markdown
- Size: 5456 bytes
- Created: 2026-04-08 18:24:21
- Modified: 2026-04-08 21:57:46

### Code

```markdown
 1 | # 景区数字人导游系统 (A5赛题) - 基础架构与协作文档
 2 | 
 3 | ## 📌 项目介绍
 4 | 本项目为“A5-景区导览服务 AI 数字人”的底层架构与管理后台模块（由 5 号成员搭建）。
 5 | 
 6 | 目前已完成了系统地基建设，包含完整的 **FastAPI 后端服务**、**MySQL 数据库架构**以及 **Vue3 + Element Plus 的管理后台前端页面**。
 7 | 
 8 | 该底座已预留了 AI 大模型接入点、数字人配置接口、游客端对话接口以及数据大屏展示功能，各模块成员可在此基础上直接进行业务逻辑的填充与功能联调。
 9 | 
10 | ---
11 | 
12 | ## 🛠️ 环境依赖与技术栈
13 | 
14 | ### 后端 (Backend)
15 | * **语言/框架**: Python 3.9.x, FastAPI
16 | * **数据库**: MySQL 8.0+
17 | * **ORM框架**: SQLAlchemy
18 | * **依赖清单**: 详见 `backend/requirements.txt` (包含 `fastapi`, `uvicorn`, `sqlalchemy`, `pymysql`, `pydantic` 等)
19 | 
20 | ### 前端管理后台 (Frontend)
21 | * **环境**: Node.js (推荐 v16+ 或 v18+)
22 | * **框架**: Vue 3 + Vite
23 | * **UI 组件库**: Element Plus
24 | * **可视化图表**: ECharts
25 | * **路由**: Vue Router 4
26 | 
27 | ---
28 | 
29 | ## 🚀 运行指南 (拿到项目后需要做什么？)
30 | 
31 | 其他小伙伴在拿到本压缩包/拉取代码后，请务必按照以下步骤启动项目：
32 | 
33 | ### 第一步：初始化数据库
34 | 1. 确保你的电脑上安装并启动了 MySQL。
35 |     1. 【2025 最新】 MySQL 数据库安装教程（超详细图文版）：从下载到配置一步到位https://blog.csdn.net/qq_51572290/article/details/154783156
36 |     2. 若想进阶进行数据库操作，可使用
37 |     Navicat Premium15 下载与安装（免费版）https://blog.csdn.net/m0_75188141/article/details/139842565
38 | 2. 运行项目中的 `sql/init.sql` 脚本，或者直接在数据库中执行：`CREATE DATABASE IF NOT EXISTS scenic_digital_human CHARACTER SET utf8mb4;`
39 | ![数据库执行命令](./images/image1.png)
40 | 3. **【关键注意】**：打开 `backend/database.py`，将第 11 行的数据库连接字符串 `mysql+pymysql://root:123qwe@127.0.0.1:3306/scenic_digital_human` 中的密码（`123qwe`）修改为你自己本地电脑的 MySQL 密码！
41 | 
42 | ### 第二步：启动后端服务
43 | 1. 打开终端，进入 `backend` 目录：`cd backend`
44 | 2. (强烈建议) 激活你的 Python 虚拟环境。
45 | 3. 安装后端依赖包：
46 |    ```bash
47 |    pip install -r requirements.txt
48 | 4.  直接在IDE中(内核是对应的虚拟环境内核)启动"main.py"
49 |     或者在虚拟环境控制台中进入"scenic-digital-human"文件夹后输入启动命令：
50 |     ```bash
51 |     python backend/main.py
52 | 5. 终端显示以下文字即正常启动
53 | ![后端启动后终端显示](./images/image2.png)
54 | 6. 然后在浏览器中输入<http://localhost:8000/docs>，即可查看自动生成的 Swagger 接口调试文档。
55 | ![api页面](./images/image3.png)
56 | 
57 | ### 第三步：启动管理前端服务
58 | 1. 打开一个新的终端，进入 frontend 目录
59 | 2. 下载前端依赖包（这步会自动生成 node_modules 文件夹）,在该目录终端中输入
60 |     ```Bash
61 |     npm install
62 | 3. 启动本地开发服务器
63 |     在目录终端中输入
64 |     ```Bash
65 |     npm run dev
66 | 4. 启动后，按住 Ctrl 单击终端里显示的链接<http://localhost:5173>
67 |     即可访问管理后台。
68 | ![管理前端页面](./images/image4.png)
69 | 
70 | ---
71 | 
72 | ## ⚠️ 团队协作注意事项 (给各成员的留言)
73 | ### 为了防止代码冲突和运行报错，请大家遵守以下协作规范：
74 | 1. **通用守则**
75 |     * 绝对不要把前端的 node_modules 文件夹和后端的 __pycache__ 文件夹发给别人或上传到代码仓库！
76 |     * 前后端均已配置好跨域代理（CORS 和 Vite Proxy），前端请求一律使用 /api/v1/... 格式，不要写死 http://127.0.0.1:8000。
77 | 2. **致 2号 (AI 大模型 + 知识库)**
78 |     * 你的主战场在 backend/main.py。
79 |     * 我已经写好了 /api/v1/chat/ask 这个核心对话接口，目前的回答是写死的假数据。你需要在这里引入 LangChain 或你的大模型 SDK，实现 RAG 向量检索和提示词(Prompt)拼接逻辑。
80 |     * /api/v1/kb/upload 文件上传接口也留好了，你可以接管它来处理知识库文档的自动解析和向量化。
81 | 3. **致 4号 (前端开发 - 游客交互端)**
82 |     * 游客端不需要集成在目前的 Vue3 管理后台里，你可以新建一个适配移动端的 H5 页面或小程序。
83 |     * 游客提问请发送 POST 请求到 http://127.0.0.1:8000/api/v1/chat/ask。
84 |     * 如果你需要获取数字人的皮肤/音色配置，请调用 GET http://127.0.0.1:8000/api/v1/config。
85 | 4. **致 6号 (数据分析 + 测试)**
86 |     * 后端每次回答游客问题时，我已经自动将对话记录写进了 conversation_logs 数据表。
87 |     * 给你留了一个专门用于数据分析的接口：GET /api/v1/logs/list，你可以用 Python 脚本调用这个接口拉取历史数据，进行情感分析或热门词频统计。
88 | 5.  **致 所有人**
89 |     * 如果在该项目的基础上进一步操作，建议将下面的markdown文件喂给ai生成你们自己对应的代码，该文件包含了scenic-digital-human目录中所有的代码文件，ai可读。
90 |     ```Bash
91 |         all_code.md 
92 |     ```
93 |     * 本项目全程使用vibe coding，一切解释权归跨国科技公司**谷歌**所有
94 |     * 有问题或需要修改的部分，请QQ联系我，但不会立即回复，敬请谅解
95 |     (∠・ω< )⌒★
```

## File: E:\scenic-digital-human\backend\database.py

- Extension: .py
- Language: python
- Size: 643 bytes
- Created: 2026-04-08 15:12:20
- Modified: 2026-04-08 17:54:32

### Code

```python
 1 | import os
 2 | from sqlalchemy import create_engine
 3 | from sqlalchemy.ext.declarative import declarative_base
 4 | from sqlalchemy.orm import sessionmaker
 5 | from dotenv import load_dotenv
 6 | 
 7 | # 加载 .env 文件
 8 | load_dotenv()
 9 | 
10 | # 优先读取环境变量，没有则使用默认值
11 | SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123qwe@127.0.0.1:3306/scenic_digital_human"
12 | engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
13 | SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
14 | Base = declarative_base()
15 | 
16 | def get_db():
17 |     db = SessionLocal()
18 |     try:
19 |         yield db
20 |     finally:
21 |         db.close()
```

## File: E:\scenic-digital-human\backend\main.py

- Extension: .py
- Language: python
- Size: 8971 bytes
- Created: 2026-04-08 15:14:53
- Modified: 2026-04-08 20:43:24

### Code

```python
  1 | import time
  2 | import logging
  3 | from typing import List
  4 | from fastapi import FastAPI, Depends, HTTPException, Query, Request, UploadFile, File
  5 | from fastapi.middleware.cors import CORSMiddleware
  6 | from sqlalchemy.orm import Session
  7 | from sqlalchemy import func
  8 | 
  9 | # 导入我们拆分好的模块
 10 | import models
 11 | import database
 12 | import schemas
 13 | 
 14 | # 1. 初始化日志
 15 | logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 16 | logger = logging.getLogger(__name__)
 17 | 
 18 | # 2. 初始化应用
 19 | app = FastAPI(
 20 |     title="景区数字人导游系统 API",
 21 |     description="支持管理后台与游客交互端的核心后端服务",
 22 |     version="1.0.0"
 23 | )
 24 | 
 25 | # 3. 配置跨域资源共享 (CORS)
 26 | # 允许 Vue3 管理后台跨域请求
 27 | app.add_middleware(
 28 |     CORSMiddleware,
 29 |     allow_origins=["*"],  # 生产环境建议设置为具体的域名，如 ["http://admin.scenic.com"]
 30 |     allow_credentials=True,
 31 |     allow_methods=["*"],
 32 |     allow_headers=["*"],
 33 | )
 34 | 
 35 | # 4. 自动创建数据库表 (如果表不存在)
 36 | models.Base.metadata.create_all(bind=database.engine)
 37 | 
 38 | # --- 核心业务接口：问答系统 ---
 39 | 
 40 | @app.post("/api/v1/chat/ask", tags=["游客交互"])
 41 | async def ask_question(request: schemas.ChatRequest, db: Session = Depends(database.get_db)):
 42 |     """
 43 |     核心问答接口：接收游客提问，调用大模型，记录日志
 44 |     """
 45 |     start_time = time.time()
 46 |     try:
 47 |         # A. (后续扩展) 检索知识库逻辑 (RAG)
 48 |         # 可以在此处通过 models.KnowledgeBase.content 进行关键词匹配或向量检索
 49 |         
 50 |         # B. 模拟调用大模型 (此处替换为 OpenAI/DeepSeek 的 SDK)
 51 |         # TODO: 实际接入大模型 API
 52 |         ai_response = f"您好！关于您提到的'{request.question}'，我是您的数字人导游。根据景区知识库，建议您..."
 53 |         
 54 |         # 模拟模型响应耗时
 55 |         duration_ms = int((time.time() - start_time) * 1000)
 56 | 
 57 |         # C. 记录对话日志到数据库
 58 |         new_log = models.ConversationLog(
 59 |             user_id=request.user_id,
 60 |             question=request.question,
 61 |             answer=ai_response,
 62 |             response_time=duration_ms
 63 |         )
 64 |         db.add(new_log)
 65 |         db.commit()
 66 | 
 67 |         return {
 68 |             "code": 200,
 69 |             "data": {
 70 |                 "answer": ai_response,
 71 |                 "log_id": new_log.id,
 72 |                 "response_time": f"{duration_ms}ms"
 73 |             },
 74 |             "message": "success"
 75 |         }
 76 |     except Exception as e:
 77 |         logger.error(f"问答接口异常: {str(e)}")
 78 |         db.rollback()
 79 |         raise HTTPException(status_code=500, detail="系统处理对话时出现异常")
 80 | 
 81 | # --- 核心业务接口：知识库管理 (CRUD) ---
 82 | 
 83 | @app.get("/api/v1/kb/list", tags=["知识库管理"])
 84 | def get_kb_list(
 85 |     skip: int = Query(0, ge=0),
 86 |     limit: int = Query(10, ge=1),
 87 |     keyword: str = None,
 88 |     db: Session = Depends(database.get_db)
 89 | ):
 90 |     """获取知识库列表，支持关键词搜索和分页"""
 91 |     query = db.query(models.KnowledgeBase)
 92 |     if keyword:
 93 |         query = query.filter(models.KnowledgeBase.title.contains(keyword))
 94 |     
 95 |     total = query.count()
 96 |     items = query.order_by(models.KnowledgeBase.id.desc()).offset(skip).limit(limit).all()
 97 |     
 98 |     return {
 99 |         "code": 200,
100 |         "data": {
101 |             "items": items,
102 |             "total": total
103 |         },
104 |         "message": "success"
105 |     }
106 | 
107 | @app.post("/api/v1/kb/add", tags=["知识库管理"])
108 | def create_kb_item(item: schemas.KBBase, db: Session = Depends(database.get_db)):
109 |     """新增一条知识"""
110 |     try:
111 |         db_item = models.KnowledgeBase(**item.dict())
112 |         db.add(db_item)
113 |         db.commit()
114 |         db.refresh(db_item)
115 |         return {"code": 200, "data": db_item, "message": "添加成功"}
116 |     except Exception as e:
117 |         db.rollback()
118 |         raise HTTPException(status_code=400, detail=f"保存失败: {str(e)}")
119 | 
120 | @app.delete("/api/v1/kb/delete/{kb_id}", tags=["知识库管理"])
121 | def delete_kb_item(kb_id: int, db: Session = Depends(database.get_db)):
122 |     """删除指定知识"""
123 |     db_item = db.query(models.KnowledgeBase).filter(models.KnowledgeBase.id == kb_id).first()
124 |     if not db_item:
125 |         raise HTTPException(status_code=404, detail="条目不存在")
126 |     db.delete(db_item)
127 |     db.commit()
128 |     return {"code": 200, "message": "删除成功"}
129 | 
130 | # --- 核心业务接口：数据统计 ---
131 | 
132 | @app.get("/api/v1/stats/overview", tags=["数据统计"])
133 | def get_stats_overview(db: Session = Depends(database.get_db)):
134 |     """获取管理后台首页 Dashboard 数据"""
135 |     try:
136 |         total_kb = db.query(models.KnowledgeBase).count()
137 |         total_logs = db.query(models.ConversationLog).count()
138 |         avg_rt = db.query(func.avg(models.ConversationLog.response_time)).scalar() or 0
139 |         
140 |         return {
141 |             "code": 200,
142 |             "data": {
143 |                 "total_kb_count": total_kb,
144 |                 "total_chat_count": total_logs,
145 |                 "avg_response_time": round(float(avg_rt), 2)
146 |             },
147 |             "message": "success"
148 |         }
149 |     except Exception as e:
150 |         raise HTTPException(status_code=500, detail="获取统计信息失败")
151 | 
152 | # --- 全局错误处理 ---
153 | 
154 | @app.middleware("http")
155 | async def add_process_time_header(request: Request, call_next):
156 |     """中间件：为所有请求记录处理时间，方便排查性能瓶颈"""
157 |     start_time = time.time()
158 |     response = await call_next(request)
159 |     process_time = time.time() - start_time
160 |     response.headers["X-Process-Time"] = str(process_time)
161 |     return response
162 | 
163 | if __name__ == "__main__":
164 |     import uvicorn
165 |     # 启动服务：uvicorn main:app --reload
166 |     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
167 | 
168 | @app.put("/api/v1/kb/update/{kb_id}", tags=["知识库管理"])
169 | def update_kb_item(kb_id: int, item: schemas.KBBase, db: Session = Depends(database.get_db)):
170 |     db_item = db.query(models.KnowledgeBase).filter(models.KnowledgeBase.id == kb_id).first()
171 |     if not db_item:
172 |         raise HTTPException(status_code=404, detail="条目不存在")
173 |     db_item.title = item.title
174 |     db_item.content = item.content
175 |     db_item.category = item.category
176 |     db.commit()
177 |     db.refresh(db_item)
178 |     return {"code": 200, "data": db_item, "message": "更新成功"}
179 | 
180 | # 新增：知识库文件上传接口 (供2号去解析，你只负责接收文件保存)
181 | @app.post("/api/v1/kb/upload", tags=["知识库管理"])
182 | async def upload_kb_file(file: UploadFile = File(...)):
183 |     # 你的任务只是把文件存下来或者传递给 2号，这里做个简单的保存模拟
184 |     file_location = f"uploads/{file.filename}"
185 |     # 实际项目中应保存文件：with open(file_location, "wb") as f: f.write(file.file.read())
186 |     return {"code": 200, "message": f"文件 {file.filename} 上传成功，已通知大模型模块进行解析。"}
187 | 
188 | @app.get("/api/v1/logs/list", tags=["日志管理"])
189 | def get_logs_list(
190 |     skip: int = Query(0, ge=0),
191 |     limit: int = Query(50, ge=1),
192 |     db: Session = Depends(database.get_db)
193 | ):
194 |     """供 6 号选手进行数据分析使用的日志接口"""
195 |     total = db.query(models.ConversationLog).count()
196 |     items = db.query(models.ConversationLog).order_by(models.ConversationLog.id.desc()).offset(skip).limit(limit).all()
197 |     return {
198 |         "code": 200,
199 |         "data": {
200 |             "items": items,
201 |             "total": total
202 |         },
203 |         "message": "success"
204 |     }
205 | 
206 | # 将以下代码加入 main.py 的路由区域
207 | 
208 | @app.get("/api/v1/config", tags=["数字人配置"])
209 | def get_config(db: Session = Depends(database.get_db)):
210 |     """获取数字人当前配置，如果没有则初始化一条默认的"""
211 |     config = db.query(models.DigitalHumanConfig).first()
212 |     if not config:
213 |         config = models.DigitalHumanConfig(
214 |             avatar_style="古风导游",
215 |             voice_type="温柔女声",
216 |             greeting_text="您好，我是您的灵山数字导游，请问有什么可以帮您？"
217 |         )
218 |         db.add(config)
219 |         db.commit()
220 |         db.refresh(config)
221 |     return {"code": 200, "data": config, "message": "success"}
222 | 
223 | @app.post("/api/v1/config", tags=["数字人配置"])
224 | def update_config(config_data: schemas.ConfigBase, db: Session = Depends(database.get_db)):
225 |     """更新数字人配置"""
226 |     config = db.query(models.DigitalHumanConfig).first()
227 |     if not config:
228 |         config = models.DigitalHumanConfig(**config_data.dict())
229 |         db.add(config)
230 |     else:
231 |         config.avatar_style = config_data.avatar_style
232 |         config.voice_type = config_data.voice_type
233 |         config.greeting_text = config_data.greeting_text
234 |     db.commit()
235 |     db.refresh(config)
236 |     return {"code": 200, "data": config, "message": "保存成功"}
```

## File: E:\scenic-digital-human\backend\models.py

- Extension: .py
- Language: python
- Size: 867 bytes
- Created: 2026-04-08 15:20:30
- Modified: 2026-04-08 15:20:33

### Code

```python
 1 | from sqlalchemy import Column, Integer, String, Text, DateTime, Float
 2 | import datetime
 3 | from database import Base  # 从 database.py 导入基类
 4 | 
 5 | class KnowledgeBase(Base):
 6 |     __tablename__ = "knowledge_base"
 7 |     
 8 |     id = Column(Integer, primary_key=True, index=True)
 9 |     title = Column(String(255), nullable=False)
10 |     content = Column(Text, nullable=False)
11 |     category = Column(String(50), default="general")
12 |     created_at = Column(DateTime, default=datetime.datetime.now)
13 | 
14 | class ConversationLog(Base):
15 |     __tablename__ = "conversation_logs"
16 |     
17 |     id = Column(Integer, primary_key=True, index=True)
18 |     user_id = Column(String(64))
19 |     question = Column(Text)
20 |     answer = Column(Text)
21 |     response_time = Column(Integer)
22 |     created_at = Column(DateTime, default=datetime.datetime.now)
23 | 
24 | # 如果有数字人配置，也写在这里...
```

## File: E:\scenic-digital-human\backend\requirements.txt

- Extension: .txt
- Language: plaintext
- Size: 62 bytes
- Created: 2026-04-08 16:41:53
- Modified: 2026-04-08 16:41:58

### Code

```plaintext
1 | fastapi
2 | uvicorn
3 | sqlalchemy
4 | pymysql
5 | pydantic
6 | python-dotenv
```

## File: E:\scenic-digital-human\backend\schemas.py

- Extension: .py
- Language: python
- Size: 558 bytes
- Created: 2026-04-08 15:14:32
- Modified: 2026-04-08 20:43:50

### Code

```python
 1 | from pydantic import BaseModel
 2 | from typing import Optional, List
 3 | 
 4 | class KBBase(BaseModel):
 5 |     title: str
 6 |     content: str
 7 |     category: Optional[str] = "general"
 8 | 
 9 | class KBResponse(KBBase):
10 |     id: int
11 |     class Config:
12 |         from_attributes = True
13 | 
14 | class ChatRequest(BaseModel):
15 |     user_id: str
16 |     question: str
17 |     stream: bool = False
18 | 
19 | class ConfigBase(BaseModel):
20 |     avatar_style: str
21 |     voice_type: str
22 |     greeting_text: str
23 | 
24 | class ConfigResponse(ConfigBase):
25 |     id: int
26 |     class Config:
27 |         from_attributes = True
```

## File: E:\scenic-digital-human\backend\test.py

- Extension: .py
- Language: python
- Size: 560 bytes
- Created: 2026-04-08 17:48:23
- Modified: 2026-04-08 17:48:47

### Code

```python
 1 | import pymysql
 2 | 
 3 | # 在这里填入你认为可能的密码列表，比如 ['123456', 'root', 'admin', '']
 4 | passwords_to_try = ['123456', 'root', '123qwe', ''] 
 5 | 
 6 | for pwd in passwords_to_try:
 7 |     try:
 8 |         conn = pymysql.connect(
 9 |             host='127.0.0.1',
10 |             user='root',
11 |             password=pwd,
12 |             database='mysql' # 先连系统库测试
13 |         )
14 |         print(f"成功了！正确的密码是: '{pwd}'")
15 |         conn.close()
16 |         break
17 |     except Exception as e:
18 |         print(f"尝试密码 '{pwd}' 失败: {e}")
```

## File: E:\scenic-digital-human\frontend\index.html

- Extension: .html
- Language: html
- Size: 409 bytes
- Created: 2026-04-08 18:00:36
- Modified: 2026-04-08 18:05:04

### Code

```html
 1 | <!DOCTYPE html>
 2 | <html lang="zh-CN">
 3 |   <head>
 4 |     <meta charset="UTF-8" />
 5 |     <link rel="icon" href="/favicon.ico" />
 6 |     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
 7 |     <title>景区数字人管理后台</title>
 8 |   </head>
 9 |   <body>
10 |     <div id="app"></div>
11 |     <!-- 引入前端入口脚本 -->
12 |     <script type="module" src="/src/main.ts"></script>
13 |   </body>
14 | </html>
```

## File: E:\scenic-digital-human\frontend\vite.config.ts

- Extension: .ts
- Language: typescript
- Size: 445 bytes
- Created: 2026-04-08 16:44:13
- Modified: 2026-04-08 16:52:27

### Code

```typescript
 1 | import { defineConfig } from 'vite'
 2 | import vue from '@vitejs/plugin-vue'
 3 | 
 4 | export default defineConfig({
 5 |   plugins: [vue()],
 6 |   server: {
 7 |     port: 5173,
 8 |     proxy: {
 9 |       // 将所有以 /api 开头的请求转发到 FastAPI 后端
10 |       '/api': {
11 |         target: 'http://127.0.0.1:8000',
12 |         changeOrigin: true,
13 |         rewrite: (path) => path // FastAPI 已经包含了 /api 前缀，所以无需重写
14 |       }
15 |     }
16 |   }
17 | })
```

## File: E:\scenic-digital-human\frontend\src\App.vue

- Extension: .vue
- Language: unknown
- Size: 1744 bytes
- Created: 2026-04-08 16:53:16
- Modified: 2026-04-08 20:54:02

### Code

```unknown
 1 | <template>
 2 |   <el-config-provider :locale="zhCn">
 3 |     <el-container class="layout-container">
 4 |       <!-- 顶部导航 -->
 5 |       <el-header class="app-header">
 6 |         <div class="logo">景区数字人导游管理系统</div>
 7 |       </el-header>
 8 | 
 9 |       <el-container>
10 |         <!-- 左侧菜单栏 -->
11 |         <el-aside width="220px" class="app-aside">
12 |           <el-menu
13 |             :default-active="$route.path"
14 |             router
15 |             class="el-menu-vertical"
16 |             background-color="#304156"
17 |             text-color="#bfcbd9"
18 |             active-text-color="#409eff"
19 |           >
20 |             <el-menu-item index="/dashboard">
21 |               <span> 数据概览</span>
22 |             </el-menu-item>
23 |             <el-menu-item index="/kb">
24 |               <span> 知识库管理</span>
25 |             </el-menu-item>
26 |             <el-menu-item index="/config">
27 |               <span> 数字人配置</span>
28 |             </el-menu-item>
29 |           </el-menu>
30 |         </el-aside>
31 | 
32 |         <!-- 右侧主体内容区域 -->
33 |         <el-main class="app-main">
34 |           <!-- 这里很关键！用来显示路由对应的页面 -->
35 |           <router-view />
36 |         </el-main>
37 |       </el-container>
38 |     </el-container>
39 |   </el-config-provider>
40 | </template>
41 | 
42 | <script setup>
43 | import { ElConfigProvider } from 'element-plus'
44 | import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
45 | </script>
46 | 
47 | <style>
48 | body { margin: 0; padding: 0; background-color: #f0f2f5; }
49 | .layout-container { height: 100vh; }
50 | .app-header {
51 |   background-color: #1890ff; color: white; display: flex;
52 |   align-items: center; font-size: 20px; font-weight: bold;
53 | }
54 | .app-aside { background-color: #304156; }
55 | .app-main { padding: 20px; }
56 | </style>
```

## File: E:\scenic-digital-human\frontend\src\env.d.ts

- Extension: .ts
- Language: typescript
- Size: 37 bytes
- Created: 2026-04-08 20:41:15
- Modified: 2026-04-08 20:41:22

### Code

```typescript
1 | /// <reference types="vite/client" />
```

## File: E:\scenic-digital-human\frontend\src\main.ts

- Extension: .ts
- Language: typescript
- Size: 274 bytes
- Created: 2026-04-08 16:45:28
- Modified: 2026-04-08 20:53:35

### Code

```typescript
 1 | import { createApp } from 'vue'
 2 | import App from './App.vue'
 3 | import router from './router' // 引入路由
 4 | import ElementPlus from 'element-plus'
 5 | import 'element-plus/dist/index.css'
 6 | 
 7 | const app = createApp(App)
 8 | app.use(router) 
 9 | app.use(ElementPlus)
10 | app.mount('#app')
```

## File: E:\scenic-digital-human\frontend\src\router\index.ts

- Extension: .ts
- Language: typescript
- Size: 709 bytes
- Created: 2026-04-08 20:36:10
- Modified: 2026-04-08 20:53:36

### Code

```typescript
 1 | import { createRouter, createWebHistory } from 'vue-router'
 2 | import Dashboard from '../views/Dashboard.vue'
 3 | import KnowledgeBase from '../views/KnowledgeBase.vue'
 4 | import DigitalHumanConfig from '../views/DigitalHumanConfig.vue'
 5 | 
 6 | const routes =[
 7 |   { path: '/', redirect: '/dashboard' },
 8 |   { path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: { title: '数据概览' } },
 9 |   { path: '/kb', name: 'KnowledgeBase', component: KnowledgeBase, meta: { title: '知识库管理' } },
10 |   { path: '/config', name: 'Config', component: DigitalHumanConfig, meta: { title: '数字人配置' } }
11 | ]
12 | 
13 | const router = createRouter({
14 |   history: createWebHistory(),
15 |   routes
16 | })
17 | 
18 | export default router
```

## File: E:\scenic-digital-human\frontend\src\views\Dashboard.vue

- Extension: .vue
- Language: unknown
- Size: 2863 bytes
- Created: 2026-04-08 20:38:51
- Modified: 2026-04-08 20:38:56

### Code

```unknown
  1 | <template>
  2 |   <div class="dashboard-container">
  3 |     <el-row :gutter="20">
  4 |       <el-col :span="8">
  5 |         <el-card shadow="hover" class="data-card">
  6 |           <div class="title">知识库总数</div>
  7 |           <div class="value">{{ stats.total_kb_count }} <span class="unit">条</span></div>
  8 |         </el-card>
  9 |       </el-col>
 10 |       <el-col :span="8">
 11 |         <el-card shadow="hover" class="data-card">
 12 |           <div class="title">累计对话人次</div>
 13 |           <div class="value">{{ stats.total_chat_count }} <span class="unit">次</span></div>
 14 |         </el-card>
 15 |       </el-col>
 16 |       <el-col :span="8">
 17 |         <el-card shadow="hover" class="data-card">
 18 |           <div class="title">平均响应时间</div>
 19 |           <div class="value">{{ stats.avg_response_time }} <span class="unit">ms</span></div>
 20 |         </el-card>
 21 |       </el-col>
 22 |     </el-row>
 23 | 
 24 |     <!-- ECharts 图表区域 -->
 25 |     <el-row style="margin-top: 20px;">
 26 |       <el-col :span="24">
 27 |         <el-card shadow="always">
 28 |           <div ref="chartRef" style="width: 100%; height: 400px;"></div>
 29 |         </el-card>
 30 |       </el-col>
 31 |     </el-row>
 32 |   </div>
 33 | </template>
 34 | 
 35 | <script setup>
 36 | import { ref, onMounted } from 'vue'
 37 | import axios from 'axios'
 38 | import * as echarts from 'echarts'
 39 | 
 40 | const stats = ref({
 41 |   total_kb_count: 0,
 42 |   total_chat_count: 0,
 43 |   avg_response_time: 0
 44 | })
 45 | const chartRef = ref(null)
 46 | 
 47 | const fetchStats = async () => {
 48 |   try {
 49 |     const res = await axios.get('/api/v1/stats/overview')
 50 |     if (res.data.code === 200) {
 51 |       stats.value = res.data.data
 52 |     }
 53 |   } catch (error) {
 54 |     console.error("获取统计数据失败", error)
 55 |   }
 56 | }
 57 | 
 58 | const initChart = () => {
 59 |   const myChart = echarts.init(chartRef.value)
 60 |   // 这里写死一些模拟数据让界面好看，实际可让 6号选手 提供真实的接口
 61 |   const option = {
 62 |     title: { text: '近七日对话量趋势' },
 63 |     tooltip: { trigger: 'axis' },
 64 |     xAxis: {
 65 |       type: 'category',
 66 |       data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
 67 |     },
 68 |     yAxis: { type: 'value' },
 69 |     series: [
 70 |       {
 71 |         data: [120, 132, 101, 134, 390, 830, 920],
 72 |         type: 'line',
 73 |         smooth: true,
 74 |         areaStyle: { color: 'rgba(24,144,255,0.2)' },
 75 |         itemStyle: { color: '#1890ff' }
 76 |       }
 77 |     ]
 78 |   }
 79 |   myChart.setOption(option)
 80 |   window.addEventListener('resize', () => myChart.resize())
 81 | }
 82 | 
 83 | onMounted(() => {
 84 |   fetchStats()
 85 |   initChart()
 86 | })
 87 | </script>
 88 | 
 89 | <style scoped>
 90 | .data-card {
 91 |   text-align: center;
 92 |   padding: 20px 0;
 93 | }
 94 | .data-card .title {
 95 |   font-size: 16px;
 96 |   color: #909399;
 97 |   margin-bottom: 10px;
 98 | }
 99 | .data-card .value {
100 |   font-size: 32px;
101 |   font-weight: bold;
102 |   color: #303133;
103 | }
104 | .data-card .unit {
105 |   font-size: 14px;
106 |   font-weight: normal;
107 |   color: #909399;
108 | }
109 | </style>
```

## File: E:\scenic-digital-human\frontend\src\views\DigitalHumanConfig.vue

- Extension: .vue
- Language: unknown
- Size: 3082 bytes
- Created: 2026-04-08 20:39:09
- Modified: 2026-04-08 20:39:14

### Code

```unknown
  1 | <template>
  2 |   <div class="config-container">
  3 |     <el-card class="box-card" v-loading="loading">
  4 |       <template #header>
  5 |         <div class="card-header">
  6 |           <span>数字人形象与交互配置</span>
  7 |         </div>
  8 |       </template>
  9 |       
 10 |       <el-form :model="form" label-width="120px" style="max-width: 600px">
 11 |         <el-form-item label="外观风格">
 12 |           <el-select v-model="form.avatar_style" placeholder="选择数字人形象" style="width: 100%">
 13 |             <el-option label="古风女导游 (推荐灵山)" value="古风导游" />
 14 |             <el-option label="现代职业装" value="现代职业" />
 15 |             <el-option label="卡通3D形象" value="卡通形象" />
 16 |           </el-select>
 17 |         </el-form-item>
 18 | 
 19 |         <el-form-item label="发音音色 (TTS)">
 20 |           <el-select v-model="form.voice_type" placeholder="选择发音风格" style="width: 100%">
 21 |             <el-option label="温柔亲切女声" value="温柔女声" />
 22 |             <el-option label="沉稳专业男声" value="沉稳男声" />
 23 |             <el-option label="活泼童声" value="活泼童声" />
 24 |           </el-select>
 25 |         </el-form-item>
 26 | 
 27 |         <el-form-item label="默认开场白">
 28 |           <el-input 
 29 |             v-model="form.greeting_text" 
 30 |             type="textarea" 
 31 |             :rows="3" 
 32 |             placeholder="请输入数字人欢迎游客时的开场白"
 33 |           />
 34 |         </el-form-item>
 35 | 
 36 |         <el-form-item>
 37 |           <el-button type="primary" @click="saveConfig" :loading="submitLoading">保存配置</el-button>
 38 |           <el-button @click="fetchConfig">重置</el-button>
 39 |         </el-form-item>
 40 |       </el-form>
 41 |     </el-card>
 42 |   </div>
 43 | </template>
 44 | 
 45 | <script setup>
 46 | import { ref, onMounted, reactive } from 'vue'
 47 | import { ElMessage } from 'element-plus'
 48 | import axios from 'axios'
 49 | 
 50 | const loading = ref(false)
 51 | const submitLoading = ref(false)
 52 | 
 53 | const form = reactive({
 54 |   avatar_style: '',
 55 |   voice_type: '',
 56 |   greeting_text: ''
 57 | })
 58 | 
 59 | const fetchConfig = async () => {
 60 |   loading.value = true
 61 |   try {
 62 |     const res = await axios.get('/api/v1/config')
 63 |     if (res.data.code === 200 && res.data.data) {
 64 |       form.avatar_style = res.data.data.avatar_style
 65 |       form.voice_type = res.data.data.voice_type
 66 |       form.greeting_text = res.data.data.greeting_text
 67 |     }
 68 |   } catch (error) {
 69 |     ElMessage.error('获取配置失败')
 70 |   } finally {
 71 |     loading.value = false
 72 |   }
 73 | }
 74 | 
 75 | const saveConfig = async () => {
 76 |   submitLoading.value = true
 77 |   try {
 78 |     const res = await axios.post('/api/v1/config', form)
 79 |     if (res.data.code === 200) {
 80 |       ElMessage.success('配置保存成功！数字人前端将同步生效。')
 81 |     }
 82 |   } catch (error) {
 83 |     ElMessage.error('保存失败')
 84 |   } finally {
 85 |     submitLoading.value = false
 86 |   }
 87 | }
 88 | 
 89 | onMounted(() => {
 90 |   fetchConfig()
 91 | })
 92 | </script>
 93 | 
 94 | <style scoped>
 95 | .config-container {
 96 |   padding: 10px;
 97 | }
 98 | .box-card {
 99 |   margin-bottom: 20px;
100 | }
101 | .card-header {
102 |   font-weight: bold;
103 |   font-size: 16px;
104 | }
105 | </style>
```

## File: E:\scenic-digital-human\frontend\src\views\KnowledgeBase.vue

- Extension: .vue
- Language: unknown
- Size: 6235 bytes
- Created: 2026-04-08 16:34:12
- Modified: 2026-04-08 18:05:13

### Code

```unknown
  1 | <template>
  2 |   <div class="kb-container">
  3 |     <!-- 顶部操作栏 -->
  4 |     <el-card class="filter-card">
  5 |       <div class="header-actions">
  6 |         <el-input
  7 |           v-model="searchQuery"
  8 |           placeholder="搜索知识标题..."
  9 |           style="width: 300px"
 10 |           clearable
 11 |           @clear="fetchData"
 12 |           @keyup.enter="fetchData"
 13 |         >
 14 |           <template #append>
 15 |             <el-button :icon="Search" @click="fetchData" />
 16 |           </template>
 17 |         </el-input>
 18 |         
 19 |         <div class="button-group">
 20 |           <el-button type="primary" :icon="Plus" @click="handleAdd">新增条目</el-button>
 21 |         </div>
 22 |       </div>
 23 |     </el-card>
 24 | 
 25 |     <!-- 数据表格 -->
 26 |     <el-card class="table-card">
 27 |       <el-table :data="tableData" v-loading="loading" border style="width: 100%">
 28 |         <el-table-column prop="id" label="ID" width="80" />
 29 |         <el-table-column prop="title" label="知识标题" width="200" show-overflow-tooltip />
 30 |         <el-table-column prop="category" label="分类" width="120">
 31 |           <template #default="{ row }">
 32 |             <el-tag>{{ row.category || '通用' }}</el-tag>
 33 |           </template>
 34 |         </el-table-column>
 35 |         <el-table-column prop="content" label="详细内容" show-overflow-tooltip />
 36 |         <el-table-column prop="created_at" label="创建时间" width="180" />
 37 |         <el-table-column label="操作" width="150" fixed="right">
 38 |           <template #default="{ row }">
 39 |             <el-button link type="primary" @click="handleEdit(row)">编辑</el-button>
 40 |             <el-button link type="danger" @click="confirmDelete(row)">删除</el-button>
 41 |           </template>
 42 |         </el-table-column>
 43 |       </el-table>
 44 | 
 45 |       <!-- 分页 -->
 46 |       <div class="pagination-container">
 47 |         <el-pagination
 48 |           v-model:current-page="currentPage"
 49 |           v-model:page-size="pageSize"
 50 |           layout="total, prev, pager, next"
 51 |           :total="total"
 52 |           @current-change="fetchData"
 53 |         />
 54 |       </div>
 55 |     </el-card>
 56 | 
 57 |     <!-- 新增/编辑对话框 -->
 58 |     <el-dialog
 59 |       v-model="dialogVisible"
 60 |       :title="form.id ? '编辑知识' : '新增知识'"
 61 |       width="600px"
 62 |     >
 63 |       <el-form :model="form" label-width="80px" :rules="rules" ref="formRef">
 64 |         <el-form-item label="标题" prop="title">
 65 |           <el-input v-model="form.title" placeholder="请输入知识点标题" />
 66 |         </el-form-item>
 67 |         <el-form-item label="分类">
 68 |           <el-select v-model="form.category" placeholder="请选择分类" style="width: 100%">
 69 |             <el-option label="景点介绍" value="景点介绍" />
 70 |             <el-option label="交通指南" value="交通指南" />
 71 |             <el-option label="餐饮住宿" value="餐饮住宿" />
 72 |             <el-option label="通用FAQ" value="general" />
 73 |           </el-select>
 74 |         </el-form-item>
 75 |         <el-form-item label="详细内容" prop="content">
 76 |           <el-input
 77 |             v-model="form.content"
 78 |             type="textarea"
 79 |             :rows="6"
 80 |             placeholder="请输入数字人回答的详细文本"
 81 |           />
 82 |         </el-form-item>
 83 |       </el-form>
 84 |       <template #footer>
 85 |         <el-button @click="dialogVisible = false">取消</el-button>
 86 |         <el-button type="primary" @click="submitForm" :loading="submitLoading">提交</el-button>
 87 |       </template>
 88 |     </el-dialog>
 89 |   </div>
 90 | </template>
 91 | 
 92 | <script setup>
 93 | import { ref, onMounted, reactive } from 'vue'
 94 | import { Search, Plus } from '@element-plus/icons-vue'
 95 | import { ElMessage, ElMessageBox } from 'element-plus'
 96 | import axios from 'axios'
 97 | 
 98 | // 状态变量
 99 | const loading = ref(false)
100 | const submitLoading = ref(false)
101 | const tableData = ref([])
102 | const searchQuery = ref('')
103 | const dialogVisible = ref(false)
104 | const currentPage = ref(1)
105 | const pageSize = ref(10)
106 | const total = ref(0)
107 | const formRef = ref(null)
108 | 
109 | const form = reactive({
110 |   id: null,
111 |   title: '',
112 |   category: 'general',
113 |   content: ''
114 | })
115 | 
116 | const rules = {
117 |   title: [{ required: true, message: '请输入标题', trigger: 'blur' }],
118 |   content: [{ required: true, message: '请输入内容', trigger: 'blur' }]
119 | }
120 | 
121 | // 获取数据
122 | const fetchData = async () => {
123 |   loading.value = true
124 |   try {
125 |     const res = await axios.get('/api/v1/kb/list', {
126 |       params: { 
127 |         skip: (currentPage.value - 1) * pageSize.value, 
128 |         limit: pageSize.value,
129 |         keyword: searchQuery.value || undefined
130 |       }
131 |     })
132 |     if (res.data.code === 200) {
133 |       tableData.value = res.data.data.items
134 |       total.value = res.data.data.total
135 |     }
136 |   } catch (error) {
137 |     ElMessage.error('获取数据失败，请确保后端服务已启动')
138 |   } finally {
139 |     loading.value = false
140 |   }
141 | }
142 | 
143 | // 新增
144 | const handleAdd = () => {
145 |   form.id = null
146 |   form.title = ''
147 |   form.content = ''
148 |   form.category = 'general'
149 |   dialogVisible.value = true
150 | }
151 | 
152 | // 编辑
153 | const handleEdit = (row) => {
154 |   Object.assign(form, row)
155 |   dialogVisible.value = true
156 | }
157 | 
158 | // 提交表单
159 | const submitForm = async () => {
160 |   await formRef.value.validate()
161 |   submitLoading.value = true
162 |   try {
163 |     if (form.id) {
164 |       // 这里的逻辑可以根据后端需要微调，目前后端只写了 add 和 delete
165 |       await axios.post('/api/v1/kb/add', form) 
166 |     } else {
167 |       await axios.post('/api/v1/kb/add', form)
168 |     }
169 |     ElMessage.success('操作成功')
170 |     dialogVisible.value = false
171 |     fetchData()
172 |   } catch (error) {
173 |     ElMessage.error('操作失败')
174 |   } finally {
175 |     submitLoading.value = false
176 |   }
177 | }
178 | 
179 | // 删除确认
180 | const confirmDelete = (row) => {
181 |   ElMessageBox.confirm('确定要删除这条知识吗？', '提示', {
182 |     type: 'warning',
183 |   }).then(async () => {
184 |     await axios.delete(`/api/v1/kb/delete/${row.id}`)
185 |     ElMessage.success('删除成功')
186 |     fetchData()
187 |   })
188 | }
189 | 
190 | onMounted(fetchData)
191 | </script>
192 | 
193 | <style scoped>
194 | .kb-container { padding: 10px; }
195 | .filter-card { margin-bottom: 20px; }
196 | .header-actions { display: flex; justify-content: space-between; }
197 | .pagination-container { margin-top: 20px; display: flex; justify-content: flex-end; }
198 | </style>
```

## File: E:\scenic-digital-human\sql\init.sql

- Extension: .sql
- Language: sql
- Size: 191 bytes
- Created: 2026-04-08 16:41:05
- Modified: 2026-04-08 16:41:09

### Code

```sql
1 | CREATE DATABASE IF NOT EXISTS scenic_digital_human CHARACTER SET utf8mb4;
2 | USE scenic_digital_human;
3 | 
4 | -- 具体的建表语句见之前的数据库设计（此处略，建议保留备份）
```

