//打开摄像头  
function runScript() {  
    fetch('/run_python_script', {  
        method: 'POST',  
        headers: {  
            'Content-Type': 'application/json'  
        },  
    })  
    .then(response => response.json())  
    .then(data => {  
        if (data.success) {  
            document.getElementById('output').textContent = data.output;  
        } else {  
            alert('Error: ' + data.error);  
        }  
    })  
    .catch(error => {  
        console.error('Error:', error);  
    });  
} 
document.getElementById('openCamera').addEventListener('click', runScript); 

//显示当前时间
function  getD1(){
    var date=new Date();
    var d1=date.toLocaleString();
    document.getElementById("currentTime").innerHTML =d1; 
}
setInterval("getD1();",1000);
