$(document).ready(function () {
    $("#incresinq").change(function () {
        var incsrttime = $('#incstarttime').val();
        var stime = new Date(incsrttime);
        var incendtime = $(this).val();
        var etime = new Date(incendtime)
        var diff = ( etime - stime);
        var diffSeconds = diff/1000;
        var HH = Math.floor(diffSeconds/3600);
        var MM = Math.floor(diffSeconds%3600)/60;
        var formatted = ((HH < 10)?("0" + HH):HH) + ":" + ((MM < 10)?("0" + MM):MM)
        //alert(text);
        //incsrttime.value = date.toString("yyyy-MM-dd HH:mm:ss");
        $("#boxres").html ("The ticket is transferred to queue after " + formatted + " hrs");
        $("#boxres").css("display", "block");

    });
});

$(document).ready(function () {
    $("#increstime").change(function () {
        var incsrttime = $('#incstarttime').val();
        var stime = new Date(incsrttime);
        var erestime = $(this).val();
        var endsoltime = new Date(erestime)
        var resdiff = (endsoltime-stime)
        var diffSeconds = resdiff/1000;
        var HH = Math.floor(diffSeconds/3600);
        var MM = Math.floor(diffSeconds%3600)/60;
        var formatted = ((HH < 10)?("0" + HH):HH) + ":" + ((MM < 10)?("0" + MM):MM)

        $("#boxsol").html ("The ticket resolved after sla hrs and took " + HH +" hrs of time, so verify the sla timeline in Service now");

        var pri = $("#priority").val();
        var prih = ""
        if (pri === 'P3') {
            prih = 8;
            alert('p3 selected' + prih);
        } else if (pri === 'P2') {
            prih = 4;
            alert('p2 selected' + prih);
        } else if (pri === 'P1') {
            prih = 2;
            alert('p1 selected' + prih);
        } else if (pri === 'P4'){
            prih = 72;
            alert('p4 selected' + prih);
        }
        if (HH > prih) {
            //alert("Ticket Resolutions Breached");
            document.getElementById("boxsol").style.backgroundColor = 'red';
            $("#boxsol").css("display", "block");
            $("#slachck").css("display", "block");
        }
        else {
            document.getElementById("boxsol").style.backgroundColor = '#8af126';
            $("#boxsol").css("display", "none");
            $("#slachck").css("display","none");
            $('input[name="sla"]').prop('checked', false);
            $("#dcoteam").css("display", "none");

        }

    });
});


$(document).ready(function () {
$('input:radio[name="sla"]').change(function () {
    if (this.checked && this.value === 'Missed') {
        alert("missed selected")
        $("#slateam").css("display", "block");
    }
    else {
        $("#slateam").css("display", "none");
        $("#dcoteam").css("display", "none");
        $('input[name="slateam"]').prop('checked', false);
    }
});
});

$(document).ready(function () {
$('input:radio[name="slateam"]').change(function () {
    if (this.checked && this.value === 'OutSideTeam') {
        alert("OutSideTeam")
        $("#dcoteam").css("display", "block");
    }
    else {
        $("#dcoteam").css("display", "none");
    }
});
});