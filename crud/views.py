from django.shortcuts import render, redirect
from .models import Member, Document, Ajax, CsvUpload,Pere,Mere,Enfant,Coordonnées,Famille,Membere
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from crud.forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def list(request):
    members_list = Member.objects.all()
    paginator = Paginator(members_list, 5)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'members': members})

@login_required
def create(request):
    if request.method == 'POST':
        member = Member(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            mobile_number=request.POST['mobile_number'],
            description=request.POST['description'],
            location=request.POST['location'],
            date=request.POST['date'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            member.full_clean()
        except ValidationError as e:
            pass
        member.save()
        messages.success(request, 'Member was created successfully!')
        return redirect('/list')
    else:
        return render(request, 'add.html')

@login_required
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)


@login_required
def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.mobile_number = request.POST['mobile_number'],
    member.description = request.POST['description'],
    member.location = request.POST['location'],
    member.date = request.POST['date'],
    member.save()
    messages.success(request, 'Member was updated successfully!')
    return redirect('/list')

@login_required
def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    messages.error(request, 'Member was deleted successfully!')
    return redirect('/list')



@login_required
def list1(request):
    peres_list = Pere.objects.all()
    paginator = Paginator(peres_list, 6)
    page = request.GET.get('page')
    try:
        peres = paginator.page(page)
    except PageNotAnInteger:
        peres = paginator.page(1)
    except EmptyPage:
        peres = paginator.page(paginator.num_pages)
    return render(request, 'list1.html', {'peres': peres})

@login_required
def create1(request):
    if request.method == 'POST':
        pere = Pere(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            etat=request.POST['etat'],
            sante=request.POST['sante'],
            profession=request.POST['profession'],
            revenu=request.POST['revenu'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            pere.full_clean()
        except ValidationError as e:
            pass
        pere.save()
        messages.success(request, 'pere was created successfully!')
        return redirect('/list1')
    else:
        return render(request, 'add1.html')

@login_required
def edit1(request, id):
    peres = Pere.objects.get(id=id)
    context = {'peres': peres}
    return render(request, 'edit1.html', context)


@login_required
def update1(request, id):
    pere = Pere.objects.get(id=id)
    pere.firstname = request.POST['firstname']
    pere.lastname = request.POST['lastname']
    pere.etat = request.POST['etat']
    pere.sante = request.POST['sante']
    pere.profession = request.POST['profession']
    pere.revenu = request.POST['revenu']
    pere.save()
    messages.success(request, 'pere was updated successfully!')
    return redirect('/list1')

@login_required
def delete1(request, id):
    pere = Pere.objects.get(id=id)
    pere.delete()
    messages.error(request, 'pere was deleted successfully!')
    return redirect('/list1')


@login_required
def list2(request):
    meres_list = Mere.objects.all()
    paginator = Paginator(meres_list, 6)
    page = request.GET.get('page')
    try:
        meres = paginator.page(page)
    except PageNotAnInteger:
        meres = paginator.page(1)
    except EmptyPage:
        meres = paginator.page(paginator.num_pages)
    return render(request, 'list2.html', {'meres': meres})

@login_required
def create2(request):
    if request.method == 'POST':
        mere = Mere(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            etat=request.POST['etat'],
            sante=request.POST['sante'],
            profession=request.POST['profession'],
            revenu=request.POST['revenu'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            mere.full_clean()
        except ValidationError as e:
            pass
        mere.save()
        messages.success(request, 'mere was created successfully!')
        return redirect('/list2')
    else:
        return render(request, 'add2.html')

@login_required
def edit2(request, id):
    meres = Mere.objects.get(id=id)
    context = {'meres': meres}
    return render(request, 'edit2.html', context)


@login_required
def update2(request, id):
    mere = Mere.objects.get(id=id)
    mere.firstname = request.POST['firstname']
    mere.lastname = request.POST['lastname']
    mere.etat = request.POST['etat']
    mere.sante = request.POST['sante']
    mere.profession = request.POST['profession']
    mere.revenu = request.POST['revenu']
    mere.save()
    messages.success(request, 'mere was updated successfully!')
    return redirect('/list2')

@login_required
def delete2(request, id):
    mere = Mere.objects.get(id=id)
    mere.delete()
    messages.error(request, 'mere was deleted successfully!')
    return redirect('/list2')



@login_required
def list3(request):
    coordonnées_list = Coordonnées.objects.all()
    paginator = Paginator(coordonnées_list, 2)
    page = request.GET.get('page')
    try:
        coordonnées = paginator.page(page)
    except PageNotAnInteger:
        coordonnées = paginator.page(1)
    except EmptyPage:
        coordonnées = paginator.page(paginator.num_pages)
    return render(request, 'list3.html', {'coordonnées': coordonnées})

@login_required
def create3(request):
    if request.method == 'POST':
        coordonnées = Coordonnées(
            adresse=request.POST['adresse'],
            mobile_number=request.POST['mobile_number'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            coordonnées.full_clean()
        except ValidationError as e:
            pass
        coordonnées.save()
        messages.success(request, 'coordonnées was created successfully!')
        return redirect('/list3')
    else:
        return render(request, 'add1.html')

@login_required
def edit3(request, id):
    coordonnées = Coordonnées.objects.get(id=id)
    context = {'coordonnées': coordonnées}
    return render(request, 'edit3.html', context)


@login_required
def update3(request, id):
    coordonnées = Coordonnées.objects.get(id=id)
    coordonnées.adresse = request.POST['adresse']
    coordonnées.mobile_number = request.POST['mobile_number']
    coordonnées.save()
    messages.success(request, 'coordonnées was updated successfully!')
    return redirect('/list3')

@login_required
def delete3(request, id):
    coordonnées = Coordonnées.objects.get(id=id)
    coordonnées.delete()
    messages.error(request, 'coordonnées was deleted successfully!')
    return redirect('/list3')


@login_required
def list4(request):
    enfants_list = Enfant.objects.all()
    paginator = Paginator(enfants_list, 6)
    page = request.GET.get('page')
    try:
        enfants = paginator.page(page)
    except PageNotAnInteger:
        enfants = paginator.page(1)
    except EmptyPage:
        enfants = paginator.page(paginator.num_pages)
    return render(request, 'list4.html', {'enfants': enfants})

@login_required
def create4(request):
    if request.method == 'POST':
        enfants = Enfant(
            firstname=request.POST['firstname'],
            date=request.POST['date'],
            etat=request.POST['etat'],
            sante=request.POST['sante'],
            profession=request.POST['profession'],
            revenu=request.POST['revenu'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            enfants.full_clean()
        except ValidationError as e:
            pass
        enfants.save()
        messages.success(request, 'enfants was created successfully!')
        return redirect('/list4')
    else:
        return render(request, 'add4.html')

@login_required
def edit4(request, id):
    enfants = Enfant.objects.get(id=id)
    context = {'enfants': enfants}
    return render(request, 'edit4.html', context)


@login_required
def update4(request, id):
    enfants = Enfant.objects.get(id=id)
    enfants.firstname = request.POST['firstname']
    enfants.date = request.POST['date']
    enfants.etat = request.POST['etat']
    enfants.sante = request.POST['sante']
    enfants.profession = request.POST['profession']
    enfants.revenu = request.POST['revenu']
    enfants.save()
    messages.success(request, 'enfants was updated successfully!')
    return redirect('/list4')

@login_required
def delete4(request, id):
    enfants = Enfant.objects.get(id=id)
    enfants.delete()
    messages.error(request, 'enfants was deleted successfully!')
    return redirect('/list4')



@login_required
def fileupload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        document = Document(
            description=request.POST['description'],
            document=myfile.name,
            uploaded_at=datetime.datetime.now(), )
        document.save()
        messages.success(request, 'Member was created successfully!')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return redirect('fileupload')
    else:
        documents = Document.objects.order_by('-uploaded_at')[:3]
        context = {'documents': documents}
    return render(request, 'fileupload.html', context)


@login_required
def ajax(request):
    if request.method == 'POST':
        if request.is_ajax():
            data = Ajax(
                text=request.POST['text'],
                search=request.POST['search'],
                email=request.POST['email'],
                telephone=request.POST['telephone'],
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            )
            data.save()
            astr = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
            return JsonResponse({'data': 'success'})
    else:
        ajax_list = Ajax.objects.order_by('-created_at')
        context = {'ajax_list': ajax_list}
    return render(request, 'ajax.html', {'ajax_list': ajax_list})


@csrf_protect
def getajax(request):
    if request.method == 'GET':
        if request.is_ajax():
            data = Ajax.objects.order_by('-created_at').first()
            created = data.created_at.strftime('%m-%d-%Y %H:%M:%S')
            datas = {"id": data.id, "text": data.text, "search": data.search, "email": data.email,
                     "telephone": data.telephone, "created_at": created}
            return JsonResponse(datas)
    else:
        return JsonResponse({'data': 'failure'})


@csrf_protect
def ajax_delete(request):
    if request.method == 'GET':
        if request.is_ajax():
            id = request.GET['id']
            ajax = Ajax.objects.get(id=id)
            ajax.delete()
            return JsonResponse({'data': 'success'})
    else:
        return JsonResponse({'data': 'failure'})


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                is_staff=True,
                is_active=True,
                is_superuser=True,
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def register_success(request):
    return render(request, 'success.html')

@login_required
def users(request):
    users_list = User.objects.all()
    paginator = Paginator(users_list, 5)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'users.html', {'users': users})

@login_required
def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.error(request, 'User was deleted successfully!')
    return redirect('/users')

@login_required
def upload_csv(request):
    if 'GET' == request.method:
        # csv_list = CsvUpload.objects.all()
        # paginator = Paginator(csv_list, 7)
        # page = request.GET.get('page')
        # try:
        #     csvdata = paginator.page(page)
        # except PageNotAnInteger:
        #     csvdata = paginator.page(1)
        # except EmptyPage:
        #     csvdata = paginator.page(paginator.num_pages)
        # return render(request, 'upload_csv.html', {'csvdata': csvdata})
        csvdata = CsvUpload.objects.all()
        context = {'csvdata': csvdata}
        return render(request, 'upload_csv.html', context)
    try:
        csv_file = request.FILES["csv_file"]

        if len(csv_file) == 0:
            messages.error(request, 'Empty File')
            return render(request, 'upload_csv.html')

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return render(request, 'upload_csv.html')

        if csv_file.multiple_chunks():
            messages.error(request, 'Uploaded file is too big (%.2f MB).' % (csv_file.size / (1000 * 1000),))
            return render(request, 'upload_csv.html')

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        for index, line in enumerate(lines):
            fields = line.split(",")
            if index == 0:
                if (fields[0] == 'name') and (fields[1] == 'description') and (fields[2] == 'end_date') and (
                        fields[3] == 'notes'):
                    pass
                else:
                    messages.error(request, 'File is not Correct Headers')
                    return render(request, 'upload_csv.html')
                    break
            else:
                print(index)
                if (len(fields[0]) != 0) and (len(fields[1]) != 0) and (len(fields[2]) != 0) and (len(fields[3]) != 0):
                    data = CsvUpload(
                        name=fields[0],
                        description=fields[1],
                        end_date=datetime.datetime.now(),
                        notes=fields[3]
                    )
                    data.save()
        messages.success(request, "Successfully Uploaded CSV File")
        return redirect('/upload/csv/')

    except Exception as e:
        messages.error(request, "Unable to upload file. " + e)
        return redirect('/upload/csv/')


@login_required
def changePassword(request):
    print('changepasword')
    return render(request, 'change_password.html')


@login_required
def deleteFiles(request, id):
    file = Document.objects.get(id=id)
    file.delete()
    messages.error(request, 'User was deleted successfully!')
    return redirect('/fileupload')



@login_required
def list5(request):
    familles_list = Famille.objects.all()
    paginator = Paginator(familles_list, 17)
    page = request.GET.get('page')
    try:
        familles = paginator.page(page)
    except PageNotAnInteger:
        familles = paginator.page(1)
    except EmptyPage:
        familles = paginator.page(paginator.num_pages)
    return render(request, 'list5.html', {'familles': familles})

@login_required
def create5(request):
    if request.method == 'POST':
        famille = Famille(
            firstname1=request.POST['firstname1'],
            lastname1=request.POST['lastname1'],
            etat1=request.POST['etat1'],
            sante1=request.POST['sante1'],
            profession1=request.POST['profession1'],
            revenu1=request.POST['revenu1'],
            firstname2=request.POST['firstname2'],
            lastname2=request.POST['lastname2'],
            etat2=request.POST['etat2'],
            sante2=request.POST['sante2'],
            profession2=request.POST['profession2'],
            revenu2=request.POST['revenu2'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            famille.full_clean()
        except ValidationError as e:
            pass
        famille.save()
        messages.success(request, 'famille was created successfully!')
        return redirect('/list5')
    else:
        return render(request, 'add5.html')

@login_required
def edit5(request, id):
    familles = Famille.objects.get(id=id)
    context = {'familles': familles}
    return render(request, 'edit5.html', context)


@login_required
def update5(request, id):
    famille = Famille.objects.get(id=id)
    famille.firstname1 = request.POST['firstname1']
    famille.lastname1 = request.POST['lastname1']
    famille.etat1 = request.POST['etat1']
    famille.sante1 = request.POST['sante1']
    famille.profession1 = request.POST['profession1']
    famille.revenu1 = request.POST['revenu1']
    famille.firstname2 = request.POST['firstname2']
    famille.lastname2 = request.POST['lastname2']
    famille.etat2 = request.POST['etat2']
    famille.sante2 = request.POST['sante2']
    famille.profession2 = request.POST['profession2']
    famille.revenu2 = request.POST['revenu2']

    famille.save()
    messages.success(request, 'famille was updated successfully!')
    return redirect('/list5')

@login_required
def delete5(request, id):
    famille = Famille.objects.get(id=id)
    famille.delete()
    messages.error(request, 'famille was deleted successfully!')
    return redirect('/list5')




@login_required
def list6(request):
    memberes_list = Membere.objects.all()
    paginator = Paginator(memberes_list, 7)
    page = request.GET.get('page')
    try:
        memberes = paginator.page(page)
    except PageNotAnInteger:
        memberes = paginator.page(1)
    except EmptyPage:
        memberes = paginator.page(paginator.num_pages)
    return render(request, 'list6.html', {'memberes': memberes})

@login_required
def create6(request):
    if request.method == 'POST':
        membere = Membere(
            code_famille=request.POST['code_famille'],
            member=request.POST['member'],
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            etat=request.POST['etat'],
            sante=request.POST['sante'],
            profession=request.POST['profession'],
            revenu=request.POST['revenu'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            membere.full_clean()
        except ValidationError as e:
            pass
        membere.save()
        messages.success(request, 'famille was created successfully!')
        return redirect('/list6')
    else:
        return render(request, 'add6.html')

@login_required
def edit6(request, id):
    memberes = Membere.objects.get(id=id)
    context = {'memberes': memberes}
    return render(request, 'edit6.html', context)


@login_required
def update6(request, id):
    membere = Membere.objects.get(id=id)
    membere.code_famille = request.POST['code_famille']
    membere.member = request.POST['member']
    membere.firstname = request.POST['firstname']
    membere.lastname = request.POST['lastname']
    membere.etat = request.POST['etat']
    membere.sante = request.POST['sante']
    membere.profession = request.POST['profession']
    membere.revenu = request.POST['revenu']

    membere.save()
    messages.success(request, 'famille was updated successfully!')
    return redirect('/list6')

@login_required
def delete6(request, id):
    membere = Membere.objects.get(id=id)
    membere.delete()
    messages.error(request, 'famille was deleted successfully!')
    return redirect('/list6')
