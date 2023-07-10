function viewconsultar() {
    let send = document.getElementById('queso');
    axios.get('/api/consultar', {
        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data
            var length = (Object.keys(datos).length) + 1;
            let estaa = '';
            for (let index = 1; index < length; index++) {
                estaa += `<div class="card1">
                <h3 class="title">${datos[index].nombre_odontologo}</h3>
                <h3 class="caption">${datos[index].fecha}, ${datos[index].hora}</h3>
                <h3 class="sub">${datos[index].sede}</h3>
                <div class="bar">
                    <div class="emptybar"></div>
                    <div class="filledbar"></div>
                </div>
                <div class="circle">
                
                </div>
                </div> `;
            }
            send.innerHTML = estaa
            
        })
        .catch(function (error) {
            console.log(error);
        });


}
window.addEventListener('load', function () {
    viewconsultar();
});

// function viewprueba() {
//     let send = document.getElementById('sal');
//     axios.get('/api/consultarodon', {
//         responseType: 'json'
//     })
//         .then(function (response) {
//             let datos = response.data
//             var length = (Object.keys(datos).length) + 1;
//             let estaa = '';
//             for (let index = 1; index < length; index++) {
//                 estaa += `<div class="card1">
//                 <h3 class="title">${datos[index].nombre_paciente}</h3>
//                 <h3 class="caption">${datos[index].fecha}, ${datos[index].hora}</h3>
//                 <h3 class="sub">${datos[index].sede}</h3>
//                 <div class="bar">
//                     <div class="emptybar"></div>
//                     <div class="filledbar"></div>
//                 </div>
//                 <div class="circle">
                
//                 </div>
//                 </div> `;
//             }
//             send.innerHTML = estaa
            
//         })
//         .catch(function (error) {
//             console.log(error);
//         });


// }
// window.addEventListener('load', function () {
//     viewprueba();
// });