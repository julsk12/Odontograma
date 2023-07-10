
let morfismo = document.getElementById('row');
function aaa() {
    const fechaini = document.getElementById("fechaini").value;
    const fechafin = document.getElementById("fechafin").value;
    console.log(fechaini, fechafin)
    axios.post('/estadisticas', {
        fecha_inicio: fechaini,
        fecha_fin: fechafin,
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
                    <span class="progressText">${datos[index].semana}</span>
                        <div class="progress">
                            <div class="progress-bar" role="progressbar" aria-valuenow="${datos[index].porcentaje}" aria-valuemin="10" aria-valuemax="100">
                                <span class="popOver1" data-toggle="tooltip1" data-placement="top" title="75%"> </span>
                                <span class="progressText">${datos[index].porcentaje}%</span>
                            </div>
                        </div>
                </div>
                        `;
            }
            morfismo.innerHTML = estaa
            $(".progress-bar").each(function() {
                each_bar_width = $(this).attr('aria-valuenow');
                $(this).width(each_bar_width + '%');
            });
        })
        .catch(function (error) {
            console.log(error);
        });


}


let send = document.getElementById('row');
function eee() {
    const fechaini = document.getElementById("fechaini").value;
    const fechafin = document.getElementById("fechafin").value;
    console.log(fechaini, fechafin)
    axios.post('/estadisticas', {
        fecha_inicio: fechaini,
        fecha_fin: fechafin,
        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data
            var length = (Object.keys(datos).length) + 1;
            let estaa = '';
            i = 0
            for (let index = 1; index < length; index++) {
                estaa += `
                
                <h2 class="fs-32 font-w700 mb-0">68</h2>
                </div>
            </div>
            <div id="column">
                <div class="card-body px-4 pb-0">
                    <div class="ay">
                        <div class="progress">
                            <div class="progress-bar" role="progressbar" aria-valuenow="65" aria-valuemin="0"
                                aria-valuemax="100">
                                <span class="popOver1" data-toggle="tooltip1" data-placement="top" title="65%">
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
                        `;
            }
            send.innerHTML = estaa
            $(".progress-bar").each(function() {
                each_bar_width = $(this).attr('aria-valuenow');
                $(this).width(each_bar_width + '%');
            });
        })
        .catch(function (error) {
            console.log(error);
        });


}

// document.getElementById("consul").addEventListener("click", eee);

