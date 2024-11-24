// pages/mian/mian.js
Page({
    /**
     * 页面的初始数据
     */
    data: {
      imgList: ['../images/轮播图.jpg', '../images/lunbo2.jpg', '../images/lunbo3.jpg'],
    },
    // 菜单
    navClick(e) {
      wx.showToast({
        title: '您点击了【' + e.currentTarget.dataset.item.title + '】',
      })
    },
    // 详情
    detailClick(e) {
      wx.showToast({
        title: e.currentTarget.dataset.item.title,
      })
    },
  })
  