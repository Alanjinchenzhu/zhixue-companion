<script>
export default {
  onLaunch: function() {
    console.log('App Launch - 智学伴侣启动')
    // 初始化全局数据
    this.globalData = {
      apiUrl: 'http://localhost:8000/api',
      userInfo: null,
      token: ''
    }
  },
  onShow: function() {
    console.log('App Show')
  },
  onHide: function() {
    console.log('App Hide')
  }
}
</script>

<style lang="scss">
/* 全局样式 */
page {
  background-color: #F5F7FA;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  font-size: 14px;
  line-height: 1.5;
  color: #333;
}

/* 主题色 */
$primary-color: #2196F3;
$success-color: #4CAF50;
$warning-color: #FF9800;
$error-color: #F44336;

/* 通用类 */
.container {
  padding: 20rpx;
}

.card {
  background: #FFFFFF;
  border-radius: 16rpx;
  padding: 24rpx;
  margin-bottom: 20rpx;
  box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.1);
}

.btn-primary {
  background: $primary-color;
  color: #FFFFFF;
  border: none;
  border-radius: 12rpx;
  padding: 20rpx 40rpx;
  font-size: 28rpx;
  font-weight: 500;
}

.btn-secondary {
  background: #F5F7FA;
  color: $primary-color;
  border: 2rpx solid $primary-color;
  border-radius: 12rpx;
  padding: 20rpx 40rpx;
  font-size: 28rpx;
  font-weight: 500;
}

.text-center {
  text-align: center;
}

.text-primary {
  color: $primary-color;
}

.mt-20 {
  margin-top: 20rpx;
}

.mb-20 {
  margin-bottom: 20rpx;
}
</style>
