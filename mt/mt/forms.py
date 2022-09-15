from django import forms


class RouterForm(forms.Form):
    identity = forms.CharField(label="имя", max_length=30, initial="router-mt")
    ip = forms.GenericIPAddressField(
        protocol="ipv4", label="IP", initial="89.221.48.2"
    )
    mask = forms.DecimalField(
        label="битовая маска",
        help_text="30",
        decimal_places=0,
        min_value=22,
        max_value=31,
        initial="30",
    )
    gw = forms.GenericIPAddressField(
        protocol="ipv4", label="шлюз", max_length=100, initial="89.221.48.1"
    )
    wifi_name = forms.CharField(
        label="WiFi сеть", max_length=30, initial="wifiname"
    )
    wifi_passwd = forms.CharField(
        label="WiFi пароль",
        min_length=8,
        max_length=64,
        initial="",
    )
    client_login = forms.CharField(
        label="логин клиента", max_length=30, initial="cl"
    )
    client_passwd = forms.CharField(
        label="пароль клиента", max_length=30, initial=""
    )
    isp_login = forms.CharField(
        label="логин провайдера",
        max_length=30,
        initial="gr",
    )
    isp_passwd = forms.CharField(
        label="пароль провайдера", max_length=30, initial=""
    )
