function registrar() {
    const nombre = document.getElementById("logname").value;
    const email = document.getElementById("logemail1").value;
    const pass = document.getElementById("logpass1").value;
    const rol = document.getElementById("rol").value;
    const Direccion = document.getElementById("Direccion").value;
    const Fecha_nacimiento = document.getElementById("Fecha_nacimiento").value;
    const Telefono = document.getElementById("Telefono").value;
    const Documento = document.getElementById("Documento").value;
    let idrol = 0;

    var emailRegex = /^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
    var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;

    var isEmailValid = emailRegex.test(email);
    var isPasswordValid = passwordRegex.test(pass);
    console.log(nombre, email, pass, rol);

if (isEmailValid && isPasswordValid) {
    if (nombre === "" && email === "" && pass === "" && rol === "..." && Direccion == "" && Fecha_nacimiento === "" && Telefono === "" && Documento === "") {
            Swal.fire({
                title: 'Hay campos vacios!',
                text: 'Por favor complete todos los campos.',
                imageUrl: 'https://www.latercera.com/resizer/sb91NqJC0m16VtB4cjbZvQxIEmc=/900x600/smart/arc-anglerfish-arc2-prod-copesa.s3.amazonaws.com/public/YPG2SOLGAJBDBHO5PRJA75IEGI.jpg',
                imageWidth: 400,
                imageHeight: 200,
                imageAlt: 'Custom image',
            })
        } else {
            Swal.fire({
                icon: 'success',
                title: 'Sus datos han sido guardados con exito',
                text: 'Disfrute su estancia'
            })
            if (rol == "Secretaria") {
                idrol = 1
            } else if (rol == "Odontologo") {
                idrol = 2
            } else if (rol == "Paciente") {
                idrol = 3
            } else {
                Swal.fire({
                    title: 'Hay campos vacios!',
                    text: 'Debe seleccionar un rol.',
                    imageUrl: 'https://www.latercera.com/resizer/sb91NqJC0m16VtB4cjbZvQxIEmc=/900x600/smart/arc-anglerfish-arc2-prod-copesa.s3.amazonaws.com/public/YPG2SOLGAJBDBHO5PRJA75IEGI.jpg',
                    imageWidth: 400,
                    imageHeight: 200,
                    imageAlt: 'Custom image',
                })
            }
            axios
                .post(
                    'api/save_registro', {
                        id: Documento,
                        nombre: nombre,
                        fecha_nacimiento: Fecha_nacimiento,
                        telefono: Telefono,
                        direccion: Direccion,
                        correo: email,
                        password: pass,
                        id_roles: idrol,
                    }, {
                        headers: {
                            "Content-Type": "multipart/form-data",
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

        document.getElementById("miform").reset();
} else {
  Swal.fire({
                    title: 'Hay valores incorrectos',
                    text: 'Por favor verifique el correo y la contraseña',
                    text: 'la contraseña debe tener  al menos 8 caracteres y debe contener al menos una letra mayúscula, una letra minúscula y un número',
                    imageUrl: 'https://www.latercera.com/resizer/sb91NqJC0m16VtB4cjbZvQxIEmc=/900x600/smart/arc-anglerfish-arc2-prod-copesa.s3.amazonaws.com/public/YPG2SOLGAJBDBHO5PRJA75IEGI.jpg',
                    imageWidth: 400,
                    imageHeight: 200,
                    imageAlt: 'Custom image',
                })

}

    
}


function login() {
    const correo = document.getElementById('logemail');
    const pass = document.getElementById('logpass');
    console.log(correo, pass);
    axios.post('/login', {
            correo: correo.value,
            password: pass.value
        })
        .then(function(response) {
            // Si el inicio de sesión es exitoso, redirige al usuario a la vista correspondiente en función de su rol
            if (response.data.rol === "Secretaria") {
                window.location.href = '/fronted/indexsecretaria';
            } else if (response.data.rol === "Odontologo") {
                window.location.href = '/fronted/indexodontologo';
            } else if (response.data.rol === "Paciente") {
                window.location.href = '/fronted/indexpaciente';
            } else {
                window.location.href = '/';
            }
        })
        .catch(function(error) {
            console.log(error);
        });
}

