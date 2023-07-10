function aggtrata(){
    const nombre_tratamiento = document.getElementById("nombre").value;
    const descripcion = document.getElementById("descripcion").value;
    const duracion = document.getElementById("duracion").value;
    const costo = document.getElementById("costo").value;
    if (nombre == ""|| descripcion == "" || duracion =="" || costo == "") {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Hay campos vacios!',
            footer: 'Por favor llene todos los campos'
          })

    } else {
        console.log(nombre_tratamiento, descripcion, duracion, costo);

        axios
            .post(
                '/api/guardartrat', {
                nombre_tratamiento: nombre_tratamiento,
                descripcion: descripcion,
                duracion: duracion,
                costo: costo
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
    Swal.fire({
        icon: 'success',
        text: 'Sus datos han sido guardados con exito!',

      })
    document.getElementById("miform").reset();
}