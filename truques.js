const nomeLivro = 'Aprendendo JS'
console.log (`Você está lendo ${nomeLivro}`) 

var circleAreaES5 = function circleArea(r){
    var PI = 3.14;
    var area = PI * r * r
    return area;
}
console.log(circleAreaES5(2));



const circleArea = r =>{ //a seta "=>" omite o comando function
    const PI = 3.14;
    const area = PI * r * r;
    return area;}
console.log (circleArea(2))

const circleArea2 = r => 3.14 * r *r; //caso a função tenha uma única instrução, pode simplificar mais
console.log(circleArea2(2));