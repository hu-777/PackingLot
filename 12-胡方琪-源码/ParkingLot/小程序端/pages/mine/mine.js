Page({

  /**
   * 页面的初始数据
   */
  data: {
    
  },
  // 菜单
  navClick(e) {
    wx.showToast({
      title: '您点击了【' + e.currentTarget.dataset.item.title + '】',
    })
  },
})
