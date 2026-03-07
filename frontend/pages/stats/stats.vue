<template>
  <view class="container">
    <!-- 本周概览 -->
    <view class="overview card">
      <view class="overview-item">
        <text class="num">{{ learningDays }}</text>
        <text class="label">学习天数</text>
      </view>
      <view class="overview-item">
        <text class="num">{{ totalQuestions }}</text>
        <text class="label">总题数</text>
      </view>
      <view class="overview-item">
        <text class="num">{{ accuracyRate }}%</text>
        <text class="label">正确率</text>
      </view>
    </view>

    <!-- 学习趋势 -->
    <view class="section card">
      <view class="section-title">学习趋势</view>
      <view class="chart-placeholder">
        <text class="chart-icon">📊</text>
        <text class="chart-hint">图表开发中</text>
      </view>
    </view>

    <!-- 知识点分布 -->
    <view class="section card">
      <view class="section-title">知识点分布</view>
      <view class="knowledge-list">
        <view class="knowledge-item">
          <text class="knowledge-name">📐 二次函数</text>
          <view class="progress-bar">
            <view class="progress" style="width: 60%"></view>
          </view>
          <text class="knowledge-percent">60%</text>
        </view>
        <view class="knowledge-item">
          <text class="knowledge-name">📐 一次函数</text>
          <view class="progress-bar">
            <view class="progress" style="width: 30%"></view>
          </view>
          <text class="knowledge-percent">30%</text>
        </view>
        <view class="knowledge-item">
          <text class="knowledge-name">📐 不等式</text>
          <view class="progress-bar">
            <view class="progress" style="width: 10%"></view>
          </view>
          <text class="knowledge-percent">10%</text>
        </view>
      </view>
    </view>

    <!-- 成就徽章 -->
    <view class="section card">
      <view class="section-title">成就徽章</view>
      <view class="badge-list">
        <view class="badge-item">
          <text class="badge-icon">🏆</text>
          <text class="badge-name">连续学习 7 天</text>
        </view>
        <view class="badge-item">
          <text class="badge-icon">🎯</text>
          <text class="badge-name">正确率 90%+</text>
        </view>
        <view class="badge-item">
          <text class="badge-icon">📚</text>
          <text class="badge-name">刷题 100 道</text>
        </view>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      learningDays: 7,
      totalQuestions: 23,
      accuracyRate: 85
    }
  },
  onLoad() {
    this.loadStats()
  },
  methods: {
    async loadStats() {
      try {
        const res = await uni.request({
          url: 'http://localhost:8000/api/stats',
          method: 'GET'
        })
        if (res.statusCode === 200) {
          const data = res.data
          this.learningDays = data.learning_days
          this.totalQuestions = data.total_questions
          this.accuracyRate = Math.round(data.accuracy_rate * 100)
        }
      } catch (e) {
        console.log('加载统计失败', e)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  padding: 20rpx;
}

.overview {
  display: flex;
  justify-content: space-around;
  padding: 40rpx 20rpx;
  
  .overview-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    
    .num {
      font-size: 48rpx;
      font-weight: 600;
      color: #2196F3;
    }
    
    .label {
      font-size: 24rpx;
      color: #999;
      margin-top: 10rpx;
    }
  }
}

.section {
  margin-top: 20rpx;
  
  .section-title {
    font-size: 32rpx;
    font-weight: 600;
    color: #333;
    margin-bottom: 20rpx;
  }
}

.chart-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60rpx 0;
  
  .chart-icon {
    font-size: 100rpx;
    margin-bottom: 20rpx;
  }
  
  .chart-hint {
    font-size: 24rpx;
    color: #999;
  }
}

.knowledge-list {
  .knowledge-item {
    display: flex;
    align-items: center;
    padding: 20rpx 0;
    
    .knowledge-name {
      width: 200rpx;
      font-size: 28rpx;
      color: #333;
    }
    
    .progress-bar {
      flex: 1;
      height: 16rpx;
      background: #F0F0F0;
      border-radius: 8rpx;
      margin: 0 20rpx;
      overflow: hidden;
      
      .progress {
        height: 100%;
        background: linear-gradient(90deg, #2196F3, #64B5F6);
        border-radius: 8rpx;
      }
    }
    
    .knowledge-percent {
      width: 80rpx;
      text-align: right;
      font-size: 24rpx;
      color: #666;
    }
  }
}

.badge-list {
  display: flex;
  flex-wrap: wrap;
  
  .badge-item {
    width: 33.33%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20rpx 0;
    
    .badge-icon {
      font-size: 60rpx;
      margin-bottom: 10rpx;
    }
    
    .badge-name {
      font-size: 24rpx;
      color: #666;
      text-align: center;
    }
  }
}
</style>
