$(function () {
    $(".accordion-body").on("click", "a", function () {
        var chartid = $(this).data("id");
        window.location.hash = chartid;
        loadInner(chartid)
    })

    function loadInner(chartid) {
        var chartid = window.location.hash;
        var pathn, i;
        switch (chartid) {
            case "#chart1":
                pathn = "/chart1";
                i = 0;
                break;
            case "#chart2":
                pathn = "/chart2";
                i = 1;
                break;
            case "#chart3":
                pathn = "/chart3";
                i = 2;
                break;
            case "#chart4":
                pathn = "/chart4";
                i = 3;
                break;
            case "#chart5":
                pathn = "/chart5";
                i = 4;
                break;
            case "#chart6":
                pathn = "/chart6";
                i = 5;
                break;
            default:
                pathn = "/chart1";
                i = 0;
                break;
        }


        $("#chartshow").load(pathn);


        $(".accordion-body a").eq(i).addClass("chart1").siblings().removeClass("chart1");

    }

    var chartid = window.location.hash;
    loadInner(chartid)

})