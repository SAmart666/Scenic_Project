<template>
  <div class="dashboard-container">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card shadow="hover" class="data-card">
          <div class="title">知识库总数</div>
          <div class="value">{{ stats.total_kb_count }} <span class="unit">条</span></div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover" class="data-card">
          <div class="title">累计对话人次</div>
          <div class="value">{{ stats.total_chat_count }} <span class="unit">次</span></div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover" class="data-card">
          <div class="title">平均响应时间</div>
          <div class="value">{{ stats.avg_response_time }} <span class="unit">ms</span></div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 数据分析图表区域 -->
    <el-row :gutter="20" style="margin-top: 20px;">
      <!-- 热门问题 -->
      <el-col :span="12">
        <el-card shadow="always">
          <template #header>
            <div class="card-header">
              <span>热门问题TOP10</span>
            </div>
          </template>
          <div ref="hotQuestionsRef" style="width: 100%; height: 300px;"></div>
        </el-card>
      </el-col>
      <!-- 游客关注点 -->
      <el-col :span="12">
        <el-card shadow="always">
          <template #header>
            <div class="card-header">
              <span>游客关注点分布</span>
            </div>
          </template>
          <div ref="focusPointsRef" style="width: 100%; height: 300px;"></div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="20" style="margin-top: 20px;">
      <!-- 情感分析 -->
      <el-col :span="12">
        <el-card shadow="always">
          <template #header>
            <div class="card-header">
              <span>游客情感分析</span>
            </div>
          </template>
          <div ref="sentimentRef" style="width: 100%; height: 300px;"></div>
        </el-card>
      </el-col>
      <!-- 响应时间 -->
      <el-col :span="12">
        <el-card shadow="always">
          <template #header>
            <div class="card-header">
              <span>响应时间分布</span>
            </div>
          </template>
          <div ref="responseTimeRef" style="width: 100%; height: 300px;"></div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import * as echarts from 'echarts'

const stats = ref({
  total_kb_count: 0,
  total_chat_count: 0,
  avg_response_time: 0
})
const analysisData = ref({
  hot_questions: [],
  focus_points: [],
  sentiment: { positive: 0, negative: 0, neutral: 0 },
  response_time: { average: 0, max: 0, min: 0 },
  total_logs: 0
})

// 图表引用
const hotQuestionsRef = ref(null)
const focusPointsRef = ref(null)
const sentimentRef = ref(null)
const responseTimeRef = ref(null)

// 获取基础统计数据
const fetchStats = async () => {
  try {
    const res = await axios.get('/api/v1/stats/overview')
    if (res.data.code === 200) {
      stats.value = res.data.data
    }
  } catch (error) {
    console.error("获取统计数据失败", error)
  }
}

// 获取数据分析统计数据
const fetchAnalysisData = async () => {
  try {
    const res = await axios.get('/api/v1/stats/analysis')
    if (res.data.code === 200) {
      analysisData.value = res.data.data
      initCharts()
    }
  } catch (error) {
    console.error("获取数据分析失败", error)
  }
}

// 初始化所有图表
const initCharts = () => {
  initHotQuestionsChart()
  initFocusPointsChart()
  initSentimentChart()
  initResponseTimeChart()
}

// 热门问题图表
const initHotQuestionsChart = () => {
  if (!hotQuestionsRef.value) return
  const myChart = echarts.init(hotQuestionsRef.value)
  const data = analysisData.value.hot_questions
  const questions = data.map(item => item[0])
  const counts = data.map(item => item[1])
  
  const option = {
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
    grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
    xAxis: { type: 'value' },
    yAxis: {
      type: 'category',
      data: questions,
      axisLabel: { interval: 0, rotate: 30 }
    },
    series: [{
      data: counts,
      type: 'bar',
      itemStyle: { color: '#1890ff' }
    }]
  }
  myChart.setOption(option)
  window.addEventListener('resize', () => myChart.resize())
}

// 游客关注点图表
const initFocusPointsChart = () => {
  if (!focusPointsRef.value) return
  const myChart = echarts.init(focusPointsRef.value)
  const data = analysisData.value.focus_points
  const keywords = data.map(item => item[0])
  const counts = data.map(item => item[1])
  
  const option = {
    tooltip: { trigger: 'item' },
    legend: { orient: 'vertical', left: 'left' },
    series: [{
      name: '关注点',
      type: 'pie',
      radius: '60%',
      data: data.map(item => ({ name: item[0], value: item[1] })),
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }]
  }
  myChart.setOption(option)
  window.addEventListener('resize', () => myChart.resize())
}

// 情感分析图表
const initSentimentChart = () => {
  if (!sentimentRef.value) return
  const myChart = echarts.init(sentimentRef.value)
  const sentiment = analysisData.value.sentiment
  
  const option = {
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
    grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
    xAxis: { type: 'category', data: ['正面', '负面', '中性'] },
    yAxis: { type: 'value' },
    series: [{
      data: [sentiment.positive, sentiment.negative, sentiment.neutral],
      type: 'bar',
      itemStyle: {
        color: function(params) {
          const colors = ['#52c41a', '#f5222d', '#d9d9d9']
          return colors[params.dataIndex]
        }
      }
    }]
  }
  myChart.setOption(option)
  window.addEventListener('resize', () => myChart.resize())
}

// 响应时间图表
const initResponseTimeChart = () => {
  if (!responseTimeRef.value) return
  const myChart = echarts.init(responseTimeRef.value)
  const responseTime = analysisData.value.response_time
  
  const option = {
    tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
    grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
    xAxis: { type: 'category', data: ['平均响应', '最大响应', '最小响应'] },
    yAxis: { type: 'value', name: 'ms' },
    series: [{
      data: [
        parseFloat(responseTime.average.toFixed(2)),
        responseTime.max,
        responseTime.min
      ],
      type: 'bar',
      itemStyle: { color: '#722ed1' }
    }]
  }
  myChart.setOption(option)
  window.addEventListener('resize', () => myChart.resize())
}

onMounted(() => {
  fetchStats()
  fetchAnalysisData()
})
</script>

<style scoped>
.data-card {
  text-align: center;
  padding: 20px 0;
}
.data-card .title {
  font-size: 16px;
  color: #909399;
  margin-bottom: 10px;
}
.data-card .value {
  font-size: 32px;
  font-weight: bold;
  color: #303133;
}
.data-card .unit {
  font-size: 14px;
  font-weight: normal;
  color: #909399;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>