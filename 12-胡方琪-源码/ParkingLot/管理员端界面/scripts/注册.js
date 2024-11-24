//注册
function doRegister()
{
    var username=document.getElementById("username").value;
    var password1=document.getElementById("password1").value;
    var password2=document.getElementById("password2").value;
    if(username==="")
    {
        alert("用户名不能为空!")
    }
    else if(password1===""||password2==="")
    {
        alert("密码不能为空！")
    }
    else if(password1 !==password2)
    {
        alert("两次输入密码不一致，请重试！")
    }
    else 
    {   
        window.localStorage.setItem("username",username);
        window.localStorage.setItem("password",password1);
        alert("注册成功，返回登录！");
    }
}
document.getElementById("submitBtn").addEventListener("click",doRegister)


//返回登录页面
function backLogin()
{
    window.location.replace('登录.html');
}
document.getElementById("backBtn").addEventListener("click",backLogin)
