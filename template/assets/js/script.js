
let respostas = [];

function aviso(){
    alert(respostas);
}

function addR1() {
    respostas.push("Resposta#1");
    console.log(respostas);
    aviso();
    // renderResp();
}

function addR2() {
    respostas.push("Resposta#2");
    console.log(respostas);
    aviso();
    // renderResp();
}

function addR3() {
    respostas.push("Resposta#3");
    console.log(respostas);
    aviso();
    // renderResp();
}

function addR4() {
    respostas.push("Resposta#3");
    console.log(respostas);
    aviso();
    // renderResp();
}

function renderResp() {
    let respList = document.getElementById("respList");
    respList.innerHTML = "";
   respostas.forEach(respostas => {
        let li = document.createElement("li");
        li.textContent = respostas;
        respList.appendChild(li);
        console.log("deu certo")
    });
}