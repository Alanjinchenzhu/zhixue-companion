<template>
  <view class="container">
    <!-- 用户信息 -->
    <view class="profile card">
      <view class="avatar">👤</view>
      <view class="info">
        <text class="nickname">学霸小明</text>
        <text class="level">LV.5 学习达人</text>
      </view>
    </view>

    <!-- 功能列表 -->
    <view class="menu-list">
      <view class="menu-item" @click="goToPage('settings')">
        <text class="menu-icon">⚙️</text>
        <text class="menu-text">设置</text>
        <text class="menu-arrow">></text>
      </view>
      <view class="menu-item" @click="goToPage('vip')">
        <text class="menu-icon">👑</text>
        <text class="menu-text">VIP 会员</text>
        <text class="menu-tag">热门</text>
        <text class="menu-arrow">></text>
      </view>
      <view class="menu-item" @click="goToPage('feedback')">
        <text class="menu-icon">💬</text>
        <text class="menu-text">意见反馈</text>
        <text class="menu-arrow">></text>
      </view>
      <view class="menu-item" @click="goToPage('about')">
        <text class="menu-icon">ℹ️</text>
        <text class="menu-text">关于我们</text>
        <text class="menu-arrow">></text>
      </view>
    </view>

    <!-- 退出登录 -->
    <view class="logout-btn" @click="logout">
      <text>退出登录</text>
    </view>
  </view>
</template>

<script>
export default {
  methods: {
    goToPage(page) {
      uni.showToast({
        title: '功能开发中',
        icon: 'none'
      })
    },
    logout() {
      uni.showModal({
        title: '提示',
        content: '确定要退出登录吗？',
        success: (res) => {
          if (res.confirm) {
            uni.showToast({
              title: '已退出',
              icon: 'success'
            })
          }
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  padding: 20rpx;
}

.profile {
  display: flex;
  align-items: center;
  padding: 40rpx 20rpx;
  
  .avatar {
    width: 120rpx;
    height: 120rpx;
    background: #E3F2FD;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 60rpx;
    margin-right: 30rpx;
  }
  
  .info {
    flex: 1;
    display: flex;
    flex-direction: column;
    
    .nickname {
      font-size: 36rpx;
      font-weight: 600;
      color: #333;
      margin-bottom: 10rpx;
    }
    
    .level {
      font-size: 24rpx;
      color: #999;
    }
  }
}

.menu-list {
  margin-top: 40rpx;
  background: #FFFFFF;
  border-radius: 16rpx;
  
  .menu-item {
    display: flex;
    align-items: center;
    padding: 30rpx 20rpx;
    border-bottom: 1rpx solid #F0F0F0;
    
    &:last-child {
      border-bottom: none;
    }
    
    .menu-icon {
      font-size: 40rpx;
      margin-right: 20rpx;
    }
    
    .menu-text {
      flex: 1;
      font-size: 28rpx;
      color: #333;
    }
    
    .menu-tag {
      background: #FF9800;
      color: #FFFFFF;
      font-size: 20rpx;
      padding: 4rpx 12rpx;
      border-radius: 8rpx;
      margin-right: 20rpx;
    }
    
    .menu-arrow {
      font-size: 28rpx;
      color: #999;
    }
  }
}

.logout-btn {
  margin-top: 60rpx;
  background: #FFFFFF;
  border-radius: 16rpx;
  padding: 30rpx 0;
  text-align: center;
  
  text {
    font-size: 28rpx;
    color: #F44336;
  }
}
</style>
