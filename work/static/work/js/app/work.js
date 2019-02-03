$("a#submits").click(function() {
    var i = $(this).parent('td').parent('tr').data('uid');
    console.log("第" + i + "行")
    var query = $("tr:eq(" + i + ")").children().eq(3).text()
    console.log("获取到文本：" + query)
    var id = $("tr:eq(" + i + ")").children().eq(4).text()
    console.log("获取到id：" + id)
    var yiwen = $("tr:eq(" + i + ")").children().eq(6).text().trim()
    console.log("获取到文本：" + yiwen)

    $.ajax({
    method: 'post',
    url: '/work/'+id +"/" + yiwen +'/change_yiwen/',
    dataType: "json",
    data: {"csrfmiddlewaretoken": "{{ csrf_token }}"},
    success: function(data) {
        console.log(data)
        $("#jindu").text(data.jindu);
        $("#paraing").text(data.paraing);
        $("#numing").text(data.numing);
        $("#mt"+id).css('display','none');
        $("#pe"+id).css('display','none');
        $("#dui"+id).css('display','block');
    }
});
})