


//mascara dos campos
    
    $('#cep').mask('00000-000');
    $('#phone').mask('(00) 00000-0000');
    $('#cpf').mask('000.000.000-00', { reverse: true });
    $('#money').mask("#.##0,00", { reverse: true });


// detectando se 'e iphone e modificando o tipo de campo data
    var isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
    if (isIOS) {
      // se o usuário estiver usando um dispositivo iOS, exiba um campo de entrada de texto para a data
      document.write('<input type="text" id="datanasc" name="datanasc" required placeholder="DD/MM/AAAA" data-toggle="tooltip" title="Insira sua data de nascimento" oninvalid="this.setCustomValidity(\'O campo data de nascimento não está preenchido, por favor preencha.\')" oninput="setCustomValidity(\'\')" onchange="calcularIdade()">');
    } else {
      // se o usuário não estiver usando um dispositivo iOS, exiba o elemento de entrada de data HTML5
      document.write('<input type="date" id="datanasc" name="datanasc" min="1900-01-01" max="2018-12-31" required placeholder="Digite sua data de nascimento" data-toggle="tooltip" title="Insira sua data de nascimento" oninvalid="this.setCustomValidity(\'O campo data de nascimento não está preenchido, por favor preencha.\')" oninput="setCustomValidity(\'\')" onchange="calcularIdade()">');
    }



    // Obtenha o elemento de entrada de data
    var campoData = document.getElementById("data");

    // Crie um novo objeto de data com a data atual
    var dataAtual = new Date();

    // Formate a data no formato necessário para o campo de data
    var formatoData = dataAtual.getFullYear() + "-" + (dataAtual.getMonth() + 1).toString().padStart(2, "0") + "-" + dataAtual.getDate().toString().padStart(2, "0");

    // Defina o valor do campo de data como a data atual formatada
    campoData.value = formatoData;

    // Definir o valor do atributo disabled como verdadeiro
    campoData.disabled = true;

    // Obtenha o elemento de entrada de idade
    var campoIdade = document.getElementById("idade");


    // Definir o valor do atributo disabled como verdadeiro
    campoIdade.disabled = true;




function calcularIdade() {

    var dataNasc = new Date(document.getElementById("datanasc").value);
    var hoje = new Date();
    var idade = hoje.getFullYear() - dataNasc.getFullYear();
    var mes = hoje.getMonth() - dataNasc.getMonth();
    if (mes < 0 || (mes === 0 && hoje.getDate() < dataNasc.getDate())) {
        idade--;
    }
    document.getElementById("idade").value = idade;

    }



    $(document).ready(function(){
      $('[data-toggle="tooltip"]').tooltip();
    });
