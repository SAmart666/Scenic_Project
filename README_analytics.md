# 数据分析功能说明

本功能为景区数字人导游系统的数据分析模块，已集成到管理后台的Dashboard页面中，提供实时的数据统计和可视化展示。

## 相关文件

- **后端**：`backend/main.py`（添加了数据分析接口）
- **前端**：`frontend/src/views/Dashboard.vue`（集成了数据分析图表）
- **数据分析脚本**：`backend/analyze_data.py`（独立的数据分析工具）

- 运行手动分析的详细数据保存在：**analysis_results** 文件夹
- 数据大屏打开管理后台即可看见
![img.png](img.png)

# 技术实现
**API接口**：`/api/v1/stats/analysis`

## 使用指南

### 方式一：管理后台集成功能（推荐）

1. **启动后端服务**
   ```bash
   cd backend
   python main.py
   ```

2. **启动前端服务**
   ```bash
   cd frontend
   npm run dev
   ```

3. **访问管理后台**
   - 打开浏览器访问：`http://localhost:5173`
   - 进入Dashboard页面，即可看到数据分析图表


### 方式二：手动运行数据分析脚本

1. **确保后端服务运行**
   ```bash
   cd backend
   python main.py
   ```

2. **安装依赖包**
   ```bash
   pip install requests jieba matplotlib pandas
   ```

3. **运行分析脚本**
   ```bash
   cd backend
   python analyze_data.py
   ```

4. **查看分析结果**
   - 分析结果保存在 `backend/analysis_results` 目录中
   - 包含以下文件：
     - `hot_questions.txt` - 热门问题统计
     - `hot_questions.png` - 热门问题图表
     - `focus_points.txt` - 游客关注点分析
     - `focus_points.png` - 关注点分布图表
     - `sentiment_analysis.txt` - 情感分析结果
     - `sentiment_analysis.png` - 情感分析图表
     - `response_time.txt` - 响应时间分析
     - `response_time.png` - 响应时间分布图表
     - `tourist_feedback_report.md` - 游客感受度报告
     - `system_test.txt` - 系统测试结果
![img_1.png](img_1.png)


5. **系统测试功能**
   - 脚本会自动测试核心对话接口
   - 发送5个测试问题到系统：
     - 门票多少钱？
     - 景区开放时间
     - 有什么好玩的景点？
     - 如何到达景区？
     - 景区有停车场吗？
   - 记录响应时间和测试结果

## 数据展示说明

### 热门问题TOP10
- **图表类型**：水平柱状图
- **数据含义**：展示出现频率最高的10个问题
- **使用建议**：将热门问题添加到知识库，提高回答效率

### 游客关注点分布
- **图表类型**：饼图
- **数据含义**：展示游客关注的各个领域占比
- **使用建议**：针对重点关注领域，优化相关内容和服务

### 情感分析
- **图表类型**：柱状图
- **数据含义**：展示正面、负面和中性情绪的分布
- **使用建议**：保持正面服务态度，及时处理负面反馈

### 响应时间分析
- **图表类型**：柱状图
- **数据含义**：展示系统响应时间的表现
- **使用建议**：监控系统性能，确保响应速度稳定


## 🔧 常见问题

### Q: 图表显示空白怎么办？
A: 检查后端服务是否正常运行，数据库中是否有对话记录。

### Q: 数据更新不及时怎么办？
A: 刷新页面即可获取最新数据，或等待自动数据刷新。

### Q: 图表显示异常怎么办？
A: 检查浏览器控制台是否有错误信息，确保ECharts库加载正常。

### Q: 如何导出分析数据？
A: 目前支持通过后端API获取原始数据，可自行编写脚本导出。

## 相关文件

- **后端**：`backend/main.py`（添加了数据分析接口）
- **前端**：`frontend/src/views/Dashboard.vue`（集成了数据分析图表）
- **数据分析脚本**：`backend/analyze_data.py`（独立的数据分析工具）

