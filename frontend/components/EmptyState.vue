<template>
  <view class="empty-state">
    <view class="icon">{{ icon }}</view>
    <text class="title">{{ title }}</text>
    <text class="subtitle" v-if="subtitle">{{ subtitle }}</text>
    <button class="action-btn" v-if="actionText" @click="handleAction">{{ actionText }}</button>
  </view>
</template>

<script>
export default {
  name: 'EmptyState',
  props: {
    icon: {
      type: String,
      default: '📭'
    },
    title: {
      type: String,
      default: '暂无数据'
    },
    subtitle: {
      type: String,
      default: ''
    },
    actionText: {
      type: String,
      default: ''
    }
  },
  methods: {
    handleAction() {
      this.$emit('action')
    }
  }
}
</script>

<style lang="scss" scoped>
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 100rpx 40rpx;
  text-align: center;
  
  .icon {
    font-size: 120rpx;
    margin-bottom: 30rpx;
  }
  
  .title {
    font-size: 32rpx;
    font-weight: 600;
    color: #666;
    margin-bottom: 16rpx;
  }
  
  .subtitle {
    font-size: 28rpx;
    color: #999;
    margin-bottom: 40rpx;
  }
  
  .action-btn {
    background: #2196F3;
    color: #FFFFFF;
    border: none;
    border-radius: 12rpx;
    padding: 20rpx 60rpx;
    font-size: 28rpx;
  }
}
</style>
