from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from backend.models import Report, Village
from backend.serializers import get_information_from_reports


class ReportsForm(forms.Form):
    raporty = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 20, "cols": 70},
        ),
    )

    def clean(self):
        cd = self.cleaned_data
        reports = cd.get("raporty")

        if reports is None:
            raise ValidationError("Co mnie pusty formularz wysyłąsz ciulu jeden!")

        reports = reports.replace('Przesłane raporty:\r\n', '')
        reports = reports.replace('[/report]\r\n', '')
        reports = reports.replace('[/report]', '')
        reports = reports.replace('- [report]', ' ')
        reports = reports.split(' ')
        reports_list = reports[1:]

        if type(reports_list) is list or len(reports_list) == 0:
            for i in reports_list:
                if len(i) == 32:
                    pass
                else:
                    raise ValidationError("Coś poszło nie tak, zobacz czy poprawnie wkleiłeś")
            return reports_list
        raise ValidationError("Powinien zawierać conajmniej 1 raport")


def home(request):
    if request.method == "POST":
        form = ReportsForm(request.POST)
        if form.is_valid():
            reports = form.data["raporty"]
            reports = reports.replace('Przesłane raporty:\r\n', '')
            reports = reports.replace('[/report]\r\n', '')
            reports = reports.replace('[/report]', '')
            reports = reports.replace('- [report]', ' ')
            reports = reports.split(' ')
            reports = reports[1:]
            for i in reports:

                data = get_information_from_reports(i)
                if data is not None:

                    if Village.objects.filter(cords=data['attacker_cords']).exists():
                        village = Village.objects.get(cords=data['attacker_cords'])
                    else:
                        village = v = Village.objects.create(cords=data['attacker_cords'])
                        v.save()
                    if not Report.objects.filter(
                            Q(attacker_cords=village) &
                            Q(battle_time=datetime.strptime(data['battle_time'], '%d.%m.%y %H:%M:%S')) &
                            Q(send_troops_off=data['send_troops_off']) &
                            Q(loos_troops_off=data['loos_troops_off'])
                    ).exists():
                        report = Report.objects.create(
                            attacker_cords=village,
                            battle_time=datetime.strptime(data['battle_time'], '%d.%m.%y %H:%M:%S'),
                            send_troops_off=data['send_troops_off'],
                            loos_troops_off=data['loos_troops_off'],
                            send_troops_def=data['send_troops_def'],
                            loos_troops_def=data['loos_troops_def'],
                            send_catapult=data['send_catapult'],
                            loos_catapult=data['loos_catapult'],
                            attack_hash=i
                        )
                        report.save()

            form = ReportsForm()
            return render(request, 'pages/home_test.html', {'form': form})
    else:
        form = ReportsForm()
    return render(request, 'pages/home_test.html', {'form': form})


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

# class AboutPageView(TemplateView):
#     template_name = 'pages/about.html'
