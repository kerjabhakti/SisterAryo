function PostSignUp(namadepan,namabelakang,email,password){
    var myHeaders = new Headers();
    myHeaders.append("Login", "rollygantengsekali");
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "namadepan": namadepan,
        "namabelakang": namabelakang,
        "email": email,
        "password": password
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("https://eoyllzy05im4t1r.m.pipedream.net", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
}
function PushButton(){
       namadepan=document.getElementById("namadepan").value;
       namabelakang=document.getElementById("namabelakang").value;
       email=document.getElementById("email").value;
       password=document.getElementById("password").value;
       PostSignUp(namadepan,namabelakang,email,password);
 }
