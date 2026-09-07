const climaForm = document.getElementById("clima-form");
const ciudadInput = document.getElementById("ciudad-input");
const resultadoContainer = document.getElementById("resultado-clima");

climaForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const ciudadIngresada = ciudadInput.value.trim();

    try {
        const response = await fetch(`http://127.0.0.1:8000/clima?ciudad=${ciudadIngresada}`);

        if (!response.ok) {
            const errorData = await response.json();
            resultadoContainer.innerHTML = `<p class="error">${errorData.detail}</p>`;
            return;
        }

        const data = await response.json();

        console.log(data)

        resultadoContainer.innerHTML = `
        <h2>${data.ciudad}</h2>
        <p class="temperatura">${data.temperatura}°C</p>
        <p class="descripcion">${data.descripcion}</p>
        <img src="https://openweathermap.org/img/wn/${data.icono}@2x.png" alt="Ícono del clima">
        `

    } catch (error) {
        console.error("Error de conexión", error);
    }
})