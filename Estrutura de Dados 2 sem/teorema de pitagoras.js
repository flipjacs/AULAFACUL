function soma(x = 1, y = 2, z = 3){
    return x+y+z
}
console.log(soma(4, 2)) //z não foi usado como parametro então terá valor default (resultado é == 9)

function areaRetangulo(a,b){
    let area = a*b
    return area
}

function hipotenusa(catA, catB){
    let hipo = Math.sqrt(Math.pow(catA, 2) + Math.pow(catB, 2))
    return hipo
}

    let opcao = Number(prompt("Digite sua escolha de cálculo"))
    if (opcao === 1){
        let a = Number(prompt("Digite o lado A"));
        let b = Number(prompt("Digite o lado B"));
        let resultado = areaRetangulo(a, b)
        console.log(resultado.toFixed(2))
    } else if (opcao === 2){    
        let catA = Number(prompt("Digite o valor do Cateto A"));
        let catB = Number(prompt("Digite o valor do Cateto B"));   
        let resultado = hipotenusa(catA, catB);
        console.log(resultado.toFixed(2));
    }
