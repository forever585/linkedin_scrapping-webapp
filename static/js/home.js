var keywordTable;
var tableData = [
    [1, 'tmp@temp.com', '111-2222-3333'],
    [2, 'tmp@temp.com', '111-2222-3333'],
    [3, 'tmp@temp.com', '111-2222-3333'],
    [4, 'tmp@temp.com', '111-2222-3333'],
    [5, 'tmp@temp.com', '111-2222-3333'],
]

var execute_time = 5
$(document).ready(() => {
    keywordTable = initDataTable('keyword_sheet', tableData)
})

function initDataTable(id, data){
    return $(`#${id}`).DataTable({
        data: data,
        deferRender: true,
        scrollCollapse: true,
        scroller: true,
        scrollY: 400,
        paging: true,
        pageLength: 10
    });
}

async function handleSubmit(){
    // let keywords = []
    // await tableData.map(item => {
    //     keyword_array = item[1].split(' ')
    //     console.log(keyword_array)
    //     for(let i = 0; i < keyword_array.length; i++){
    //         let keyword = keyword_array[i]
    //         console.log(keyword)
    //         if(keyword.length > 2 && keyword.length < 7 && !keywords.includes(keyword))  {
    //             keywords.push(keyword)
    //         }
    //     }
    // })
    // submitForm(keywords)
}

function submitForm(data){
    // $('<input type="hidden" name="generated_keywords"/>').val(data).appendTo('#keywords_form');
    // $("#keywords_form").submit();
}
