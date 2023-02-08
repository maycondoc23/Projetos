
// first request
var xhr1 = new XMLHttpRequest();
xhr1.open('GET', '/total_maquinas');
xhr1.onload = function() {
    if (xhr1.status === 200) {
        var data1 = JSON.parse(xhr1.responseText);
        document.getElementById('card-totalmachine').innerHTML = data1;
    }
    else {
        console.log('Request 1 failed.  Returned status of ' + xhr1.status);
    }
};
xhr1.send();

// second request
var xhr2 = new XMLHttpRequest();
xhr2.open('GET', '/total_tarefas');
xhr2.onload = function() {
    if (xhr2.status === 200) {
        var data2 = JSON.parse(xhr2.responseText);
        document.getElementById('card-totaltarefas').innerHTML = data2;
    }
    else {
        console.log('Request 2 failed.  Returned status of ' + xhr2.status);
    }
};
xhr2.send();


// second request
var xhr3 = new XMLHttpRequest();
xhr3.open('GET', '/total_concluidas');
xhr3.onload = function() {
    if (xhr3.status === 200) {
        var data3 = JSON.parse(xhr3.responseText);
        document.getElementById('card-totalconcluidas').innerHTML = data3;
    }
    else {
        console.log('Request 3 failed.  Returned status of ' + xhr3.status);
    }
};
xhr3.send();
// second request
var xhr4 = new XMLHttpRequest();
xhr4.open('GET', '/total_pendentes');
xhr4.onload = function() {
    if (xhr4.status === 200) {
        var data4 = JSON.parse(xhr4.responseText);
        document.getElementById('card-totalpendentes').innerHTML = data4;
    }
    else {
        console.log('Request 4 failed.  Returned status of ' + xhr4.status);
    }
};
xhr4.send();




  $('.nav-link').click(function(){
    $('.nav-link').removeClass('active');
    $(this).addClass('active');
  });


  
  document.getElementById("search-input").addEventListener("input", function() {
    var searchValue = this.value.toLowerCase();
    var table = document.getElementById("minha-tabela");
    var rows = table.getElementsByTagName("tr");

    // Oculta todas as linhas (menos o cabeçalho)
    for (var i = 1; i < rows.length; i++) {
        rows[i].style.display = "none";
    }

    // Mostra as linhas que possuem o valor da pesquisa
    for (var i = 1; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        for (var j = 0; j < cells.length; j++) {
            var cellValue = cells[j].textContent.toLowerCase();
            if (cellValue.indexOf(searchValue) !== -1) {
                rows[i].style.display = "";
                break;
            }
        }
    }
});
