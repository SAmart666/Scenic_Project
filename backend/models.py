from sqlalchemy import Column, Integer, String, Text, DateTime, Float
import datetime
from database import Base  # 从 database.py 导入基类

class KnowledgeBase(Base):
    __tablename__ = "knowledge_base"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(50), default="general")
    created_at = Column(DateTime, default=datetime.datetime.now)

class ConversationLog(Base):
    __tablename__ = "conversation_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(64))
    question = Column(Text)
    answer = Column(Text)
    response_time = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now)

# 如果有数字人配置，也写在这里...