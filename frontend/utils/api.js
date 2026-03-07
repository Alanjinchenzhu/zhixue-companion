/**
 * API 请求封装
 */

const BASE_URL = 'http://localhost:8000/api'

// 获取 Token
function getToken() {
  return uni.getStorageSync('token') || ''
}

// 设置 Token
function setToken(token) {
  uni.setStorageSync('token', token)
}

// 清除 Token
function clearToken() {
  uni.removeStorageSync('token')
}

// 请求封装
function request(options) {
  return new Promise((resolve, reject) => {
    const token = getToken()
    
    uni.request({
      url: BASE_URL + options.url,
      method: options.method || 'GET',
      data: options.data || {},
      header: {
        'Content-Type': 'application/json',
        'Authorization': token ? `Bearer ${token}` : ''
      },
      timeout: 30000,
      success: (res) => {
        if (res.statusCode === 200) {
          resolve(res.data)
        } else if (res.statusCode === 401) {
          // Token 过期，清除并跳转登录
          clearToken()
          uni.navigateTo({ url: '/pages/user/login' })
          reject(new Error('未授权'))
        } else {
          reject(new Error(res.data.detail || '请求失败'))
        }
      },
      fail: (err) => {
        reject(err)
      }
    })
  })
}

// API 方法
export const api = {
  // 认证
  login: (data) => request({ url: '/auth/login', method: 'POST', data }),
  register: (data) => request({ url: '/auth/register', method: 'POST', data }),
  getMe: () => request({ url: '/auth/me', method: 'GET' }),
  
  // 题目
  getQuestions: (params) => request({ url: '/questions', method: 'GET', data: params }),
  getQuestion: (id) => request({ url: `/questions/${id}`, method: 'GET' }),
  createQuestion: (data) => request({ url: '/questions', method: 'POST', data }),
  updateMastery: (id, mastery) => request({ url: `/questions/${id}/mastery`, method: 'PUT', data: { mastery } }),
  analyzeQuestion: (id) => request({ url: `/questions/${id}/analyze`, method: 'POST' }),
  
  // 统计
  getStats: () => request({ url: '/stats', method: 'GET' }),
  
  // 上传
  uploadFile: (filePath) => {
    const token = getToken()
    return new Promise((resolve, reject) => {
      uni.uploadFile({
        url: BASE_URL + '/upload',
        filePath: filePath,
        name: 'file',
        header: {
          'Authorization': token ? `Bearer ${token}` : ''
        },
        success: (res) => {
          const data = JSON.parse(res.data)
          if (res.statusCode === 200) {
            resolve(data)
          } else {
            reject(new Error(data.detail || '上传失败'))
          }
        },
        fail: (err) => reject(err)
      })
    })
  }
}

// 导出工具方法
export { getToken, setToken, clearToken, request }
