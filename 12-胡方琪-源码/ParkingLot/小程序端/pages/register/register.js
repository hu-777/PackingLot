// pages/register/register.js
Page({
  /**
   * 页面的初始数据
   */
  data: {
       shoujihao: '',
       chepaihao: '',
       password: '',
       onfirmPassword: '',
       ErrorMessage1: '',
       ErrorMessage2: '',
       ErrorMessage3: '',
       ErrorMessage4: '',
       saveName:[],
       saveId:[],

  },
  // 提交表单
  onRegisterFormClick: function (event) {
       // 获取表单
       var shoujihao=event.detail.value.shoujihao+"";
       var chepaihao=event.detail.value.chepaihao+"";
       var password=event.detail.value.password+"";
       var confirmPassword=event.detail.value.confirmPassword+"";
       //确认密码
       if(password!=confirmPassword){
         wx.showToast({
           title: '两次输入密码不一致，请重试！',
         })
       }
       else{
      // 拿来返回数据
       var registerReturnDatas=[shoujihao,chepaihao,password];
       // 获取本地账号和昵称
       var saveName=this.data.saveName;
       var saveId=this.data.saveId;
       // 数组赋值另一个数组
       var saveName2=new Array;
       var saveId2=new Array;
       for(var i=0;i<saveName.length;i++){
            saveName2.push(saveName[i]);
            saveId2.push(saveId[i]);
       }
       console.log(saveName2);
       console.log(saveId2);
       // 循环
       var i=0;
       do{
            if((inputName!=''&inputId!=''&inputPassword!=''&inputRepassword!='')&&(inputPassword==inputRepassword)&&(inputName!=saveName2[i]&inputId!=saveId2[i])){
                 console.log(inputId[i]);
                 console.log('scueess');
                 // 返回数据
                 wx.setStorageSync('registerReturnDatas', registerReturnDatas);
                 wx.navigateBack({
                      delta: 1,
                 })
            }
            i++;
       }while(i<saveName2.length-1);
       }
       wx.showToast({
         title: '注册成功，返回登录！',
         icon:'success',
         duration:2000
       },
       wx.navigateTo({
         url: '/pages/login/login.wxml',
       })
       )
      
  },
  //点击注册
  registerBtn:function(){
    wx.showToast({
      title: '注册成功，返回登录！',
      icon:'success',
      duration:2000
    },
    setTimeout(function () {
      wx.navigateTo({
        url: '/pages/index/index',
      })
    }, 1000) 
    )
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
       // 初始化数据-获取已有账号
       var that=this;
       var getSomeAccounts= wx.getStorageSync('RegisteredTransfer');
       // 定义数组
       var saveName=[];
       var saveId=[];
       // 把数据整合成数组
       for(var i=0;i<getSomeAccounts.length;i++){
            saveName.push(getSomeAccounts[i].name);
            saveId.push(getSomeAccounts[i].id);
       }
       // 数据保存到data
       this.setData({
            saveName:saveName,
            saveId:saveId
       })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

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
