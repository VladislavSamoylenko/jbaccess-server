let removal = [
    {name: 'person', path: '/person'},
    {name: 'key', path: '/keys'},
    {name: 'role', path: '/roles'}
];

$(document).ready( () => {
    $('.clear').click( (event) => {
        $(event.target).parents('form').find('input').val('');
        Materialize.updateTextFields();
    });

    removal.forEach(element => deleteItem(element));

    $('select').material_select();

    $('select[name=role]').change(event => {
        $(event.currentTarget).parents('form').submit()
    })
});

function deleteItem(item) {
    let $element = $('.delete-' + item.name);
    if ($element)
        $element.click(event => {
            let id = $(event.currentTarget).attr('data-id');

            $.ajax({
                url: `${item.path}/${id}`,
                type: 'DELETE',
                success: result => {
                    window.location.replace(window.location.href)
                }
            });
        })
}