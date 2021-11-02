import datetime
from urllib.request import urlopen

from bs4 import BeautifulSoup
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from backend.models import Attack, Village, Report


class AttackSerializer(serializers.ModelSerializer):
    attacker_cords = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Attack
        fields = ['url', 'defender_cords', 'attacker_cords', 'distance', 'attack_type', 'entry_time', 'defender_name',
                  'attacker_name']


class AttackCreateSerializer(serializers.ModelSerializer):
    attacker_cords = serializers.CharField(max_length=7, min_length=7)

    class Meta:
        model = Attack
        fields = ['defender_cords', 'attacker_cords', 'distance', 'attack_type', 'entry_time', 'defender_name',
                  'attacker_name']

    def create(self, validated_data):
        if Village.objects.filter(cords=validated_data['attacker_cords']).exists():
            village = Village.objects.get(cords=validated_data['attacker_cords'])
        else:
            village = v = Village.objects.create(cords=validated_data['attacker_cords'])
            v.save()

        attack = Attack.objects.create(
            defender_cords=validated_data['defender_cords'],
            attacker_cords=village,
            distance=validated_data['distance'],
            attack_type=validated_data['attack_type'],
            entry_time=validated_data['entry_time'],
            defender_name=validated_data['defender_name'],
            attacker_name=validated_data['attacker_name'],
        )
        return attack

    def validate(self, data):
        if Attack.objects.filter(
                Q(defender_cords=data['defender_cords']) &
                Q(distance=data['distance']) &
                Q(entry_time=data['entry_time'])
        ).exists():
            raise serializers.ValidationError({"duplicate": "This attack is already in the database"})
        return data

class ReportCreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['attack_hash', ]

    def validate_attack_hash(self, data):
        if Report.objects.filter(attack_hash=data).exists():
            raise serializers.ValidationError({"duplicate": "This report is already in the database"})

        data_report = get_information_from_reports(data)
        if data_report is None:
            raise serializers.ValidationError({"report": "raport został skasowany lub nie zawiera informacji o ataku"})
        return data

    def create(self, validated_data):
        data = get_information_from_reports(validated_data['attack_hash'])

        if Village.objects.filter(cords=data['attacker_cords']).exists():
            village = Village.objects.get(cords=data['attacker_cords'])
        else:
            village = v = Village.objects.create(cords=data['attacker_cords'])
            v.save()

        # date_time_obj = datetime.datetime.strptime(data['battle_time'], '%d/%m/%y %H:%M:%S')
        if not Report.objects.filter(
                Q(attacker_cords=village) &
                Q(battle_time=datetime.datetime.strptime(data['battle_time'], '%d.%m.%y %H:%M:%S')) &
                Q(send_troops_off=data['send_troops_off']) &
                Q(loos_troops_off=data['loos_troops_off'])
        ).exists():
            report = Report.objects.create(
                attacker_cords=village,
                battle_time=datetime.datetime.strptime(data['battle_time'], '%d.%m.%y %H:%M:%S'),
                send_troops_off=data['send_troops_off'],
                loos_troops_off=data['loos_troops_off'],
                send_troops_def=data['send_troops_def'],
                loos_troops_def=data['loos_troops_def'],
                send_catapult=data['send_catapult'],
                loos_catapult=data['loos_catapult'],
                attack_hash=validated_data['attack_hash']
            )
            report.save()
            return report
        raise ValidationError("taki raport jest juz w bazie")

class ReportSerializer(serializers.ModelSerializer):
    attacker_cords = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Report
        fields = ['url', 'attacker_cords', 'battle_time', 'send_troops_off', 'loos_troops_off', 'send_troops_def',
                  'loos_troops_def', 'send_catapult', 'loos_catapult', 'attack_hash']


class AttackSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = ['url', 'defender_cords', 'distance', 'attack_type', 'entry_time', 'defender_name',
                  'attacker_name']


class ReportSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['url', 'battle_time', 'send_troops_off', 'loos_troops_off', 'send_troops_def',
                  'loos_troops_def', 'send_catapult', 'loos_catapult', 'attack_hash']


class VillageSerializer(serializers.ModelSerializer):
    villages_attacks = AttackSpecSerializer(many=True, read_only=True)
    villages_reports = ReportSpecSerializer(many=True, read_only=True)

    class Meta:
        model = Village
        fields = ['cords', 'villages_attacks', 'villages_reports']


class VillageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = ['cords']


def scrap_report(report_hash, s='pl169'):
    data = []
    link = f'https://{s}.plemiona.pl/public_report/{report_hash}/'
    page = urlopen(link)
    soup = BeautifulSoup(page, features='lxml')
    targets = ['attack_info_att', 'attack_info_def']
    for i in targets:
        x = soup.body.find('table', id=i)
        rows = x.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

    x = soup.body.find('h4')
    data = [str(x)[4:-5], data[1], data[4], data[5], data[8], data[11], data[12]]
    return data


def get_information_from_reports(report_hash: str, archers=True):
    try:
        data = scrap_report(report_hash=report_hash)
        # print('aaaa', data)
        if archers:
            attack_data = {
                'battle_time': data[0],
                'attacker_cords': data[1][1][-12:-5],
                'attack_hash': data[1][1][-12:-5],
                'send_troops_off':
                    int(data[2][3]) + (int(data[2][6]) * 4) + (int(data[2][7]) * 5) + (int(data[2][9]) * 5),
                'loos_troops_off':
                    int(data[3][3]) + (int(data[3][6]) * 4) + (int(data[3][7]) * 5) + (int(data[3][9]) * 5),
                'send_troops_def':
                    int(data[2][1]) + int(data[2][2]) + int(data[2][4]) + (int(data[2][8]) * 6),
                'loos_troops_def':
                    int(data[3][1]) + int(data[3][2]) + int(data[3][4]) + (int(data[3][8]) * 6),
                'send_catapult': int(data[2][10]),
                'loos_catapult': int(data[2][10]),
            }
            return attack_data

        else:
            print('na razie nie ma obsługi świata bez łuczników')
    except AttributeError:
        return None
