
// script.js
document.addEventListener('DOMContentLoaded', (event) => {
    const radioButtons = document.querySelectorAll('input[name="age-group"]');
    let selectedValue;

    radioButtons.forEach(radio => {
        radio.addEventListener('change', (event) => {
            selectedValue = event.target.value;
            console.log(`Selected age group: ${selectedValue}`);
            // Aqui você pode adicionar código para enviar o valor para um servidor ou armazená-lo localmente
        });
    });
});
