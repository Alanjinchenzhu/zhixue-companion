<template>
  <view class="container">
    <view class="logo">
      <text class="logo-icon">📚</text>
      <text class="logo-text">智学伴侣</text>
    </view>

    <view class="form">
      <view class="form-item">
        <text class="label">用户名</text>
        <input 
          class="input" 
          v-model="username" 
          placeholder="请输入用户名"
          type="text"
        />
      </view>

      <view class="form-item">
        <text class="label">密码</text>
        <input 
          class="input" 
          v-model="password" 
          placeholder="请输入密码"
          type="password"
        />
      </view>

      <button class="login-btn" @click="handleLogin" :loading="loading">
        登录
      </button>

      <view class="actions">
        <text class="link" @click="goToRegister">注册账号</text>
        <text class="link" @click="forgotPassword">忘记密码？</text>
      </view>
    </view>

    <LoadingSpinner :loading="loading" text="登录中..." />
  </view>
</template>

<script>
import { api } from '@/utils/api.js'
import { user } from '@/utils/storage.js'
import LoadingSpinner from '@/components/LoadingSpinner.vue'

export default {
  components: {
    LoadingSpinner
  },
  data() {
    return {
      username: '',
      password: '',
      loading: false
    }
  },
  methods: {
    async handleLogin() {
      if (!this.username || !this.password) {
        uni.showToast({
          title: '请填写用户名和密码',
          icon: 'none'
        })
        return
      }

      this.loading = true

      try {
        const res = await api.login({
          username: this.username,
          password: this.password
        })

        user.setToken(res.access_token)

        uni.showToast({
          title: '登录成功',
          icon: 'success'
        })

        setTimeout(() => {
          uni.switchTab({
            url: '/pages/index/index'
          })
        }, 1000)
      } catch (e) {
        uni.showToast({
          title: e.message || '登录失败',
          icon: 'none'
        })
      } finally {
        this.loading = false
      }
    },

    goToRegister() {
      uni.navigateTo({
        url: '/pages/user/register'
      })
    },

    forgotPassword() {
      uni.showToast({
        title: '请联系客服重置密码',
        icon: 'none'
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  padding: 60rpx 40rpx;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.logo {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 80rpx;

  .logo-icon {
    font-size: 120rpx;
    margin-bottom: 20rpx;
  }

  .logo-text {
    font-size: 48rpx;
    color: #FFFFFF;
    font-weight: 600;
  }
}

.form {
  background: #FFFFFF;
  border-radius: 24rpx;
  padding: 40rpx;

  .form-item {
    margin-bottom: 30rpx;

    .label {
      display: block;
      font-size: 28rpx;
      color: #333;
      margin-bottom: 12rpx;
      font-weight: 500;
    }

    .input {
      width: 100%;
      height: 88rpx;
      background: #F5F7FA;
      border-radius: 12rpx;
      padding: 0 24rpx;
      font-size: 28rpx;
      border: 2rpx solid transparent;
      transition: all 0.3s;

      &:focus {
        background: #FFFFFF;
        border-color: #2196F3;
      }
    }
  }

  .login-btn {
    width: 100%;
    height: 88rpx;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #FFFFFF;
    border: none;
    border-radius: 12rpx;
    font-size: 32rpx;
    font-weight: 600;
    margin-top: 40rpx;
  }

  .actions {
    display: flex;
    justify-content: space-between;
    margin-top: 30rpx;

    .link {
      font-size: 26rpx;
      color: #2196F3;
    }
  }
}
</style>
