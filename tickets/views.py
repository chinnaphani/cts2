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
    # print(team)
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
        # print(request.session['username'])
        # return render(request,"tktcreate.html")
        return redirect('/tktcreate',{"username" : username})
        # return render(request, 'loggedin.html', {"username": username})


        # return HttpResponse ('You are logged in as '+request.POST.get('username'))

    my_context = {}
    return render(request,"login.html",my_context)

def tkt_create(request):
    signuser="test"
    sconfirm = ""
    if request.session.has_key('username'):
        signuser = request.session['username']
        # print(ram)
    else:
        # return render(request, 'login.html', {})
        return redirect('/login')
    obj = TeamName.objects.all()
    context = {'name': obj,'username':signuser,'sconfirm':sconfirm}
    # context = {}
    return render(request,"tktcreate.html",context)


def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")


def addentry(request):
    if request.method == 'POST':

        ticketnumber = request.POST.get('ticketno')
        # seng = request.POST.get('username')
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
                              incsolddate=incsolddate,slasatus=slasatus,slamteam=slamteam
                              )
        # Ticket.objects.create(teamname=steam)
        # Ticket.objects.create(name=seng)

        # print(ticketnumber)
    # obj = TeamName.objects.all()
    context = {'sconfirm': "Your Ticket is Saved " }
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'),context)
