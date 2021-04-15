function handleFormSubmit(event){
    event.preventDefault();
    const data = new FormData(event.target);
    const formJSON = Object.fromEntries(data.entries());
    var table = $('#myTable').DataTable();
    table.destroy();
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(formJSON),
        dataType: 'json',
        url: 'http://127.0.0.1:5000/customTableDisplay',

    }).done(function (data) {
        if (data["message"] == 'err'){
            alert(data["error"]);
        }
        else {
                $('#myTable').empty();
                $('#myTable').dataTable({
                    "columnDefs": [
                        {"className": "dt-center", "targets": "_all"}
                    ],
                    "data": data.data.DATA,
                    "columns": data.data.COLUMNS,
                    "bDestroy": true
                });
        }
    })
    const results = document.querySelector('.results pre');
    results.innerText = JSON.stringify(formJSON, null, 1);


}

function listRecords() {
    var table = $('#myTable').DataTable();
    table.destroy();
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: 'http://127.0.0.1:5000/getRecords',

    }).done(function (data) {
        $('#myTable').empty();
        $('#myTable').dataTable({
                "columnDefs": [
                    {"className": "dt-center", "targets": "_all"},
                    {"targets": -3, "data": null, "defaultContent": "<button id='0'>Edit</button>"},
                    {"targets": -2, "data": null, "defaultContent": "<button id='1'>Duplicate</button>"},
                    {"targets": -1, "data": null, "defaultContent": "<button id='2'>Delete</button>"}
            ],
                "data": data.data.DATA,
                "columns": data.data.COLUMNS,
                "bDestroy": true

        });
            $('#myTable tbody').on( 'click', 'button', function (event) {
                var table = $('#myTable').DataTable();
                var rowId = table.row($(this).parents('tr')).data();
                rowId.push(event.target.id);
                alert(rowId)
                rowId = {
                    "title": rowId[1],
                    "description": rowId[2],
                    "columns": rowId[3],
                    "buttonId": rowId[4]
                }
                console.log(rowId,'rowId')
                /*$.post('http://127.0.0.1:5000/updateRecords', JSON.stringify(rowId), function (data){
                    window.location.replace('/');
                    $('body').html(data);
                })*/
                $.ajax({
                    type: 'POST',
                    data: JSON.stringify(rowId),
                    dataType: 'json',
                    contentType: 'application/json',
                    url: 'http://127.0.0.1:5000/updateRecords',
                }).done(function (data){
                    console.log(data);
                    postForm('/', data);
                })


        });
    })

}
function postForm(path, params, method) {
    method = method || 'post';

    var form = document.createElement('form');
    form.setAttribute('method', method);
    form.setAttribute('action', path);

    for (var key in params) {
        if (params.hasOwnProperty(key)) {
            var hiddenField = document.createElement('input');
            hiddenField.setAttribute('type', 'hidden');
            hiddenField.setAttribute('name', key);
            hiddenField.setAttribute('value', params[key]);

            form.appendChild(hiddenField);
        }
    }

    document.body.appendChild(form);
    form.submit();
}


function sendButtonData(jsonData){

}

const customTableForm = document.querySelector('.customTable-form');
if (customTableForm){
    customTableForm.addEventListener('submit', handleFormSubmit);
}


