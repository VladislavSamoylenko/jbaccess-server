$(document).ready( () => {
    $('.clear').click( (event) => {
        $(event.target).parents('form').find('input').val('');
    })
});