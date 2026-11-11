function toggleCheckbox(element){
    var xhr = new XMLHttpRequest();
    if(element.checked){
        xhr.open("GET","/update?output=" + element.id + "&state=1", true)
    } else{
        xhr.open("GET","/update?output=" + element.id + "&state=0", true)
    }
    xhr.send();
}
    const boton = document.getElementById('guardarHora');
    const lista = document.getElementById('listaHorarios');
    let horarios = [];
    function actualizarLista() {
      lista.innerHTML = '';
      horarios.forEach(hora => {
        const li = document.createElement('li');
        li.textContent = hora;
        lista.appendChild(li);
      });
    }
    boton.addEventListener('click', () => {
      const ahora = new Date();
      const horaFormateada = ahora.toLocaleTimeString();
      horarios.unshift(horaFormateada); // Añade al inicio
      if (horarios.length > 5) horarios.pop(); // Elimina el último si hay más de 5
      actualizarLista();
    });

async function actualizarAlarma() {
    try {
        const response = await fetch('/input', { cache: "no-store"});
        const estado = (await response.text()).trim();
        document.getElementById("indicador").classList.toggle("activo", estado === "1")
    } catch (error) {
        console.error("Error al actualizar boton:", error)
    }
    setTimeout(actualizarAlarma, 1000);
}
