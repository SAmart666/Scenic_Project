import time
import logging
from typing import List
from fastapi import FastAPI, Depends, HTTPException, Query, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func

# 导入我们拆分好的模块
import models
import database
import schemas

# 1. 初始化日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 2. 初始化应用
app = FastAPI(
    title="景区数字人导游系统 API",
    description="支持管理后台与游客交互端的核心后端服务",
    version="1.0.0"
)

# 3. 配置跨域资源共享 (CORS)
# 允许 Vue3 管理后台跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议设置为具体的域名，如 ["http://admin.scenic.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. 自动创建数据库表 (如果表不存在)
models.Base.metadata.create_all(bind=database.engine)

# --- 核心业务接口：问答系统 ---

@app.post("/api/v1/chat/ask", tags=["游客交互"])
async def ask_question(request: schemas.ChatRequest, db: Session = Depends(database.get_db)):
    """
    核心问答接口：接收游客提问，调用大模型，记录日志
    """
    start_time = time.time()
    try:
        # A. (后续扩展) 检索知识库逻辑 (RAG)
        # 可以在此处通过 models.KnowledgeBase.content 进行关键词匹配或向量检索
        
        # B. 模拟调用大模型 (此处替换为 OpenAI/DeepSeek 的 SDK)
        # TODO: 实际接入大模型 API
        ai_response = f"您好！关于您提到的'{request.question}'，我是您的数字人导游。根据景区知识库，建议您..."
        
        # 模拟模型响应耗时
        duration_ms = int((time.time() - start_time) * 1000)

        # C. 记录对话日志到数据库
        new_log = models.ConversationLog(
            user_id=request.user_id,
            question=request.question,
            answer=ai_response,
            response_time=duration_ms
        )
        db.add(new_log)
        db.commit()

        return {
            "code": 200,
            "data": {
                "answer": ai_response,
                "log_id": new_log.id,
                "response_time": f"{duration_ms}ms"
            },
            "message": "success"
        }
    except Exception as e:
        logger.error(f"问答接口异常: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=500, detail="系统处理对话时出现异常")

# --- 核心业务接口：知识库管理 (CRUD) ---

@app.get("/api/v1/kb/list", tags=["知识库管理"])
def get_kb_list(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    keyword: str = None,
    db: Session = Depends(database.get_db)
):
    """获取知识库列表，支持关键词搜索和分页"""
    query = db.query(models.KnowledgeBase)
    if keyword:
        query = query.filter(models.KnowledgeBase.title.contains(keyword))
    
    total = query.count()
    items = query.order_by(models.KnowledgeBase.id.desc()).offset(skip).limit(limit).all()
    
    return {
        "code": 200,
        "data": {
            "items": items,
            "total": total
        },
        "message": "success"
    }

@app.post("/api/v1/kb/add", tags=["知识库管理"])
def create_kb_item(item: schemas.KBBase, db: Session = Depends(database.get_db)):
    """新增一条知识"""
    try:
        db_item = models.KnowledgeBase(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return {"code": 200, "data": db_item, "message": "添加成功"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"保存失败: {str(e)}")

@app.delete("/api/v1/kb/delete/{kb_id}", tags=["知识库管理"])
def delete_kb_item(kb_id: int, db: Session = Depends(database.get_db)):
    """删除指定知识"""
    db_item = db.query(models.KnowledgeBase).filter(models.KnowledgeBase.id == kb_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="条目不存在")
    db.delete(db_item)
    db.commit()
    return {"code": 200, "message": "删除成功"}

# --- 核心业务接口：数据统计 ---

@app.get("/api/v1/stats/overview", tags=["数据统计"])
def get_stats_overview(db: Session = Depends(database.get_db)):
    """获取管理后台首页 Dashboard 数据"""
    try:
        total_kb = db.query(models.KnowledgeBase).count()
        total_logs = db.query(models.ConversationLog).count()
        avg_rt = db.query(func.avg(models.ConversationLog.response_time)).scalar() or 0
        
        return {
            "code": 200,
            "data": {
                "total_kb_count": total_kb,
                "total_chat_count": total_logs,
                "avg_response_time": round(float(avg_rt), 2)
            },
            "message": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="获取统计信息失败")

# --- 全局错误处理 ---

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """中间件：为所有请求记录处理时间，方便排查性能瓶颈"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

if __name__ == "__main__":
    import uvicorn
    # 启动服务：uvicorn main:app --reload
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

@app.put("/api/v1/kb/update/{kb_id}", tags=["知识库管理"])
def update_kb_item(kb_id: int, item: schemas.KBBase, db: Session = Depends(database.get_db)):
    db_item = db.query(models.KnowledgeBase).filter(models.KnowledgeBase.id == kb_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="条目不存在")
    db_item.title = item.title
    db_item.content = item.content
    db_item.category = item.category
    db.commit()
    db.refresh(db_item)
    return {"code": 200, "data": db_item, "message": "更新成功"}

# 新增：知识库文件上传接口 (供2号去解析，你只负责接收文件保存)
@app.post("/api/v1/kb/upload", tags=["知识库管理"])
async def upload_kb_file(file: UploadFile = File(...)):
    # 你的任务只是把文件存下来或者传递给 2号，这里做个简单的保存模拟
    file_location = f"uploads/{file.filename}"
    # 实际项目中应保存文件：with open(file_location, "wb") as f: f.write(file.file.read())
    return {"code": 200, "message": f"文件 {file.filename} 上传成功，已通知大模型模块进行解析。"}

@app.get("/api/v1/logs/list", tags=["日志管理"])
def get_logs_list(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1),
    db: Session = Depends(database.get_db)
):
    """供 6 号选手进行数据分析使用的日志接口"""
    total = db.query(models.ConversationLog).count()
    items = db.query(models.ConversationLog).order_by(models.ConversationLog.id.desc()).offset(skip).limit(limit).all()
    return {
        "code": 200,
        "data": {
            "items": items,
            "total": total
        },
        "message": "success"
    }

@app.get("/api/v1/stats/analysis", tags=["数据统计"])
def get_analysis_stats(db: Session = Depends(database.get_db)):
    """获取数据分析统计数据"""
    try:
        # 获取所有对话日志
        logs = db.query(models.ConversationLog).all()
        
        # 1. 热门问题统计
        questions = [log.question for log in logs]
        question_counts = {}
        for q in questions:
            if q in question_counts:
                question_counts[q] += 1
            else:
                question_counts[q] = 1
        hot_questions = sorted(question_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # 2. 游客关注点分析
        keywords = [
            '门票', '价格', '开放', '时间', '路线', '导览', '景点', '历史', '文化',
            '美食', '住宿', '交通', '停车', '厕所', '服务', '设施', '活动', '表演'
        ]
        keyword_counts = {}
        for log in logs:
            for keyword in keywords:
                if keyword in log.question:
                    if keyword in keyword_counts:
                        keyword_counts[keyword] += 1
                    else:
                        keyword_counts[keyword] = 1
        focus_points = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # 3. 情感分析
        positive_words = ['好', '棒', '满意', '喜欢', '赞', '感谢', '谢谢', '不错', '优秀']
        negative_words = ['差', '糟糕', '不满', '失望', '讨厌', '问题', '投诉', '贵', '慢']
        sentiment = {'positive': 0, 'negative': 0, 'neutral': 0}
        
        for log in logs:
            positive_count = sum(1 for word in positive_words if word in log.question)
            negative_count = sum(1 for word in negative_words if word in log.question)
            if positive_count > negative_count:
                sentiment['positive'] += 1
            elif negative_count > positive_count:
                sentiment['negative'] += 1
            else:
                sentiment['neutral'] += 1
        
        # 4. 响应时间分析
        response_times = [log.response_time for log in logs if log.response_time]
        response_time_stats = {
            'average': sum(response_times) / len(response_times) if response_times else 0,
            'max': max(response_times) if response_times else 0,
            'min': min(response_times) if response_times else 0
        }
        
        return {
            "code": 200,
            "data": {
                "hot_questions": hot_questions,
                "focus_points": focus_points,
                "sentiment": sentiment,
                "response_time": response_time_stats,
                "total_logs": len(logs)
            },
            "message": "success"
        }
    except Exception as e:
        logger.error(f"数据分析接口异常: {str(e)}")
        raise HTTPException(status_code=500, detail="获取数据分析失败")

# 将以下代码加入 main.py 的路由区域

@app.get("/api/v1/config", tags=["数字人配置"])
def get_config(db: Session = Depends(database.get_db)):
    """获取数字人当前配置，如果没有则初始化一条默认的"""
    config = db.query(models.DigitalHumanConfig).first()
    if not config:
        config = models.DigitalHumanConfig(
            avatar_style="古风导游",
            voice_type="温柔女声",
            greeting_text="您好，我是您的灵山数字导游，请问有什么可以帮您？"
        )
        db.add(config)
        db.commit()
        db.refresh(config)
    return {"code": 200, "data": config, "message": "success"}

@app.post("/api/v1/config", tags=["数字人配置"])
def update_config(config_data: schemas.ConfigBase, db: Session = Depends(database.get_db)):
    """更新数字人配置"""
    config = db.query(models.DigitalHumanConfig).first()
    if not config:
        config = models.DigitalHumanConfig(**config_data.dict())
        db.add(config)
    else:
        config.avatar_style = config_data.avatar_style
        config.voice_type = config_data.voice_type
        config.greeting_text = config_data.greeting_text
    db.commit()
    db.refresh(config)
    return {"code": 200, "data": config, "message": "保存成功"}