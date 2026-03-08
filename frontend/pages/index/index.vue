<template>
  <view class="container">
    <!-- 顶部状态栏 -->
    <view class="header card">
      <view class="streak">
        <text class="icon">🔥</text>
        <text class="text">连续学习 {{ learningDays }} 天</text>
      </view>
      <view class="stats-row">
        <view class="stat-item">
          <text class="num">{{ totalQuestions }}</text>
          <text class="label">总题数</text>
        </view>
        <view class="stat-item">
          <text class="num">{{ masteredQuestions }}</text>
          <text class="label">已掌握</text>
        </view>
        <view class="stat-item">
          <text class="num">{{ accuracyRate }}%</text>
          <text class="label">正确率</text>
        </view>
      </view>
    </view>

    <!-- 快捷操作 -->
    <view class="quick-actions card">
      <view class="action-btn" @click="goToCamera">
        <view class="icon">📸</view>
        <text class="text">拍题</text>
      </view>
      <view class="action-btn" @click="goToStats">
        <view class="icon">📊</view>
        <text class="text">统计</text>
      </view>
      <view class="action-btn" @click="goToNotes">
        <view class="icon">📝</view>
        <text class="text">笔记</text>
      </view>
    </view>

    <!-- 今日任务 -->
    <view class="section card">
      <view class="section-header">
        <text class="title">今日任务</text>
        <text class="more">查看全部 ></text>
      </view>
      <view class="task-list">
        <view class="task-item">
          <text class="checkbox">●</text>
          <text class="task-text">复习数学错题 3 道</text>
        </view>
        <view class="task-item">
          <text class="checkbox">●</text>
          <text class="task-text">复习英语错题 2 道</text>
        </view>
        <view class="task-item">
          <text class="checkbox">○</text>
          <text class="task-text">完成今日测验</text>
        </view>
      </view>
    </view>

    <!-- 搜索框 -->
    <view class="section card">
      <view class="search-box">
        <input 
          class="search-input" 
          v-model="searchKeyword" 
          placeholder="搜索题目、知识点..."
          @confirm="searchQuestions"
        />
        <button class="search-btn" @click="searchQuestions">🔍 搜索</button>
      </view>
    </view>

    <!-- 最近错题 -->
    <view class="section card">
      <view class="section-header">
        <text class="title">最近错题</text>
        <text class="more">查看全部 ></text>
      </view>
      <view class="question-list">
        <view class="question-item" v-for="(item, index) in recentQuestions" :key="index" @click="goToQuestion(item)">
          <view class="question-tag" :class="item.subject">{{ item.subject }}</view>
          <view class="question-info">
            <text class="question-title">{{ item.title }}</text>
            <text class="question-date">{{ item.date }}</text>
          </view>
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
      masteredQuestions: 15,
      accuracyRate: 85,
      searchKeyword: '',
      recentQuestions: [
        { id: 1, subject: 'math', title: '二次函数最值问题', date: '2026-03-07' },
        { id: 2, subject: 'english', title: '英语时态练习', date: '2026-03-06' },
        { id: 3, subject: 'math', title: '一次函数应用题', date: '2026-03-05' }
      ],
      searchResults: []
    }
  },
  onLoad() {
    this.loadStats()
  },
  onPullDownRefresh() {
    this.loadStats()
    setTimeout(() => {
      uni.stopPullDownRefresh()
    }, 1000)
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
          this.totalQuestions = data.total_questions
          this.masteredQuestions = data.mastered_questions
          this.accuracyRate = Math.round(data.accuracy_rate * 100)
        }
      } catch (e) {
        console.log('加载统计失败', e)
      }
    },
    goToCamera() {
      uni.navigateTo({
        url: '/pages/camera/camera'
      })
    },
    goToStats() {
      uni.navigateTo({
        url: '/pages/stats/stats'
      })
    },
    goToNotes() {
      uni.showToast({
        title: '功能开发中',
        icon: 'none'
      })
    },
    goToQuestion(item) {
      uni.navigateTo({
        url: `/pages/question/question?id=${item.id}`
      })
    },
    async searchQuestions() {
      if (!this.searchKeyword.trim()) {
        uni.showToast({
          title: '请输入搜索内容',
          icon: 'none'
        })
        return
      }
      
      uni.showLoading({
        title: '搜索中...'
      })
      
      try {
        const res = await uni.request({
          url: 'http://localhost:8000/api/questions',
          method: 'GET',
          data: {
            keyword: this.searchKeyword,
            limit: 20
          }
        })
        
        if (res.statusCode === 200) {
          this.searchResults = res.data
          if (this.searchResults.length === 0) {
            uni.showToast({
              title: '未找到相关题目',
              icon: 'none'
            })
          } else {
            uni.navigateTo({
              url: `/pages/search/search?keyword=${this.searchKeyword}`
            })
          }
        }
      } catch (e) {
        console.log('搜索失败', e)
        uni.showToast({
          title: '搜索失败，请重试',
          icon: 'none'
        })
      } finally {
        uni.hideLoading()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  padding: 20rpx;
}

.header {
  .streak {
    display: flex;
    align-items: center;
    margin-bottom: 30rpx;
    
    .icon {
      font-size: 36rpx;
      margin-right: 10rpx;
    }
    
    .text {
      font-size: 28rpx;
      color: #FF9800;
      font-weight: 600;
    }
  }
  
  .stats-row {
    display: flex;
    justify-content: space-around;
    
    .stat-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      
      .num {
        font-size: 40rpx;
        font-weight: 600;
        color: #2196F3;
      }
      
      .label {
        font-size: 24rpx;
        color: #999;
        margin-top: 8rpx;
      }
    }
  }
}

.quick-actions {
  display: flex;
  justify-content: space-around;
  padding: 40rpx 20rpx;
  
  .action-btn {
    display: flex;
    flex-direction: column;
    align-items: center;
    
    .icon {
      font-size: 48rpx;
      margin-bottom: 10rpx;
    }
    
    .text {
      font-size: 24rpx;
      color: #666;
    }
  }
}

.section {
  .search-box {
    display: flex;
    align-items: center;
    padding: 20rpx 0;
    
    .search-input {
      flex: 1;
      height: 72rpx;
      padding: 0 24rpx;
      background: #F5F7FA;
      border-radius: 36rpx;
      font-size: 28rpx;
      color: #333;
    }
    
    .search-btn {
      margin-left: 20rpx;
      padding: 0 32rpx;
      height: 72rpx;
      line-height: 72rpx;
      background: linear-gradient(90deg, #2196F3, #1E88E5);
      color: #FFF;
      border-radius: 36rpx;
      font-size: 28rpx;
      border: none;
    }
  }
  
  .section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20rpx;
    
    .title {
      font-size: 32rpx;
      font-weight: 600;
      color: #333;
    }
    
    .more {
      font-size: 24rpx;
      color: #999;
    }
  }
  
  .task-list {
    .task-item {
      display: flex;
      align-items: center;
      padding: 16rpx 0;
      
      .checkbox {
        font-size: 28rpx;
        color: #2196F3;
        margin-right: 16rpx;
      }
      
      .task-text {
        font-size: 28rpx;
        color: #333;
      }
    }
  }
  
  .question-list {
    .question-item {
      display: flex;
      align-items: center;
      padding: 20rpx 0;
      border-bottom: 1rpx solid #F0F0F0;
      
      .question-tag {
        padding: 6rpx 12rpx;
        border-radius: 8rpx;
        font-size: 24rpx;
        margin-right: 16rpx;
        
        &.math {
          background: #E3F2FD;
          color: #2196F3;
        }
        
        &.english {
          background: #E8F5E9;
          color: #4CAF50;
        }
      }
      
      .question-info {
        flex: 1;
        display: flex;
        flex-direction: column;
        
        .question-title {
          font-size: 28rpx;
          color: #333;
          margin-bottom: 8rpx;
        }
        
        .question-date {
          font-size: 24rpx;
          color: #999;
        }
      }
    }
  }
}
</style>
