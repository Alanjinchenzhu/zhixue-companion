<template>
  <view class="container">
    <view class="upload-area" @click="chooseImage">
      <view class="camera-icon">📷</view>
      <text class="upload-text">点击拍照或上传图片</text>
      <text class="upload-hint">支持数学公式识别</text>
    </view>
    
    <view class="tips card">
      <view class="tips-title">💡 小贴士</view>
      <view class="tips-list">
        <text class="tip-item">• 确保题目清晰完整</text>
        <text class="tip-item">• 支持数学公式识别</text>
        <text class="tip-item">• 一次最多上传 3 题</text>
      </view>
    </view>
    
    <view class="recent-uploads card" v-if="recentUploads.length > 0">
      <view class="section-title">最近上传</view>
      <view class="upload-item" v-for="(item, index) in recentUploads" :key="index">
        <image :src="item.image" mode="aspectFill" class="upload-image"></image>
        <text class="upload-status">{{ item.status }}</text>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      recentUploads: []
    }
  },
  methods: {
    chooseImage() {
      uni.chooseImage({
        count: 3,
        sizeType: ['compressed'],
        sourceType: ['album', 'camera'],
        success: (res) => {
          const tempFilePaths = res.tempFilePaths
          console.log('选择的图片:', tempFilePaths)
          this.uploadImage(tempFilePaths[0])
        }
      })
    },
    async uploadImage(filePath) {
      uni.showLoading({ title: '识别中...' })
      
      try {
        // 调用后端 API 上传
        const res = await uni.request({
          url: 'http://localhost:8000/api/upload',
          method: 'POST',
          header: {
            'content-type': 'multipart/form-data'
          }
        })
        
        uni.hideLoading()
        
        if (res.statusCode === 200) {
          uni.showToast({
            title: '上传成功',
            icon: 'success'
          })
          
          this.recentUploads.unshift({
            image: filePath,
            status: '识别成功',
            time: new Date().toLocaleTimeString()
          })
        } else {
          uni.showToast({
            title: '上传失败',
            icon: 'none'
          })
        }
      } catch (e) {
        uni.hideLoading()
        uni.showToast({
          title: '网络错误',
          icon: 'none'
        })
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  padding: 40rpx;
}

.upload-area {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #FFFFFF;
  border: 4rpx dashed #2196F3;
  border-radius: 24rpx;
  padding: 80rpx 40rpx;
  margin-bottom: 40rpx;
  
  .camera-icon {
    font-size: 100rpx;
    margin-bottom: 20rpx;
  }
  
  .upload-text {
    font-size: 32rpx;
    color: #333;
    margin-bottom: 10rpx;
  }
  
  .upload-hint {
    font-size: 24rpx;
    color: #999;
  }
}

.tips {
  .tips-title {
    font-size: 28rpx;
    font-weight: 600;
    color: #333;
    margin-bottom: 20rpx;
  }
  
  .tips-list {
    display: flex;
    flex-direction: column;
    
    .tip-item {
      font-size: 24rpx;
      color: #666;
      line-height: 2;
    }
  }
}

.recent-uploads {
  margin-top: 40rpx;
  
  .section-title {
    font-size: 28rpx;
    font-weight: 600;
    color: #333;
    margin-bottom: 20rpx;
  }
  
  .upload-item {
    display: flex;
    align-items: center;
    padding: 20rpx 0;
    border-bottom: 1rpx solid #F0F0F0;
    
    .upload-image {
      width: 100rpx;
      height: 100rpx;
      border-radius: 12rpx;
      margin-right: 20rpx;
    }
    
    .upload-status {
      font-size: 24rpx;
      color: #4CAF50;
    }
  }
}
</style>
