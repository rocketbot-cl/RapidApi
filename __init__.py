# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import http.client

module = GetParams("module")

if module == "validMail":

    try:

        api_key = GetParams("api_key")
        mail = GetParams("mail")
        var_ = GetParams("var_")

        print(api_key,mail)

        conn = http.client.HTTPSConnection("pozzad-email-validator.p.rapidapi.com")

        headers = {
            'x-rapidapi-host': "pozzad-email-validator.p.rapidapi.com",
            'x-rapidapi-key': api_key
            }

        conn.request("GET", "/emailvalidator/validateEmail/"+mail+"", headers=headers)

        res = conn.getresponse()
        data = res.read()

        data = data.decode("utf-8")
        if "false" in data:
            data = False
        else:
            data = True

        SetVar(var_,data)

    except:
        PrintException()
