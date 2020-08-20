from django.shortcuts import render,HttpResponse, redirect
from .models import Engineer,TeamName,Ticket
from .forms import EngineerForm
from django.contrib.auth.models import User
from cts.services.ldap import get_LDAP_user
# Create your views here.

# def enginner_view(request):
#     obj = Engineer.objects.all()
#     context = {'name': obj }
#     return render(request,"engview.html",context)

def team_view(request):
    obj = TeamName.objects.all()
    context = {'name': obj }
    return render(request,"engview.html",context)

def enginner_create(request):
    form = EngineerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EngineerForm()
    context = {'form':form}
    return render(request, "engcreate.html",context)

def load_teams(request):
    team = request.GET.get('teamname')
    print(team)
    # teamname = 'Citrix Team'
    engineers = Engineer.objects.filter(teamname_id=team).order_by('name')
    # for x in teams:
    #     print(x.name)
    return render(request, 'team_dropdown_list_options.html', {'engineers': engineers})

# authuser = ""

def loginPage(request):
    username = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if get_LDAP_user(username,password) is None:
            return HttpResponse ('Your ID does not exit')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = True
            # user.save()
            request.session['username'] = username
        # return render(request,"tktcreate.html")
        return redirect('/tktcreate')
        # return render(request, 'loggedin.html', {"username": username})


        # return HttpResponse ('You are logged in as '+request.POST.get('username'))

    my_context = {}
    return render(request,"login.html",my_context)

def tkt_create(request):
    tktname = ""
    if request.session.has_key('username'):
        tktname = request.session['username']
    else:
        return render(request, 'login.html', {})
        # print(tktname)


    # username = request.session['username']
    # print(username)
    obj = TeamName.objects.all()
    context = {'name': obj}

    if request.method == 'POST':

        ticketnumber = request.POST.get('ticketno')
        # seng = request.POST.get('ticketno')
        steam = request.POST.get('ticketno')
        pri = request.POST.get('priority')
        ticketstatus = request.POST.get('status')
        tktdescription = request.POST.get('tktdes')
        inccreddate = request.POST.get('incstarttime')
        increcddate = request.POST.get('incresinq')
        incsolddate = request.POST.get('increstime')
        slasatus = request.POST.get('sla')
        slamteam = request.POST.get('slateam')
        if slamteam == "OutSideTeam":
            slamteam = request.POST.get('teamname')
        else:
            slamteam = request.POST.get('slateam')
        # s = request.POST.get('remone')
        # print(s)


        #print(pri)

        Ticket.objects.create(ticketno=ticketnumber,teamname=steam, priority=pri,ticketstatus=ticketstatus,
                              tktdescription=tktdescription,inccreddate=inccreddate,increcddate=increcddate,
                              incsolddate=incsolddate,slasatus=slasatus,slamteam=slamteam,name=tktname
                              )
        # Ticket.objects.create(teamname=steam)
        # Ticket.objects.create(name=seng)

        # print(ticketnumber)
    # obj = TeamName.objects.all()
    # context = {'name': obj }
    return render(request,"tktcreate.html",context)
