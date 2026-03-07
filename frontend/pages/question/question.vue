<template>
  <view class="container">
    <!-- 题目标签 -->
    <view class="tags card">
      <view class="tag math">📐 数学 · 二次函数</view>
      <view class="tag difficulty">🔥 难度：中等</view>
      <view class="tag date">📅 2026-03-07</view>
    </view>

    <!-- 题目内容 -->
    <view class="section card">
      <view class="section-title">题目内容</view>
      <view class="question-content">
        <text class="content-text">已知函数 f(x) = x² + 2x + 1，求函数的最小值。</text>
      </view>
    </view>

    <!-- AI 分析 -->
    <view class="section card">
      <view class="section-title">🤖 AI 分析</view>
      <view class="analysis-list">
        <view class="analysis-item">
          <text class="analysis-label">🎯 知识点</text>
          <text class="analysis-value">二次函数最值问题</text>
        </view>
        <view class="analysis-item">
          <text class="analysis-label">💡 解题思路</text>
          <text class="analysis-value">配方法或求导法</text>
        </view>
        <view class="analysis-item">
          <text class="analysis-label">⚠️ 易错点</text>
          <text class="analysis-value">符号处理、配方不完整</text>
        </view>
      </view>
    </view>

    <!-- 相似题推荐 -->
    <view class="section card">
      <view class="section-title">相似题推荐</view>
      <view class="similar-list">
        <view class="similar-item">
          <text class="similar-title">类似题 1 (85% 相似)</text>
        </view>
        <view class="similar-item">
          <text class="similar-title">类似题 2 (78% 相似)</text>
        </view>
      </view>
    </view>

    <!-- 掌握程度 -->
    <view class="mastery card">
      <text class="mastery-label">掌握程度</text>
      <view class="mastery-options">
        <button class="mastery-btn" :class="{ active: mastery === 'unlearned' }" @click="setMastery('unlearned')">未掌握</button>
        <button class="mastery-btn" :class="{ active: mastery === 'partial' }" @click="setMastery('partial')">部分</button>
        <button class="mastery-btn" :class="{ active: mastery === 'mastered' }" @click="setMastery('mastered')">掌握</button>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      questionId: 1,
      mastery: 'unlearned'
    }
  },
  methods: {
    async setMastery(level) {
      this.mastery = level
      try {
        await uni.request({
          url: `http://localhost:8000/api/questions/${this.questionId}/mastery`,
          method: 'PUT',
          data: { mastery: level }
        })
        uni.showToast({
          title: '已更新',
          icon: 'success'
        })
      } catch (e) {
        console.log('更新失败', e)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  padding: 20rpx;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 16rpx;
  
  .tag {
    padding: 8rpx 16rpx;
    border-radius: 8rpx;
    font-size: 24rpx;
    
    &.math {
      background: #E3F2FD;
      color: #2196F3;
    }
    
    &.difficulty {
      background: #FFF3E0;
      color: #FF9800;
    }
    
    &.date {
      background: #F5F5F5;
      color: #666;
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

.question-content {
  .content-text {
    font-size: 28rpx;
    line-height: 2;
    color: #333;
  }
}

.analysis-list {
  .analysis-item {
    display: flex;
    padding: 16rpx 0;
    border-bottom: 1rpx solid #F0F0F0;
    
    .analysis-label {
      width: 200rpx;
      font-size: 28rpx;
      color: #666;
    }
    
    .analysis-value {
      flex: 1;
      font-size: 28rpx;
      color: #333;
    }
  }
}

.similar-list {
  .similar-item {
    padding: 20rpx 0;
    border-bottom: 1rpx solid #F0F0F0;
    
    .similar-title {
      font-size: 28rpx;
      color: #2196F3;
    }
  }
}

.mastery {
  margin-top: 40rpx;
  
  .mastery-label {
    font-size: 28rpx;
    font-weight: 600;
    color: #333;
    display: block;
    margin-bottom: 20rpx;
  }
  
  .mastery-options {
    display: flex;
    gap: 20rpx;
    
    .mastery-btn {
      flex: 1;
      background: #F5F5F5;
      color: #666;
      border: 2rpx solid #E0E0E0;
      border-radius: 12rpx;
      padding: 16rpx 0;
      font-size: 28rpx;
      
      &.active {
        background: #2196F3;
        color: #FFFFFF;
        border-color: #2196F3;
      }
    }
  }
}
</style>
