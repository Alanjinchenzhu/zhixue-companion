<template>
  <view class="loading-overlay" v-if="loading">
    <view class="spinner">
      <view class="circle"></view>
      <view class="circle"></view>
      <view class="circle"></view>
    </view>
    <text class="loading-text">{{ text }}</text>
  </view>
</template>

<script>
export default {
  name: 'LoadingSpinner',
  props: {
    loading: {
      type: Boolean,
      default: false
    },
    text: {
      type: String,
      default: '加载中...'
    }
  }
}
</script>

<style lang="scss" scoped>
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.spinner {
  display: flex;
  gap: 20rpx;
  margin-bottom: 30rpx;
}

.circle {
  width: 30rpx;
  height: 30rpx;
  background: #2196F3;
  border-radius: 50%;
  animation: bounce 1.4s infinite ease-in-out both;
  
  &:nth-child(1) {
    animation-delay: -0.32s;
  }
  
  &:nth-child(2) {
    animation-delay: -0.16s;
  }
}

@keyframes bounce {
  0%, 80%, 100% {
    transform: scale(0);
  }
  40% {
    transform: scale(1);
  }
}

.loading-text {
  color: #FFFFFF;
  font-size: 28rpx;
}
</style>
