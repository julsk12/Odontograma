var timeout;

function startTokenExpirationTimer() {
  clearTimeout(timeout);
  timeout = setTimeout(handleTokenExpired, 300000); // 300000 ms = 5 minutos
}

function resetTokenExpirationTimer() {
  clearTimeout(timeout);
  startTokenExpirationTimer();
}
function checkTokenExpiration() {
    const token = localStorage.getItem('token'); // Obtén el token almacenado en el local storage

    // Verifica si el usuario ya está en la página de inicio de sesión
    if (window.location.pathname === '/login') {
      return;
    }

    axios.get('checktoken', {
        headers: {
          Authorization: `Bearer ${token}` // Incluye el token en el encabezado de la solicitud
        }
      })
      .then(function (response) {
        const data = response.data;
        if (data.token_expired) {
          handleTokenExpired();
        } else {
          resetTokenExpirationTimer();
        }
      })
      .catch(function (error) {
        if (error.response && error.response.status === 401) {
          handleTokenExpired();
        } else {
          console.log(error);
        }
      });

    console.log('Authorization Header:', `Bearer ${token}`);
  }

  function handleTokenExpired() {
    alert('Tu sesión ha expirado');
    console.log("Si Pasó aquí");
    localStorage.removeItem('token'); // Elimina el token del local storage
    window.location.href = '/fronted/indexlogin'; // Redirige a la página indexlogin
  }

  // Llama a la función checkTokenExpiration al cargar la página
  window.addEventListener('load', function () {
    checkTokenExpiration();

    startTokenExpirationTimer();

  // Reinicia el temporizador de expiración del token al detectar actividad del usuario
  window.addEventListener('mousemove', resetTokenExpirationTimer);
  window.addEventListener('keydown', resetTokenExpirationTimer);

    // Verificar el estado del token cada 5 segundos
  setInterval(checkTokenExpiration, 5000);

  
  });