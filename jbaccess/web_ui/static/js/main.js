$(document).ready( () => {
    $('.clear').click( (event) => {
        $(event.target).parents('form').find('input').val('');
        Materialize.updateTextFields();
    });

    $('.delete-person').click( (event) => {
        let id = $(event.currentTarget).attr('data-id');

        $.ajax({
            url: `/person/${id}`,
            type: 'DELETE',
            success: result => {
               window.location.replace(window.location.href)
            }
        });
    })
});