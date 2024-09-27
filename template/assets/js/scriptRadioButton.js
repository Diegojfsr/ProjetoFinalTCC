
// script.js
document.addEventListener('DOMContentLoaded', (event) => {
    const radioButtons = document.querySelectorAll('input[type="radio"]');
    let selectedValues = {};

    radioButtons.forEach(radio => {
        radio.addEventListener('change', (event) => {
            const name = event.target.name;
            const value = event.target.value;
            selectedValues[name] = value;
            console.log(`Selected values:`, selectedValues);
            // Aqui você pode adicionar código para enviar os valores para um servidor ou armazená-los localmente
        });
    });
})
