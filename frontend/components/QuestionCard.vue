<template>
  <view class="question-card" @click="handleClick">
    <view class="question-header">
      <view class="subject-tag" :class="subject">{{ subjectText }}</view>
      <view class="difficulty-tag" :class="difficulty">{{ difficultyText }}</view>
    </view>
    <view class="question-content">{{ content }}</view>
    <view class="question-footer">
      <text class="date">{{ date }}</text>
      <view class="mastery-tag" :class="mastery">{{ masteryText }}</view>
    </view>
  </view>
</template>

<script>
export default {
  name: 'QuestionCard',
  props: {
    id: {
      type: Number,
      default: 0
    },
    content: {
      type: String,
      default: ''
    },
    subject: {
      type: String,
      default: 'math'
    },
    difficulty: {
      type: String,
      default: 'medium'
    },
    mastery: {
      type: String,
      default: 'unlearned'
    },
    date: {
      type: String,
      default: ''
    }
  },
  computed: {
    subjectText() {
      const map = {
        math: '📐 数学',
        english: '🔤 英语',
        physics: '⚡ 物理',
        chemistry: '🧪 化学'
      }
      return map[this.subject] || this.subject
    },
    difficultyText() {
      const map = {
        easy: '简单',
        medium: '中等',
        hard: '困难'
      }
      return map[this.difficulty] || this.difficulty
    },
    masteryText() {
      const map = {
        unlearned: '未掌握',
        partial: '部分掌握',
        mastered: '已掌握'
      }
      return map[this.mastery] || this.mastery
    }
  },
  methods: {
    handleClick() {
      this.$emit('click', this.id)
    }
  }
}
</script>

<style lang="scss" scoped>
.question-card {
  background: #FFFFFF;
  border-radius: 16rpx;
  padding: 24rpx;
  margin-bottom: 20rpx;
  box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  
  &:active {
    transform: scale(0.98);
  }
  
  .question-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16rpx;
    
    .subject-tag {
      padding: 6rpx 12rpx;
      border-radius: 8rpx;
      font-size: 24rpx;
      
      &.math {
        background: #E3F2FD;
        color: #2196F3;
      }
      
      &.english {
        background: #E8F5E9;
        color: #4CAF50;
      }
      
      &.physics {
        background: #FFF3E0;
        color: #FF9800;
      }
      
      &.chemistry {
        background: #F3E5F5;
        color: #9C27B0;
      }
    }
    
    .difficulty-tag {
      padding: 4rpx 8rpx;
      border-radius: 4rpx;
      font-size: 20rpx;
      
      &.easy {
        background: #E8F5E9;
        color: #4CAF50;
      }
      
      &.medium {
        background: #FFF3E0;
        color: #FF9800;
      }
      
      &.hard {
        background: #FFEBEE;
        color: #F44336;
      }
    }
  }
  
  .question-content {
    font-size: 28rpx;
    line-height: 1.8;
    color: #333;
    margin-bottom: 16rpx;
  }
  
  .question-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    
    .date {
      font-size: 24rpx;
      color: #999;
    }
    
    .mastery-tag {
      padding: 4rpx 12rpx;
      border-radius: 4rpx;
      font-size: 20rpx;
      
      &.unlearned {
        background: #FFEBEE;
        color: #F44336;
      }
      
      &.partial {
        background: #FFF3E0;
        color: #FF9800;
      }
      
      &.mastered {
        background: #E8F5E9;
        color: #4CAF50;
      }
    }
  }
}
</style>
