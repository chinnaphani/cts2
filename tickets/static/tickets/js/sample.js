var startTime = '08:00';
var endTime = '17:00';

$(document).ready(function () {
    $("#incresinq").change(function () {
        var incsrttime = $('#incstarttime').val();

        var stime = new Date(incsrttime);
        var incendtime = $(this).val();
        splittime = incendtime.split('T');
        curr_time = splittime[1];
        //alert(curr_time);
        //alert(new Date(curr_time))
        var etime = new Date(incendtime);
        var diff = ( etime - stime);
        var diffSeconds = diff/1000;
        var HH = Math.floor(diffSeconds/3600);
        var MM = Math.floor(diffSeconds%3600)/60;
        var formatted = ((HH < 10)?("0" + HH):HH) + ":" + ((MM < 10)?("0" + MM):MM);
        //alert(formatted + "test");
        //incsrttime.value = date.toString("yyyy-MM-dd HH:mm:ss");
        $("#remone").html ("The ticket is transferred to queue after " + formatted + " hrs");


        if (curr_time > startTime && curr_time < endTime) {
         //alert("In Business Hrs");
           }
        else {
            var mtime = new Date("01/01/2007 " + curr_time);
            var mendtime = new Date("01/01/2007 " + startTime);
            var laptime = mendtime-mtime;
            var lapsec = laptime/1000;
            var lapHH = Math.floor(lapsec/3600);
            var lapMM = Math.floor(lapsec%3600)/60;
            var slap = ""
            var mlap = ""
            if (lapHH<0 && lapMM<0){
                slap = lapHH+24;
                mlap = lapMM+60;
            }
            else {
                slap = lapHH;
                mlap = lapMM;
            }
            //alert(slap + ":"+ mlap)
            //alert('Out Side Business Hrs');
            $("#remtwo").html ("The ticket received in out of business hrs & lapsed " + slap + ":"+ mlap + " hr " + "of time ");
            }
    });
});

var tickestatus = ""

$(document).ready(function () {
$('input:radio[name="status"]').change(function () {
    if (this.checked && this.value === 'Resolved') {
        tickestatus = "Resolved"
    }
    else if (this.checked && this.value === 'Transferred'){
        tickestatus = "Transferred"
    }
});
});

$(document).ready(function () {
    $("#increstime").change(function () {
        var incsrttime = $('#incstarttime').val();

        // var dateTimeSplit = $('#increstime').val().split(' ');
        var stime = new Date(incsrttime);
        var erestime = $(this).val();
        var endsoltime = new Date(erestime);
        var resdiff = (endsoltime-stime);
        var diffSeconds = resdiff/1000;
        var HH = Math.floor(diffSeconds/3600);
        var MM = Math.floor(diffSeconds%3600)/60;
        var formatted = ((HH < 10)?("0" + HH):HH) + ":" + ((MM < 10)?("0" + MM):MM);

        if (tickestatus === 'Resolved'){
            //alert('test')
            $("#remthree").html ("The ticket resolved after sla hrs and took " + HH +" hrs of time, so verify the sla timeline in Service now");

        } else if (tickestatus === 'Transferred'){
            $("#remthree").html ("The ticket transferred from our team after sla hrs and took " + HH +" hrs of time, so verify the sla timeline in Service now");
        } else if (tickestatus ===""){
            alert("Please Select Ticket Status")

        }


        //$(".remarks").html ("The ticket resolved after sla hrs and took " + HH +" hrs of time, so verify the sla timeline in Service now");

        var pri = $("#priority").val();
        var prih = ""
        if (pri === 'P3') {
            prih = 8;
            //alert('p3 selected' + prih);
        } else if (pri === 'P2') {
            prih = 4;
            //alert('p2 selected' + prih);
        } else if (pri === 'P1') {
            prih = 2;
            //alert('p1 selected' + prih);
        } else if (pri === 'P4'){
            prih = 72;
            //alert('p4 selected' + prih);
        }
        if (HH > prih) {
            //alert("Ticket Resolutions Breached");
           $("#slachck").css("display", "block");
        }
        else {
            $("#slachck").css("display","none");
            $('input[name="sla"]').prop('checked', false);
            $(".slateam").css("display", "none");

        }

    });
});


$(document).ready(function () {
$('input:radio[name="sla"]').change(function () {
    if (this.checked && this.value === 'Missed') {
        //alert("missed selected")
        $(".slateam").css("display", "block");
    }
    else {
        $(".slateam").css("display", "none");
        $(".dcoteam").css("display", "none");
        $('input[name="slateam"]').prop('checked', false);
    }
});
});

$(document).ready(function () {
$('input:radio[name="slateam"]').change(function () {
    if (this.checked && this.value === 'OutSideTeam') {
        //alert("OutSideTeam")
        $(".dcoteam").css("display", "block");
    }
    else {
        $(".dcoteam").css("display", "none");
    }
});
});

function validateForm() {
  var ftkt = document.forms["tktcreate"]["ticketno"].value;
  if (ftkt === "") {
    alert("Name must be filled out");
    return false;
  }

   var fpri = document.forms["tktcreate"]["priority"].value;
  if ('none' === fpri) {
    alert("priority must be filled out");
    return false;
  }

  var fstatus = document.forms["tktcreate"]["status"].value;
  if (fstatus === "") {
    alert("Status must be filled out");
    return false;
  }




}