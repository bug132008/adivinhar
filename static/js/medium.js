const inputChute = document.querySelector("#chuteInput")
const botaoDeChutar = document.getElementById("btnChute")
const dicaSp = document.getElementById("dica")
const reset = document.getElementById("reset")
const numAnterior = document.getElementById("chuteA")
dicaSp.innerHTML = "Chute um número"
function gerar(){
  const random = (num) => Math.floor(Math.random() * num);
  return random(200)
}
function dica(v){
  const dica1 = "Fale um número maior!"
  const dica2 = "Fale um número menor!"
  const dica0 = "Acho que isso não é um número!"
  if(v == "menor"){
    dicaSp.innerHTML = dica2
  }
  else if(v == "maior"){
    dicaSp.innerHTML = dica1
  }
  else if(v == "não"){
    dicaSp.innerHTML = dica0
  }
}
function vencer(param){
  if(param == 1){
    dicaSp.innerHTML = "Você venceu!"
    reset.classList.remove("n")
    //dicaSp.classList.add("n")
    inputChute.classList.add("n")
    botaoDeChutar.classList.add("n")
  }
}
function resetar(){
  numeroGerado = gerar()
  reset.classList.add("n")
  dicaSp.innerHTML = "Chute um número"
  numAnterior.innerHTML = ""
  inputChute.value = ""
  inputChute.classList.remove("n")
  botaoDeChutar.classList.remove("n")
}
function chutar(){
  let chute = inputChute.value
  let numeroChutado = parseInt(chute)
  verificar(numeroChutado)
  inputChute.value = ""
}
function verificar(numero){
  let t = String(numero)
  if(t == "NaN"){
    dica("não")
  }
  else if(numero > numeroGerado){
    dica("menor")
    numAnterior.innerHTML = numero
  }
  else if(numero < numeroGerado){
    dica("maior")
    numAnterior.innerHTML = numero
  }
  else if(numero == numeroGerado){
    vencer(1)
    numAnterior.innerHTML = numero
  }
}
let numeroGerado = gerar()
