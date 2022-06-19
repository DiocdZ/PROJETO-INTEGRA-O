window.addEventListener('load', function () {



    const botao1 = document.querySelector("#botao1");
    const botao2 = document.querySelector("#botao2");
    /*const botao3 = document.querySelector("#botao3");*/
    console.log(botao1)

    const div1 = document.querySelector("#div1");
    const div2 = document.querySelector("#div2");
    /*const div3 = document.querySelector("#div3");*/

    // Exibe nome e preço

    let incrementaBotao = 1
    console.log(incrementaBotao)

    botao1.addEventListener("click", function () {
        botao1.style.opacity = "1"
        

        fetch(`http://127.0.0.1:5000/videos/${incrementaBotao}`)
            .then(function (resposta) {
                return resposta.json()
            })
            .then(function (dados) {
                mosta_imagens(dados)
                incrementaBotao += 1
                // document.querySelector("#p1").innerHTML = `<p>${dados[1]}</p>: <link> ${dados[2]}</link> :<img src="${dados[3]}">`
            })
    });






    function mosta_imagens(dados) {

        //dados.forEach(element => { 
        //    document.querySelector("#p1").appendChild(`<p>${element[1]}</p>: 
        //   <link> ${element[2]}</link> :<img src="${element[3]}">`)
        // console.log(element)
        //});

        dados.forEach(elemento => {
            let img = document.createElement("img")
            img.src = `${elemento[3]}`

            const imgemComLink = document.createElement("a")
            imgemComLink.href = elemento[2]
            imgemComLink.appendChild(img)
            
            let titulo = document.createElement("h3")
            let text = document.createTextNode(`${elemento[1]}`)
            titulo.appendChild(text)

            document.getElementById("p1").appendChild(titulo);
            document.getElementById("p1").appendChild(imgemComLink);

        })

      //  botao2.addEventListener("click", function () {
          //  botao2.style.opacity = "1"
          //  fetch('http://127.0.0.1:5000/mostra/2')
          //      .then(function (resposta) {
          //          return resposta.json()
           //     })
           //     .then(function (dados) {
         //           document.querySelector("#p2").innerHTML = `${dados[1]}: R$ ${dados[2]}`
         //       })
       // });//
    }
    //botao3.addEventListener("click", function(){*/
    /*    botao3.style.opacity = "1"
        fetch('http://127.0.0.1:5000/lista/3')
        .then(function(resposta) {
            return resposta.json()
        })
        .then(function(dados) {
            document.querySelector("#p3").innerHTML = `${dados[1]}: R$ ${dados[2]}`
          })
    });*/

    // Oculta nome e preço
    div1.addEventListener("click", function () {
        document.querySelector("#p1").innerHTML = ''
    });

    /*div2.addEventListener("click", function(){ 
        document.querySelector("#p2").innerHTML = ''
    });

    div3.addEventListener("click", function(){
        document.querySelector("#p3").innerHTML = ''
    });*/
})