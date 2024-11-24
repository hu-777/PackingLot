// pages/loginIn/loginIn.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },
  // 登录提交表单
  LoginInBindSubmit: function (event) {
      //表单1
      var LoginInInputUsername=event.detail.value.shoujihao;
      //表单2
      var LoginInInputPassword=event.detail.value.password;
      //得到本地数据集合
      var LoginTranferValue= wx.getStorageSync('LoginTranferValue');
      // 判断登录
      for(var i=0;i<LoginTranferValue.length;i++){
          var LoginInName=LoginTranferValue[i].name;//昵称
          if(LoginInInputUsername==LoginTranferValue[i].id&&LoginInInputPassword==LoginTranferValue[i].password){
             
              // 返回账号前清空本地缓存数据
              wx.clearStorageSync();
               // 登录成功返回账号昵称
              wx.setStorageSync('LogInAndReturnToTheAccount', LoginTranferValue[i].name);
              wx.navigateBack({
                delta: 1,
              })
          }
      }
      wx.showToast({
        title: '登陆成功！',
        icon:'success',
        duration:2000
      }),
      wx.switchTab({
        url: '/pages/login/login',
      })
  },

  //登录
  loginBtn:function(){
    wx.showToast({
      title: '登陆成功！',
      icon:'success',
      duration:2000
    }),
    setTimeout(function () {
      wx.switchTab({
        url: '/pages/main/main',
      })
    }, 1000) 
  },

  onLoad: function (options) {
      console.log('登录界面加载');
      
      
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
      console.log('登录界面渲染');
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
      console.log('登录界面显示');
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
      console.log('登录界面隐藏');
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})
