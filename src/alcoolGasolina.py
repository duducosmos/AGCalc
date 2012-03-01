#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
AGCalc: Calculator for the rate between alchool or petrol and it say
if is better put on or another.

copyright : Eduardo dos Santos Pereira. 2012.

    AGCalc is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.
    PyGraWC is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = 'Eduardo dos Santos Pereira'
__email__ = 'pereira.somoza@gmail.com'
__data__ = '26/02/2012'
__license__ = 'General Public License - http://www.gnu.org/licenses/'

import android

droid = android.Android()

myLayout = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/background"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#ff000000">
<TextView
    android:id="@+id/textview1"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Alcool ou Gasolina"
    android:hint="Alcool ou Gasolina" />
<TextView
    android:id="@+id/textview2"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Qual o Valor do Alcool?"
    android:gravity="center" />
<EditText
    android:id="@+id/edittext1"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:textSize="18sp"
    android:gravity="center"
    android:inputType="numberDecimal" />
<TextView
    android:id="@+id/textview3"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Qual o Valor da Gasolina?"
    android:gravity="center" />
<EditText
    android:id="@+id/edittext2"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:textSize="18sp"
    android:gravity="center"    
    android:inputType="numberDecimal" />
<TextView
    android:id="@+id/textview4"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:gravity="center" />
<Button
    android:id="@+id/button1"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Calcula" />
<Button
    android:id="@+id/button2"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Sobre" />
<Button
    android:id="@+id/button3"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Sair" />
</LinearLayout>
"""

def alcoolGasolina(val,vgas):
    V = val/vgas
    if(V > 0.70):
        droid.ttsSpeak("Melhor Comprar Gasolina")
        return """O valor do alcool e de cerca de
    %s do valor da gasolina,
    melhor colocar gasolina.""" %(round(V,2))
    else:
        droid.ttsSpeak("Melhor Comprar Alcool")
        return """O valor do alcool e de cerca de
    %s do valor da gasolina,
    Pode colocar alcool.""" %(round(V,2))

def sobre():
    mensagem = """
    Programa que calcula a se compensa comprar alcool ou gasolina.
    Desenvolvido por: Eduardo dos Santos Pereira.
    
    O alcool es trinta porcento menos eficiente que a
    gasolina. Assim, se o valor do litro de alcool for menor
    que setenta porcento do valor do litro da gasolina, melhor 
    comprar alcool. 
    
    e-mail: pereira.somoza@gmail.com
    """
     
    droid.ttsSpeak(mensagem)
    droid.dialogCreateAlert("Sobre",mensagem)
    droid.dialogSetPositiveButtonText('Sair')
    droid.dialogShow()
    
    
    
def eventLoop():
    while True:
        event = droid.eventWait().result
        key = event["data"]
        if key.has_key("key"):
            if key["key"] == "4":
                return

        if event["name"] == "click":
            id = event["data"]["id"]

            if id == "button1":                
                dadoA = droid.fullQueryDetail("edittext1").result
                dadoG = droid.fullQueryDetail("edittext2").result
                
                if(dadoA["text"] != "" and dadoG["text"] != ""):
                    val = float(dadoA["text"])
                    vgas = float(dadoG["text"])
                    resultado = alcoolGasolina(val,vgas)

                else:
                    resultado = "Entre com numeros"

                droid.fullSetProperty("textview4","text",resultado)
            elif id =="button2":
                sobre()

            elif id == "button3":
                return
        elif event["name"] == "screen":
            if envent["data"] == "destroy":
                return


droid.fullShow(myLayout)
eventLoop()
droid.fullDismiss()
