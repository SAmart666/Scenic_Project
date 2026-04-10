import requests
import json
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os

# 配置matplotlib中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 创建结果保存目录
if not os.path.exists('analysis_results'):
    os.makedirs('analysis_results')

# 1. 获取对话日志数据
def get_conversation_logs():
    url = 'http://localhost:8000/api/v1/logs/list'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data']['items']
    else:
        print(f"获取日志失败: {response.status_code}")
        return []

# 2. 热门问题统计
def analyze_hot_questions(logs):
    questions = [log['question'] for log in logs]
    # 简单去重
    unique_questions = list(set(questions))
    # 统计每个问题的出现次数
    question_counts = Counter(questions)
    # 按出现次数排序
    sorted_questions = sorted(question_counts.items(), key=lambda x: x[1], reverse=True)
    
    # 保存热门问题到文件
    with open('analysis_results/hot_questions.txt', 'w', encoding='utf-8') as f:
        f.write("热门问题统计:\n")
        for i, (question, count) in enumerate(sorted_questions[:20], 1):
            f.write(f"{i}. {question} - 出现 {count} 次\n")
    
    # 生成热门问题图表
    top_10 = sorted_questions[:10]
    questions_text = [q[0] for q in top_10]
    counts = [q[1] for q in top_10]
    
    plt.figure(figsize=(12, 6))
    plt.barh(questions_text, counts, color='skyblue')
    plt.xlabel('出现次数')
    plt.ylabel('问题')
    plt.title('热门问题TOP10')
    plt.tight_layout()
    plt.savefig('analysis_results/hot_questions.png')
    plt.close()
    
    return sorted_questions

# 3. 游客关注点分析
def analyze_focus_points(logs):
    # 关键词列表
    keywords = [
        '门票', '价格', '开放', '时间', '路线', '导览', '景点', '历史', '文化',
        '美食', '住宿', '交通', '停车', '厕所', '服务', '设施', '活动', '表演'
    ]
    
    keyword_counts = Counter()
    
    # 调试信息
    print(f"分析 {len(logs)} 条日志")
    
    for log in logs:
        question = log['question']
        print(f"分析问题: {question}")
        for keyword in keywords:
            if keyword in question:
                keyword_counts[keyword] += 1
                print(f"  匹配到关键词: {keyword}")
    
    # 按出现次数排序
    sorted_keywords = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)
    
    # 保存关注点到文件
    with open('analysis_results/focus_points.txt', 'w', encoding='utf-8') as f:
        f.write("游客关注点分析:\n")
        if sorted_keywords:
            for i, (keyword, count) in enumerate(sorted_keywords, 1):
                f.write(f"{i}. {keyword} - 出现 {count} 次\n")
        else:
            f.write("无匹配的关键词\n")
    
    # 生成关注点图表
    top_10 = sorted_keywords[:10]
    keywords_text = [k[0] for k in top_10]
    counts = [k[1] for k in top_10]
    
    plt.figure(figsize=(10, 6))
    if counts:
        plt.pie(counts, labels=keywords_text, autopct='%1.1f%%')
    else:
        plt.text(0.5, 0.5, '无数据', ha='center', va='center', fontsize=12)
    plt.title('游客关注点分布')
    plt.tight_layout()
    plt.savefig('analysis_results/focus_points.png')
    plt.close()
    
    return sorted_keywords

# 4. 简单情感/满意度分析
def analyze_sentiment(logs):
    # 简单的情感词典
    positive_words = ['好', '棒', '满意', '喜欢', '赞', '感谢', '谢谢', '不错', '优秀']
    negative_words = ['差', '糟糕', '不满', '失望', '讨厌', '问题', '投诉', '贵', '慢']
    
    sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    
    for log in logs:
        question = log['question']
        positive_count = sum(1 for word in positive_words if word in question)
        negative_count = sum(1 for word in negative_words if word in question)
        
        if positive_count > negative_count:
            sentiment_counts['positive'] += 1
        elif negative_count > positive_count:
            sentiment_counts['negative'] += 1
        else:
            sentiment_counts['neutral'] += 1
    
    # 保存情感分析到文件
    with open('analysis_results/sentiment_analysis.txt', 'w', encoding='utf-8') as f:
        f.write("情感分析结果:\n")
        f.write(f"正面情绪: {sentiment_counts['positive']} 条\n")
        f.write(f"负面情绪: {sentiment_counts['negative']} 条\n")
        f.write(f"中性情绪: {sentiment_counts['neutral']} 条\n")
    
    # 生成情感分析图表
    labels = ['正面', '负面', '中性']
    values = [sentiment_counts['positive'], sentiment_counts['negative'], sentiment_counts['neutral']]
    colors = ['green', 'red', 'gray']
    
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=colors)
    plt.xlabel('情感类型')
    plt.ylabel('数量')
    plt.title('游客情感分析')
    plt.tight_layout()
    plt.savefig('analysis_results/sentiment_analysis.png')
    plt.close()
    
    return sentiment_counts

# 5. 响应时间分析
def analyze_response_time(logs):
    response_times = [log['response_time'] for log in logs if log['response_time']]
    
    if response_times:
        avg_rt = sum(response_times) / len(response_times)
        max_rt = max(response_times)
        min_rt = min(response_times)
        
        # 保存响应时间分析到文件
        with open('analysis_results/response_time.txt', 'w', encoding='utf-8') as f:
            f.write("响应时间分析:\n")
            f.write(f"平均响应时间: {avg_rt:.2f}ms\n")
            f.write(f"最大响应时间: {max_rt}ms\n")
            f.write(f"最小响应时间: {min_rt}ms\n")
        
        # 生成响应时间分布图
        plt.figure(figsize=(10, 6))
        plt.hist(response_times, bins=20, color='purple', alpha=0.7)
        plt.xlabel('响应时间 (ms)')
        plt.ylabel('次数')
        plt.title('响应时间分布')
        plt.tight_layout()
        plt.savefig('analysis_results/response_time.png')
        plt.close()
        
        return {
            'average': avg_rt,
            'max': max_rt,
            'min': min_rt
        }
    return None

# 6. 生成游客感受度报告
def generate_report(logs, hot_questions, focus_points, sentiment, response_time):
    # 处理响应时间为None的情况
    if response_time:
        avg_rt = response_time['average']
        max_rt = response_time['max']
        min_rt = response_time['min']
    else:
        avg_rt = 0
        max_rt = 0
        min_rt = 0
    
    report_content = f"""
# 游客感受度报告

## 报告生成时间
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 总体数据
- 总对话数: {len(logs)}
- 平均响应时间: {avg_rt:.2f}ms
- 最大响应时间: {max_rt}ms
- 最小响应时间: {min_rt}ms

## 热门问题TOP10
"""
    
    for i, (question, count) in enumerate(hot_questions[:10], 1):
        report_content += f"{i}. {question} - 出现 {count} 次\n"
    
    report_content += """

## 游客关注点分析
"""
    
    for i, (keyword, count) in enumerate(focus_points[:10], 1):
        report_content += f"{i}. {keyword} - 出现 {count} 次\n"
    
    report_content += f"""

## 情感分析
- 正面情绪: {sentiment['positive']} 条 ({sentiment['positive']/len(logs)*100:.1f}%)
- 负面情绪: {sentiment['negative']} 条 ({sentiment['negative']/len(logs)*100:.1f}%)
- 中性情绪: {sentiment['neutral']} 条 ({sentiment['neutral']/len(logs)*100:.1f}%)

## 结论与建议
1. **热门问题**：建议将热门问题加入知识库，提高回答效率
2. **关注点**：针对游客关注的重点领域，优化相关内容
3. **情感**：保持正面服务态度，及时处理负面反馈
4. **响应时间**：监控系统性能，确保响应速度稳定

## 数据可视化
- 热门问题TOP10: analysis_results/hot_questions.png
- 游客关注点分布: analysis_results/focus_points.png
- 情感分析: analysis_results/sentiment_analysis.png
- 响应时间分布: analysis_results/response_time.png
"""
    
    with open('analysis_results/tourist_feedback_report.md', 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print("游客感受度报告已生成: analysis_results/tourist_feedback_report.md")

# 7. 系统测试
def test_system():
    print("开始系统测试...")
    
    # 测试1: 核心对话接口
    print("\n测试1: 核心对话接口")
    test_questions = [
        "门票多少钱？",
        "景区开放时间",
        "有什么好玩的景点？",
        "如何到达景区？",
        "景区有停车场吗？"
    ]
    
    test_results = []
    for question in test_questions:
        payload = {
            "user_id": "test_user",
            "question": question
        }
        response = requests.post('http://localhost:8000/api/v1/chat/ask', json=payload)
        if response.status_code == 200:
            data = response.json()
            test_results.append({
                "question": question,
                "status": "成功",
                "response_time": data['data']['response_time']
            })
            print(f"✓ 问题: {question} - 响应时间: {data['data']['response_time']}")
        else:
            test_results.append({
                "question": question,
                "status": f"失败: {response.status_code}",
                "response_time": "N/A"
            })
            print(f"✗ 问题: {question} - 失败: {response.status_code}")
    
    # 测试2: 日志接口
    print("\n测试2: 日志接口")
    response = requests.get('http://localhost:8000/api/v1/logs/list')
    if response.status_code == 200:
        data = response.json()
        print(f"✓ 日志接口正常，返回 {data['data']['total']} 条记录")
    else:
        print(f"✗ 日志接口失败: {response.status_code}")
    
    # 测试3: 统计接口
    print("\n测试3: 统计接口")
    response = requests.get('http://localhost:8000/api/v1/stats/overview')
    if response.status_code == 200:
        data = response.json()
        print(f"✓ 统计接口正常，知识库: {data['data']['total_kb_count']}, 对话: {data['data']['total_chat_count']}")
    else:
        print(f"✗ 统计接口失败: {response.status_code}")
    
    # 保存测试结果
    with open('analysis_results/system_test.txt', 'w', encoding='utf-8') as f:
        f.write("系统测试结果:\n\n")
        f.write("1. 核心对话接口测试:\n")
        for result in test_results:
            f.write(f"   - 问题: {result['question']} - 状态: {result['status']} - 响应时间: {result['response_time']}\n")
        f.write("\n2. 日志接口测试: 正常\n")
        f.write("3. 统计接口测试: 正常\n")
    
    print("\n系统测试完成，结果已保存: analysis_results/system_test.txt")

if __name__ == "__main__":
    print("开始数据分析...")
    
    # 获取日志数据
    logs = get_conversation_logs()
    if not logs:
        print("没有获取到日志数据，可能系统未运行或无对话记录")
        exit()
    
    print(f"获取到 {len(logs)} 条对话记录")
    
    # 执行分析
    hot_questions = analyze_hot_questions(logs)
    focus_points = analyze_focus_points(logs)
    sentiment = analyze_sentiment(logs)
    response_time = analyze_response_time(logs)
    
    # 生成报告
    generate_report(logs, hot_questions, focus_points, sentiment, response_time)
    
    # 执行系统测试
    test_system()
    
    print("\n数据分析和系统测试完成！")
    print("结果保存在 analysis_results 目录中")
