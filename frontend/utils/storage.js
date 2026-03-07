/**
 * 本地存储封装
 */

const STORAGE_KEY = {
  TOKEN: 'token',
  USER_INFO: 'user_info',
  SETTINGS: 'settings',
  CACHE: 'cache_'
}

// 设置存储
export function set(key, value) {
  try {
    uni.setStorageSync(key, value)
    return true
  } catch (e) {
    console.error('存储失败', e)
    return false
  }
}

// 获取存储
export function get(key, defaultValue = null) {
  try {
    const value = uni.getStorageSync(key)
    return value !== '' ? value : defaultValue
  } catch (e) {
    console.error('读取失败', e)
    return defaultValue
  }
}

// 删除存储
export function remove(key) {
  try {
    uni.removeStorageSync(key)
    return true
  } catch (e) {
    console.error('删除失败', e)
    return false
  }
}

// 清空存储
export function clear() {
  try {
    uni.clearStorageSync()
    return true
  } catch (e) {
    console.error('清空失败', e)
    return false
  }
}

// 带缓存时间的存储
export function setWithExpiry(key, value, ttl) {
  const now = new Date().getTime()
  const item = {
    value: value,
    expiry: now + ttl
  }
  return set(key, item)
}

// 获取带缓存时间的存储
export function getWithExpiry(key) {
  const item = get(key)
  if (!item) return null
  
  const now = new Date().getTime()
  if (now > item.expiry) {
    remove(key)
    return null
  }
  return item.value
}

// 用户相关
export const user = {
  setToken: (token) => set(STORAGE_KEY.TOKEN, token),
  getToken: () => get(STORAGE_KEY.TOKEN),
  clearToken: () => remove(STORAGE_KEY.TOKEN),
  
  setInfo: (info) => set(STORAGE_KEY.USER_INFO, info),
  getInfo: () => get(STORAGE_KEY.USER_INFO),
  clearInfo: () => remove(STORAGE_KEY.USER_INFO)
}

// 设置相关
export const settings = {
  set: (key, value) => {
    const current = get(STORAGE_KEY.SETTINGS, {})
    current[key] = value
    return set(STORAGE_KEY.SETTINGS, current)
  },
  get: (key) => {
    const current = get(STORAGE_KEY.SETTINGS, {})
    return current[key]
  }
}
