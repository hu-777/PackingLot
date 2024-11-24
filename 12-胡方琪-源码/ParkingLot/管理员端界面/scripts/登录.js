//点击改变图片
let myImage = document.querySelector("img");

myImage.onclick = function () {
  let mySrc = myImage.getAttribute("src");
  if (mySrc === "images/图片1.jpg") 
  {
    myImage.setAttribute("src", "images/图片2.jpg");
  }
   else 
  {
    myImage.setAttribute("src", "images/图片1.jpg");
  }
}

//注册界面跳转
function registerJump()
{
  window.location.replace('注册.html');
}
document.getElementById("registerBtn").addEventListener("click",registerJump)


//登录
function logIn() 
{
  var unm=document.getElementsById("username").value;
  var psw=document.getElementsById("password").value;
  var username=localStorage.getItem("username");
  var password=localStorage.getItem("password");
  if(username==null||password==null)
  {
    alert("您还未注册，请先注册！");
  }
  if(unm===username&&psw==password)
  {
    alert("登录成功！");
    window.open('主界面.html');
  }
  else
  {
    alert("用户名或密码错误！");
  }
}
document.getElementById("loginBtn").addEventListener("click",logIn)

//记住密码
function remeber()
{
  var box=document.getElementById("remeber");
  alert(box.checked);
  if(ture)
  {
    window.localStorage.setItem("username",username);
    window.localStorage.setItem("password",password);
  }
  else{
    window.localStorage.removeItem("username"); 
    window.localStorage.removeItem("password");
  }
}

//初始化登录界面
function initLoginPage()
{
  var unm=window.localStorage.getItem("username");
  var psw=window.localStorage.getItem("password");
  if(unm&&psw)
  {
    document.getElementById("username").value=username;
    document.getElementById("password").value=password;
  }
}

function log()
{
  window.alert("账号或密码错误，请重试！");

}document.getElementById("loginBtn").addEventListener("click",log)