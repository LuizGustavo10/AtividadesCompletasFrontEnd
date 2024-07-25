// script.js
document.addEventListener("DOMContentLoaded", function() {
    const menuItems = document.querySelectorAll('.menu-item');

    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            // Remove a classe 'selected' de todos os itens
            menuItems.forEach(i => i.classList.remove('selected'));
            
            // Adiciona a classe 'selected' ao item clicado
            this.classList.add('selected');
        });
    });
});