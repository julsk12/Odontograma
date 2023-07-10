

let morfismo = document.getElementById('row1');
function grafica1() {

    axios.post('estadisticasdashboard', {

        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data
            var length = (Object.keys(datos).length) + 1;
            let estaa = '';
            i = 0
            for (let index = 1; index < length; index++) {
                estaa += `
                <div class="barWrapper">
                    <span class="progressText" id="js">${datos[index].semana}</span>
                        <div class="progress1">
                            <div class="progress-bar1" role="progressbar" aria-valuenow="${datos[index].porcentaje}" aria-valuemin="10" aria-valuemax="100">
                                <span class="popOver1" data-toggle="tooltip1" data-placement="top" title="75%"> </span>
                                <span class="progressText">${datos[index].porcentaje}%</span>
                            </div>
                        </div>
                </div>
                        `;
            }
            morfismo.innerHTML = estaa
            $(".progress-bar1").each(function () {
                each_bar_width = $(this).attr('aria-valuenow');
                $(this).width(each_bar_width + '%');
            });
        })
        .catch(function (error) {

        });


}
window.addEventListener('load', function () {
    grafica1();
});
let send = document.getElementById('grafiquita');
function grafiquita() {
    axios.get('total', {
        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data
            let data_list = Object.keys(datos)
            var length = (Object.keys(datos).length);
            let estaa = '';
            for (let index = 0; index < length; index++) {
                estaa += `
                 <h2 class="fs-32 font-w700">${datos.clientes}</h2>
                 <span class="fs-18 font-w500 d-block">Total clientes</span>
                 <span class="d-block fs-16 font-w400"><small class="text-danger">Desde el último mes</small></span>`;
            }
            send.innerHTML = estaa

        })
        .catch(function (error) {

        });


}
window.addEventListener('load', function () {
    grafiquita();
});

let sky = document.getElementById('gras');
function gras() {
    axios.get('odontotal', {
        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data
            let data_list = Object.keys(datos)
            var length = (Object.keys(datos).length);
            let blue = '';
            for (let index = 0; index < length; index++) {
                blue += `
                 <h2 class="fs-32 font-w700">${datos.odontologo}</h2>
                 <span class="fs-18 font-w500 d-block">Total odontologos</span>
                 <span class="d-block fs-16 font-w400"><small class="text-danger"></small> Desde el ultimo mes</span>`;
            }
            sky.innerHTML = blue

        })
        .catch(function (error) {

        });


}

window.addEventListener('load', function () {
    gras();
});


let give = document.getElementById('paratratamientos');
function gros() {
    axios.get('paratratamientos', {
        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data
            // let data_list = Object.keys(datos)
            var length = (Object.keys(datos).length);
            // console.log(length);
            // console.log(datos.porcentaje);
            // console.log(data_list);
            let me = '';
            console.log(datos.porcentaje);
            me += `     
                     <div class="circle-graph" data-percent="${datos.porcentaje}">
                     <p class="pan">Tratamientos en progreso</p>
                   </div>
                   <div> 
                     <p class="porcentaje">${datos.porcentaje}%</p>
                   </div>
                   <div class="texto" id="texto">
                     <p>Cuenta con un alto indice de tratamientos en progreso</p>
                     <p>cuenta con un porcentaje de ${datos.porcentaje}%</p>
                   </div>`;
            give.innerHTML = me
            $(function () {
                $('.circle-graph').easyPieChart({
                    scaleColor: false,
                    lineWidth: 20,
                    lineCap: 'butt',
                    barColor: '#a378aa',
                    trackColor: '#e7b8ef',
                    size: 150,
                    animate: 800
                });
            });
        })
        .catch(function (error) {
            console.log(error);
        });


}

window.addEventListener('load', function () {
    gros();
});

let morf = document.getElementById('row2');
function grafica2() {

    axios.post('estadisticasdashboard2', {

        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data
            var length = (Object.keys(datos).length) + 1;
            let estaa = '';
            i = 0
            for (let index = 1; index < length; index++) {
                estaa += `
                <div class="barWrapper">
                    <span class="progressText" id="js">${datos[index].semana}</span>
                        <div class="progress1">
                            <div class="progress-bar1" role="progressbar" aria-valuenow="${datos[index].porcentaje}" aria-valuemin="10" aria-valuemax="100">
                                <span class="popOver1" data-toggle="tooltip1" data-placement="top" title="75%"> </span>
                                <span class="progressText">${datos[index].porcentaje}%</span>
                            </div>
                        </div>
                </div>
                        `;
            }
            morf.innerHTML = estaa
            $(".progress-bar1").each(function () {
                each_bar_width = $(this).attr('aria-valuenow');
                $(this).width(each_bar_width + '%');
            });
        })
        .catch(function (error) {

        });


}
window.addEventListener('load', function () {
    grafica2();
});

let dont = document.getElementById('paratratamientos1');

function col() {
    const tooth = document.getElementById('tooth');
    axios
    .post(
        'estimacion', {
            estimacion: tooth.value
    }, {
        headers: {
            'Content-Type': 'application/json'
        },
    }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err);
    });

}
function gris() {
    axios.get('paratratamientos2', {
        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data
            let me = '';
            console.log(datos.porcentaje);
            me += `     
                   <div class="circle-graph" data-percent="${datos.porcentaje}">
                   <p class="pan">Tratamientos en progreso</p>
                 </div>
                 <div> 
                   <p class="porcentaje">${datos.porcentaje}%</p>
                 </div>
                 <div class="texto" id="texto">
                   <p>Cuenta con un alto indice de tratamientos en progreso</p>
                   <p>cuenta con un porcentaje de ${datos.porcentaje}%</p>
                 </div>`;
            dont.innerHTML = me
            $(function () {
                $('.circle-graph').easyPieChart({
                    scaleColor: false,
                    lineWidth: 20,
                    lineCap: 'butt',
                    barColor: '#a378aa',
                    trackColor: '#e7b8ef',
                    size: 150,
                    animate: 800
                });
            });
        })
        .catch(function (error) {
            console.log(error);
        });


}

window.addEventListener('load', function () {
    gris();
});

function cal() {
    const tooth = document.getElementById('tooth');
    axios
    .post(
        'estimacion1', {
            estimacion: tooth.value
    }, {
        headers: {
            'Content-Type': 'application/json'
        },
    }
    )
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.log(err);
    });

}