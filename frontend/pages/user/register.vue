<template>
  <view class="container">
    <view class="header">
      <text class="title">注册账号</text>
      <text class="subtitle">开启高效学习之旅</text>
    </view>

    <view class="form">
      <view class="form-item">
        <text class="label">用户名</text>
        <input 
          class="input" 
          v-model="username" 
          placeholder="4-20 位字母或数字"
          type="text"
        />
      </view>

      <view class="form-item">
        <text class="label">邮箱</text>
        <input 
          class="input" 
          v-model="email" 
          placeholder="选填，用于找回密码"
          type="text"
        />
      </view>

      <view class="form-item">
        <text class="label">密码</text>
        <input 
          class="input" 
          v-model="password" 
          placeholder="6-20 位密码"
          type="password"
        />
      </view>

      <view class="form-item">
        <text class="label">确认密码</text>
        <input 
          class="input" 
          v-model="confirmPassword" 
          placeholder="再次输入密码"
          type="password"
        />
      </view>

      <button class="register-btn" @click="handleRegister" :loading="loading">
        注册
      </button>

      <view class="actions">
        <text>已有账号？</text>
        <text class="link" @click="goToLogin">立即登录</text>
      </view>
    </view>

    <LoadingSpinner :loading="loading" text="注册中..." />
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
      email: '',
      password: '',
      confirmPassword: '',
      loading: false
    }
  },
  methods: {
    async handleRegister() {
      // 验证
      if (!this.username || !this.password) {
        uni.showToast({
          title: '请填写必填项',
          icon: 'none'
        })
        return
      }

      if (this.username.length < 4 || this.username.length > 20) {
        uni.showToast({
          title: '用户名 4-20 位',
          icon: 'none'
        })
        return
      }

      if (this.password.length < 6 || this.password.length > 20) {
        uni.showToast({
          title: '密码 6-20 位',
          icon: 'none'
        })
        return
      }

      if (this.password !== this.confirmPassword) {
        uni.showToast({
          title: '两次密码不一致',
          icon: 'none'
        })
        return
      }

      this.loading = true

      try {
        const res = await api.register({
          username: this.username,
          password: this.password,
          email: this.email
        })

        user.setToken(res.token)

        uni.showToast({
          title: '注册成功',
          icon: 'success'
        })

        setTimeout(() => {
          uni.switchTab({
            url: '/pages/index/index'
          })
        }, 1000)
      } catch (e) {
        uni.showToast({
          title: e.message || '注册失败',
          icon: 'none'
        })
      } finally {
        this.loading = false
      }
    },

    goToLogin() {
      uni.redirectTo({
        url: '/pages/user/login'
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  padding: 60rpx 40rpx;
  min-height: 100vh;
  background: #F5F7FA;
}

.header {
  margin-bottom: 60rpx;

  .title {
    display: block;
    font-size: 48rpx;
    font-weight: 600;
    color: #333;
    margin-bottom: 12rpx;
  }

  .subtitle {
    display: block;
    font-size: 28rpx;
    color: #999;
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

  .register-btn {
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
    justify-content: center;
    align-items: center;
    margin-top: 30rpx;
    font-size: 28rpx;
    color: #666;

    .link {
      color: #2196F3;
      margin-left: 10rpx;
    }
  }
}
</style>
