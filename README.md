# 景区数字人导游系统 (A5赛题) - 基础架构与协作文档

## 📌 项目介绍
本项目为“A5-景区导览服务 AI 数字人”的底层架构与管理后台模块（由 5 号成员搭建）。

目前已完成了系统地基建设，包含完整的 **FastAPI 后端服务**、**MySQL 数据库架构**以及 **Vue3 + Element Plus 的管理后台前端页面**。

该底座已预留了 AI 大模型接入点、数字人配置接口、游客端对话接口以及数据大屏展示功能，各模块成员可在此基础上直接进行业务逻辑的填充与功能联调。

---

## 🛠️ 环境依赖与技术栈

### 后端 (Backend)
* **语言/框架**: Python 3.9.x, FastAPI
* **数据库**: MySQL 8.0+
* **ORM框架**: SQLAlchemy
* **依赖清单**: 详见 `backend/requirements.txt` (包含 `fastapi`, `uvicorn`, `sqlalchemy`, `pymysql`, `pydantic` 等)

### 前端管理后台 (Frontend)
* **环境**: Node.js (推荐 v16+ 或 v18+)
* **框架**: Vue 3 + Vite
* **UI 组件库**: Element Plus
* **可视化图表**: ECharts
* **路由**: Vue Router 4

---

## 🚀 运行指南 (拿到项目后需要做什么？)

其他小伙伴在拿到本压缩包/拉取代码后，请务必按照以下步骤启动项目：

### 第一步：初始化数据库
1. 确保你的电脑上安装并启动了 MySQL。
    1. 【2025 最新】 MySQL 数据库安装教程（超详细图文版）：从下载到配置一步到位https://blog.csdn.net/qq_51572290/article/details/154783156
    2. 若想进阶进行数据库操作，可使用
    Navicat Premium15 下载与安装（免费版）https://blog.csdn.net/m0_75188141/article/details/139842565
2. 运行项目中的 `sql/init.sql` 脚本，或者直接在数据库中执行：`CREATE DATABASE IF NOT EXISTS scenic_digital_human CHARACTER SET utf8mb4;`
![数据库执行命令](./images/image1.png)
3. **【关键注意】**：打开 `backend/database.py`，将第 11 行的数据库连接字符串 `mysql+pymysql://root:123qwe@127.0.0.1:3306/scenic_digital_human` 中的密码（`123qwe`）修改为你自己本地电脑的 MySQL 密码！

### 第二步：启动后端服务
1. 打开终端，进入 `backend` 目录：`cd backend`
2. (强烈建议) 激活你的 Python 虚拟环境。
3. 安装后端依赖包：
   ```bash
   pip install -r requirements.txt
4.  直接在IDE中(内核是对应的虚拟环境内核)启动"main.py"
    或者在虚拟环境控制台中进入"scenic-digital-human"文件夹后输入启动命令：
    ```bash
    python backend/main.py
5. 终端显示以下文字即正常启动
![后端启动后终端显示](./images/image2.png)
6. 然后在浏览器中输入<http://localhost:8000/docs>，即可查看自动生成的 Swagger 接口调试文档。
![api页面](./images/image3.png)

### 第三步：启动管理前端服务
1. 确保你的电脑上安装Node.js(推荐 v16+ 或 v18+)。
   Node.js 安装指南（Windows 版本）https://youmoxiang.blog.csdn.net/article/details/154790636
2. 打开一个新的终端，进入 frontend 目录，下载前端依赖包（这步会自动生成 node_modules 文件夹）,在该目录终端中输入
    ```Bash
    npm install
3. 启动本地开发服务器
    在目录终端中输入
    ```Bash
    npm run dev
4. 启动后，按住 Ctrl 单击终端里显示的链接<http://localhost:5173>
    即可访问管理后台。
![管理前端页面](./images/image4.png)

---

## ⚠️ 团队协作注意事项 (给各成员的留言)
### 为了防止代码冲突和运行报错，请大家遵守以下协作规范：
1. **通用守则**
    * 绝对不要把前端的 node_modules 文件夹和后端的 __pycache__ 文件夹发给别人或上传到代码仓库！
    * 前后端均已配置好跨域代理（CORS 和 Vite Proxy），前端请求一律使用 /api/v1/... 格式，不要写死 http://127.0.0.1:8000。
2. **致 2号 (AI 大模型 + 知识库)**
    * 你的主战场在 backend/main.py。
    * 我已经写好了 /api/v1/chat/ask 这个核心对话接口，目前的回答是写死的假数据。你需要在这里引入 LangChain 或你的大模型 SDK，实现 RAG 向量检索和提示词(Prompt)拼接逻辑。
    * /api/v1/kb/upload 文件上传接口也留好了，你可以接管它来处理知识库文档的自动解析和向量化。
3. **致 4号 (前端开发 - 游客交互端)**
    * 游客端不需要集成在目前的 Vue3 管理后台里，你可以新建一个适配移动端的 H5 页面或小程序。
    * 游客提问请发送 POST 请求到 http://127.0.0.1:8000/api/v1/chat/ask。
    * 如果你需要获取数字人的皮肤/音色配置，请调用 GET http://127.0.0.1:8000/api/v1/config。
4. **致 6号 (数据分析 + 测试)**
    * 后端每次回答游客问题时，我已经自动将对话记录写进了 conversation_logs 数据表。
    * 给你留了一个专门用于数据分析的接口：GET /api/v1/logs/list，你可以用 Python 脚本调用这个接口拉取历史数据，进行情感分析或热门词频统计。
5.  **致 所有人**
    * 如果在该项目的基础上进一步操作，建议将下面的markdown文件喂给ai生成你们自己对应的代码，该文件包含了scenic-digital-human目录中所有的代码文件，ai可读。
    ```Bash
        all_code.md 
    ```
    * 本项目全程使用vibe coding，一切解释权归跨国科技公司**谷歌**所有
    * 有问题或需要修改的部分，请QQ联系我，但不会立即回复，敬请谅解
    (∠・ω< )⌒★
