

function viewinfo() {
    let morfismo = document.getElementById('info');
    let i = 0;

    axios.get('/api/misdatos', {
        responseType: 'json'
    })

        .then(function (response) {
            let datos = response.data
            var length = (Object.keys(datos).length) + 1;
            let listper = '';
            i = 0
            for (let index = 1; index < length; index++) {
                listper += `<a class="titulo">Datos basicos</a><br>
                            <a class="subs">Nombre:</a>
                                <a class="datos">${datos[index].nombre}</a><br>
                            <a class="subs">Documento:</a>
                                <a class="datos">${datos[index].id}</a><br>
                            <a class="subs">Fecha de nacimiento:</a>
                                <a class="datos">${datos[index].fecha_nacimiento}</a><br></br>
                            <a class="titulo">Datos De contacto</a><br>
                            <a class="subs">Correo:</a>
                                <a class="datos">${datos[index].correo}</a><br>
                            <a class="subs">Dirección:</a>
                                <a class="datos">${datos[index].direccion}</a><br>
                            <a class="subs">Teléfono:</a>
                                <a class="datos">${datos[index].telefono}</a>`;
            }
            morfismo.innerHTML = listper

        })
        .catch(function (error) {
            // Maneja los errores aquí
            console.log(error);
        });
}

window.addEventListener('load', function () {
    viewinfo();
});

